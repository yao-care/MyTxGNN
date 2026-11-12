"""本站（MyTxGNN）查核機制的在地設定（2026-11-12 建）：頁面文字、資料來源、頁首規則、許可證格式、歷史刪改提交。

同目錄 page_format／licenses／withdrawn 與 scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py 都讀這裡；核心流程比照 TwTxGNN 與 UsTxGNN，只有這份是本站自己的寫法。
本站的市場資料是 NPRA 藥品註冊（data.gov.my 的 pharmaceutical_products.csv 現行註冊與 pharmaceutical_products_cancelled.csv
撤銷清單；註冊號 MAL…），頁面文字用馬來文。
本站沒有程式產生的許可證表（「Maklumat Pasaran Malaysia」段落的表是報告寫的），所以沒有程式區塊標記。
"""
import re

SITE = "MyTxGNN"
CODE = "my"
BUNDLE_KEY = "npra"  # 證據包裡本站市場資料的鍵

# ---------- 頁首等級（page_format） ----------
LEVEL_LABELS = ["Tahap Bukti", "Aras Bukti", "Paras Bukti"]  # 總覽表的證據等級欄名（2026-11-12 實測 626／4／3 頁）
HEADER_LABEL = r"Tahap bukti"
WITHDRAWN = r"Ditarik balik"
# 頁首規則：2026-11-12 實測 598 頁有總覽等級，頁首全部＝格裡第一個等級（主預測）；整格取最高會有 4 頁不同
HEADER_RULE = "first"
DESC_LEVEL_RE = re.compile(r"tahap bukti (L[1-5]|N/A)", re.I)


def desc_level_text(level):
    return "kegunaan diketahui sahaja" if level == "N/A" else f"tahap bukti {level}"


DISCLAIMER_RE = re.compile(r"^## Penafian\b", re.M)

# ---------- 頁面文字（apply_drug_reviews） ----------
T = {
    "label": {"correct": "Pembetulan semakan", "annotate": "Nota semakan", "rereview": "Menunggu semakan semula",
              "rereview_result": "Keputusan semakan semula"},
    "action": {"correct": "Dibetulkan", "annotate": "Nota ditambah", "rereview": "Ditanda untuk semakan semula",
               "section": "Bahagian bersumber ditambah", "rereview_result": "Semakan semula selesai",
               "header_level": "Tahap bukti pengepala dikira semula daripada Gambaran Ringkas",
               "description_level": "Tahap bukti dalam keterangan halaman diselaraskan dengan pengepala"},
    "verdict": {"maintain": "Dikekalkan", "downgrade": "Diturunkan", "upgrade": "Dinaikkan", "withdraw": "Ditarik balik"},
    "log_head": "## Rekod Semakan",
    "log_cols": "| Tarikh semakan | Perkara | Tindakan | Sumber |",
    "head": "> **{label} ({date})**: ",
    "originally": "Asalnya dinyatakan: \"{claim}\"",
    "source": "Sumber: {src}.",
    "decision": "Cadangan keputusan: {note}",
    "level_same": "tahap bukti {o} kekal",
    "level_change": "tahap bukti {o} → {n}",
    "table_updated": (" {labels} di halaman ini telah dikemas kini mengikut keputusan semakan semula; nilai asal disenaraikan "
                      "dalam Rekod Semakan di bawah."),
    "rereviewed": "Ditanda untuk semakan semula → telah disemak semula (lihat keputusan semakan semula)",
    "hdr": "Tahap bukti pengepala dikira semula daripada Gambaran Ringkas ({o} → {n})",
    "hdr_withdraw": "Ramalan utama ditarik balik semasa semakan semula; tahap bukti pengepala dikira semula ({o} → {n})",
    "listed_under": ", kini disenaraikan di bawah \"{t}\"",
    "rr": "Semakan semula: {v}, {c}",
    "tu": "; {l}: \"{a}\" → \"{b}\"",
    "desc": ("Keterangan halaman: \"tahap bukti {o}\" ditukar kepada \"{n}\" (mengikut tahap bukti pengepala; teks lain tidak "
             "berubah, teks asal disimpan dalam rekod)"),
    "revised": " (disemak {d}; versi terdahulu disimpan dalam rekod)",
    "superseded": "Digantikan oleh jadual pendaftaran yang dijana program (asalnya: {a})",
    "regen": "Tiada lagi selepas laporan dijana semula ({d}: {n}; asalnya: {a})",
    "prog": "Tiada lagi selepas pembetulan program ({d}: {n}; asalnya: {a})",
    "wd": "Semakan ditarik balik ({d}: {n}; asalnya: {a})",
    "intro": ("Berikut ialah rekod semakan halaman ini: kenyataan yang disemak terhadap data pendaftaran produk NPRA "
              "(data.gov.my). Pembetulan terhad kepada kenyataan fakta asas; ramalan model, tahap bukti dan kesimpulan "
              "tidak ditulis semula."),
    "intro_levels": ("Berikut ialah rekod semakan halaman ini; tahap bukti pengepala mengikut Gambaran Ringkas. Ramalan model, "
                     "jadual gambaran dan kesimpulan tidak ditulis semula."),
    "intro_rr": ("Berikut ialah rekod semakan halaman ini. Pembetulan terhad kepada kenyataan fakta asas dan teks ramalan model "
                 "tidak ditulis semula; tahap bukti dan keputusan hanya diubah oleh keputusan semakan semula (penurunan, "
                 "kenaikan atau penarikan balik), dengan nilai asal disenaraikan di bawah."),
}

# ---------- 許可證（licenses、build_license_snapshot） ----------
MARKET_SEC = re.compile(r"^## Maklumat Pasaran (?:di )?Malaysia\s*$")
ID_RE = re.compile(r"\bMAL\d{8}[A-Z]{0,5}\b")  # NPRA 註冊號（2026-11-12 依證據包實測：MAL＋8 碼數字＋0–5 個字母）


def own_ids(tf):
    return sorted({str(r.get("reg_no") or "").strip() for r in tf.get("records") or [] if r.get("reg_no")})


# ---------- 刪改轉紀錄（reviews_from_edits） ----------
# 2026-10-31～11-06 的許可證刪改（git log docs/_drugs；排程狀態格 d52034e2、欄位名統一、排除表、AI 重產、description、表格空行不算）
COMMITS = ["5a37df06", "58c20f92"]
# 期間內以 AI 整份重產報告或套排除表重寫段落的提交
REGEN_COMMITS = ["33e13285", "40ffaec8", "04324438", "5cea38e3", "478827ba", "fc8dcc33", "63cea5ad", "03d964eb", "16a9c46b",
                 "626b71a2"]
SOURCES = [{"title": "NPRA pharmaceutical product registrations (data.gov.my)",
            "url": "https://data.gov.my/data-catalogue/pharmaceutical_products"}]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z0-9(*"\[])|\n')
PROGRAM_LINES = []
CLASSIFY = [
    ("tw", re.compile(r"Taiwan|TFDA", re.I)),
    ("cancel", re.compile(r"dibatalkan|pembatalan|batal|tamat tempoh|luput|tidak (lagi )?dipasarkan|tidak (lagi )?sah|"
                          r"tidak (berdaftar|didaftarkan)|tidak mempunyai (sebarang )?(lesen|pendaftaran|produk berdaftar)|"
                          r"tiada (sebarang )?(lesen|pendaftaran|produk berdaftar)|belum (ada|didaftarkan)", re.I)),
    ("count", re.compile(r"\d+\s*(lesen|pendaftaran|produk)|kesemua|semua [^.]{0,40}sah|\bsah\b|dipasarkan", re.I)),
    ("combo", re.compile(r"bahan tunggal|kombinasi|gabungan|pelbagai bahan", re.I)),
]
SUMMARY = "Dipadam: \"{text}\""
REGEN_NOTE = "laporan dijana semula pada November 2026 dan tidak lagi mengandungi kenyataan ini"


def reason_kind(reason):
    """人工清單（scripts/license_sentence_fixes.json）的中文理由 → 類別；判斷不了回 None（改用被刪文字分類）"""
    if re.search(r"台灣|TFDA|模板殘留", reason):
        return "tw"
    if re.search(r"撤銷|過期|註銷", reason):
        return "count"  # 人工清單這類理由是「正文說有效，事實是已撤銷／過期」，用不分方向的狀態說明
    if re.search(r"查無|未上市", reason):
        return "cancel"
    if re.search(r"單方|複方", reason):
        return "combo"
    if re.search(r"張|有效|總數", reason):
        return "count"
    return None


def _fig(fc):
    if not fc or fc.get("total") is None:
        return ""
    return (f" Ubat ini mempunyai {fc['total']} pendaftaran (sah: {fc.get('valid') or 0}); angka semasa terdapat dalam "
            "Gambaran Ringkas dan jadual di bawah Maklumat Pasaran Malaysia.")


def note_for(kind, date, fc):
    d = f"data pendaftaran produk NPRA (data.gov.my) yang dibina semula mengikut bahan aktif pada {date}"
    if kind == "tw":
        return "Dipadam: teks templat sisa mengenai TFDA Taiwan, yang tidak berkaitan dengan halaman Malaysia ini."
    if kind == "cancel":
        return (f"Dipadam: ia menyatakan ubat ini tidak berdaftar, pendaftarannya dibatalkan atau tamat tempoh, atau tidak dipasarkan "
                f"di Malaysia, yang tidak sepadan dengan {d}." + _fig(fc))
    if kind == "count":
        return f"Dipadam: bilangan atau status pendaftaran yang dinyatakan tidak sepadan dengan {d}." + _fig(fc)
    if kind == "combo":
        return f"Dipadam: penerangan produk bahan tunggal atau kombinasi tidak sepadan dengan {d}." + _fig(fc)
    return f"Dipadam: ia bercanggah dengan {d}." + _fig(fc)


# ---------- 原適應症交叉驗證（check_original_indications） ----------
ORIG_LABELS = ["Indikasi Asal"]
ORIG_NONE_RE = re.compile(r"^\s*(tiada|tidak (tersedia|diketahui|direkodkan)|—|-|N/A)", re.I)
ORIG_SPLIT_RE = re.compile(r"[;,/()]+|\bdan\b|\batau\b", re.I)
