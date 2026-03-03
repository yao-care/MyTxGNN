"""主成分名稱標準化"""

import re
from typing import List, Tuple


def normalize_ingredient(name: str) -> str:
    """標準化單一成分名稱

    處理邏輯：
    1. 移除括號內的同義詞（EQ TO ...）
    2. 移除其他括號內容（如 VIT B2）
    3. 統一大小寫
    4. 移除多餘空白

    Args:
        name: 原始成分名稱

    Returns:
        標準化後的名稱
    """
    if not name:
        return ""

    # 統一全形括號為半形
    name = name.replace("（", "(").replace("）", ")")

    # 移除括號內容（包含 EQ TO 的同義詞、VIT 等）
    # 但保留括號前的主名稱
    name = re.sub(r"\s*\([^)]*\)", "", name)

    # 移除鹽類後綴的多餘資訊（保留鹽類如 HCL, SODIUM 等）
    name = name.strip()

    # 統一大寫
    name = name.upper()

    # 移除多餘空白
    name = re.sub(r"\s+", " ", name)

    return name.strip()


def extract_ingredients(ingredient_str: str) -> List[str]:
    """從主成分略述欄位提取所有成分

    FDA 資料中多成分以 ; 或 ;; 分隔

    Args:
        ingredient_str: 主成分略述欄位原始值

    Returns:
        標準化後的成分列表
    """
    if not ingredient_str:
        return []

    # 統一分隔符號
    # 有些用 ;; 有些用 ;
    ingredient_str = ingredient_str.replace(";;", ";").replace("；", ";")

    # 分割
    parts = ingredient_str.split(";")

    # 標準化每個成分
    ingredients = []
    for part in parts:
        normalized = normalize_ingredient(part)
        if normalized and normalized not in ingredients:
            ingredients.append(normalized)

    return ingredients


def extract_primary_ingredient(ingredient_str: str) -> str:
    """提取主要成分（第一個成分）

    Args:
        ingredient_str: 主成分略述欄位原始值

    Returns:
        主要成分名稱（標準化後）
    """
    ingredients = extract_ingredients(ingredient_str)
    return ingredients[0] if ingredients else ""


def get_all_synonyms(ingredient_str: str) -> List[Tuple[str, List[str]]]:
    """提取成分及其所有同義詞

    從括號中的 EQ TO 提取同義詞

    Args:
        ingredient_str: 主成分略述欄位原始值

    Returns:
        [(主名稱, [同義詞列表]), ...]
    """
    if not ingredient_str:
        return []

    # 統一分隔符號
    ingredient_str = ingredient_str.replace(";;", ";").replace("；", ";")
    parts = ingredient_str.split(";")

    results = []
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # 統一括號
        part = part.replace("（", "(").replace("）", ")")

        # 提取主名稱（括號前的部分）
        main_match = re.match(r"^([^(]+)", part)
        if not main_match:
            continue

        main_name = main_match.group(1).strip().upper()
        main_name = re.sub(r"\s+", " ", main_name)

        # 提取所有 EQ TO 同義詞
        synonyms = []
        eq_matches = re.findall(r"EQ TO\s+([^)]+)", part, re.IGNORECASE)
        for match in eq_matches:
            syn = match.strip().upper()
            syn = re.sub(r"\s+", " ", syn)
            # 清理可能的尾部括號內容
            syn = re.sub(r"\s*\(.*$", "", syn)
            if syn and syn != main_name:
                synonyms.append(syn)

        results.append((main_name, synonyms))

    return results
