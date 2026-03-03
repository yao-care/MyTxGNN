#!/usr/bin/env python3
"""執行知識圖譜方法預測 - Malaysia 版本

使用 TxGNN 知識圖譜進行老藥新用預測。

使用方法:
    uv run python scripts/run_kg_prediction.py

前置條件:
    1. 已執行 process_fda_data.py
    2. 已執行 prepare_external_data.py

產生檔案:
    data/processed/repurposing_candidates.csv

注意:
    馬來西亞資料沒有適應症欄位，預測將基於成分到 DrugBank 的映射，
    並從知識圖譜中找出潛在的新適應症。
"""

from pathlib import Path

import pandas as pd
import yaml
from tqdm import tqdm

from txgnn.data.loader import load_fda_drugs, filter_active_drugs, parse_ingredients
from txgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank, get_mapping_stats
from txgnn.predict.repurposing import find_repurposing_candidates


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    print("=" * 60)
    print("執行知識圖譜方法預測 (Malaysia)")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    config = load_field_config()
    field_mapping = config["field_mapping"]

    # 1. 載入藥品資料
    print("1. 載入藥品資料...")
    fda_df = load_fda_drugs()
    active_df = filter_active_drugs(fda_df)
    print(f"   總藥品數: {len(fda_df):,}")
    print(f"   處方藥/西藥: {len(active_df):,}")

    # 2. DrugBank 映射
    print()
    print("2. 執行 DrugBank 映射...")
    # 使用正規化後的成分欄位
    drug_mapping = map_fda_drugs_to_drugbank(
        active_df,
        ingredient_field="ingredients_normalized",
        license_field=field_mapping["license_id"],
        brand_field=field_mapping["brand_name_local"],
    )

    stats = get_mapping_stats(drug_mapping)
    print(f"   成分總數: {stats['total_ingredients']:,}")
    print(f"   映射成功: {stats['mapped_ingredients']:,}")
    print(f"   映射率: {stats['mapping_rate']*100:.1f}%")
    print(f"   唯一 DrugBank ID: {stats['unique_drugbank_ids']:,}")

    # 3. 找出有 DrugBank 映射的藥品
    print()
    print("3. 篩選有效映射...")
    valid_mappings = drug_mapping[drug_mapping["drugbank_id"].notna()].copy()
    print(f"   有效映射數: {len(valid_mappings):,}")

    # 4. 尋找老藥新用候選
    print()
    print("4. 尋找老藥新用候選...")
    print("   (從知識圖譜中找出每個藥物的潛在新適應症)")

    candidates = find_repurposing_candidates(
        drug_mapping=valid_mappings,
        indication_mapping=None,  # 馬來西亞沒有適應症資料
        base_dir=base_dir,
    )

    print(f"   候選數: {len(candidates):,}")

    # 5. 統計分析
    print()
    print("5. 統計分析...")
    if len(candidates) > 0:
        unique_drugs = candidates["drugbank_id"].nunique()
        unique_diseases = candidates["disease_id"].nunique()
        print(f"   涉及藥物數: {unique_drugs:,}")
        print(f"   涉及疾病數: {unique_diseases:,}")

        # 按疾病分類統計
        if "disease_name" in candidates.columns:
            top_diseases = candidates["disease_name"].value_counts().head(10)
            print()
            print("   潛在適應症 Top 10:")
            for disease, count in top_diseases.items():
                print(f"     - {disease}: {count:,} 個藥物")

    # 6. 儲存結果
    print()
    print("6. 儲存結果...")
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "repurposing_candidates.csv"
    candidates.to_csv(output_path, index=False)
    print(f"   已儲存至: {output_path}")

    # 同時儲存 DrugBank 映射結果
    mapping_path = output_dir / "drugbank_mapping.csv"
    drug_mapping.to_csv(mapping_path, index=False)
    print(f"   DrugBank 映射: {mapping_path}")

    print()
    print("=" * 60)
    print("完成！")
    print("=" * 60)
    print()
    print("下一步: 生成 FHIR 資源")
    print("  uv run python scripts/generate_fhir_resources.py")


if __name__ == "__main__":
    main()
