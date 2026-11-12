"""藥物頁許可證資訊的驗證（2026-11-12 建，本站查核機制；比照 TwTxGNN 的 gate 許可證項目）。

依 snapshots/ 下的許可證快照（scripts/build_license_snapshot.py 產生）檢查，不需要 data/：
  1. 市場段落（site.MARKET_SEC）表格第一欄含本站號碼格式（site.ID_RE）的格子，整格都是本藥的號碼（快照 own）。
  2. 有程式產生的許可證表的站（site.program_block_problems 存在）：程式區塊＝依快照重算的結果。
  3. 概覽表的狀態列與張數列＝事實層的寫法：用本站 tools/txgnn/.claude/check_drug_page.py 的 marketed_text／
     not_marketed_text／unknown_status_text／not_reg_text／count_text（checker M1／M4 的同一套函式）。
  4. 表格列寫的狀態不得跟事實相反（checker row_status_conflicts）。
修法：資料變了→跑每週排程（或 scripts/build_license_snapshot.py）；正文說法不對→寫查核紀錄再跑 scripts/apply_drug_reviews.py。
"""
from __future__ import annotations

import gzip
import importlib.util
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

from . import site as C

ROOT = Path(__file__).resolve().parents[3]
SNAP = ROOT / "snapshots" / f"{C.CODE}_licenses.json.gz"
SITE = C.SITE


def _load(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


@lru_cache(maxsize=None)
def CK():
    return _load(f"{SITE}_check_drug_page", ROOT / "tools" / "txgnn" / ".claude" / "check_drug_page.py")


@lru_cache(maxsize=None)
def snapshot():
    if not SNAP.exists():
        return {}
    return json.loads(gzip.open(SNAP).read().decode("utf-8"))


def section(lines):
    for k, ln in enumerate(lines):
        if C.MARKET_SEC.match(ln):
            b = next((j for j in range(k + 1, len(lines)) if lines[j].startswith("## ")), len(lines))
            return k + 1, b
    return None, None


def tables(lines):
    out, cur = [], []
    for ln in lines + [""]:
        if ln.startswith("|"):
            cur.append(ln)
        elif cur:
            out.append(cur)
            cur = []
    return out


def rows(tbl):
    return [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in tbl[2:]]


def expected_status(fc):
    ck = CK()
    lang = ck.LANG.get(SITE, "en")
    ms, v, n, partial = fc.get("market_status"), fc.get("valid"), fc.get("total"), fc.get("partial")
    if ms == "Marketed":
        return ck.marketed_text(SITE, lang, v, n, partial, fc)
    if ms == "Approved, not marketed":
        return ck.not_marketed_text(SITE, lang, fc)
    if ms == "Status unknown" and SITE in ck.UNKNOWN_ST:
        return ck.unknown_status_text(SITE, lang, fc)
    if ms == "Not marketed" and SITE in ck.VET_ONLY:
        return ck.not_reg_text(SITE, lang, fc)
    return None


def page_problems(stem, text):
    e = (snapshot().get("drugs") or {}).get(stem)
    if e is None:
        return []
    ck = CK()
    body = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", text, flags=re.S)
    lines = body.replace("\r\n", "\n").split("\n")
    errs = []
    own = {ck.mv2.norm_id(x) for x in e["own"]}
    own |= {ck.mv2.norm_id(x) for x in (getattr(C, "EXTRA_OWN", {}).get(stem) or {})}  # 事實層漏收、已人工對照主管機關清單的號碼
    a, b = section(lines)
    partial = bool((e.get("facts") or {}).get("partial"))
    if a is not None:
        # 事實層是部分紀錄（證據包只收了一部分許可證，例 Kr 每藥最多 20 筆）時，表格裡的號碼可能屬於本藥但不在快照，不驗歸屬
        if C.ID_RE is not None and not partial:
            for t in tables(lines[a:b]):
                for r in rows(t):
                    cell = r[0] if r else ""
                    cell = re.sub(r"^\[([^\]]+)\]\([^)]*\)$", r"\1", cell.strip())  # 號碼格是 Markdown 連結時取連結文字
                    # 第一欄含本站號碼格式時，整格（號碼可帶後綴或括號，例 Za「55/8.2/0055.053」「G115 (ACT 101/1965)」）要是本藥的號碼
                    # 整格不是本藥號碼時，再看格裡符合號碼格式的部分（例 My「MAL19973350AZ (kombinasi)」：號碼後面加註）
                    if C.ID_RE.search(cell) and ck.mv2.norm_id(cell) not in own \
                            and not any(ck.mv2.norm_id(m.group(0)) in own for m in C.ID_RE.finditer(cell)):
                        errs.append(f"市場段落表格的號碼不屬於本藥：{cell}")
        if hasattr(C, "program_block_problems"):
            errs += C.program_block_problems(lines[a:b], e)
    fc = e.get("facts")
    if fc:
        all_rows = [r for t in tables(lines) for r in rows(t)]
        st = ck.status_row(SITE, all_rows)
        want_s = expected_status(fc)
        if st is not None and want_s and st[1] != want_s:
            errs.append(f"狀態列「{st[1][:50]}」≠ 事實層寫法「{want_s}」")
        cr = ck.count_row(SITE, all_rows)
        if cr is not None and (fc.get("total") is not None or fc.get("partial")):
            want_c = ck.count_text(SITE, ck.LANG.get(SITE, "en"), fc)
            if cr[1] != want_c:
                errs.append(f"張數列「{cr[1][:50]}」≠ 事實層寫法「{want_c}」")
        lic = {ck.mv2.norm_id(k): v for k, v in (fc.get("licenses") or {}).items()}
        if a is not None:
            for t in tables(lines[a:b]):
                for code, d in ck.row_status_conflicts(SITE, rows(t), lic):
                    errs.append(f"許可證表列的狀態跟事實相反：{d}")
    return errs


def site_problems(drugs_dir=None):
    drugs_dir = drugs_dir or ROOT / "docs" / "_drugs"
    if not snapshot():
        return [f"找不到 {SNAP.relative_to(ROOT)}（跑 scripts/build_license_snapshot.py）"]
    out = []
    for f in sorted(drugs_dir.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in t[:3000] or re.search(r"^layout:\s*id_redirect", t[:3000], re.M):
            continue
        out += [f"{f.name}：{x}" for x in page_problems(f.stem, t)]
    return out


if __name__ == "__main__":
    errs = site_problems()
    for x in errs[:50]:
        print("  ✗", x)
    print(f"許可證檢查：{'✗' if errs else '✓'} {len(errs)} 項")
    sys.exit(1 if errs else 0)
