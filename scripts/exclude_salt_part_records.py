"""證據包排除「本藥只是另一個藥的鹽類／共晶／溶劑合物／配位基部分」的 NPRA 登記（2026-11-24 第三輪，用戶決定；全程不用 AI）。

背景：原收集器（src/mytxgnn/collectors/npra.py 的 _search_drugs）依頁名子字串比對 product／active_ingredient／generic_name，
所以 arginine 頁收進 COVERSYL 5MG（PERINDOPRIL ARGININE；成分是 perindopril，arginine 只是鹽類），程式表還列成 Bahan tunggal；
同類還有 potassium_chloride 收進 Glucosamine Sulfate Potassium Chloride（成分是 glucosamine sulfate，KCl 是複鹽的穩定劑）等。
這些登記的有效成分不是本藥，不屬於本藥的市場事實。

規則（下表 SALT_PART，每筆附依據；只列這幾類，不放寬到一般的子字串誤收）：
- 某登記 active_ingredient 的每個成分（「名稱[劑量]」）裡，含本藥名稱（整字）的成分都符合表上的「另一個藥」寫法，
  而且沒有任何一個成分本身就是本藥（同 scripts/rebuild_licenses_by_ingredient.py 的成分主體比法，或去掉鹽類／水合物／藥典字樣後只剩本藥）
  → 從 npra.records 移到 npra.excluded_records（原紀錄照存，加 excluded_reason、excluded_basis、excluded＝日期），不刪資料。
- 同一個證據包又在 records 裡出現同一號碼（例如之後重新收集）時，重跑會再排除；排除過的號碼不會被
  rebuild_licenses_by_ingredient.py 補回（它跳過 excluded_records 的號碼）。
- 只動證據包；狀態列、張數列、程式表、快照由之後的 license_refresh／build_license_snapshot 依新證據包重算。
每週排程（.github/workflows/license-refresh.yml）在 merge_duplicate_bundles.py 之後、license_refresh 之前跑；重新收集證據包之後也要再跑。
用法（repo 根目錄）：python3 scripts/exclude_salt_part_records.py [--dry-run] [--report out.tsv]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
sys.path.insert(0, str(ROOT / "scripts"))
import rebuild_licenses_by_ingredient as rb  # noqa: E402

TODAY = "2026-11-24"
# 證據包名 → [(本藥名稱在成分裡的寫法, 另一個藥的成分寫法（正規化後的 regex）, 依據)]
SALT_PART = {
    "arginine": [("arginine", r"\bperindopril arginine\b",
                  "perindopril arginine 是 perindopril 的 L-arginine 鹽（ACE 抑制劑 COVERSYL／Triveram 等），有效成分是 perindopril")],
    "potassium_chloride": [("potassium chloride", r"\bglucosamine (sulfate|sulphate) potassium chloride\b",
                            "glucosamine sulfate potassium chloride 是 glucosamine sulfate 以氯化鉀穩定的複鹽，有效成分是 glucosamine")],
    "sodium_chloride": [("sodium chloride", r"\bglucosamine (sulfate|sulphate) sodium chloride\b",
                         "glucosamine sulfate sodium chloride 是 glucosamine sulfate 以氯化鈉穩定的複鹽，有效成分是 glucosamine")],
    "potassium_acetate": [("potassium acetate", r"\bhydroxymatairesinol potassium acetate\b",
                           "7-hydroxymatairesinol potassium acetate 是木酚素 7-hydroxymatairesinol 的鉀鹽／醋酸鉀錯合物，有效成分是 7-hydroxymatairesinol")],
    "mannitol": [("mannitol", r"\bdapagliflozin mannitol\b",
                  "dapagliflozin mannitol 是 dapagliflozin 與甘露醇的共晶（Dapamac），有效成分是 dapagliflozin")],
    "propylene_glycol": [("propylene glycol", r"\bdasatinib (s )?propylene glycol\b",
                          "dasatinib (S)-propylene glycol 是 dasatinib 的丙二醇溶劑合物，有效成分是 dasatinib")],
    "polyethylene_glycol": [("polyethylene glycol", r"\bmethoxy polyethylene glycol epoetin beta\b",
                             "methoxy polyethylene glycol-epoetin beta 是 PEG 化的 epoetin beta（MIRCERA），有效成分是 epoetin beta")],
    "sodium_phosphate": [("sodium phosphate", r"\b(betamethasone|dexamethasone|prednisolone|riboflavin( 5)?) (di)?sodium phosphate\b",
                          "betamethasone／dexamethasone／prednisolone／riboflavin sodium phosphate 是該藥的磷酸鈉酯鹽，有效成分是該藥")],
    "zinc": [("zinc", r"\bbacitracin zinc\b", "bacitracin zinc 是 bacitracin 的鋅鹽（外用抗生素），有效成分是 bacitracin")],
    "methionine": [("methionine", r"^(zinc methionine|methionine bound zinc complex)\b",
                    "zinc methionine 是鋅的甲硫胺酸螯合物（鋅補充劑），有效成分是鋅；甲硫胺酸只是配位基")],
}
NOISE = re.compile(r"\b(" + rb.SALT + r"|ph eur|pheur|eur|ph|usp|bp|ip|jp|ep|b p|u s p|heptahydrate|\d+h2o|\d+)\b")


def rid(r):
    return str(r.get("reg_no") or "").strip()


def is_self(page, comps):
    """有成分本身就是本藥（主體比法同 rebuild_licenses_by_ingredient；或去掉鹽類／水合物／藥典字樣後只剩本藥名稱）"""
    terms, salt_named = rb.terms_for(page)
    full = rb.norm(page.replace("_", " "))
    for c in comps:
        if rb.base(c, keep_salt=salt_named) in terms:
            return True
        if re.search(r"\b" + re.escape(full) + r"\b", c):
            rest = " ".join(NOISE.sub(" ", re.sub(r"\b" + re.escape(full) + r"\b", " ", c)).split())
            if not rest:
                return True
    return False


def salt_part(page, r):
    """(依據, 符合的成分) 或 None"""
    comps = rb.components(r.get("active_ingredient"))
    if not comps or is_self(page, comps):
        return None
    for name, rx, basis in SALT_PART.get(page, []):
        hits = [c for c in comps if re.search(r"\b" + re.escape(name) + r"\b", c)]
        if hits and all(re.search(rx, c) for c in hits):
            return basis, hits
    return None


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    out, n = [], 0
    for page in sorted(SALT_PART):
        f = BUNDLES / page / "drug_bundle.json"
        if not f.exists():
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("npra") or {}
        recs = reg.get("records") or []
        exc = reg.get("excluded_records") or []
        have_exc = {rid(x) for x in exc}
        keep, move = [], []
        for r in recs:
            hit = salt_part(page, r)
            if hit:
                move.append(r)
                out.append(f"{page}\t{rid(r)}\t{r.get('product')}\t{'; '.join(hit[1])}\t{hit[0]}")
                if rid(r) not in have_exc:
                    exc.append(dict(r, excluded_reason="本藥只是另一個藥的鹽類／共晶／溶劑合物／配位基部分（成分：" + "; ".join(hit[1]) + "）",
                                    excluded_basis=hit[0], excluded=TODAY))
                    have_exc.add(rid(r))
            else:
                keep.append(r)
        if move:
            n += len(move)
            print(f"{page}\t{len(recs)} → {len(keep)}\t排除 {len(move)}")
            if not dry:
                reg.update(records=keep, excluded_records=exc, found=bool(keep))
                b["npra"] = reg
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\treg_no\tproduct\tcomponents\tbasis\n" + "\n".join(out) + "\n", encoding="utf-8")
    print(f"共排除 {n} 筆{'（試跑）' if dry else ''}")


if __name__ == "__main__":
    main(sys.argv[1:])
