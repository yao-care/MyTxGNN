#!/usr/bin/env python3
"""產生許可證快照 snapshots/<站碼>_licenses.json.gz（2026-11-12 建，本站查核機制；比照 TwTxGNN snapshots/tfda_licenses.json.gz）。

gate（scripts/check_seo_docs.py）要在沒有 data/ 的環境也能驗證頁面上的號碼屬於本藥、狀態列與張數列跟事實一致
（有程式許可證表的站另驗程式表），所以把驗證要用的部分存成快照放進 git。
內容（鍵＝藥物頁檔名去 .md）：facts（事實層那一筆）、own（本藥擁有的許可證號）、rows／nrows（2026-11-24 起：市場段落程式許可證表
最多可列的 30 列與可列總數，scripts/sync_license_tables.py 的 program_rows；gate 比頁面上的前 N 列）；
meta：產生日、Release tag、規則所在檔案。
什麼時候跑：證據包或事實層變了之後（每週許可證排程、依成分重建都會自動跑，並把 snapshots/ 跟 docs/ 一起 commit）。
用法（repo 根目錄，先還原 data/ 並在工作目錄跑 dump_license_facts）：
  python3 scripts/build_license_snapshot.py --ws <工作目錄> [--release-tag data-YYYYMMDD-HHMMSS]
  python3 scripts/build_license_snapshot.py   （不帶 --ws：不重建快照，只重排程式表＋正文張數改寫；2026-11-24）
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
    return m if hasattr(m, "program_rows") else None


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
        if S is not None:  # 2026-11-24：市場段落程式許可證表最多可列的 30 列與可列總數（選列依 config/license_table_pins.json）
            e["rows"], e["nrows"] = S.program_rows(tf, fc, S.pins_for(page.stem))
        drugs[page.stem] = e
    meta = {"built": dt.date.today().isoformat(), "release_tag": tag, "pages": len(drugs),
            "rule": "事實層：tools/txgnn/.claude/dump_license_facts_20261021.py；號碼：src/mytxgnn/regulatory/site.py own_ids"}
    OUT.parent.mkdir(exist_ok=True)
    raw = json.dumps({"meta": meta, "drugs": drugs}, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with gzip.GzipFile(OUT, "wb", mtime=0) as fh:
        fh.write(raw)
    print(f"許可證快照：{len(drugs)} 頁 → {OUT.relative_to(ROOT)}（{OUT.stat().st_size // 1024} KB）")


if __name__ == "__main__":
    # 2026-11-19：說明頁／證據等級頁的資料檔跟著重算（scripts/local_facts.py；--check 時不跑）
    import atexit as _lf_ax, os as _lf_os, subprocess as _lf_sp, sys as _lf_sys
    _lf_here = _lf_os.path.dirname(_lf_os.path.abspath(__file__))  # 先算好：atexit 時 __main__ 的 __file__ 已不在（NameError，2026-11-19 修）
    _lf_fail = []  # 2026-11-20：結尾自動重算的回傳值以前被丟掉，失敗不會被發現；現在失敗會印 ✗ 並讓整支 exit 1
    def _lf_chk(r, what):
        if r.returncode:
            print(f"  ✗ 結尾自動重算失敗：{what}（exit {r.returncode}）", file=_lf_sys.stderr)
            _lf_fail.append(what)
        return r
    _lf_ax.register(lambda: _lf_fail and (_lf_sys.stdout.flush(), _lf_os._exit(1)))  # 最先註冊＝最後執行
    _lf_ax.register(lambda: "--check" in _lf_sys.argv or _lf_chk(_lf_sp.run([_lf_sys.executable, _lf_os.path.join(_lf_here, "local_facts.py"), "--write"]), "local_facts.py --write"))
    # 2026-11-19：藥物頁 description 句尾依許可證快照事實層重算（tools/txgnn/.claude/drug_meta_description.py；--check 時不跑）
    _dl_root = _lf_os.path.dirname(_lf_os.path.dirname(_lf_os.path.abspath(__file__)))
    _dl_p = _lf_os.path.join(_dl_root, "tools", "txgnn", ".claude", "drug_meta_description.py")
    _lf_ax.register(lambda: "--check" in _lf_sys.argv or not _lf_os.path.exists(_dl_p) or _lf_chk(_lf_sp.run([_lf_sys.executable, _dl_p, "--apply", "--root", _dl_root]), "drug_meta_description.py --apply"))
    a = sys.argv[1:]
    tag = a[a.index("--release-tag") + 1] if "--release-tag" in a else ""
    if not re.fullmatch(r"(data-[\w-]+)?", tag):
        sys.exit("--release-tag 要是 data-… 的 tag")
    if "--ws" in a:
        build(a[a.index("--ws") + 1], tag)
    else:  # 2026-11-24 第三輪：不帶 --ws 時不重建快照（沒有事實層），只依現有快照／證據包重排程式表、跑正文張數改寫
        print("沒有 --ws：快照不重建，只重排程式許可證表、改寫正文張數")
    # 2026-11-24：快照換了，市場段落的程式許可證表先依同一份證據包重排（每週排程的 sync_tables 只重排狀態有變的藥時，
    # 證據包補收、排序變了的藥也跟上；只改程式區塊）
    _tbl = _slt()
    if _tbl is not None:
        print(f"程式許可證表：重排 {len(_tbl.run())} 頁")
    # 2026-11-12：快照換了事實，正文許可證張數跟著改寫（每週排程是先套紀錄再建快照，所以這裡用新快照再跑一次）
    if "--no-rewrite" not in a:  # license_rebuild_run 轉紀錄前建快照時不改寫正文（不然改寫會被當成刪改轉成紀錄）
        import subprocess
        subprocess.run([sys.executable, str(ROOT / "scripts" / "rewrite_license_counts.py")], check=True)
