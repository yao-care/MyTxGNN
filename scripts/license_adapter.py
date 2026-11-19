"""MY（NPRA，data.gov.my）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://storage.data.gov.my/healthcare/pharmaceutical_products.csv（免金鑰）。欄位 reg_no、status、date_end。
這份檔只收現行有效的註冊（PRODUCT APPROVED／CONDITIONAL REGISTRATION）。
2026-10-31 加上同站的撤銷資料集 pharmaceutical_products_cancelled.csv（Pihak Berkuasa Kawalan Dadah 撤銷註冊的全量清單），
在這份查到、現行檔沒有的 reg_no 狀態寫 CANCELLED_STATUS。
2026-11-05（用戶決定）：兩份都查不到的不再預設為有效，改依證據包紀錄的到期日（date_end）判定：已過期 → EXPIRED_STATUS
（reviewer 的註銷字樣含 expir，算非有效）；未過期 → UNKNOWN_STATUS（2026-11-05 用戶決定：不算有效也不算註銷，
概覽另列「status tidak dapat disahkan」張數；preprocess，本週沒有對到的號碼才處理）。之後任一份清單查到就換成該清單的狀態。
登記號尾碼不同就是不同產品（實測同號碼不同尾碼有 5 組是不同藥），只做完全比對。
證據包（npra 區塊）紀錄 reg_no、status＝NPRA 原文。
2026-11-17（用戶要求確認 11-16 排程「新資料查不到」的 324 張）：data.gov.my 只有這兩份藥品註冊資料集（現行、撤銷），逐號比對：
- 50 張是同一張註冊換了尾碼（NPRA 登記號後的類別字母改了，例：MAL09020971ARZ→MAL09020971ACRZ、MAL21046030AZ 到期後
  以 MAL21046030ARZ 續證）。判定條件：前 8 位數字相同，產品名與有效成分（去 HTML 實體、空白、大小寫）都相同（持有人可不同，
  例：Progynova 由 Bayer 轉 Menarini）。新號不在同一個證據包（12 張）：status_index 讓舊號沿用新號的現行狀態；
  新號已在同一個證據包（38 張）：舊號是同一張註冊的重複一筆，寫 RETIRED_STATUS（算非有效，免得算兩張）。ALIASES 記對照。
  「同一個證據包」逐個證據包判斷（preprocess 標 npra_duplicate_of，update 換狀態；2026-11-17 修正，原本用全站聯集）。
  產品名或成分不同的同號不同尾碼（例：MAL11030014AZ Prevulcer／MAL11030014HA Toltravet）不認。
- 兩份都沒有、證據包到期日已過（208 張＋同號不同產品 1 張）＝NPRA 現行註冊已不列且未續證：preprocess 照舊寫 EXPIRED_STATUS，
  另記 npra_not_listed（第一次發現日；又出現在清單就拿掉）；confirmed_absent() 讓排程列成「現行清單確認已不列」，不算查不到。
- 兩份都沒有、到期日未到（65 張，例：Cymbalta MAL05092473ARZ）：維持 2026-11-05 用戶決定的 UNKNOWN_STATUS（不推定撤銷；
  NPRA QUEST 單筆查詢擋自動化請求，無法逐號確認），照舊列在「新資料查不到」。
兩份資料集任一份下載失敗或現行號碼少於 MIN_CURRENT 時不做上述判定（CURRENT 留空）。
2026-11-19（用戶以瀏覽器在 NPRA QUEST3+ https://quest3plus.bpfk.gov.my/pmo2/index.php 逐筆查上面 65 張 UNKNOWN_STATUS 的號碼，
並對照 data.gov.my 兩份資料集 2026-11-19 03:00 版；結果 txgnn/.claude/manual_license_lookup_20261117/my_npra_result_20261119.csv）：
- 換號 3 張（前 8 碼相同、持有人與成分相同，產品名不同所以自動換尾碼規則認不到）收在 MY_RENUMBERED（人工確認表，每筆附依據）：
  處理同換尾碼（新號不在同一個證據包→沿用新號狀態並寫 now listed as；在同一個證據包→RETIRED_STATUS）。不放寬自動規則。
- 61 張兩份資料集都沒有、QUEST3+ 依號碼與品名也查不到，收在 MY_NOT_LISTED_CONFIRMED：preprocess 寫 NOT_LISTED_STATUS、
  license_status＝cancelled（事實層非有效；NPRA 沒有公開撤銷日，頁面不寫成 dibatalkan）、npra_manual_check＝查核日；
  confirmed_absent 回真。這張表不依賴下載；之後任一份清單又查到就照清單狀態並拿掉這些標記。
- MAL19890435ACZ TUSSIFED SYRUP：QUEST3+ 仍列、data.gov.my 兩份都不列，兩邊矛盾，維持 UNKNOWN_STATUS。
"""
import csv
import html
import io
import json
import re
import time
from pathlib import Path

import requests

RAW_FILE = "raw/npra_status.json"
URL = "https://storage.data.gov.my/healthcare/pharmaceutical_products.csv"
CANCELLED_URL = "https://storage.data.gov.my/healthcare/pharmaceutical_products_cancelled.csv"
CANCELLED_STATUS = "Cancelled"  # data.gov.my 資料集英文名 Cancelled Pharmaceutical Products
CURRENT: set = set()   # fetch() 填：現行檔＋撤銷檔的登記號；空的就不做「不在清單」判定
MIN_CURRENT = 20000    # 現行檔登記號少於這個數＝下載或格式有問題，不判定
_CUR_ROWS = {}         # 現行檔：reg_no → {product, active_ingredient, status}（換尾碼比對用）
ALIASES = {}           # status_index 填：舊登記號 → 現行檔裡同一產品的新登記號
# 舊號、新號都在同一個證據包時舊號的狀態（含 reviewer 的註銷字樣 retir，算非有效；新號那筆照常算有效）
RETIRED_STATUS = "Registration number retired (not in current NPRA register; same product now listed as {})"

_MANUAL_BASIS = ("NPRA QUEST3+ (https://quest3plus.bpfk.gov.my/pmo2/index.php) manual search by registration number and product name, 2026-11-19; "
                 "data.gov.my pharmaceutical_products.csv / pharmaceutical_products_cancelled.csv, version 2026-11-19 03:00 (MYT)")
# 2026-11-19 人工確認的換號：舊號 → (新號, 依據)。新號在 data.gov.my 現行檔為 PRODUCT APPROVED
MY_RENUMBERED = {
    "MAL16035030N": ("MAL16035030NC", _MANUAL_BASIS + "; new number MAL16035030NC 'MHD NutriCenta Enteric-Coated Softgel', "
                     "CAMERON BIOSCIENCE (M) SDN. BHD. (same holder), PRODUCT APPROVED, end date 2031-03-26"),
    "MAL23046028ACZ": ("MAL23046028AZ", _MANUAL_BASIS + "; Xostavid 40 now listed as MAL23046028AZ 'Urilog 40 (Febuxostat Film Coated "
                       "Tablets 40 mg)', HEALOL PHARMACEUTICALS SDN. BHD. (same holder, same ingredient), PRODUCT APPROVED, end date 2028-04-06"),
    "MAL23046029ACZ": ("MAL23046029AZ", _MANUAL_BASIS + "; now listed as MAL23046029AZ 'Urilog 80 (Febuxostat Film Coated Tablets 80 mg)', "
                       "HEALOL PHARMACEUTICALS SDN. BHD. (same holder, same ingredient), PRODUCT APPROVED, end date 2028-04-06"),
}
# 2026-11-19 人工確認：兩份 data.gov.my 資料集都沒有、QUEST3+ 依號碼與品名都查不到的號碼 → 證據包品名（依據同 _MANUAL_BASIS）
# MAL20066031NC：同前 8 碼的 MAL20066031NCR 是 watsons 魚油、持有人不同，不是換號
MY_MANUAL_CHECKED = "2026-11-19"
MY_NOT_LISTED_CONFIRMED = {
    "MAL17025022ACZ": "Genvoya (Elvitegravir 150mg/Cobicistat 150mg/Emtricitabine 200mg/Tenofovir alafenamide10mg) Film-Coated Tablets",
    "MAL20040573AZ": "DHNP HYDROXYUREA CAPSULE 500MG",
    "MAL16115027ACRZ": "ESBRIET HARD CAPSULES 267MG",
    "MAL19970944XZ": "ASPIRIN CARDIO",
    "MAL21056004AZ": "Triveram 10mg/5mg/5mg (atorvastatin/perindopril arginine/amlodipine) film-coated tablets",
    "MAL21056005AZ": "Triveram 20mg/5mg/5mg (atorvastatin/perindopril arginine/amlodipine) film-coated tablets",
    "MAL21056006AZ": "Triveram 20mg/10mg/5mg (atorvastatin/perindopril arginine/amlodipine) film-coated tablets",
    "MAL21056007AZ": "Triveram 20mg/10mg/10mg (atorvastatin/perindopril arginine/amlodipine) film-coated tablets",
    "MAL21056008AZ": "Triveram 40mg/10mg/10mg (atorvastatin/perindopril arginine/amlodipine) film-coated tablets",
    "MAL22056017NC": "JH NUTRITION HEMACEL TABLET",
    "MAL19871097ACRZ": "MADOPAR ROCHE 125 CAPSULE",
    "MAL19871056AZ": "SALMODIL SYRUP",
    "MAL20132279AZ": "Salmodil-SF Expectorant Syrup",
    "MAL19962487X": "MULTI ELIXIR",
    "MAL26026009X": "ROIHI-TSUBOKO PLASTER",
    "MAL13045055XC": "Chimpanzee Brand Medicated Oil",
    "MAL20000004ARZ": "CELEBREX CAPSULE 100MG",
    "MAL20066031NC": "Bio+ Omega3 TG Fish Oil EPA/DHA 540/360 Plus Softgel",
    "MAL07090895XZ": "Mycoderm-C  Powder 1% w/w",
    "MAL19116032ACRZ": "CUBICIN (DAPTOMYCIN FOR INJECTION) 500MG VIAL",
    "MAL19890423AZ": "REMETHAN 50 E.C. TABLET",
    "MAL19990992ACRZ": "CATAFLAM 1.5% DROPS",
    "MAL10063022XCS": "daflon 500mg tablets",
    "MAL19872253AZ": "MOTILIUM ORAL SUSPENSION 1MG/ML",
    "MAL05092473ARZ": "Cymbalta Capsule 30mg",
    "MAL05092474ARZ": "Cymbalta Capsule 60mg",
    "MAL16125023AZ": "FORSTAVIR-LE ( Efavirenz 600 mg, Lamivudine 300 mg and Tenofovir Disoproxil Fumarate 300 mg ) Film-coated Tablets",
    "MAL18046182ARZ": "Fluconazole Kabi 2mg/ml solution for infusion",
    "MAL07031127ACZ": "Prozac Capsule 20mg",
    "MAL06081215AZ": "LIGNOCAINE HCl - FRESENIUS 2% INJECTION",
    "MAL20040909ARZ": "TARIVID OPHTHALMIC SOLUTION",
    "MAL17107023ARZ": "Piperacillin/Tazobactam Kabi 2g/0.25g Powder for Solution for Infusion",
    "MAL19056024AZ": "ALOJA 75 (Pregabalin Capsules 75 mg)",
    "MAL19056025AZ": "ALOJA 150 (Pregabalin Capsules 150 mg)",
    "MAL20041156AZ": "RISPERDAL CONSTA 25MG",
    "MAL20041157AZ": "RISPERDAL CONSTA 37.5MG",
    "MAL20041158AZ": "RISPERDAL CONSTA 50MG",
    "MAL20020816ARSZ": "MABTHERA VIALS 100MG/10ML",
    "MAL20020817ARSZ": "MABTHERA VIALS 500MG/50ML",
    "MAL22026008AZ": "TRAMASURE-100 Tramadol Hydrochloride Injection 50mg/ml",
    "MAL19950210AZ": "NAVELBINE 10MG,INJECTABLE SOLUTION",
    "MAL19950211AZ": "NAVELBINE INJECTABLE 50MG",
    "MAL19126017ARZ": "Noradrenaline Sintetica 1mg/ml Concentrate for Solution for Infusion",
    "MAL09011482ACZ": "Cancidas Injection 50mg/vial",
    "MAL24106008XCE": "Cortal Glucosamine Chondroitin MSM Capsule",
    "MAL14015013ARZ": "FORXIGA 5MG FILM-COATED TABLET",
    "MAL19056104AZ": "BEVESPI AEROSPHERE 7.2 / 5.0 micrograms pressurised inhalation, suspension",
    "MAL25026029XCZ": "Cortal Sore Throat Spray 0.45 %w/v",
    "MAL20102073AZ": "VICTOZA 6MG/ML SOLUTION FOR INJECTION IN PRE-FILLED PEN",
    "MAL25036144XC": "Cortal Analgesic Cream",
    "MAL16115037AZ": "BLOKTIENE CHEWABLE TABLET 4mg",
    "MAL16115038AZ": "BLOKTIENE CHEWABLE TABLET 5MG",
    "MAL23026029NC": "SLOAGE TABLET",
    "MAL19870712AZ": "Oxytocin-Richter solution for injection 10 I.U / 1 ml",
    "MAL07021408ARZ": "Nootropil Tablet  800 mg",
    "MAL07021409ARZ": "Nootropil Tablet 1200 mg",
    "MAL09061595ARZ": "Sodium Chloride Kabi 0.9%w/v Solution for Infusion",
    "MAL20081740AZ": "CHAMPIX 0.5MG FILM-COATED TABLETS",
    "MAL20081741AZ": "CHAMPIX 1.0MG FILM-COATED TABLETS",
    "MAL20040542AZ": "VFEND 50MG TABLET",
    "MAL20071669ACZ": "VFEND POWDER FOR ORAL SUSPENSION 40MG/ML",
}
# 不可以 "Status unknown (registration number not found" 開頭（reviewer 會判成 unknown）；不寫 cancelled（NPRA 沒有公開撤銷）
NOT_LISTED_STATUS = ("Not in current NPRA register (checked " + MY_MANUAL_CHECKED + " in NPRA QUEST3+ and both data.gov.my datasets; "
                     "date of removal from the register not published)")


def _get(url):
    for attempt in range(4):
        try:
            r = requests.get(url, timeout=300)
            r.raise_for_status()
            return csv.DictReader(io.StringIO(r.content.decode("utf-8-sig")))
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def fetch():
    rows = _get(URL)
    if "reg_no" not in (rows.fieldnames or []) or "status" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    CURRENT.clear()
    _CUR_ROWS.clear()
    out = []
    for x in rows:
        k = (x.get("reg_no") or "").strip()
        if not k:
            continue
        out.append({"reg_no": k, "status": (x["status"] or "").strip(), "date_end": (x.get("date_end") or "").strip()})
        _CUR_ROWS[k] = {"product": x.get("product") or "", "active_ingredient": x.get("active_ingredient") or "",
                        "status": (x["status"] or "").strip()}
    seen = {x["reg_no"] for x in out}
    can = _get(CANCELLED_URL)
    if "reg_no" not in (can.fieldnames or []):
        raise RuntimeError(f"撤銷資料集欄位改變：{can.fieldnames}")
    n = 0
    for x in can:
        k = (x.get("reg_no") or "").strip()
        if k and k not in seen:
            out.append({"reg_no": k, "status": CANCELLED_STATUS, "date_end": (x.get("date_end") or "").strip()})
            seen.add(k)
            n += 1
    if n < 500:
        raise RuntimeError(f"撤銷資料集只解析出 {n} 筆，疑似格式改變")
    if len(_CUR_ROWS) >= MIN_CURRENT:
        CURRENT.update(seen)
    return out


def validate(new, old):
    p = []
    if len(new) < 15000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


EXPIRED_STATUS = "Expired (not in current NPRA register)"
# 不可含 reviewer 的註銷字樣（cancel／withdraw／revok／expir…），reviewer 依 UNKNOWN_RX 判成 unknown
UNKNOWN_STATUS = "Status unknown (registration number not found in either NPRA dataset, not yet past its end date)"
_IDX = {}


def _norm(v):
    return re.sub(r"\s+", " ", html.unescape(str(v or ""))).strip().lower()


_BUNDLE_RECS = {}
_CO_IDS = {}   # reg_no → 跟它同一個證據包（任一個藥）的所有登記號


def _bundle_records():
    """站上證據包的 npra 紀錄：reg_no → 紀錄（換尾碼比對、確認到期日用；同號多筆取第一筆）"""
    if not _BUNDLE_RECS:
        for f in sorted((Path(__file__).resolve().parents[1] / "data/bundles").glob("*/drug_bundle.json")):
            try:
                b = json.loads(f.read_text(encoding="utf-8"))
            except Exception:
                continue
            recs = (b.get("npra") or {}).get("records") or []
            ids = {record_id(r) for r in recs}
            for r in recs:
                _BUNDLE_RECS.setdefault(record_id(r), r)
                _CO_IDS.setdefault(record_id(r), set()).update(ids)
    return _BUNDLE_RECS


def _alias(k, rec):
    """現行檔裡同一張註冊換了尾碼的新號：前 8 位數字相同、產品名與有效成分都相同；只有唯一一個才認"""
    m = re.match(r"MAL\d{8}", k)
    if not m or not CURRENT:
        return None
    hit = [a for a, c in _CUR_ROWS.items() if a != k and a.startswith(m.group(0))
           and _norm(c["product"]) == _norm(rec.get("product")) and _norm(c["product"])
           and _norm(c["active_ingredient"]) == _norm(rec.get("active_ingredient"))]
    return hit[0] if len(hit) == 1 else None


def status_index(new):
    _IDX.clear()
    _IDX.update({r["reg_no"]: r["status"] for r in new if r["status"]})
    ALIASES.clear()
    if CURRENT:
        for k, rec in _bundle_records().items():
            if k and k not in _IDX:
                a = _alias(k, rec)
                if a and _CUR_ROWS[a]["status"]:
                    ALIASES[k] = a
                    # 全站共用的狀態只能是「沿用新號」；新號是否在「同一個」證據包要逐個證據包判斷（同一個舊號可能在好幾個藥的證據包裡，
                    # 例：Enhertu MAL24046001ACZ 在 trastuzumab 與 trastuzumab_deruxtecan，新號只在後者），由 preprocess 標 npra_duplicate_of、
                    # update 換成 RETIRED_STATUS（2026-11-17 修正：原本用全站聯集判斷，trastuzumab 頁少算 1 張）
                    _IDX[k] = f"{_CUR_ROWS[a]['status']} (now listed as {a})"
        for k, (a, _basis) in MY_RENUMBERED.items():  # 2026-11-19 人工確認的換號（產品名不同，自動規則認不到）
            if k not in _IDX and a in _CUR_ROWS and _CUR_ROWS[a]["status"]:
                ALIASES[k] = a
                _IDX[k] = f"{_CUR_ROWS[a]['status']} (now listed as {a})"
    return dict(_IDX)


def confirmed_absent(lid):
    """給 license_refresh：現行檔與撤銷檔都沒有、也不是換尾碼，而且證據包到期日已過＝確認已不是現行註冊"""
    k = str(lid or "").strip()
    if not CURRENT or not _IDX or k in _IDX:
        return False
    if k in MY_NOT_LISTED_CONFIRMED:  # 2026-11-19 人工確認（QUEST3+＋data.gov.my）
        return True
    rec = _bundle_records().get(k)
    return bool(rec) and expired(rec)


def expired(rec, today=None):
    """現行檔與撤銷檔都查不到、到期日已過的紀錄（2026-11-05）"""
    from datetime import date
    end = str(rec.get("date_end") or rec.get("expiry_date") or "").strip()[:10]
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", end)) and end < (today or date.today().isoformat())


def preprocess(b):
    """兩份資料都查不到的登記號：到期日已過就改成 EXPIRED_STATUS，未過期改成 UNKNOWN_STATUS（不再預設有效）。回傳是否有變"""
    if not _IDX:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    recs = (b.get("npra") or {}).get("records") or []
    ids = {record_id(r) for r in recs}
    for r in recs:
        k = record_id(r)
        a = ALIASES.get(k)
        if a and a in ids:  # 新號在同一個證據包：舊號是同一張註冊的重複一筆（update 會寫 RETIRED_STATUS）
            if r.get("npra_duplicate_of") != a:
                r["npra_duplicate_of"] = a
                ch = True
        elif CURRENT and r.pop("npra_duplicate_of", None) is not None:
            ch = True
        if k and k not in _IDX:
            manual = k in MY_NOT_LISTED_CONFIRMED
            want = NOT_LISTED_STATUS if manual else EXPIRED_STATUS if expired(r) else UNKNOWN_STATUS
            if r.get("status") != want:
                r["status"] = want
                ch = True
            if manual and (r.get("license_status") != "cancelled" or r.get("npra_manual_check") != MY_MANUAL_CHECKED):
                r["license_status"] = "cancelled"  # 事實層非有效（2026-11-19 人工確認不在 NPRA 現行註冊）
                r["npra_manual_check"] = MY_MANUAL_CHECKED
                ch = True
            if CURRENT and not r.get("npra_not_listed"):
                r["npra_not_listed"] = today  # 2026-11-17：兩份資料集都沒有，第一次發現的日期
                ch = True
        elif k and r.get("npra_not_listed"):
            r.pop("npra_not_listed", None)
            ch = True
        if k and k in _IDX and r.get("npra_manual_check"):  # 人工確認不列的號又出現在清單：照清單狀態（update 寫），拿掉標記
            r.pop("npra_manual_check", None)
            r.pop("license_status", None)
            ch = True
    return ch


def record_id(rec):
    return str(rec.get("reg_no") or rec.get("license_id") or "").strip()


def update(rec, new):
    a = ALIASES.get(record_id(rec))
    if a and rec.get("npra_duplicate_of") == a:  # preprocess 判定新號在同一個證據包
        new = RETIRED_STATUS.format(a)
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True
