"""正文許可證張數的程式改寫（2026-11-12 建，本站查核機制；概念比照 TwTxGNN page_postprocess.rewrite_count_prose，規則是本站馬來文句型）。

用戶 2026-11-12 決定：正文裡「N lesen sah／N pendaftaran／N produk berdaftar」這類 NPRA 許可證張數敘述，由程式依許可證快照
（snapshots/my_licenses.json.gz 的 facts）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Tw：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥許可證張數」的地方，其餘一律不動：
  - 句子要有許可證名詞（lesen／pendaftaran／berdaftar／didaftar／kebenaran；在市場段落「Maklumat Pasaran Malaysia」裡
    「N produk」也算），且沒有交互作用、試驗、文獻等字樣。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（列在 skipped）：有保留（sekurang-kurangnya、sebahagian、mungkin tidak lengkap）、講證據包或查詢結果
    （Pakej Bukti、pertanyaan／kueri NPRA、diambil、ditemui、mengembalikan）、相對數（lain、lagi、selain itu、tambahan）、
    劑型或廠商子集；事實層 partial 的頁整頁不動。
  - 數字不動：顯示筆數（senarai／jadual／disenaraikan／di atas／di bawah、「N daripada M」的 N）、劑量與年份。
角色看數字右側：dibatalkan→註銷；sah／aktif／masih sah→有效；tunggal／satu bahan→單方（句中有 sah／aktif 用有效單方）；
gabungan／kombinasi→複方；其餘→總數。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
同一句另有明確的有效／註銷數字時，沒有限定詞的數字確定是總數。
數字已等於該角色的任一合理讀法（沒有限定詞的總數＝總數或有效數）就不動；不等於時兩種讀法相同才改，不同就列為 ambiguous。
原數字是 0 的句子（建立在 0 張前提上）不改、列為 zero-premise，要改請寫查核紀錄。
前提檢查：句子說「semuanya／kesemuanya sah」而有效≠總數、說全部是單方或全部是複方而事實不符時整句不動、列出。
"""
from __future__ import annotations

import re

from . import site as C

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z*\[(>-])")
NUM = re.compile(r"(?<![\w.,/-])(\d{1,3}(?:,\d{3})+|\d+)(?![\w.,/%-]|,\d)")
NOUN = r"(?:lesen|pendaftaran|produk|rekod(?: lesen| pendaftaran)?|kebenaran)"
LICENSE = re.compile(r"\blesen\b|\bpendaftaran\b|berdaftar|didaftar|terdaftar|\bkebenaran\b|\d+\)?\s+(?:ialah\s+)?produk\b")
NOT_LICENSE = re.compile(r"interaksi|ujian klinikal|percubaan|kajian|artikel|PMID|NCT|kes |pesakit|kesan sampingan|"
                         r"\bmg\b|\bml\b|%|tahun|bulan|minggu|hari|calon|ramalan|skor", re.I)
HEDGED = re.compile(r"sekurang-kurangnya|sebahagian|tidak lengkap|mungkin|Pakej Bukti|pertanyaan|kueri|query|diambil|"
                    r"ditemui|mengembalikan|dikembalikan|Evidence Pack|\blain\b|\blagi\b|selain itu|selebihnya|\bbaki\b|tambahan|termasuk satu|"
                    r"veterinar|haiwan|eksport|pengeluar|syarikat|Sdn|Bhd|tablet|kapsul|suntikan|sirap|krim|salap|"
                    r"titisan|serbuk|larutan|bentuk dos", re.I)
DISPLAY = re.compile(r"(senarai|jadual|disenaraikan|menyenaraikan|di atas|di bawah|berikut|ditunjukkan|dipaparkan)", re.I)
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)


def _role(s, a, b):
    left, right = s[max(0, a - 25):a].lower(), s[b:b + 45].lower()
    if re.match(r"\s*daripada\s+\d", right) or re.search(r"(hanya|lima|lima \()\s*$", left) or DISPLAY.search(left):
        return "display"
    if DISPLAY.search(right[:30]) and not re.match(rf"\s*{NOUN}", right):
        return "display"
    head = re.match(rf"\s*(?:{NOUN}\s*)?(?:yang\s+)?(?:\w+\s+){{0,3}}", right)
    near = right[:40]
    if re.match(r"\s*(?:\w+\s+){0,3}(telah\s+)?dibatalkan", near):
        return "cancelled"
    if re.match(r"\s*(?:\w+\s+){0,2}(?:ialah\s+|untuk\s+)?produk\s+(?:\w+\s+)?(?:gabungan|kombinasi)", near) \
            or re.match(r"\s*(?:\w+\s+){0,1}(?:ialah\s+)?(?:produk\s+)?(?:gabungan|kombinasi)", near):
        return "combo"
    if re.match(r"\s*(?:\w+\s+){0,2}(?:ialah\s+|untuk\s+)?produk\s+(?:\w+\s+)?(?:tunggal|satu)", near) \
            or re.match(r"\s*(?:\w+\s+){0,2}(?:bahan|ramuan|ingredien)\s+(?:aktif\s+)?tunggal", near):
        return "single"
    if re.match(rf"\s*(?:{NOUN}\s+)?(?:\w+\s+)?(?:yang\s+)?(?:masih\s+)?(?:sah|aktif)\b", near):
        return "valid"
    if re.match(rf"\s*{NOUN}\b", right) or re.search(r"(jumlah|sebanyak|terdapat|daripada|semua|kesemua|memegang|ialah)\s+$", left):
        return "total"
    return None


def _readings(role, f, sent, explicit=False):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    st, vs = f.get("single_total"), f.get("valid_single")
    validctx = bool(re.search(r"\bsah\b|\baktif\b", sent))
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if role == "single":
        if validctx:
            return {vs}, vs
        return {st, vs}, st if st == vs else None
    if role == "combo":
        ct = None if t is None or st is None else t - st
        cv = None if v is None or vs is None else v - vs
        if validctx:
            return {cv}, cv
        return {ct, cv}, ct if ct == cv else None
    if explicit:  # 同一句另有明確的有效／註銷數字：沒有限定詞的那個就是總數
        return {t}, t
    return {t, v}, t if t == v else None


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"(semuanya|kesemuanya|semua)[^.]{0,25}\b(sah|aktif)\b|tiada lesen (yang )?dibatalkan|0 dibatalkan", lo) \
            and (f.get("valid") != f.get("total") or f.get("cancelled")):
        return False
    if re.search(r"(semuanya|kesemuanya|semua)[^.]{0,30}(tunggal|satu bahan)", lo):
        if f.get("single_total") != f.get("total"):
            return False
    if re.search(r"(semuanya|kesemuanya|semua)[^.]{0,30}(gabungan|kombinasi)", lo):
        if f.get("single_total"):
            return False
    return True


def rewrite_sentence(sent, f, market=False):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not NUM.search(sent) or not (LICENSE.search(sent) or (market and re.search(r"\d+\s+produk", sent))):
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    subs = []
    for m, role in found:
        if role in (None, "display"):
            continue
        old = int(m.group(1).replace(",", ""))
        ok, v = _readings(role, f, sent, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(f"{v:,}" if v >= 1000 else str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped, market=False):
    if ln.startswith(("|", "#")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f, market)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動，免得改了一句、旁邊的句子對不上
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial"):
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, market = [], False
    for ln in body.split("\n"):
        if ln.startswith("## "):
            market = bool(C.MARKET_SEC.match(ln))
        lines.append(ln if "\x00" in ln else _line(ln, facts, protect, skipped, market))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
