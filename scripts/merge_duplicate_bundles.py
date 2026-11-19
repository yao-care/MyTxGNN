"""同一 DrugBank ID 的重複公開頁「合併後轉址」：把被轉址頁的 NPRA 登記號併進保留頁的證據包（2026-11-19，用戶決定）。

背景：公開藥物頁 amlodipine_besilate／amlodipine_besylate（DB00381）、diphenhydramine_hcl／diphenhydramine_hydrochloride（DB01075）、
ambroxol_hcl／ambroxol_hydrochloride（DB06742）預測相同，但原收集器依頁名的成分寫法比對 NPRA active_ingredient，
同一個鹽寫成 besilate／besylate、HCl／Hydrochloride 就收在不同頁，兩頁的登記號只有部分重疊（共同 3、19、0 張），
所以 11-19 第一輪轉址時沒轉。用戶決定合併：被轉址頁改轉址，它的登記號併進保留頁的證據包。

收錄規則（照本站原規則，不放寬）：保留頁證據包原有的紀錄＋被轉址頁證據包的紀錄（原收集器與 2026-11-05 依成分補收收進來的，
欄位與狀態照原樣），依 reg_no 去重，另記 merged_from（被轉址頁證據包名）、added。之後新註冊的另一種寫法由
scripts/rebuild_licenses_by_ingredient.py 的 MERGE_TERMS 收進保留頁。狀態照每週排程（license_adapter）更新；
舊號、新號（換尾碼）合併後落在同一個證據包時，排程的 preprocess 會把舊號標 RETIRED_STATUS（不算兩張）。
只加不刪、可重複執行；重新收集證據包之後要再跑一次。每週排程（license-refresh.yml）在 license_refresh 前先跑。
用法（repo 根目錄）：python3 scripts/merge_duplicate_bundles.py [--dry-run]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
ADDED = "2026-11-19"

# 保留頁證據包 → 被轉址頁證據包（保留頁照 2026-11-19 規則：查核紀錄數→字數（差 5% 內算平手）→NPRA 成分名寫法）
MERGES = {
    "amlodipine_besilate": ["amlodipine_besylate"],
    "diphenhydramine_hcl": ["diphenhydramine_hydrochloride"],
    "ambroxol_hydrochloride": ["ambroxol_hcl"],
}


def rid(r):
    return str(r.get("reg_no") or r.get("license_id") or "").strip()


def main(argv):
    dry = "--dry-run" in argv
    for keep, drops in MERGES.items():
        f = BUNDLES / keep / "drug_bundle.json"
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.setdefault("npra", {})
        recs = reg.get("records") or []
        have = {rid(r) for r in recs}
        add = []
        for d in drops:
            for r in (json.loads((BUNDLES / d / "drug_bundle.json").read_text(encoding="utf-8")).get("npra") or {}).get("records") or []:
                k = rid(r)
                if k and k not in have:
                    have.add(k)
                    add.append(dict(r, merged_from=d, added=ADDED))
        print(f"{keep}\t{len(recs)} → {len(recs) + len(add)} 個登記號\t補 {len(add)}（自 {','.join(drops)}）")
        if add and not dry:
            reg.update(found=True, records=recs + add)
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
