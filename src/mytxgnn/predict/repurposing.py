"""老藥新用預測 - 基於 TxGNN 知識圖譜 (Malaysia 版本)"""

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd


def load_drug_disease_relations(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 藥物-疾病關係

    Args:
        filepath: CSV 檔案路徑

    Returns:
        藥物-疾病關係 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drug_disease_relations.csv"

    return pd.read_csv(filepath)


def build_drug_indication_map(relations_df: pd.DataFrame) -> Dict[str, Set[str]]:
    """建立藥物 -> 適應症集合的映射

    Args:
        relations_df: 藥物-疾病關係 DataFrame

    Returns:
        {drug_name: {disease1, disease2, ...}}
    """
    # 只取 indication 和 off-label use
    indications = relations_df[relations_df["relation"].isin(["indication", "off-label use"])]

    drug_map = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"]

        if drug not in drug_map:
            drug_map[drug] = set()
        drug_map[drug].add(disease)

    return drug_map


def find_repurposing_candidates(
    drug_mapping: pd.DataFrame,
    indication_mapping: Optional[pd.DataFrame] = None,
    relations_df: Optional[pd.DataFrame] = None,
    base_dir: Optional[Path] = None,
) -> pd.DataFrame:
    """找出老藥新用候選

    對於馬來西亞資料（沒有適應症欄位），直接從知識圖譜中
    找出每個藥物的所有潛在適應症。

    Args:
        drug_mapping: 藥品 DrugBank 映射結果
        indication_mapping: 適應症疾病映射結果（馬來西亞資料為 None）
        relations_df: TxGNN 藥物-疾病關係
        base_dir: 專案根目錄

    Returns:
        老藥新用候選 DataFrame
    """
    if relations_df is None:
        if base_dir:
            filepath = base_dir / "data" / "external" / "drug_disease_relations.csv"
        else:
            filepath = None
        relations_df = load_drug_disease_relations(filepath)

    # 建立 TxGNN 藥物適應症映射
    kg_drug_map = build_drug_indication_map(relations_df)

    # 取得有效的 DrugBank 映射
    valid_drugs = drug_mapping[drug_mapping["drugbank_id"].notna()].copy()

    # 偵測欄位名稱（支援不同語言版本）
    license_field = _detect_field(valid_drugs.columns, ["reg_no", "許可證字號", "license_id"])
    brand_field = _detect_field(valid_drugs.columns, ["product", "中文品名", "brand_name"])
    ingredient_field = _detect_field(valid_drugs.columns, ["normalized_ingredient", "標準化成分", "ingredient"])

    if indication_mapping is not None and len(indication_mapping) > 0:
        # 有適應症資料的情況（如台灣）
        return _find_candidates_with_indications(
            valid_drugs, indication_mapping, kg_drug_map,
            license_field, brand_field, ingredient_field
        )
    else:
        # 無適應症資料的情況（如馬來西亞）
        return _find_candidates_without_indications(
            valid_drugs, kg_drug_map,
            license_field, brand_field, ingredient_field
        )


def _detect_field(columns: pd.Index, candidates: List[str]) -> str:
    """偵測欄位名稱"""
    for c in candidates:
        if c in columns:
            return c
    return candidates[0]  # 預設使用第一個


def _find_candidates_without_indications(
    valid_drugs: pd.DataFrame,
    kg_drug_map: Dict[str, Set[str]],
    license_field: str,
    brand_field: str,
    ingredient_field: str,
) -> pd.DataFrame:
    """無適應症資料時的候選搜尋（馬來西亞版本）

    直接從知識圖譜中找出每個藥物的所有適應症作為候選。
    """
    # 取得唯一的藥品-成分組合
    unique_pairs = valid_drugs[[license_field, ingredient_field, brand_field, "drugbank_id"]].drop_duplicates()

    candidates = []

    for _, row in unique_pairs.iterrows():
        license_no = row[license_field]
        drug_name = row[ingredient_field]
        brand_name = row[brand_field]
        drugbank_id = row["drugbank_id"]

        # 查詢 TxGNN 中該藥物的所有適應症
        kg_diseases = kg_drug_map.get(drug_name.upper() if pd.notna(drug_name) else "", set())

        for disease in kg_diseases:
            candidates.append({
                "license_id": license_no,
                "brand_name": brand_name,
                "ingredient": drug_name,
                "drugbank_id": drugbank_id,
                "disease_name": disease,
                "disease_id": None,  # 需要額外映射
                "source": "TxGNN Knowledge Graph",
                "is_new": None,  # 無法判斷是否為新適應症
            })

    result_df = pd.DataFrame(candidates)

    # 去重
    if len(result_df) > 0:
        # First: remove exact duplicates per license
        result_df = result_df.drop_duplicates(
            subset=["license_id", "ingredient", "disease_name"]
        )

        # Second: for DL prediction efficiency, keep only unique (drugbank_id, disease) pairs
        # This prevents redundant DL predictions for the same drug-disease combination
        # We keep the first occurrence (arbitrary license_id as representative)
        result_df = result_df.drop_duplicates(
            subset=["drugbank_id", "disease_name"],
            keep="first"
        )

    return result_df


def _find_candidates_with_indications(
    valid_drugs: pd.DataFrame,
    indication_mapping: pd.DataFrame,
    kg_drug_map: Dict[str, Set[str]],
    license_field: str,
    brand_field: str,
    ingredient_field: str,
) -> pd.DataFrame:
    """有適應症資料時的候選搜尋

    比較現有適應症與知識圖譜，找出潛在新適應症。
    """
    # 偵測 indication_mapping 的欄位
    ind_license_field = _detect_field(indication_mapping.columns, ["license_id", "許可證字號"])
    ind_disease_field = _detect_field(indication_mapping.columns, ["disease_name", "疾病名稱"])

    # 建立藥品的現有適應症
    tw_diseases_df = indication_mapping[
        indication_mapping[ind_disease_field].notna()
    ][[ind_license_field, ind_disease_field]].copy()

    tw_diseases_df["disease_lower"] = tw_diseases_df[ind_disease_field].str.lower()
    tw_drug_diseases = tw_diseases_df.groupby(ind_license_field)["disease_lower"].apply(set).to_dict()

    # 取得唯一的藥品-成分組合
    unique_pairs = valid_drugs[[license_field, ingredient_field, brand_field, "drugbank_id"]].drop_duplicates()

    candidates = []

    for _, row in unique_pairs.iterrows():
        license_no = row[license_field]
        drug_name = row[ingredient_field]
        brand_name = row[brand_field]
        drugbank_id = row["drugbank_id"]

        # 查詢 TxGNN 中該藥物的所有適應症
        kg_diseases = kg_drug_map.get(drug_name.upper() if pd.notna(drug_name) else "", set())
        if not kg_diseases:
            continue

        # 取得現有適應症
        existing_diseases = tw_drug_diseases.get(license_no, set())

        # 找出潛在新適應症
        for disease in kg_diseases:
            disease_lower = disease.lower()

            # 檢查是否已存在
            is_new = all(
                existing_d not in disease_lower and disease_lower not in existing_d
                for existing_d in existing_diseases
            )

            if is_new:
                candidates.append({
                    "license_id": license_no,
                    "brand_name": brand_name,
                    "ingredient": drug_name,
                    "drugbank_id": drugbank_id,
                    "disease_name": disease,
                    "disease_id": None,
                    "source": "TxGNN Knowledge Graph",
                    "is_new": True,
                })

    result_df = pd.DataFrame(candidates)

    # 去重
    if len(result_df) > 0:
        # First: remove exact duplicates per license
        result_df = result_df.drop_duplicates(
            subset=["license_id", "ingredient", "disease_name"]
        )

        # Second: for DL prediction efficiency, keep only unique (drugbank_id, disease) pairs
        # This prevents redundant DL predictions for the same drug-disease combination
        # We keep the first occurrence (arbitrary license_id as representative)
        result_df = result_df.drop_duplicates(
            subset=["drugbank_id", "disease_name"],
            keep="first"
        )

    return result_df


def generate_repurposing_report(candidates_df: pd.DataFrame) -> dict:
    """生成老藥新用報告統計

    Args:
        candidates_df: 候選藥物 DataFrame

    Returns:
        統計報告字典
    """
    if len(candidates_df) == 0:
        return {
            "total_candidates": 0,
            "unique_drugs": 0,
            "unique_diseases": 0,
            "top_diseases": [],
            "top_drugs": [],
        }

    # 偵測欄位名稱
    ingredient_field = _detect_field(candidates_df.columns, ["ingredient", "藥物成分"])
    disease_field = _detect_field(candidates_df.columns, ["disease_name", "潛在新適應症"])

    unique_drugs = candidates_df[ingredient_field].nunique()
    unique_diseases = candidates_df[disease_field].nunique()

    # 最常見的潛在新適應症
    top_diseases = candidates_df[disease_field].value_counts().head(10).to_dict()

    # 最多潛在新適應症的藥物
    drug_counts = candidates_df.groupby(ingredient_field)[disease_field].nunique()
    top_drugs = drug_counts.sort_values(ascending=False).head(10).to_dict()

    return {
        "total_candidates": len(candidates_df),
        "unique_drugs": unique_drugs,
        "unique_diseases": unique_diseases,
        "top_diseases": top_diseases,
        "top_drugs": top_drugs,
    }
