"""MY（NPRA，data.gov.my）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://storage.data.gov.my/healthcare/pharmaceutical_products.csv（免金鑰）。欄位 reg_no、status、date_end。
這份檔只收現行有效的註冊（PRODUCT APPROVED／CONDITIONAL REGISTRATION），沒有撤銷紀錄：
新檔查不到的 reg_no 保留原狀態、列在 summary（不推定為撤銷）。
證據包（npra 區塊）紀錄 reg_no、status＝NPRA 原文。
"""
import csv
import io
import time

import requests

RAW_FILE = "raw/npra_status.json"
URL = "https://storage.data.gov.my/healthcare/pharmaceutical_products.csv"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=300)
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    rows = csv.DictReader(io.StringIO(r.content.decode("utf-8-sig")))
    if "reg_no" not in (rows.fieldnames or []) or "status" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    return [{"reg_no": (x["reg_no"] or "").strip(), "status": (x["status"] or "").strip(), "date_end": (x.get("date_end") or "").strip()}
            for x in rows if x.get("reg_no")]


def validate(new, old):
    p = []
    if len(new) < 15000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["reg_no"]: r["status"] for r in new if r["status"]}


def record_id(rec):
    return str(rec.get("reg_no") or rec.get("license_id") or "").strip()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True
