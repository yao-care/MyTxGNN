#!/usr/bin/env python3
"""Markdown 表格前後補空行（2026-11-03，MyTxGNN）。

為什麼需要這支：
    kramdown（GitHub Pages 的 Markdown 引擎）要求表格前後都是空行。
    「## Gambaran ringkas」標題下一行直接接表格，或表格最後一列下一行直接接「## Penafian」，
    整張表會被排成一段純文字（線上看到的是 `| … | … | |——|——|`）。
    2026-11-03 實測：本站 53 個藥物頁、137 處有這個問題（多半是「僅已知用途」版面的快速總覽與三張
    已知用途小表，以及緊接免責聲明標題的表）。這是渲染錯誤，不是內容問題：只補空行，不改任何字。
    docs/blog.md 的 `{% if site.posts.size > 0 %}` 下一行直接接表格，Liquid 渲染後那行是空行，不算問題（見規則第二條）。

規則：
    - 表格＝以 `|` 開頭的一行，下一行是分隔列（`|---|---|`）；表格延續到最後一個以 `|` 開頭的連續行
      （儲存格內含換行而斷成兩行、後半行不以 `|` 開頭但以 `|` 結尾的，kramdown 仍當成同一張表，也算在內）。
    - 表格前一行不是空行、不是表格行、也不是整行的 Liquid 控制標籤（`{% if … %}` 渲染後是空行）→ 補一個空行。
    - 表格後一行不是空行、不是 `{:`（kramdown 屬性列要緊貼表格）、也不是 Liquid `{%` → 補一個空行。
    - 引言（`> `）裡的表格同樣檢查；前後還在引言內就補 `>`，表格後直接接非引言的一行（kramdown 會把它吞進引言）補空行。
    - 跳過 front matter、``` 程式碼區塊、轉址頁（layout: id_redirect）。

用法：
    python3 scripts/fix_table_spacing.py            # 修正並列出改了哪些檔
    python3 scripts/fix_table_spacing.py --check    # 只檢查；有問題回非零（scripts/check_seo_docs.py 也會呼叫）
    python3 scripts/fix_table_spacing.py --touch    # 修正，並把有改到的藥物頁 last_modified_at 設成今天
                                                    # （表格從純文字變成表格，頁面確實變了，sitemap lastmod 應反映）
"""
from __future__ import annotations

import datetime as _dt
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
# 整行只有一個 Liquid 控制標籤（{% if %}、{% for %}…，不含會吃掉前面換行的 {%-）：渲染後是空行，等同表格前的空行。
LIQUID_CTRL = re.compile(
    r"^\{%\s+(if|unless|elsif|else|endif|endunless|for|endfor|assign|case|when|endcase|capture|endcapture)\b[^%]*-?%\}\s*$"
)


def _fm_end(lines: list[str]) -> int:
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return i + 1
    return 0


def _split_quote(line: str) -> tuple[bool, str]:
    """引言（`> …`）裡的表格也要檢查：回傳 (是否在引言內, 去掉一層 `>` 之後的內容)。"""
    s = line.lstrip()
    if s.startswith(">"):
        return True, s[1:].lstrip(" ")
    return False, line


def _is_row(line: str) -> bool:
    return line.lstrip().startswith("|")


def _is_continuation(line: str) -> bool:
    """上一列儲存格內含換行而斷成兩行的後半（例：`필름코팅 정제 | 유효 |`）。

    kramdown 把含 `|` 的行當成同一張表的下一列，表格沒有被切斷；在它前面補空行反而會把表切成兩半，
    所以視為表格的一部分、不補。斷行本身是資料問題，不在這支的範圍（只補空行、不改字）。
    """
    s = line.strip()
    return bool(s) and not s.startswith(("#", "<", "{", ">")) and "|" in s and s.endswith("|")


def problems(text: str) -> list[tuple[str, int, str]]:
    """回傳 [('before'|'after', 行號, 要補的行)]：需要在該行之前補一行的位置。

    一般表格補空行；引言裡的表格前後若還在引言內，補 `>`（只有 `>` 的引言空行），引言才不會被切斷。
    """
    lines = text.replace("\r\n", "\n").split("\n")
    start = _fm_end(lines)
    out: list[tuple[str, int, str]] = []
    fence = False
    i = start
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
            i += 1
            continue
        quoted, body = _split_quote(line)
        if not fence and _is_row(body) and i + 1 < len(lines):
            q2, body2 = _split_quote(lines[i + 1])
            if q2 == quoted and SEP.match(body2):
                filler = ">" if quoted else ""
                if i > start:
                    pq, prev = _split_quote(lines[i - 1])
                    if pq == quoted and prev.strip() and not _is_row(prev) and not LIQUID_CTRL.match(prev.strip()):
                        out.append(("before", i, filler))
                j = i + 2
                while j < len(lines):
                    qj, bj = _split_quote(lines[j])
                    if qj != quoted or not (_is_row(bj) or _is_continuation(bj)):
                        break
                    j += 1
                if j < len(lines):
                    qn, nb = _split_quote(lines[j])
                    if quoted and not qn:
                        # 引言裡的表格後面直接接非引言的一行（例：`## 면책 조항`）：kramdown 會把它當引言的延續吞進去
                        if lines[j].strip():
                            out.append(("after", j, ""))
                    else:
                        nxt = nb.lstrip() if quoted else lines[j].lstrip()
                        if nxt and not nxt.startswith(("{:", "{%")):
                            out.append(("after", j, filler))
                i = j
                continue
        i += 1
    return out


def fix(text: str) -> str:
    probs = problems(text)
    if not probs:
        return text
    nl = "\r\n" if "\r\n" in text else "\n"  # 保留原檔換行字元
    lines = text.replace("\r\n", "\n").split("\n")
    for _, idx, filler in sorted(probs, key=lambda p: p[1], reverse=True):
        lines.insert(idx, filler)
    return nl.join(lines)


def targets() -> list[Path]:
    out = []
    for f in sorted(DOCS.rglob("*.md")):
        rel = f.relative_to(DOCS).parts
        if rel[0] in ("_site", "vendor", ".jekyll-cache", "node_modules"):
            continue
        head = f.read_text(encoding="utf-8", errors="replace")[:600]
        if re.search(r"^layout:\s*id_redirect", head, re.M):
            continue
        out.append(f)
    return out


def main(argv: list[str]) -> int:
    check = "--check" in argv
    touch = "--touch" in argv
    today = _dt.date.today().isoformat()
    bad = []
    for f in targets():
        t = f.read_bytes().decode("utf-8")
        probs = problems(t)
        if not probs:
            continue
        bad.append((f, len(probs)))
        if check:
            continue
        new = fix(t)
        if touch and f.parent.name == "_drugs":
            new = re.sub(r"^(last_modified_at:\s*)\d{4}-\d{2}-\d{2}", rf"\g<1>{today}", new, count=1, flags=re.M)
        f.write_bytes(new.encode("utf-8"))
    if check:
        for f, n in bad:
            print(f"  - {f.relative_to(DOCS)}：{n} 處表格前後缺空行（跑 scripts/fix_table_spacing.py）")
        return 1 if bad else 0
    print(f"[table-spacing] 修正 {len(bad)} 個檔、{sum(n for _, n in bad)} 處")
    for f, n in bad:
        print(f"    {f.relative_to(DOCS)}  {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
