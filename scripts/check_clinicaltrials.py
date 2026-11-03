#!/usr/bin/env python3
"""
Check ClinicalTrials.gov for new clinical trials related to our drug list.
Creates GitHub Issues when new trials are found.

NOTE: Filters out known/approved indications to focus on repurposing evidence.

2026-11-03 門檻（cache 結構與 key 不變）：
- 「新試驗」以 StudyFirstPostDate 落在查詢窗內判斷；只是 LastUpdatePostDate 更新的舊試驗寫入 cache、不開 issue。
- 至少一筆新試驗的 condition 直接對到目前的預測新適應症才開 issue；issue 只列命中的試驗，標題只掛命中的預測。
- 已核准／已知用途：drug_list 的 approved_indication（search-index 的知識圖譜原適應症）與預測同名、或只差 type 2／subtype A 等限定詞者不算命中（見 is_known_indication）。
"""

import json
import os
import re
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

from github_utils import create_issue, close_older_clinicaltrials_issues


# 2026-11-03：已核准用途排除改成嚴格比對。原本的關鍵字比對會誤殺（例如 amlodipine 的
# pulmonary hypertension 因為 hypertension 被排除）；現在只認兩種情形：
#   1. 正規化後名稱完全相同
#   2. 一方是另一方前後加上限定詞（type 2、subtype A、form、variant 等）
# approved_indication 是 extract_drug_list.py 輸出的「; 」分隔已知適應症（英文疾病名）。
_QUALIFIER_WORDS = {"type", "subtype", "form", "variant", "group", "class", "grade", "stage"}


def _norm_indication(name: str) -> list:
    name = re.sub(r"\((disease|disorder)\)", " ", (name or "").lower())
    return re.sub(r"[^\w]+", " ", name).split()


def _is_qualifier(words: list) -> bool:
    # 限定詞要以 type／subtype 等字開頭（"type 2"、"subtype a"）；單獨的字母不算（hepatitis b ≠ hepatitis）
    return bool(words) and words[0] in _QUALIFIER_WORDS and all(
        w in _QUALIFIER_WORDS or re.fullmatch(r"\d+[a-z]?|[ivx]+|[a-z]", w) for w in words)


def _same_or_qualified(a: list, b: list) -> bool:
    if a == b:
        return True
    short, long_ = (a, b) if len(a) < len(b) else (b, a)
    if not short or len(short) == len(long_):
        return False
    n = len(short)
    for i in range(len(long_) - n + 1):
        if long_[i:i + n] == short and _is_qualifier(long_[:i] + long_[i + n:]) \
                and (i == 0 or i + n == len(long_)):
            return True
    return False


def is_known_indication(approved_indication: str, predicted_indication: str) -> bool:
    """Is the predicted indication one of the drug's known (approved) indications?

    Strict match against each '; '-separated known indication: identical after
    normalization, or one is the other plus a qualifier (e.g. 'type 2', 'subtype A').
    """
    if not approved_indication or not predicted_indication:
        return False
    pred = _norm_indication(predicted_indication)
    return any(_same_or_qualified(pred, _norm_indication(k))
               for k in re.split(r"[;；]", approved_indication) if k.strip())

# Configuration
API_BASE = "https://clinicaltrials.gov/api/v2/studies"
CACHE_FILE = Path(__file__).parent.parent / "data" / "cache" / "clinicaltrials_cache.json"
DRUG_LIST_FILE = Path(__file__).parent / "drug_list.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/EuTxGNN")
RATE_LIMIT_DELAY = 0.5  # seconds between API calls


def load_cache() -> dict:
    """Load the cache of previously seen trial IDs."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": None, "seen_trials": {}}


def save_cache(cache: dict):
    """Save the cache."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    cache["last_check"] = datetime.now().isoformat()
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def load_drug_list() -> list:
    """Load the drug list."""
    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["drugs"]



# --- 試驗與藥物的關係必須是結構化的介入角色（JpTxGNN #26713）---
# query.term 全文搜尋會把只在描述中提到藥名的試驗（例：安慰劑用的生理食鹽水、AI 工具研究）
# 也當成該藥的新試驗。改用 query.intr，並要求藥名出現在介入措施名稱／別名、且不是安慰劑組。
_SALTS = {"hydrochloride", "hcl", "sodium", "potassium", "calcium", "sulfate", "sulphate", "maleate", "fumarate",
          "tartrate", "citrate", "acetate", "mesylate", "besylate", "succinate", "phosphate", "bromide", "chloride"}


def _norm_name(text) -> str:
    import unicodedata
    t = unicodedata.normalize("NFKD", str(text or "")).encode("ascii", "ignore").decode().lower()
    return " ".join("".join(c if c.isalnum() else " " for c in t).split())


def _role_bound(study: dict, drug_name: str) -> bool:
    full = _norm_name(drug_name)
    core = " ".join(w for w in full.split() if w not in _SALTS) or full
    ivs = (study.get("protocolSection", {}).get("armsInterventionsModule", {}) or {}).get("interventions", []) or []
    for iv in ivs:
        name = _norm_name(iv.get("name", ""))
        if "placebo" in name:
            continue
        text = " " + " ".join([name] + [_norm_name(n) for n in (iv.get("otherNames") or [])]) + " "
        if (full and f" {full} " in text) or (core and f" {core} " in text):
            return True
    return False

def _clean_condition(name: str) -> str:
    name = re.sub(r"\s*\((disease|disorder)\)\s*", " ", name, flags=re.I)
    return re.sub(r"\s+", " ", name).strip().replace('"', "")


def known_predictions(approved_indication: str, predicted: list) -> list:
    """預測中屬於已知原適應症者：用 is_known_indication 的嚴格比對（正規化後同名，或一方只多 type 2／subtype A
    等限定詞）；不用關鍵字模糊比對，避免把 HCV 當成 HBV 的已知用途、把 pulmonary hypertension 當成 hypertension。"""
    return [p for p in predicted if is_known_indication(approved_indication, p)]


def _first_posted(study: dict) -> str:
    return ((study.get("protocolSection", {}).get("statusModule", {}) or {})
            .get("studyFirstPostDateStruct", {}) or {}).get("date", "")


def _trial_hits(study: dict, indications: list) -> list:
    """試驗 condition 直接對到哪些預測新適應症（沿用原本 issue 內文「Matched predicted indication」的比對規則）。"""
    conds = [c.lower() for c in study.get("protocolSection", {}).get("conditionsModule", {}).get("conditions", []) if c]
    return [i for i in indications
            if any(_clean_condition(i).lower() in c or c in _clean_condition(i).lower() for c in conds)]


def search_trials(drug_name: str, days_back: int = 7, conditions: list = None) -> list:
    """Search for trials updated in the last N days.

    2026-10-16：conditions 給預測新適應症時，只抓「藥＋這些疾病」的試驗。
    2026-11-03：查詢範圍不變（LastUpdatePostDate 窗），多取 StudyFirstPostDate 供判斷是否為新登錄試驗。
    """
    min_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")

    params = {
        "query.intr": drug_name,
        "filter.advanced": f"AREA[LastUpdatePostDate]RANGE[{min_date},MAX]",
        "pageSize": 50,
        "fields": "NCTId,BriefTitle,OverallStatus,Phase,EnrollmentCount,Condition,LastUpdatePostDate,StudyFirstPostDate,InterventionName,InterventionType,InterventionOtherName"
    }
    # ClinicalTrials.gov 對過長片語回 400「Too complicated query」：略過超過 6 個字的疾病名
    conds = [f'"{_clean_condition(c)}"' for c in (conditions or [])
             if len(_clean_condition(c)) > 3 and len(_clean_condition(c).split()) <= 6]
    if conditions and not conds:
        return []
    if conds:
        params["query.cond"] = " OR ".join(conds)

    try:
        response = requests.get(API_BASE, params=params, timeout=30)
        if response.status_code == 400 and len(conds) > 3:
            params["query.cond"] = " OR ".join(conds[:3])
            response = requests.get(API_BASE, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        return [s for s in data.get("studies", []) if _role_bound(s, drug_name)]
    except requests.RequestException as e:
        print(f"Error searching trials for {drug_name}: {e}")
        return []


ROLE_PATTERNS = [
    (r"refractory|relapsed|after failure|inadequate response|switch(ing)? (from|to)|prior (therapy|treatment)|resistant to", "drug may be prior/frontline therapy, not the tested intervention"),
    (r"conditioning|myeloablative|transplant", "drug may be used as transplant conditioning"),
    (r"versus|vs\.?|compared with|comparator", "comparative study — check whether the drug is the comparator arm"),
]


def _role_flags(text: str) -> str:
    """N-02：標出需要人工判讀藥物角色的試驗（以標題關鍵字判斷，僅供提示）。"""
    t = (text or "").lower()
    return "; ".join(msg for pat, msg in ROLE_PATTERNS if re.search(pat, t))


def create_github_issue(drug_name: str, new_trials: list, indications: list = None, other_new: int = 0):
    """Create a GitHub Issue for new trials found.

    new_trials 只放直接命中預測的試驗；indications 只放命中的預測；other_new 是其餘未命中的新試驗數（只記 cache）。
    """
    indications = indications or []
    ind_label = "; ".join(indications[:2]) + (" …" if len(indications) > 2 else "")
    title = f"🔬 New Clinical Trials: {drug_name} ({len(new_trials)} trials)"
    if ind_label:
        title += f" → {ind_label}"  # 接在數量後面，github_utils 以「：…(」擷取藥名才對得上

    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would create issue for {drug_name} with {len(new_trials)} new trials")
        for trial in new_trials[:3]:
            nct_id = trial.get("protocolSection", {}).get("identificationModule", {}).get("nctId", "Unknown")
            brief_title = trial.get("protocolSection", {}).get("identificationModule", {}).get("briefTitle", "Unknown")
            print(f"  - {nct_id}: {brief_title[:60]}...")
        return

    # Close older issues for this drug before creating a new one
    closed_count = close_older_clinicaltrials_issues(drug_name)
    if closed_count > 0:
        print(f"  → Closed {closed_count} older issue(s) for {drug_name}")

    # Format trial details
    trial_details = []
    for trial in new_trials:
        protocol = trial.get("protocolSection", {})
        id_module = protocol.get("identificationModule", {})
        status_module = protocol.get("statusModule", {})
        design_module = protocol.get("designModule", {})

        nct_id = id_module.get("nctId", "Unknown")
        brief_title = id_module.get("briefTitle", "Unknown")
        status = status_module.get("overallStatus", "Unknown")
        phase = ", ".join(design_module.get("phases", ["Unknown"]))
        enrollment = design_module.get("enrollmentInfo", {}).get("count", "Unknown")

        conds = protocol.get("conditionsModule", {}).get("conditions", [])
        hit = _trial_hits(trial, indications or [])
        role = _role_flags(brief_title)
        trial_details.append(
            f"### {nct_id}\n"
            f"- **Title**: {brief_title}\n"
            f"- **Conditions**: {'; '.join(conds) if conds else '-'}\n"
            f"- **Matched predicted indication**: {'; '.join(hit) if hit else '(no direct condition match)'}\n"
            + (f"- **⚠ Role flag**: {role}\n" if role else "")
            + f"- **First posted**: {_first_posted(trial) or 'Unknown'}\n"
            f"- **Status**: {status}\n"
            f"- **Phase**: {phase}\n"
            f"- **Enrollment**: {enrollment}\n"
            f"- **Link**: https://clinicaltrials.gov/study/{nct_id}\n"
        )

    body = f"""## 🔬 New Clinical Trials Detected

This issue was automatically created by GitHub Actions.

### Drug Name
{drug_name}

### Predicted New Indication(s)
{chr(10).join("- " + x for x in indications) if indications else "-"}

### NCT IDs
{", ".join(t.get("protocolSection", {}).get("identificationModule", {}).get("nctId", "") for t in new_trials)}

### Data Source
ClinicalTrials.gov

### Evidence Type
New Clinical Trials (first posted within the check window, condition directly matches a predicted indication)

### Details
Found **{len(new_trials)}** new clinical trials matching a predicted indication:

{"".join(trial_details)}{f"{chr(10)}_{other_new} other new trial(s) without a direct condition match were recorded in the cache only._{chr(10)}" if other_new else ""}

### Suggested Actions
- [ ] Review trial details
- [ ] Evaluate if drug report evidence level needs updating
- [ ] Add trial information to report

---
*Auto-detected at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    # Create the issue with deduplication check
    labels = ["auto-detected", "needs-review", "clinicaltrials"]
    create_issue(title, body, labels)


def main():
    print("=" * 60)
    print("ClinicalTrials.gov Evidence Checker")
    print("(Filtering out known/approved indications)")
    print(f"Started at: {datetime.now().isoformat()}")
    print("=" * 60)

    # Load data
    cache = load_cache()
    drugs = load_drug_list()

    print(f"Loaded {len(drugs)} drugs from drug list")
    print(f"Last check: {cache.get('last_check', 'Never')}")

    # Check each drug
    new_findings = []
    seen_trials = cache.get("seen_trials", {})
    skipped_known = 0
    days_back = 7
    min_first_post = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    stats = {"updated_only": 0, "no_direct_match": 0}

    for i, drug in enumerate(drugs):
        drug_name = drug["name"]

        predicted = drug.get("predicted_indications") or []
        if not predicted or not drug.get("inn"):
            continue

        # Skip predictions that are known/approved indications (exact match with KG original indications)
        known = known_predictions(drug.get("approved_indication", ""), predicted)
        eligible = [x for x in predicted if x not in known]
        if not eligible:
            skipped_known += 1
            continue

        print(f"\n[{i+1}/{len(drugs)}] Checking: {drug_name}")

        trials = search_trials(drug["inn"], days_back=days_back, conditions=predicted)
        time.sleep(RATE_LIMIT_DELAY)

        if not trials:
            continue

        # Filter to truly new trials
        drug_seen = seen_trials.get(drug_name, [])
        is_initial_discovery = not drug_seen  # First time checking this drug
        new_trials = []

        for trial in trials:
            nct_id = trial.get("protocolSection", {}).get("identificationModule", {}).get("nctId")
            if nct_id and nct_id not in drug_seen:
                new_trials.append(trial)
                drug_seen.append(nct_id)

        if new_trials:
            # 新登錄（StudyFirstPostDate 在窗內）才算新試驗；只更新的舊試驗只記 cache
            first_posted = [t for t in new_trials if _first_posted(t) >= min_first_post]
            hit_trials = [t for t in first_posted if _trial_hits(t, eligible)]
            print(f"  [eval] unseen={len(new_trials)} first_posted={len(first_posted)} direct_hit={len(hit_trials)}")
            # Skip issue creation for initial discovery (first time seeing this drug)
            if is_initial_discovery:
                print(f"  Initial discovery: {len(new_trials)} trials (baseline established)")
            # Skip if only 1 trial - wait for more evidence
            elif len(first_posted) < 2:
                if len(first_posted) < len(new_trials):
                    stats["updated_only"] += 1
                print(f"  Only {len(first_posted)} newly posted trial(s) "
                      f"({len(new_trials) - len(first_posted)} updated older trial(s) cached only) - below threshold")
            elif not hit_trials:
                stats["no_direct_match"] += 1
                print(f"  {len(first_posted)} new trials, none directly matches a predicted indication - cached only")
            else:
                print(f"  Found {len(hit_trials)} new trials matching predicted indications!")
                hits = {x for t in hit_trials for x in _trial_hits(t, eligible)}
                new_findings.append({
                    "drug": drug_name,
                    "trials": hit_trials,
                    "indications": [x for x in eligible if x in hits],
                    "other_new": len(first_posted) - len(hit_trials),
                })

        # Update seen trials
        seen_trials[drug_name] = drug_seen

    # Update cache
    cache["seen_trials"] = seen_trials
    save_cache(cache)

    # Create issues for new findings
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Skipped (known indications): {skipped_known}")
    print(f"Not opened - only updated older trials: {stats['updated_only']}")
    print(f"Not opened - no direct predicted-indication match: {stats['no_direct_match']}")

    if new_findings:
        print(f"New findings: {len(new_findings)}")
        print("\nCreating Issues...")
        for finding in new_findings:
            create_github_issue(finding["drug"], finding["trials"], finding["indications"], finding["other_new"])
    else:
        print("No new trials found.")

    print(f"\nCompleted at: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
