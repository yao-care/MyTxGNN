"""NPRA 藥品資料載入與過濾 - Malaysia 版本"""

import json
import re
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_ingredient_name(ingredient_str: str) -> str:
    """解析成分名稱（去除劑量資訊）

    Args:
        ingredient_str: 原始成分字串，如 "LEVETIRACETAM[500 mg]"

    Returns:
        成分名稱，如 "LEVETIRACETAM"
    """
    if not ingredient_str or pd.isna(ingredient_str):
        return ""

    # 去除 [...] 部分
    match = re.match(r"^([^\[]+)", ingredient_str.strip())
    if match:
        return match.group(1).strip()
    return ingredient_str.strip()


def parse_ingredients(ingredients_str: str, separator: str = ",") -> list[str]:
    """解析多個成分

    Args:
        ingredients_str: 原始成分字串
        separator: 分隔符

    Returns:
        成分名稱列表
    """
    if not ingredients_str or pd.isna(ingredients_str):
        return []

    parts = ingredients_str.split(separator)
    names = []
    for part in parts:
        name = parse_ingredient_name(part)
        if name:
            names.append(name)
    return names


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 NPRA 藥品資料

    Args:
        filepath: JSON 檔案路徑，預設為 data/raw/my_fda_drugs.json

    Returns:
        包含所有藥品的 DataFrame

    Raises:
        FileNotFoundError: 找不到資料檔案時，提供下載指引
    """
    config = load_field_config()

    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "my_fda_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到藥品資料: {filepath}\n"
            f"請先執行以下步驟：\n"
            f"1. 執行: uv run python scripts/process_fda_data.py\n"
            f"   （腳本會自動從 data.gov.my 下載資料）"
        )

    with open(filepath, "r", encoding=config.get("encoding", "utf-8")) as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """過濾有效藥品

    Args:
        df: 原始藥品 DataFrame

    Returns:
        僅包含有效藥品的 DataFrame（處方藥、非處方藥、新化學實體、生物製劑）
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]
    included_descriptions = config.get("included_descriptions", [])

    # 取得欄位名稱
    status_field = field_mapping.get("status", "status")
    description_field = field_mapping.get("dosage_form", "description")
    ingredients_field = field_mapping.get("ingredients", "active_ingredient")

    active = df.copy()

    # 按產品類型過濾（排除保健品、天然產品、獸醫用品）
    if included_descriptions and description_field in active.columns:
        active = active[active[description_field].isin(included_descriptions)]

    # 過濾有成分的藥品（TxGNN 需要）
    if ingredients_field and ingredients_field in active.columns:
        active = active[active[ingredients_field].notna() & (active[ingredients_field] != "")]

    # 重設索引
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """取得藥品資料摘要統計

    Args:
        df: 藥品 DataFrame

    Returns:
        摘要統計字典
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]

    ingredients_field = field_mapping.get("ingredients", "active_ingredient")
    description_field = field_mapping.get("dosage_form", "description")

    summary = {"total_count": len(df)}

    if ingredients_field and ingredients_field in df.columns:
        summary["with_ingredient"] = int(df[ingredients_field].notna().sum())

        # 統計唯一成分數
        all_ingredients = set()
        separator = config.get("ingredient_separator", ",")
        for ing_str in df[ingredients_field].dropna():
            for name in parse_ingredients(ing_str, separator):
                all_ingredients.add(name.upper())
        summary["unique_ingredients"] = len(all_ingredients)

    if description_field and description_field in df.columns:
        summary["by_description"] = df[description_field].value_counts().to_dict()

    return summary
