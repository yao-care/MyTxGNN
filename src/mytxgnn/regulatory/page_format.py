"""藥物頁的確定性格式規則：頁首證據等級、description 的等級、表格前後空行（2026-11-12 建，本站查核機制）。

核心流程比照 TwTxGNN src/twtxgnn/regulatory/page_format.py；本站的寫法（總覽列標題、頁首列、撤回字樣、description 句型）
與頁首規則細節在同目錄 site.py。scripts/apply_drug_reviews.py 與 gate（scripts/check_seo_docs.py）都呼叫這裡，規則只有一份。

頁首等級：頁首（front matter evidence_level、parent、頁首「等級: **Lx**」列）由 Quick Overview 的證據等級格決定；
  site.HEADER_RULE＝"first"：取格裡第一個等級（主預測）；"max"：整格取最高（數字最小）。規則依本站現有頁面實測，見 site.py。
  格裡沒有 Lx 或沒有這一列：頁首不動。主預測重審撤回（table_updates 把格換成 site.WITHDRAWN 開頭的字）時，
  頁首改取其他預測表（表頭有證據等級欄）保留的最高等級；沒有就是 N/A，parent 歸 docs/known-uses.md 的 title。
description 的等級：只把 description 裡的等級字樣換成目前頁首等級（site.DESC_LEVEL_RE、site.desc_level_text），其他文字不動。
表格前後空行：本站 scripts/fix_table_spacing.py（gate 既有項目），這裡直接用它。
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

from . import site as C

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs"
EVIDENCE_PAGES = ("evidence-high.md", "evidence-medium.md", "evidence-low.md")
KNOWN_USES_PAGE = "known-uses.md"
NA = "N/A"
OVERVIEW_ROW_RE = re.compile(r"^\|\s*(?:" + "|".join(re.escape(x) for x in C.LEVEL_LABELS) + r")\s*\|([^|\n]*)\|", re.M)
WITHDRAWN_CELL_RE = re.compile(r"^\s*(\*\*)?(?:" + C.WITHDRAWN + r")", re.I)
REVIEW_BLOCK_RE = re.compile(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", re.S)
LEVEL_RE = r"(?:L[1-5]|N/A)"
HEADER_RE = re.compile(r"^((?:" + C.HEADER_LABEL + r")\s*[:：]\s*\*\*)(" + LEVEL_RE + r")(\*\*)", re.M)
_PARENTS: dict = {}


def _fts():
    s = importlib.util.spec_from_file_location(f"{C.SITE}_fix_table_spacing", ROOT / "scripts" / "fix_table_spacing.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


_FTS = _fts()


def best_level(cell):
    lv = re.findall(r"L([1-5])", cell or "")
    return f"L{min(lv)}" if lv else None


def first_level(cell):
    m = re.search(r"L([1-5])", cell or "")
    return f"L{m.group(1)}" if m else None


def overview_level(text):
    m = OVERVIEW_ROW_RE.search(REVIEW_BLOCK_RE.sub("", text))
    if not m:
        return None
    return first_level(m.group(1)) if C.HEADER_RULE == "first" else best_level(m.group(1))


def overview_withdrawn(text):
    m = OVERVIEW_ROW_RE.search(REVIEW_BLOCK_RE.sub("", text))
    return bool(m and WITHDRAWN_CELL_RE.match(m.group(1)) and not best_level(m.group(1)))


def other_prediction_levels(text):
    text = REVIEW_BLOCK_RE.sub("", text)
    out, col, fence = [], None, False
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("```"):
            fence = not fence
        if fence or not ln.startswith("|"):
            col = None
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        prev = lines[i - 1] if i else ""
        if not prev.startswith("|"):
            col = next((k for k, c in enumerate(cells) if c in C.LEVEL_LABELS), None)
            continue
        if col is None or set(ln.replace("|", "").strip()) <= set("-: "):
            continue
        if col < len(cells):
            lv = best_level(cells[col])
            if lv:
                out.append(lv)
    return out


def target_level(text):
    best = overview_level(text)
    if best:
        return best
    if overview_withdrawn(text):
        return best_level(" ".join(other_prediction_levels(text))) or NA
    return None


def parent_titles():
    if not _PARENTS:
        p = DOCS / KNOWN_USES_PAGE
        if p.exists():
            m = re.search(r"^title:\s*(.+?)\s*$", p.read_text(encoding="utf-8"), re.M)
            if m:
                _PARENTS[NA] = m.group(1).strip().strip('"').strip("'")
        for fname in EVIDENCE_PAGES:
            p = DOCS / fname
            if not p.exists():
                continue
            m = re.search(r"^title:\s*(.+?)\s*$", p.read_text(encoding="utf-8"), re.M)
            if not m:
                continue
            title = m.group(1).strip().strip('"').strip("'")
            lv = [int(x) for x in re.findall(r"L([1-5])", title)]
            for n in range(min(lv), max(lv) + 1) if lv else []:
                _PARENTS.setdefault(f"L{n}", title)
    return _PARENTS


def _split_fm(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    return (text[:end], text[end:]) if end >= 0 else (None, text)


def header_state(text):
    fm, rest = _split_fm(text)
    fm = fm or ""
    lv = re.search(rf"^evidence_level:[ \t]*\"?({LEVEL_RE})\"?[ \t]*$", fm, re.M)
    par = re.search(r"^parent:[ \t]*(.*?)[ \t]*$", fm, re.M)
    head = HEADER_RE.search(rest)
    return {"evidence_level": lv.group(1) if lv else None,
            "parent": par.group(1).strip().strip('"').strip("'") if par else None,
            "header": head.group(2) if head else None}


def sync_header_level(text):
    best = target_level(text)
    fm, rest = _split_fm(text)
    if not best or fm is None:
        return text
    fm = re.sub(rf"^(evidence_level:[ \t]*\"?){LEVEL_RE}", lambda x: x.group(1) + best, fm, count=1, flags=re.M)
    parent = parent_titles().get(best)
    if parent:
        old = re.search(r"^parent:[ \t]*(.*?)[ \t]*$", fm, re.M)
        if old and old.group(1).strip().strip('"').strip("'") != parent:
            fm = re.sub(r"^parent:.*$", lambda x: f"parent: {parent}", fm, count=1, flags=re.M)
    rest = HEADER_RE.sub(lambda x: x.group(1) + best + x.group(3), rest, count=1)
    return fm + rest


def _desc_line(fm):
    return re.search(r"^description:.*$", fm, re.M)


def description_level_text(level):
    return C.desc_level_text(level)


def sync_description_level(text):
    fm, rest = _split_fm(text)
    lv = header_state(text)["evidence_level"]
    m = _desc_line(fm or "")
    if not m or not lv:
        return text
    line = C.DESC_LEVEL_RE.sub(lambda _: C.desc_level_text(lv), m.group(0))
    return fm[:m.start()] + line + fm[m.end():] + rest


def description_level_problems(text):
    fm, _ = _split_fm(text)
    lv = header_state(text)["evidence_level"]
    m = _desc_line(fm or "")
    if not m or not lv:
        return []
    bad = sorted({x.upper() for x in C.DESC_LEVEL_RE.findall(m.group(0)) if x.upper() != lv})
    return [f"description 寫等級 {x}，頁首等級={lv}" for x in bad]


def header_problems(text):
    best = target_level(text)
    st = header_state(text)
    if not best:
        want = parent_titles().get(NA)
        # front matter 沒有 parent 的頁不掛在任何列表頁下（例：layout: drug 的 noindex 頁），不驗 parent
        if st["evidence_level"] == NA and want and st["parent"] is not None and st["parent"] != want:
            return [f"parent={st['parent']}，N/A 頁應為 {want}（docs/known-uses.md 的 title）"]
        return []
    errs = []
    if st["evidence_level"] != best:
        errs.append(f"front matter evidence_level={st['evidence_level']}，Quick Overview 等級（規則 {C.HEADER_RULE}）={best}")
    if st["header"] not in (None, best):
        errs.append(f"頁首等級列={st['header']}，Quick Overview 等級={best}")
    want = parent_titles().get(best)
    if want and st["parent"] != want:
        errs.append(f"parent={st['parent']}，應為 {want}")
    return errs


def fix_table_spacing(text):
    return _FTS.fix(text)


def table_spacing_problems(text):
    return [f"第 {i + 1} 行的表格{'前' if k == 'before' else '後'}面缺空行" for k, i in _FTS.problems(text)]
