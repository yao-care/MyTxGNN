#!/usr/bin/env python3
"""「## Maklumat Pasaran (di) Malaysia」段落的許可證表改由程式依證據包產生（2026-11-24，用戶決定；全程不用 AI）。

為什麼：以前這張表是報告（AI）寫的自由格式表（多數是「| Nombor Kebenaran | Nama Produk | Bentuk Dos | Indikasi Diluluskan |」，
劑型、適應症欄多是「Tidak direkodkan」），每週許可證排程只改得到概覽表的狀態列與張數列，表裡寫死的狀態跟著 NPRA 資料變動就過期，
checker 擋整頁、開 issue。改成程式表後，每週排程（scripts/license_adapter.py 的 sync_tables 掛鉤）依同一套規則重排，gate 依快照驗內容。

表格（比照 HkTxGNN／SgTxGNN 的程式表）：
- 段落裡原有的第一張表（不論原欄位）換成「| No. Pendaftaran | Nama Produk (NPRA, bahasa asal) | Jenis | Pemegang Pendaftaran | Status |」；
  資料是證據包 npra.records（data.gov.my 的 NPRA 現行註冊與撤銷清單）。號碼、產品名、持有人照 NPRA 原文（不翻譯）。
- 選列與順序：換表當時報告原表列出的登記號（config/license_table_pins.json，依原表順序）在前——正文常寫「Contoh produk bahan
  tunggal:」「Jadual hanya menyenaraikan produk berbahan tunggal」，換成別的列會對不上；其餘（以及原本沒有表的頁）依程式排序：
  單一成分在前、複方在後；同類中 Sah 在前、狀態不明其次、非有效在後；再依登記號。
  單一成分／複方照 NPRA active_ingredient 的成分個數（「名稱[劑量]」幾組），規則同 reviewer drug_evidence_pack（事實層 single_total）。
- Status 欄照本站既有寫法（每筆依證據包 status 原文換算，不寫成 dibatalkan 的情況照實寫）：
  PRODUCT APPROVED→Sah；CONDITIONAL REGISTRATION→Sah (pendaftaran bersyarat)；換尾碼沿用新號→Sah (kini disenaraikan sebagai MAL…)；
  Cancelled→Dibatalkan Pendaftaran；Expired→Tamat tempoh (tiada dalam daftar semasa NPRA)；
  RETIRED_STATUS→Nombor pendaftaran lama; produk yang sama kini didaftarkan sebagai MAL…；
  MY_NOT_LISTED_CONFIRMED→Tidak lagi tersenarai dalam daftar semasa NPRA (disemak YYYY-MM-DD)；UNKNOWN_STATUS→Status tidak dapat disahkan。
- 列數＝原表列數（最多 30 列），正文「Jadual di bawah menyenaraikan 5 …」之類的說法照樣成立；總數多於列數時，表下加一句
  「Jadual di atas menyenaraikan N daripada M pendaftaran NPRA bagi ubat ini.」
- 段落裡沒有表、證據包有紀錄的頁，程式區塊加在段落結尾（結尾的「---」分隔線之前），列數 min(5, 總數)（2026-11-24 第二輪，
  用戶決定「缺表的頁補程式表」：177 個公開頁；正文「Butiran lesen individu tidak disenaraikan／tidak tersedia …」等跟新表矛盾的
  句子另以查核紀錄 my-lic-20261124b-* 刪除或改寫）。證據包沒有任何紀錄、段落也沒有表的頁不加。
  證據包沒有任何紀錄、段落原本有表時，程式區塊只放 NONE_LINE。
- 表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照事實層改寫）。
程式區塊標記：程式表（連同表下說明句，或 NONE_LINE）前後各一行「<!-- licenses:begin -->」「<!-- licenses:end -->」（前後空行）。
program_rows 給 scripts/build_license_snapshot.py（快照存最多 30 列可列的列與總數 nrows，gate 比頁面上的前 N 列）；
carry_block 給 scripts/sync_notes_to_docs.py 重寫整頁時移植舊頁的程式區塊；run 給 scripts/license_adapter.py 的 sync_tables、
scripts/apply_drug_reviews.py、scripts/build_license_snapshot.py（沒有 data/bundles 時依快照的列重排）。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--dry-run] [--from-snapshot] [--pins] [頁 ...]
  --pins：從目前頁面的報告原表重新產生 config/license_table_pins.json（只在第一次換表前用；換表後原表已不在頁面上）。
"""
import gzip
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_RE = re.compile(r"^## Maklumat Pasaran (?:di )?Malaysia\s*$")
HEAD = ["| No. Pendaftaran | Nama Produk (NPRA, bahasa asal) | Jenis | Pemegang Pendaftaran | Status |",
        "|------|------|------|------|------|"]
NONE_LINE = "Tiada pendaftaran NPRA yang mengandungi bahan aktif ubat ini dalam data yang digunakan untuk laporan ini."
SHOW = "Jadual di atas menyenaraikan {n} daripada {m} pendaftaran NPRA bagi ubat ini."
SHOW_RX = re.compile(r"^Jadual di atas menyenaraikan \d+ daripada \d+ pendaftaran NPRA bagi ubat ini\.$")
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
MAX_ROWS = 30  # 10-31 known_use_pages 程式表最多 30 列（8 頁），沿用
# known_use_pages_20261022.py 舊程式表下的部分紀錄提示句：證據包現在都是完整紀錄（事實層 partial 0），換表時拿掉（同 CO）
PART_NOTE = "Data hanya mengandungi sebahagian pendaftaran; senarai mungkin tidak lengkap."
SINGLE, COMBO = "Bahan tunggal", "Kombinasi"
ID_RE = re.compile(r"\bMAL\d{8}[A-Z]{0,5}\b")
SNAP = ROOT / "snapshots" / "my_licenses.json.gz"
PINS_FILE = ROOT / "config" / "license_table_pins.json"

_UNKNOWN = re.compile(r"^Status unknown \(registration number not found")
_CANCELLED = re.compile(r"cancel|withdraw|revok|suspen|expir|lapse|discontinu|retir|inactive", re.I)


def cell(x, cap=None):
    s = re.sub(r"\s+", " ", html.unescape(str(x or "")).replace("|", "/")).strip()
    s = re.sub(r"(\d\s*|/)KG\b", r"\1kg", s)  # checker P5 會把大寫 KG 當成「知識圖譜（KG）」字樣（只改單位大小寫）
    return s[:cap].rstrip() + "…" if cap and len(s) > cap else s


def reg(r):
    return str(r.get("reg_no") or "").strip()


def is_combo(r):
    """成分個數 > 1（同 reviewer drug_evidence_pack 的 kind：active_ingredient 裡「名稱[」幾組）"""
    if r.get("kind"):
        return r["kind"] == "combo"
    return len(re.findall(r"[^,\[\]]+\[", str(r.get("active_ingredient") or ""))) > 1


def status_class(r):
    """valid／unknown／cancelled：同 reviewer drug_evidence_pack 的判法（事實層）"""
    st = str(r.get("status") or "")
    if _UNKNOWN.search(st):
        return "unknown"
    if r.get("license_status"):
        return r["license_status"]
    return "cancelled" if _CANCELLED.search(st) else "valid"


def status_label(r):
    st = str(r.get("status") or "").strip()
    cls = status_class(r)
    if cls == "unknown":
        return "Status tidak dapat disahkan"
    if r.get("npra_manual_check"):
        return f"Tidak lagi tersenarai dalam daftar semasa NPRA (disemak {r['npra_manual_check']})"
    m = re.match(r"Registration number retired .*now listed as (MAL\w+)\)", st)
    if m:
        return f"Nombor pendaftaran lama; produk yang sama kini didaftarkan sebagai {m.group(1)}"
    if st.startswith("Expired"):
        return "Tamat tempoh (tiada dalam daftar semasa NPRA)"
    if st == "Cancelled":
        return "Dibatalkan Pendaftaran"
    m = re.fullmatch(r"(PRODUCT APPROVED|CONDITIONAL REGISTRATION)(?: \(now listed as (MAL\w+)\))?", st)
    if m and cls == "valid":
        extra = (["pendaftaran bersyarat"] if m.group(1) == "CONDITIONAL REGISTRATION" else []) + \
                ([f"kini disenaraikan sebagai {m.group(2)}"] if m.group(2) else [])
        return "Sah" + (f" ({'; '.join(extra)})" if extra else "")
    return cell(st, 80) or "Tidak direkodkan"  # 其他寫法照 NPRA 原文（2026-11-24 實測 0 筆）


def uniq(recs):
    seen = {}
    for r in recs or []:
        k = reg(r)
        if k and k not in seen:
            seen[k] = r
    return list(seen.values())


_PINS = None


def pins_for(stem):
    """換表當時報告原表依序列出的登記號（config/license_table_pins.json）；沒有就是 []"""
    global _PINS
    if _PINS is None:
        _PINS = json.loads(PINS_FILE.read_text(encoding="utf-8")).get("pins", {}) if PINS_FILE.exists() else {}
    return _PINS.get(stem) or _PINS.get(stem.replace("-", "_")) or _PINS.get(stem.replace("_", "-")) or []


_RANK = {"valid": 0, "unknown": 1, "cancelled": 2}
_NEG = []


def _neg_word(r):
    """有效登記的產品名／持有人含 checker 的註銷字樣（tools/txgnn/.claude/rewrite_market_v2_20261021.py 的 TABLE_NEG；
    例 levonorgestrel「Revoke-1.5 Levonorgestrel Tablet」的 revok）：checker M1 會把整列當成「有效寫成註銷」，
    所以程式排序時放在同類最後（原表選列不受影響；2026-11-24）"""
    if not _NEG:
        try:
            import importlib.util
            sp = importlib.util.spec_from_file_location("my_mv2", ROOT / "tools/txgnn/.claude/rewrite_market_v2_20261021.py")
            m = importlib.util.module_from_spec(sp)
            sp.loader.exec_module(m)
            _NEG.append(m.TABLE_NEG)
        except Exception:
            _NEG.append(None)
    rx = _NEG[0]
    return bool(rx) and status_class(r) == "valid" and bool(rx.search(f"{cell(r.get('product'))} {cell(r.get('holder'))}"))


def table_rows(recs, pins=()):
    """全部可列的列：pins（原表選列）依序在前，其餘依程式排序"""
    u = sorted(uniq(recs), key=lambda r: (is_combo(r), _RANK.get(status_class(r), 3), _neg_word(r), reg(r)))
    rank = {k: i for i, k in enumerate(pins or [])}
    u.sort(key=lambda r: rank.get(reg(r), len(rank)))  # 穩定排序：沒選的保持程式排序
    return [f"| {reg(r)} | {cell(r.get('product'), 100) or 'Tidak direkodkan'} | {COMBO if is_combo(r) else SINGLE} | "
            f"{cell(r.get('holder'), 70) or 'Tidak direkodkan'} | {status_label(r)} |" for r in u]


def block_from_rows(rows, nrows, n=None):
    """程式區塊的內容（不含標記）：n 列的表＋（總數較多時）SHOW 句；n 預設 min(5, 總數)；沒有任何紀錄時是 NONE_LINE 一句"""
    if not rows:
        return [NONE_LINE]
    n = min(5, len(rows)) if n is None else min(n, len(rows))
    return HEAD + rows[:n] + (["", SHOW.format(n=n, m=nrows)] if nrows > n else [])


def program_rows(tf, fc=None, pins=()):
    """快照用：(程式表最多可列的列, 可列總數)"""
    rows = table_rows((tf or {}).get("records") or [], pins)
    return rows[:MAX_ROWS], len(rows)


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def bounds(lines):
    """市場段落 (標題下一行, 段落結尾)；沒有回 (None, None)"""
    for i, ln in enumerate(lines):
        if SEC_RE.match(ln):
            j = next((k for k in range(i + 1, len(lines)) if re.match(r"^#{1,2} ", lines[k])), len(lines))
            return i + 1, j
    return None, None


def _first_table(lines, a, b):
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        return None, None
    x = y = tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    return x, y


def _tail(lines, a, b):
    """段落結尾的插入位置：段落最後的空行與「---」分隔線之前（段落沒有內容時＝標題下）"""
    k = b
    while k > a and lines[k - 1].strip() in ("", "---"):
        k -= 1
    return k


def process(text, rows, nrows):
    """rows：可列的列（已排好、最多 30）；回傳新內容（沒變回 None）。
    段落裡已有程式區塊→原位重排；沒有程式區塊但有表→第一張表換成程式區塊；段落裡沒有任何表→有紀錄就加在段落結尾（見檔頭說明）"""
    lines = text.split("\n")
    a, b = bounds(lines)
    if a is None:
        return add_section(text, rows, nrows) if ADD_SECTIONS else None
    sec = lines[a:b]
    if BEGIN in sec and END in sec:
        i, j = a + sec.index(BEGIN), a + sec.index(END)
        old = [l for l in lines[i + 1:j] if l.startswith("|")]
        n = min(MAX_ROWS, max(1, len(old) - 2)) if old else None
        lines = lines[:i] + wrap(block_from_rows(rows, nrows, n)) + lines[j + 1:]
    else:
        lines = strip_marks(lines)
        a, b = bounds(lines)
        x, y = _first_table(lines, a, b)
        if x is None:
            if not rows:
                return None
            k = _tail(lines, a, b)
            lines = lines[:k] + [""] + wrap(block_from_rows(rows, nrows)) + [""] + lines[k:]
            t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
            return t2 if t2 != text else None
        n = min(MAX_ROWS, max(1, y - x - 1))
        rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and l.strip() not in (NONE_LINE, PART_NOTE)]
        lines = lines[:x] + ([""] if lines[x - 1].strip() else []) + wrap(block_from_rows(rows, nrows, n)) + [""] + rest + lines[b:]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return t2 if t2 != text else None


# 2026-11-24 第三輪（用戶決定 B，比照 JpTxGNN 的 add_section）：公開頁整頁沒有「## Maklumat Pasaran di Malaysia」段落、證據包卻有紀錄的
# （量測 222 頁，多是新版報告格式），補一個段落放程式表（列數 min(5, 總數)，總數較多時加 SHOW 句）。
# 位置：安全性段落（Pertimbangan Keselamatan／Keselamatan…／Maklumat Keselamatan）之前；沒有就「(Keputusan )Kesimpulan／Keputusan dan
# Langkah Seterusnya」之前；再沒有就「Penafian」之前（緊接在前的「---」分隔線與查核紀錄區塊標記之前）。noindex 頁與證據包沒有紀錄的頁不補。
# 超過 200 頁，先回報用戶，用戶 2026-11-24 同意（不設頁數上限）；gate（src/mytxgnn/regulatory/licenses.py page_problems）擋「公開頁有證據包紀錄卻沒有市場段落」。
ADD_SECTIONS = True
ADD_TITLE = "## Maklumat Pasaran di Malaysia"
ADD_BEFORE = (re.compile(r"^## (Pertimbangan Keselamatan|Keselamatan\b.*|Maklumat Keselamatan)\s*$"),
              re.compile(r"^## (Keputusan )?(Kesimpulan|Keputusan) dan Langkah Seterusnya\s*$"),
              re.compile(r"^## Penafian\s*$"))


def add_section(text, rows, nrows):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    if re.search(r"^noindex:\s*true", fm, re.M) or not rows:
        return None
    lines = text.split("\n")
    at = None
    for rx in ADD_BEFORE:
        at = next((i for i, l in enumerate(lines) if rx.match(l)), None)
        if at is not None:
            break
    if at is None:
        return None
    k = at
    while k > 0 and (lines[k - 1].strip() in ("", "---", "<!-- review:begin log -->")):
        k -= 1
    sec = ["", ADD_TITLE, ""] + wrap(block_from_rows(rows, nrows)) + [""]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:k] + sec + lines[k:]))
    return t2 if t2 != text else None


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落，取代新頁模型寫的第一張表（連同表下程式文字）；
    新頁段落沒有表時加在段落結尾（同 process）。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    a, b = bounds(lines)
    if a is None:
        return new_text
    x, y = _first_table(lines, a, b)
    if x is None:
        k = _tail(lines, a, b)
        out = lines[:k] + [""] + blk + [""] + lines[k:]
    else:
        rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and l.strip() not in (NONE_LINE, PART_NOTE)]
        out = lines[:x] + [""] + blk + [""] + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def bundle_file(stem):
    for key in dict.fromkeys((stem, stem.replace("-", "_"), stem.replace("_", "-"))):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return f
    return None


def _is_redirect(raw):
    return "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]


def make_pins():
    """從目前頁面的報告原表收原表列出、屬於本藥證據包的登記號（依原表順序）"""
    pins = {}
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        raw = page.read_text(encoding="utf-8")
        bf = bundle_file(page.stem)
        if _is_redirect(raw) or bf is None or BEGIN in raw:
            continue
        own = {reg(r) for r in (json.loads(bf.read_text(encoding="utf-8")).get("npra") or {}).get("records") or []}
        lines = raw.split("\n")
        a, b = bounds(lines)
        if a is None:
            continue
        x, y = _first_table(lines, a, b)
        if x is None:
            continue
        ids = []
        for ln in lines[x + 2:y + 1]:
            first = ln.strip().strip("|").split("|")[0]
            for m in ID_RE.finditer(first):
                if m.group(0) in own and m.group(0) not in ids:
                    ids.append(m.group(0))
        if ids:
            pins[page.stem] = ids
    PINS_FILE.parent.mkdir(exist_ok=True)
    PINS_FILE.write_text(json.dumps({"_note": "換表當時（2026-11-24）報告原表依序列出、屬於本藥證據包的 NPRA 登記號；"
                                              "scripts/sync_license_tables.py 選列時放在最前面（見該檔說明）",
                                     "pins": pins}, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return pins


def run(only=None, dry=False, from_snapshot=None):
    """全站（或 only 指定的頁，檔名去 .md）重排程式表。回傳改到的頁。
    有 data/bundles 就依證據包；沒有（或 from_snapshot=True）就依快照存的列（rows、nrows）。"""
    if from_snapshot is None:
        from_snapshot = not (ROOT / "data/bundles").is_dir()
    snap = {}
    if from_snapshot:
        if not SNAP.exists():
            return []
        snap = json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs") or {}
    changed = []
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        raw = page.read_bytes().decode("utf-8")
        if _is_redirect(raw):
            continue
        if from_snapshot:
            e = snap.get(page.stem)
            if not e or "rows" not in e:
                continue
            rows, nrows = e["rows"], e.get("nrows", len(e["rows"]))
        else:
            bf = bundle_file(page.stem)
            if bf is None:
                continue
            tf = json.loads(bf.read_text(encoding="utf-8")).get("npra") or {}
            rows, nrows = program_rows(tf, None, pins_for(page.stem))
        crlf = "\r\n" in raw[:500]
        new = process(raw.replace("\r\n", "\n"), rows, nrows)
        if new is None:
            continue
        changed.append(page.stem)
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--pins" in a:
        print(f"原表選列：{len(make_pins())} 頁 → {PINS_FILE.relative_to(ROOT)}")
        sys.exit(0)
    if "--add-sections" in a:
        ADD_SECTIONS = True
    ch = run({x for x in a if not x.startswith("--")} or None, "--dry-run" in a, True if "--from-snapshot" in a else None)
    print(f"許可證表{'（試跑）' if '--dry-run' in a else ''}改 {len(ch)} 頁")
