"""DrugBank 映射模組 - 支援多語言版本"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

from .normalizer import extract_ingredients, get_all_synonyms


def load_drugbank_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 DrugBank 詞彙表

    Args:
        filepath: CSV 檔案路徑，預設為 data/external/drugbank_vocab.csv

    Returns:
        DrugBank 詞彙表 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drugbank_vocab.csv"

    return pd.read_csv(filepath)


def build_name_index(drugbank_df: pd.DataFrame) -> Dict[str, str]:
    """建立名稱索引（名稱 -> DrugBank ID）

    Args:
        drugbank_df: DrugBank 詞彙表

    Returns:
        名稱到 ID 的對照字典
    """
    index = {}

    for _, row in drugbank_df.iterrows():
        name_upper = row["drug_name_upper"]
        drugbank_id = row["drugbank_id"]

        # 完整名稱
        index[name_upper] = drugbank_id

        # 移除常見鹽類後綴，建立別名
        salt_suffixes = [
            " HCL", " HYDROCHLORIDE", " SODIUM", " POTASSIUM",
            " SULFATE", " SULPHATE", " MALEATE", " ACETATE",
            " CITRATE", " PHOSPHATE", " BROMIDE", " CHLORIDE",
            " TARTRATE", " FUMARATE", " SUCCINATE", " MESYLATE",
            " BESYLATE", " CALCIUM", " MAGNESIUM", " NITRATE",
            " LACTATE", " GLUCONATE", " DISODIUM", " MONOHYDRATE",
            " DIHYDRATE", " TRIHYDRATE", " ANHYDROUS",
            " DIPROPIONATE", " PROPIONATE", " ACETONIDE",
            " VALERATE", " BUTYRATE", " HEXAHYDRATE",
        ]

        for suffix in salt_suffixes:
            if name_upper.endswith(suffix):
                base_name = name_upper[:-len(suffix)].strip()
                if base_name and base_name not in index:
                    index[base_name] = drugbank_id

    # 添加常見同義詞對照
    synonym_map = {
        # 維生素
        "NIACINAMIDE": "NICOTINAMIDE",
        "NICOTINIC ACID": "NIACIN",
        "PYRIDOXINE": "VITAMIN B6",
        "THIAMINE": "VITAMIN B1",
        "RIBOFLAVIN": "VITAMIN B2",
        "CYANOCOBALAMIN": "VITAMIN B12",
        "ASCORBIC ACID": "VITAMIN C",
        "TOCOPHEROL": "VITAMIN E",
        "RETINOL": "VITAMIN A",
        "CHOLECALCIFEROL": "VITAMIN D3",
        "ERGOCALCIFEROL": "VITAMIN D2",
        "PHYTONADIONE": "VITAMIN K1",
        # 常見藥物別名
        "ACETYLSALICYLIC ACID": "ASPIRIN",
        "PARACETAMOL": "ACETAMINOPHEN",
        "ADRENALINE": "EPINEPHRINE",
        "NORADRENALINE": "NOREPINEPHRINE",
        "LIGNOCAINE": "LIDOCAINE",
        "FRUSEMIDE": "FUROSEMIDE",
        "SALBUTAMOL": "ALBUTEROL",
        # L- 前綴處理
        "L-MENTHOL": "LEVOMENTHOL",
        "MENTHOL": "LEVOMENTHOL",
        "DL-MENTHOL": "RACEMENTHOL",
        "L-ADRENALINE": "EPINEPHRINE",
        # 水合物/無水
        "CAFFEINE ANHYDROUS": "CAFFEINE",
        "DEXTROSE MONOHYDRATE": "GLUCOSE",
        "DEXTROSE": "GLUCOSE",
        "GLUCOSE MONOHYDRATE": "GLUCOSE",
    }

    for alias, canonical in synonym_map.items():
        if canonical in index and alias not in index:
            index[alias] = index[canonical]

    return index


def map_ingredient_to_drugbank(
    ingredient: str,
    name_index: Dict[str, str],
) -> Optional[str]:
    """將單一成分映射到 DrugBank ID

    映射策略（優先順序）：
    1. 完全匹配
    2. 移除鹽類後綴後匹配
    3. 使用基本名稱匹配

    Args:
        ingredient: 標準化後的成分名稱
        name_index: 名稱索引

    Returns:
        DrugBank ID，若無法映射則回傳 None
    """
    if not ingredient:
        return None

    ingredient = ingredient.upper().strip()

    # 1. 完全匹配
    if ingredient in name_index:
        return name_index[ingredient]

    # 2. 移除常見的鹽類後綴
    salt_patterns = [
        r"\s+HCL$", r"\s+HYDROCHLORIDE$", r"\s+SODIUM$",
        r"\s+POTASSIUM$", r"\s+SULFATE$", r"\s+MALEATE$",
        r"\s+ACETATE$", r"\s+CITRATE$", r"\s+PHOSPHATE$",
        r"\s+BROMIDE$", r"\s+CHLORIDE$", r"\s+TARTRATE$",
        r"\s+HBR$", r"\s+HYDROBROMIDE$", r"\s+FUMARATE$",
        r"\s+SUCCINATE$", r"\s+MESYLATE$", r"\s+BESYLATE$",
        r"\s+CALCIUM$", r"\s+MAGNESIUM$", r"\s+NITRATE$",
        r"\s+LACTATE$", r"\s+GLUCONATE$", r"\s+DISODIUM$",
        r"\s+ANHYDROUS$", r"\s+MONOHYDRATE$", r"\s+DIHYDRATE$",
        r"\s+TRIHYDRATE$", r"\s+HEXAHYDRATE$",
        r"\s+DIPROPIONATE$", r"\s+PROPIONATE$", r"\s+ACETONIDE$",
        r"\s+VALERATE$", r"\s+BUTYRATE$", r"\s+MONONITRATE$",
    ]

    base_ingredient = ingredient
    for pattern in salt_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 2b. 移除 L-/D-/DL- 前綴
    prefix_patterns = [r"^L-", r"^D-", r"^DL-"]
    base_ingredient = ingredient
    for pattern in prefix_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 3. 嘗試移除括號內容
    base_ingredient = re.sub(r"\s*\([^)]*\)", "", ingredient).strip()
    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    return None


def _detect_field(columns, candidates: List[str], default: str = "") -> str:
    """偵測欄位名稱"""
    for c in candidates:
        if c in columns:
            return c
    return default if default else candidates[0]


def map_fda_drugs_to_drugbank(
    fda_df: pd.DataFrame,
    drugbank_df: Optional[pd.DataFrame] = None,
    ingredient_field: Optional[str] = None,
    license_field: Optional[str] = None,
    brand_field: Optional[str] = None,
) -> pd.DataFrame:
    """將藥品映射到 DrugBank（支援多語言版本）

    Args:
        fda_df: 藥品 DataFrame
        drugbank_df: DrugBank 詞彙表（可選）
        ingredient_field: 成分欄位名稱（可選，自動偵測）
        license_field: 許可證欄位名稱（可選，自動偵測）
        brand_field: 品名欄位名稱（可選，自動偵測）

    Returns:
        包含映射結果的 DataFrame
    """
    if drugbank_df is None:
        drugbank_df = load_drugbank_vocab()

    # 自動偵測欄位名稱
    if ingredient_field is None:
        ingredient_field = _detect_field(
            fda_df.columns,
            ["ingredients_normalized", "主成分略述", "active_ingredient", "ingredients"]
        )
    if license_field is None:
        license_field = _detect_field(
            fda_df.columns,
            ["reg_no", "許可證字號", "license_id"]
        )
    if brand_field is None:
        brand_field = _detect_field(
            fda_df.columns,
            ["product", "中文品名", "brand_name"]
        )

    # 建立索引
    name_index = build_name_index(drugbank_df)

    results = []

    for _, row in fda_df.iterrows():
        ingredient_str = row.get(ingredient_field, "")
        if not ingredient_str or pd.isna(ingredient_str):
            continue

        # 提取所有成分及同義詞
        synonyms_data = get_all_synonyms(str(ingredient_str))

        for main_name, synonyms in synonyms_data:
            # 先嘗試主名稱
            drugbank_id = map_ingredient_to_drugbank(main_name, name_index)

            # 若失敗，嘗試同義詞
            if drugbank_id is None:
                for syn in synonyms:
                    drugbank_id = map_ingredient_to_drugbank(syn, name_index)
                    if drugbank_id:
                        break

            results.append({
                "reg_no": row.get(license_field, ""),
                "product": row.get(brand_field, ""),
                "original_ingredient": str(ingredient_str)[:200],
                "normalized_ingredient": main_name,
                "synonyms": "; ".join(synonyms) if synonyms else "",
                "drugbank_id": drugbank_id,
                "mapped": drugbank_id is not None,
            })

    return pd.DataFrame(results)


def get_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算映射統計

    Args:
        mapping_df: 映射結果 DataFrame

    Returns:
        統計字典
    """
    # 偵測欄位名稱
    mapped_field = _detect_field(mapping_df.columns, ["mapped", "映射成功"], "mapped")
    ingredient_field = _detect_field(mapping_df.columns, ["normalized_ingredient", "標準化成分"], "normalized_ingredient")

    total = len(mapping_df)

    if mapped_field in mapping_df.columns:
        success = mapping_df[mapped_field].sum()
        success_df = mapping_df[mapping_df[mapped_field]]
    else:
        success = mapping_df["drugbank_id"].notna().sum()
        success_df = mapping_df[mapping_df["drugbank_id"].notna()]

    if ingredient_field in mapping_df.columns:
        unique_ingredients = mapping_df[ingredient_field].nunique()
    else:
        unique_ingredients = total

    unique_drugbank = success_df["drugbank_id"].nunique() if len(success_df) > 0 else 0

    return {
        "total_ingredients": total,
        "mapped_ingredients": int(success),
        "mapping_rate": success / total if total > 0 else 0,
        "unique_ingredients": unique_ingredients,
        "unique_drugbank_ids": unique_drugbank,
    }
