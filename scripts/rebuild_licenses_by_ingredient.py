"""MY 依成分補收證據包的許可證紀錄、並依到期日判定查不到的登記號（2026-11-05，用戶核准；全程不用 AI；做法比照 Kr／Za）。

1. 狀態：重新下載 data.gov.my 的 NPRA 現行註冊（pharmaceutical_products.csv）與撤銷清單（scripts/license_adapter.fetch）。
   現行檔的號碼 → 原文狀態（PRODUCT APPROVED／CONDITIONAL REGISTRATION）；撤銷清單 → Cancelled；
   兩份都查不到的不再預設有效：證據包紀錄的到期日（date_end）已過 → license_adapter.EXPIRED_STATUS，
   未過期 → license_adapter.UNKNOWN_STATUS（2026-11-05 用戶決定：狀態未知，不算有效也不算註銷）。
2. 補收：原收集器依藥名比對 active_ingredient，拼法不同的沒收進（selegiline 頁 0 張；NPRA 有 SELEGOS 5MG，成分寫 SELEGILIN HCL）。
   改依成分比：active_ingredient 每個成分（「名稱[含量]」）去掉鹽類／酯類／水合物字尾與括號別名後，等於本藥主體、
   或只差字尾 e（selegilin／selegiline），就補收（只補收、不刪原紀錄；複方也收，與原收集器相同）。
   頁名本身帶鹽類或 dl-／d-／l- 前綴時，只收同一個鹽／同一寫法。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--skip-download] [--dry-run] [--report out.tsv] [頁 ...]
"""
import csv
import io
import json
import re
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
RAW = ROOT / "data/raw"
sys.path.insert(0, str(ROOT / "scripts"))
import license_adapter as ad  # noqa: E402

SALT = (r"hydrochloride|hcl|hydrobromide|besylate|besilate|maleate|mesylate|mesilate|tartrate|bitartrate|fumarate|hemifumarate|succinate|"
        r"citrate|acetate|diacetate|dipropionate|propionate|valerate|butyrate|phosphate|sulfate|sulphate|nitrate|lactate|gluconate|palmitate|"
        r"hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|sesquihydrate|hemihydrate|anhydrous|hydrous|"
        r"sodium|potassium|calcium|magnesium|disodium|dipotassium|cilexetil|axetil|medoxomil|dihydrochloride|bromide|chloride|iodide|"
        r"tosylate|edisylate|pamoate|embonate|stearate|oleate|mandelate|camsylate|xinafoate|furoate|aceponate|hyclate|trometamol|tromethamine|"
        r"arginine|lysine|meglumine|olamine|erbumine|tert butylamine|benzathine|procaine|esylate|napadisilate")
SALT_RX = re.compile(r"\b(" + SALT + r")\b")
HYD_RX = re.compile(r"\b(hydrate|monohydrate|dihydrate|trihydrate|tetrahydrate|pentahydrate|hexahydrate|sesquihydrate|hemihydrate|anhydrous|hydrous)\b")
# 同一成分的別名（頁名主體 → 成分欄可能的主體寫法）
SYN = {"vitamin a": ["retinol"], "retinol": ["vitamin a"], "acetaminophen": ["paracetamol"], "paracetamol": ["acetaminophen"],
       "ascorbic acid": ["vitamin c"], "cholecalciferol": ["vitamin d3"], "ergocalciferol": ["vitamin d2"],
       "thiamine": ["vitamin b1"], "riboflavin": ["vitamin b2"], "pyridoxine": ["vitamin b6"], "cyanocobalamin": ["vitamin b12"],
       "tocopherol": ["vitamin e"], "alpha tocopherol": ["vitamin e", "tocopherol"], "epinephrine": ["adrenaline"],
       "norepinephrine": ["noradrenaline"], "acetylsalicylic acid": ["aspirin"], "levothyroxine": ["thyroxine"],
       "glyceryl trinitrate": ["nitroglycerin"], "nitroglycerin": ["glyceryl trinitrate"]}
NO_REBUILD = re.compile(r"^(calcium|copper|magnesium|zinc|iron|iodine|potassium|sodium|chromium|selenium|manganese|fluoride|chloride|"
                        r"phosphorus|phosphate|water|glucose|dextrose|oxygen|nitrogen|sodium chloride|potassium chloride|hydrogen peroxide)$")


def norm(x):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", str(x or "").lower()).split())


def base(x, keep_salt=False):
    """成分主體：去掉鹽類／酯類／水合物字尾（keep_salt 時只去水合物）"""
    t = norm(x) if keep_salt else re.sub(r"^(dl|d|l)( alpha)? (?=[a-z]{4})", "", norm(x))  # dl-／d-／l- 前綴：頁名帶前綴時只收同一寫法
    t = (HYD_RX if keep_salt else SALT_RX).sub(" ", t)
    return " ".join(t.split())


def components(text):
    names = re.findall(r"([^\[\]]+?)\[[^\]]*\]", str(text or "")) or [str(text or "")]
    out = []
    for n in names:
        n = re.sub(r"\([^)]*\)", " ", n.strip().lstrip(","))
        n = norm(n)
        if n:
            out.append(n)
    return out


def variants(t):
    return {t, t[:-1] if t.endswith("e") else t + "e"}


def terms_for(page):
    full = norm(page.replace("_", " "))
    salt_named = base(full) != base(full, keep_salt=True)
    b = base(full, keep_salt=salt_named)
    out = set()
    for t in {b} | set(SYN.get(b, [])):
        out |= variants(t)
    return {t for t in out if len(t) >= 4}, salt_named


def record(r, status):
    return {"registry": "NPRA Malaysia", "reg_no": r["reg_no"], "product": r.get("product") or "", "active_ingredient": r.get("active_ingredient") or "",
            "generic_name": r.get("generic_name") or "", "holder": r.get("holder") or "", "description": r.get("description") or "",
            "status": status, "date_reg": r.get("date_reg") or "", "date_end": r.get("date_end") or "",
            "url": f"https://npra.gov.my/index.php/search/product/{r['reg_no']}", "source": "NPRA by ingredient (2026-11-05 rebuild)"}


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    cur = RAW / "pharmaceutical_products.csv"
    if "--skip-download" not in argv:
        new = ad.fetch()
        p = ad.validate(new, None)
        if p:
            raise SystemExit("資料檢查沒過：" + "；".join(p))
        r = requests.get(ad.URL, timeout=300)
        r.raise_for_status()
        cur.write_bytes(r.content)
        (RAW / "npra_status.json").write_text(json.dumps(new, ensure_ascii=False, indent=1), encoding="utf-8")
    new = json.loads((RAW / "npra_status.json").read_text(encoding="utf-8"))
    idx = ad.status_index(new)
    rows = [x for x in csv.DictReader(io.StringIO(cur.read_bytes().decode("utf-8-sig"))) if x.get("reg_no")]
    index = {}
    for x in rows:
        for c in components(x.get("active_ingredient")):
            for keep in (False, True):
                index.setdefault((base(c, keep_salt=keep), keep), set()).add(x["reg_no"].strip())
    by_no = {x["reg_no"].strip(): x for x in rows}
    out, kept_future, n_add, n_exp, changed = [], 0, 0, 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("npra") or {}
        recs = reg.get("records") or []
        ch = False
        for r in recs:
            k = ad.record_id(r)
            if k in idx:
                ch |= ad.update(r, idx[k])
            elif ad.expired(r):
                if r.get("status") != ad.EXPIRED_STATUS:
                    r["status"] = ad.EXPIRED_STATUS; ch = True; n_exp += 1
            else:
                kept_future += 1  # 2026-11-05 用戶決定：狀態未知（不算有效也不算註銷）
                if r.get("status") != ad.UNKNOWN_STATUS:
                    r["status"] = ad.UNKNOWN_STATUS; ch = True
        terms, salt_named = terms_for(page)
        add = []
        if terms and not any(NO_REBUILD.match(t) for t in terms):
            have = {ad.record_id(r) for r in recs}
            hit = set()
            for t in terms:
                hit |= index.get((t, salt_named), set())
            add = [record(by_no[k], idx.get(k) or by_no[k].get("status") or "") for k in sorted(hit - have)]
        if add:
            b["npra"] = dict(reg, found=True, records=recs + add)
            ch = True
            n_add += len(add)
            out.append(f"{page}\t{len(recs)}\t{len(add)}\t{','.join(sorted(terms))}\t{';'.join(a['reg_no'] for a in add[:20])}")
        if ch:
            changed += 1
            if not dry:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\told_records\tadded\tterms\tadded_ids\n" + "\n".join(out) + "\n", encoding="utf-8")
    print(f"改 {changed} 個證據包：補收 {len(out)} 個藥 {n_add} 筆；查不到且已過期改 Expired {n_exp} 筆；查不到、未過期改狀態未知 {kept_future} 筆")


if __name__ == "__main__":
    main(sys.argv[1:])
