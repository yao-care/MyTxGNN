#!/usr/bin/env python3
"""產生許可證快照 snapshots/<站碼>_licenses.json.gz（2026-11-12 建，本站查核機制；比照 TwTxGNN snapshots/tfda_licenses.json.gz）。

gate（scripts/check_seo_docs.py）要在沒有 data/ 的環境也能驗證頁面上的號碼屬於本藥、狀態列與張數列跟事實一致
（有程式許可證表的站另驗程式表），所以把驗證要用的部分存成快照放進 git。
內容（鍵＝藥物頁檔名去 .md）：facts（事實層那一筆）、own（本藥擁有的許可證號）、rows／total（有程式表的站：程式算出的表格列與總數）；
meta：產生日、Release tag、規則所在檔案。
什麼時候跑：證據包或事實層變了之後（每週許可證排程、依成分重建都會自動跑，並把 snapshots/ 跟 docs/ 一起 commit）。
用法（repo 根目錄，先還原 data/ 並在工作目錄跑 dump_license_facts）：
  python3 scripts/build_license_snapshot.py --ws <工作目錄> [--release-tag data-YYYYMMDD-HHMMSS]
"""
import datetime as dt
import gzip
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from mytxgnn.regulatory import site as C  # noqa: E402

OUT = ROOT / "snapshots" / f"{C.CODE}_licenses.json.gz"
SLT = ROOT / "scripts" / getattr(C, "PROGRAM_SCRIPT", "sync_license_tables.py")  # 產生程式許可證表的本站程式（有 rows_of 才用）


def _slt():
    if not SLT.exists():
        return None
    s = importlib.util.spec_from_file_location(f"{C.SITE}_slt", SLT)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m if hasattr(m, "rows_of") else None


def bundle_for(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return key, json.loads(f.read_text(encoding="utf-8"))
    return None, None


def build(ws, tag=""):
    p = Path(ws) / ".claude/cache/license_facts" / f"{C.SITE}.json"
    if not p.exists():
        sys.exit(f"找不到事實層 {p}（先跑 dump_license_facts）")
    fs = json.loads(p.read_text(encoding="utf-8"))
    S = _slt()
    drugs = {}
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        head = page.read_text(encoding="utf-8", errors="replace")[:3000]
        if "layout: id_redirect" in head or 'http-equiv="refresh"' in head:
            continue
        key, b = bundle_for(page.stem)
        if b is None:
            continue
        tf = b.get(C.BUNDLE_KEY) or {}
        fc = fs.get(key) or fs.get(page.stem) or fs.get(page.stem.replace("-", "_"))
        e = {"bundle": key, "facts": fc, "own": C.own_ids(tf)}
        if S is not None:
            r, total = S.rows_of(tf, fc)
            e["rows"], e["total"] = r[:20], total
        drugs[page.stem] = e
    meta = {"built": dt.date.today().isoformat(), "release_tag": tag, "pages": len(drugs),
            "rule": "事實層：tools/txgnn/.claude/dump_license_facts_20261021.py；號碼：src/mytxgnn/regulatory/site.py own_ids"}
    OUT.parent.mkdir(exist_ok=True)
    raw = json.dumps({"meta": meta, "drugs": drugs}, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with gzip.GzipFile(OUT, "wb", mtime=0) as fh:
        fh.write(raw)
    print(f"許可證快照：{len(drugs)} 頁 → {OUT.relative_to(ROOT)}（{OUT.stat().st_size // 1024} KB）")


if __name__ == "__main__":
    a = sys.argv[1:]
    ws = a[a.index("--ws") + 1]
    tag = a[a.index("--release-tag") + 1] if "--release-tag" in a else ""
    if not re.fullmatch(r"(data-[\w-]+)?", tag):
        sys.exit("--release-tag 要是 data-… 的 tag")
    build(ws, tag)
    # 2026-11-12：快照換了事實，正文許可證張數跟著改寫（每週排程是先套紀錄再建快照，所以這裡用新快照再跑一次）
    import subprocess
    subprocess.run([sys.executable, str(ROOT / "scripts" / "rewrite_license_counts.py")], check=True)
