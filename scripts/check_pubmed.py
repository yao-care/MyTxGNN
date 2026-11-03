#!/usr/bin/env python3
"""
Check PubMed for new publications related to our drug list.
Creates GitHub Issues when new papers are found.

NOTE: Filters out known/approved indications to focus on repurposing evidence.

2026-11-03 門檻（查詢與 cache 結構、key 不變）：
- 至少一篇新論文的標題或摘要直接提到目前的預測新適應症才開 issue；issue 只列命中的論文，標題只掛命中的預測。
  未命中的新論文只寫入 cache。
- 已核准／已知用途：drug_list 的 approved_indication（search-index 的知識圖譜原適應症）與預測同名、或只差 type 2／subtype A 等限定詞者不算命中（見 is_known_indication）。
"""

import json
import os
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

import requests

from github_utils import create_issue, close_older_pubmed_issues


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
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
ESUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
CACHE_FILE = Path(__file__).parent.parent / "data" / "cache" / "pubmed_cache.json"
DRUG_LIST_FILE = Path(__file__).parent / "drug_list.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/EuTxGNN")
NCBI_API_KEY = os.environ.get("NCBI_API_KEY")  # Optional, for higher rate limits
RATE_LIMIT_DELAY = 0.4 if NCBI_API_KEY else 1.0  # seconds between API calls


def load_cache() -> dict:
    """Load the cache of previously seen PMIDs."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": None, "seen_pmids": {}}


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


def search_pubmed(drug_name: str, indication: str = "", days_back: int = 7) -> list:
    """Search PubMed for recent publications."""
    # Build search query
    query_parts = [f'"{drug_name}"[Title/Abstract]']
    if indication:
        # Clean up indication text
        indication = indication.split("(")[0].strip()
        if indication and len(indication) > 3:
            query_parts.append(f'"{indication}"[Title/Abstract]')

    query = " AND ".join(query_parts)

    params = {
        "db": "pubmed",
        "term": query,
        "datetype": "edat",  # Entry date
        "reldate": days_back,  # Last N days
        "retmode": "json",
        "retmax": 50,
        "sort": "date"
    }

    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    try:
        response = requests.get(ESEARCH_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        id_list = data.get("esearchresult", {}).get("idlist", [])
        return id_list
    except requests.RequestException as e:
        print(f"Error searching PubMed for {drug_name}: {e}")
        return []


def _clean_indication(name: str) -> str:
    name = re.sub(r"\s*\((disease|disorder)\)\s*", " ", name, flags=re.I)
    return re.sub(r"\s+", " ", name).strip().replace('"', "")


def search_pubmed_predicted(inn: str, indications: list, days_back: int = 7) -> list:
    """2026-10-16：查「INN AND (預測新適應症1 OR …)」，只抓和預測有關的新文獻。"""
    terms = [f'"{_clean_indication(i)}"[Title/Abstract]' for i in indications if len(_clean_indication(i)) > 3]
    if not terms:
        return []
    query = f'"{inn}"[Title/Abstract] AND (' + " OR ".join(terms) + ")"
    params = {
        "db": "pubmed",
        "term": query,
        "datetype": "edat",
        "reldate": days_back,
        "retmode": "json",
        "retmax": 50,
        "sort": "date",
    }
    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY
    try:
        response = requests.get(ESEARCH_URL, params=params, timeout=30)
        response.raise_for_status()
        return response.json().get("esearchresult", {}).get("idlist", [])
    except requests.RequestException as e:
        print(f"Error searching PubMed for {inn}: {e}")
        return []


ROLE_PATTERNS = [
    (r"refractory|relapsed|after failure|inadequate response|switch(ing)? (from|to)|prior (therapy|treatment)|resistant to", "drug may be prior/frontline therapy, not the tested intervention"),
    (r"conditioning|myeloablative|before (stem cell|bone marrow) transplant|transplant(ation)? regimen", "drug may be used as transplant conditioning"),
    (r"versus|vs\.?|compared with|comparator|placebo-controlled", "comparative study — check whether the drug is the comparator arm"),
    (r"adverse|toxicity|induced|associated with .* use|case of .* after", "may describe an adverse effect rather than efficacy"),
]


def _role_flags(text: str) -> str:
    """N-02：標出「藥只是前線治療／條件療法／對照組／不良反應」等需要人工判讀的情況（以標題關鍵字判斷，僅供提示）。"""
    t = (text or "").lower()
    return "; ".join(msg for pat, msg in ROLE_PATTERNS if re.search(pat, t))


def _norm_text(text: str) -> str:
    return " " + " ".join(re.sub(r"[^\w]+", " ", (text or "").lower()).split()) + " "


def known_predictions(approved_indication: str, predicted: list) -> list:
    """預測中屬於已知原適應症者：用 is_known_indication 的嚴格比對（正規化後同名，或一方只多 type 2／subtype A
    等限定詞）；不用關鍵字模糊比對，避免把 HCV 當成 HBV 的已知用途、把 pulmonary hypertension 當成 hypertension。"""
    return [p for p in predicted if is_known_indication(approved_indication, p)]


def text_hits(text: str, indications: list) -> list:
    """文字中直接提到哪些預測新適應症（沿用標題比對：清掉 (disease) 後的整段名稱出現在文字中；標點視為空白）。"""
    hay = _norm_text(text)
    return [i for i in indications if _norm_text(_clean_indication(i)).strip()
            and " " + _norm_text(_clean_indication(i)).strip() in hay]


def get_abstracts(pmids: list) -> dict:
    """efetch 取摘要（只對標題未命中的新論文查）；失敗回空 dict（等同只看標題，寧可不開 issue）。"""
    if not pmids:
        return {}
    params = {"db": "pubmed", "id": ",".join(pmids), "rettype": "abstract", "retmode": "xml"}
    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY
    try:
        response = requests.get(EFETCH_URL, params=params, timeout=60)
        response.raise_for_status()
        root = ET.fromstring(response.content)
    except (requests.RequestException, ET.ParseError) as e:
        print(f"Error getting abstracts: {e}")
        return {}
    out = {}
    for art in root.iter("PubmedArticle"):
        pmid = art.findtext("MedlineCitation/PMID") or ""
        out[pmid] = " ".join("".join(t.itertext()) for t in art.iter("AbstractText"))
    return out


def mark_hits(papers: list, indications: list):
    """在每篇 paper 寫入 matched（命中的預測）與 matched_in（title／abstract）。"""
    for p in papers:
        p["matched"] = text_hits(p.get("title", ""), indications)
        p["matched_in"] = "title" if p["matched"] else ""
    need = [p["pmid"] for p in papers if not p["matched"]]
    if need:
        abstracts = get_abstracts(need)
        time.sleep(RATE_LIMIT_DELAY)
        for p in papers:
            if not p["matched"] and abstracts.get(p["pmid"]):
                p["matched"] = text_hits(abstracts[p["pmid"]], indications)
                p["matched_in"] = "abstract" if p["matched"] else ""


def matched_indications(papers: list, indications: list) -> list:
    """以論文標題比對命中哪些預測新適應症；比對不到就回傳空串列。"""
    titles = " ".join(p.get("title", "") for p in papers).lower()
    return [i for i in indications if _clean_indication(i).lower() in titles]


def get_paper_details(pmids: list) -> list:
    """Get details for a list of PMIDs."""
    if not pmids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json"
    }

    if NCBI_API_KEY:
        params["api_key"] = NCBI_API_KEY

    try:
        response = requests.get(ESUMMARY_URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        result = data.get("result", {})
        papers = []

        for pmid in pmids:
            paper_data = result.get(pmid, {})
            if paper_data and "title" in paper_data:
                papers.append({
                    "pmid": pmid,
                    "title": paper_data.get("title", ""),
                    "source": paper_data.get("source", ""),
                    "pubdate": paper_data.get("pubdate", ""),
                    "authors": [a.get("name", "") for a in paper_data.get("authors", [])[:3]]
                })

        return papers
    except requests.RequestException as e:
        print(f"Error getting paper details: {e}")
        return []


def create_github_issue(drug_name: str, new_papers: list, indications: list = None, other_new: int = 0):
    """Create a GitHub Issue for new papers found.

    new_papers 只放直接命中預測的論文；indications 只放命中的預測；other_new 是其餘未命中的新論文數（只記 cache）。
    """
    indications = indications or []
    ind_label = "; ".join(indications[:2]) + (" …" if len(indications) > 2 else "")
    title = f"📚 New Publications: {drug_name} ({len(new_papers)} papers)"
    if ind_label:
        title += f" → {ind_label}"  # 接在數量後面，github_utils 以「：…(」擷取藥名才對得上

    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Would create issue for {drug_name} with {len(new_papers)} new papers")
        for paper in new_papers[:3]:
            print(f"  - PMID {paper['pmid']}: {paper['title'][:60]}...")
        return

    # Close older issues for this drug before creating a new one
    closed_count = close_older_pubmed_issues(drug_name)
    if closed_count > 0:
        print(f"  → Closed {closed_count} older issue(s) for {drug_name}")

    # Format paper details
    paper_details = []
    for paper in new_papers:
        authors = ", ".join(paper["authors"]) + (" et al." if len(paper["authors"]) >= 3 else "")
        hit = paper.get("matched") or text_hits(paper["title"], indications)
        where = f" (in {paper['matched_in']})" if paper.get("matched_in") else ""
        role = _role_flags(paper["title"])
        paper_details.append(
            f"### PMID: {paper['pmid']}\n"
            f"- **Title**: {paper['title']}\n"
            f"- **Matched predicted indication**: {'; '.join(hit) + where if hit else '(no direct match)'}\n"
            + (f"- **⚠ Role flag**: {role}\n" if role else "")
            + f"- **Journal**: {paper['source']}\n"
            f"- **Publication Date**: {paper['pubdate']}\n"
            f"- **Authors**: {authors}\n"
            f"- **Link**: https://pubmed.ncbi.nlm.nih.gov/{paper['pmid']}/\n"
        )

    body = f"""## 📚 New Publications Detected

This issue was automatically created by GitHub Actions.

### Drug Name
{drug_name}

### Predicted New Indication(s)
{chr(10).join("- " + x for x in indications) if indications else "-"}

### PMIDs
{", ".join(p["pmid"] for p in new_papers)}

### Data Source
PubMed

### Evidence Type
New Academic Publications (title or abstract directly mentions a predicted indication)

### Details
Found **{len(new_papers)}** new publications matching a predicted indication:

{"".join(paper_details)}{f"{chr(10)}_{other_new} other new publication(s) without a direct match were recorded in the cache only._{chr(10)}" if other_new else ""}

### Suggested Actions
- [ ] Review paper abstracts
- [ ] Evaluate publication type (RCT, observational, case report, etc.)
- [ ] Evaluate if drug report evidence level needs updating
- [ ] Add publication information to report

---
*Auto-detected at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    # Create the issue with deduplication check
    labels = ["auto-detected", "needs-review", "pubmed"]
    create_issue(title, body, labels)


def main():
    print("=" * 60)
    print("PubMed Evidence Checker")
    print("(Filtering out known/approved indications)")
    print(f"Started at: {datetime.now().isoformat()}")
    print(f"NCBI API Key: {'Configured' if NCBI_API_KEY else 'Not configured (slower rate limit)'}")
    print("=" * 60)

    # Load data
    cache = load_cache()
    drugs = load_drug_list()

    print(f"Loaded {len(drugs)} drugs from drug list")
    print(f"Last check: {cache.get('last_check', 'Never')}")

    # Check each drug
    new_findings = []
    seen_pmids = cache.get("seen_pmids", {})
    skipped_known = 0
    no_direct_match = 0

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

        pmids = search_pubmed_predicted(drug["inn"], predicted, days_back=7)
        time.sleep(RATE_LIMIT_DELAY)

        if not pmids:
            continue

        # Filter to truly new papers
        drug_seen = seen_pmids.get(drug_name, [])
        is_initial_discovery = not drug_seen  # First time checking this drug
        new_pmids = [p for p in pmids if p not in drug_seen]

        if new_pmids:
            # Get paper details
            papers = get_paper_details(new_pmids)
            time.sleep(RATE_LIMIT_DELAY)

            if papers:
                # Skip issue creation for initial discovery
                if is_initial_discovery:
                    print(f"  Initial discovery: {len(papers)} papers (baseline established)")
                # Skip if only 1 paper - wait for more evidence
                elif len(papers) < 2:
                    print(f"  [eval] unseen=1 direct_hit=-")
                    print(f"  Only {len(papers)} paper found - below threshold")
                else:
                    mark_hits(papers, eligible)
                    hit_papers = [p for p in papers if p["matched"]]
                    print(f"  [eval] unseen={len(papers)} direct_hit={len(hit_papers)}")
                    if not hit_papers:
                        no_direct_match += 1
                        print(f"  {len(papers)} new papers, none directly mentions a predicted indication - cached only")
                    else:
                        print(f"  Found {len(hit_papers)} new papers matching predicted indications!")
                        hits = {x for p in hit_papers for x in p["matched"]}
                        new_findings.append({
                            "drug": drug_name,
                            "papers": hit_papers,
                            "indications": [x for x in eligible if x in hits],
                            "other_new": len(papers) - len(hit_papers),
                        })

            # Update seen PMIDs
            drug_seen.extend(new_pmids)

        seen_pmids[drug_name] = drug_seen

    # Update cache
    cache["seen_pmids"] = seen_pmids
    save_cache(cache)

    # Create issues for new findings
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Skipped (known indications): {skipped_known}")
    print(f"Not opened - no direct predicted-indication match: {no_direct_match}")

    if new_findings:
        print(f"New findings: {len(new_findings)}")
        print("\nCreating Issues...")
        for finding in new_findings:
            create_github_issue(finding["drug"], finding["papers"], finding["indications"], finding["other_new"])
    else:
        print("No new papers found.")

    print(f"\nCompleted at: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
