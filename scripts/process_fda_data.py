#!/usr/bin/env python3
"""處理 NPRA 藥品資料 - Malaysia 版本

將從 data.gov.my 下載的藥品資料轉換為標準 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    https://data.gov.my/data-catalogue/pharmaceutical_products
    授權: CC BY 4.0

產生檔案:
    data/raw/my_fda_drugs.json
"""

import json
import re
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_data(url: str, output_path: Path) -> Path:
    """從 data.gov.my 下載資料

    Args:
        url: 下載 URL
        output_path: 輸出檔案路徑

    Returns:
        下載的檔案路徑
    """
    print(f"從 data.gov.my 下載資料...")
    print(f"URL: {url}")

    response = requests.get(url, timeout=60)
    response.raise_for_status()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(response.content)

    print(f"下載完成: {output_path}")
    print(f"檔案大小: {output_path.stat().st_size / 1024 / 1024:.1f} MB")

    return output_path


def parse_ingredient_name(ingredient_str: str) -> str:
    """解析成分名稱（去除劑量資訊）"""
    if not ingredient_str or pd.isna(ingredient_str):
        return ""
    match = re.match(r"^([^\[]+)", ingredient_str.strip())
    if match:
        return match.group(1).strip()
    return ingredient_str.strip()


def normalize_ingredients(ingredients_str: str, separator: str = ",") -> str:
    """正規化成分字串

    將 "IMIPENEM MONOHYDRATE[530.1 mg],CILASTATIN SODIUM[530.7 mg]"
    轉換為 "IMIPENEM MONOHYDRATE;;CILASTATIN SODIUM"
    """
    if not ingredients_str or pd.isna(ingredients_str):
        return ""

    parts = ingredients_str.split(separator)
    names = []
    for part in parts:
        name = parse_ingredient_name(part)
        if name:
            names.append(name)

    return ";;".join(names)


def process_csv(csv_path: Path, output_path: Path) -> Path:
    """處理 CSV 並轉換為 JSON

    Args:
        csv_path: CSV 檔案路徑
        output_path: 輸出 JSON 檔案路徑

    Returns:
        輸出檔案路徑
    """
    config = load_field_config()

    print(f"讀取 CSV: {csv_path}")
    df = pd.read_csv(csv_path)
    print(f"原始資料: {len(df):,} 筆")

    # 新增正規化的成分欄位
    print("正規化成分名稱...")
    separator = config.get("ingredient_separator", ",")
    df["ingredients_normalized"] = df["active_ingredient"].apply(
        lambda x: normalize_ingredients(x, separator)
    )

    # 統計
    included_descriptions = config.get("included_descriptions", [])
    if included_descriptions:
        filtered = df[df["description"].isin(included_descriptions)]
        print(f"處方藥/西藥: {len(filtered):,} 筆")
    else:
        filtered = df

    # 轉換為 JSON
    print(f"儲存至: {output_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    records = df.to_dict(orient="records")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(records):,} 筆藥品資料")

    return output_path


def main():
    print("=" * 60)
    print("處理 NPRA 藥品資料 (Malaysia)")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    config = load_field_config()
    data_source = config.get("data_source", {})

    # 檢查是否已有 CSV 檔案
    csv_path = raw_dir / "pharmaceutical_products.csv"
    if not csv_path.exists():
        # 下載資料
        url = data_source.get("url", "https://storage.data.gov.my/healthcare/pharmaceutical_products.csv")
        download_data(url, csv_path)
    else:
        print(f"使用現有 CSV: {csv_path}")
        print(f"檔案大小: {csv_path.stat().st_size / 1024 / 1024:.1f} MB")

    print()

    # 處理並轉換為 JSON
    output_path = raw_dir / "my_fda_drugs.json"
    process_csv(csv_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
