"""MY（NPRA，data.gov.my）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://storage.data.gov.my/healthcare/pharmaceutical_products.csv（免金鑰）。欄位 reg_no、status、date_end。
這份檔只收現行有效的註冊（PRODUCT APPROVED／CONDITIONAL REGISTRATION）。
2026-10-31 加上同站的撤銷資料集 pharmaceutical_products_cancelled.csv（Pihak Berkuasa Kawalan Dadah 撤銷註冊的全量清單），
在這份查到、現行檔沒有的 reg_no 狀態寫 CANCELLED_STATUS。
2026-11-05（用戶決定）：兩份都查不到的不再預設為有效，改依證據包紀錄的到期日（date_end）判定：已過期 → EXPIRED_STATUS
（reviewer 的註銷字樣含 expir，算非有效）；未過期 → 保留原狀態、列在 summary（preprocess，本週沒有對到的號碼才處理）。
登記號尾碼不同就是不同產品（實測同號碼不同尾碼有 5 組是不同藥），只做完全比對。
證據包（npra 區塊）紀錄 reg_no、status＝NPRA 原文。
"""
import csv
import io
import re
import time

import requests

RAW_FILE = "raw/npra_status.json"
URL = "https://storage.data.gov.my/healthcare/pharmaceutical_products.csv"
CANCELLED_URL = "https://storage.data.gov.my/healthcare/pharmaceutical_products_cancelled.csv"
CANCELLED_STATUS = "Cancelled"  # data.gov.my 資料集英文名 Cancelled Pharmaceutical Products


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
    out = [{"reg_no": (x["reg_no"] or "").strip(), "status": (x["status"] or "").strip(), "date_end": (x.get("date_end") or "").strip()}
           for x in rows if x.get("reg_no")]
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
    return out


def validate(new, old):
    p = []
    if len(new) < 15000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


EXPIRED_STATUS = "Expired (not in current NPRA register)"
_IDX = {}


def status_index(new):
    _IDX.clear()
    _IDX.update({r["reg_no"]: r["status"] for r in new if r["status"]})
    return dict(_IDX)


def expired(rec, today=None):
    """現行檔與撤銷檔都查不到、到期日已過的紀錄（2026-11-05）"""
    from datetime import date
    end = str(rec.get("date_end") or rec.get("expiry_date") or "").strip()[:10]
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", end)) and end < (today or date.today().isoformat())


def preprocess(b):
    """兩份資料都查不到的登記號：到期日已過就改成 EXPIRED_STATUS（不再預設有效）。回傳是否有變"""
    if not _IDX:
        return False
    ch = False
    for r in (b.get("npra") or {}).get("records") or []:
        k = record_id(r)
        if k and k not in _IDX and expired(r) and r.get("status") != EXPIRED_STATUS:
            r["status"] = EXPIRED_STATUS
            ch = True
    return ch


def record_id(rec):
    return str(rec.get("reg_no") or rec.get("license_id") or "").strip()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True
