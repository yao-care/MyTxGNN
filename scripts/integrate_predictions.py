#!/usr/bin/env python3
"""
Integrate KG and DL prediction results for BrTxGNN.

This script combines predictions from:
1. Knowledge Graph (KG) method - fast, filters known indications
2. Deep Learning (DL) method - slow, higher precision, broader coverage

Output:
- Unified prediction results with confidence levels
- Predictions supported by both methods are marked as high confidence
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"

# Input files
KG_PREDICTIONS = DATA_DIR / "processed" / "repurposing_candidates.csv.gz"
DL_PREDICTIONS = DATA_DIR / "processed" / "txgnn_dl_predictions.csv.gz"
DRUG_MAPPING = DATA_DIR / "processed" / "drug_mapping.csv"

# Output files
OUTPUT_FILE = DATA_DIR / "processed" / "integrated_predictions.csv.gz"
STATS_FILE = DATA_DIR / "processed" / "integration_stats.json"

# Column mapping for this project
KG_COLS = {
    "license_id": "license_id",
    "brand_name": "brand_name",
    "ingredient": "ingredient",
    "drugbank_id": "drugbank_id",
    "indication": "disease_name",
    "source": "source",
}

DL_COLS = {
    "drugbank_id": "drugbank_id",
    "indication": "潛在新適應症",
    "score": "txgnn_score",
}

MAPPING_COLS = {
    "license_id": "reg_no",
    "brand_name": "product",
    "ingredient": "normalized_ingredient",
    "drugbank_id": "drugbank_id",
    "success": "mapping_success",
}


def load_kg_predictions() -> pd.DataFrame:
    """Load KG prediction results."""
    print("Loading KG predictions...")
    kg = pd.read_csv(KG_PREDICTIONS)
    # Normalize column names
    rename_map = {}
    if KG_COLS["indication"] != "potential_indication" and KG_COLS["indication"] in kg.columns:
        rename_map[KG_COLS["indication"]] = "potential_indication"
    if KG_COLS["ingredient"] != "drug_ingredient" and KG_COLS["ingredient"] in kg.columns:
        rename_map[KG_COLS["ingredient"]] = "drug_ingredient"
    if rename_map:
        kg = kg.rename(columns=rename_map)
        if "potential_indication" in rename_map.values():
            KG_COLS["indication"] = "potential_indication"
        if "drug_ingredient" in rename_map.values():
            KG_COLS["ingredient"] = "drug_ingredient"
    print(f"  KG predictions: {len(kg):,}")
    print(f"  KG drugs: {kg[KG_COLS['drugbank_id']].nunique():,}")
    print(f"  KG indications: {kg[KG_COLS['indication']].nunique():,}")
    return kg


def load_dl_predictions(score_threshold: float = 0.5) -> pd.DataFrame:
    """Load DL prediction results with optional filtering."""
    print(f"\nLoading DL predictions (score >= {score_threshold})...")

    # Read in chunks to handle large file
    chunks = []
    total_rows = 0

    for chunk in pd.read_csv(DL_PREDICTIONS, chunksize=1_000_000):
        # Filter by score threshold
        filtered = chunk[chunk[DL_COLS["score"]] >= score_threshold]
        chunks.append(filtered)
        total_rows += len(chunk)

    dl = pd.concat(chunks, ignore_index=True)
    print(f"  Total DL predictions: {total_rows:,}")
    print(f"  Filtered DL predictions (score >= {score_threshold}): {len(dl):,}")
    print(f"  DL drugs: {dl[DL_COLS['drugbank_id']].nunique():,}")
    print(f"  DL indications: {dl[DL_COLS['indication']].nunique():,}")

    return dl


def load_drug_mapping() -> pd.DataFrame:
    """Load drug mapping to local FDA products."""
    print("\nLoading drug mapping...")
    mapping = pd.read_csv(DRUG_MAPPING)
    # Keep only successful mappings
    if MAPPING_COLS["success"] in mapping.columns:
        mapping = mapping[mapping[MAPPING_COLS["success"]] == True]
    print(f"  Mapped drugs: {len(mapping):,}")
    print(f"  Unique DrugBank IDs: {mapping[MAPPING_COLS['drugbank_id']].nunique():,}")
    return mapping


def integrate_predictions(
    kg: pd.DataFrame,
    dl: pd.DataFrame,
    mapping: pd.DataFrame
) -> pd.DataFrame:
    """Integrate KG and DL predictions using vectorized operations."""
    print("\nIntegrating predictions...")

    # Create composite key for efficient joining
    kg["_key"] = kg[KG_COLS["drugbank_id"]] + "|" + kg[KG_COLS["indication"]]
    dl["_key"] = dl[DL_COLS["drugbank_id"]] + "|" + dl[DL_COLS["indication"]]

    # Get max DL score per (drug, indication) pair using groupby (vectorized)
    print("  Computing DL scores...")
    dl_scores = dl.groupby("_key")[DL_COLS["score"]].max().reset_index()
    dl_scores = dl_scores.rename(columns={DL_COLS["score"]: "dl_score"})
    print(f"  DL unique pairs: {len(dl_scores):,}")

    # Create sets for comparison
    kg_keys = set(kg["_key"])
    dl_keys = set(dl_scores["_key"])

    common = kg_keys & dl_keys
    kg_only = kg_keys - dl_keys
    dl_only = dl_keys - kg_keys

    print(f"\n  Common predictions (KG + DL): {len(common):,}")
    print(f"  KG only predictions: {len(kg_only):,}")
    print(f"  DL only predictions: {len(dl_only):,}")

    # Process KG predictions (merge with DL scores)
    print("\n  Processing KG predictions...")
    kg_unified = kg.merge(dl_scores, on="_key", how="left")
    kg_unified["kg_prediction"] = True
    kg_unified["dl_prediction"] = kg_unified["dl_score"].notna()

    # Process DL-only predictions (need to map to local products)
    print("  Processing DL-only predictions...")
    dl_only_keys = dl_scores[dl_scores["_key"].isin(dl_only)].copy()

    if len(dl_only_keys) > 0:
        # Extract drugbank_id and indication from key
        dl_only_keys[[DL_COLS["drugbank_id"], "potential_indication"]] = \
            dl_only_keys["_key"].str.split("|", expand=True)

        # Map to local products
        dl_mapped = dl_only_keys.merge(
            mapping[[MAPPING_COLS["license_id"], MAPPING_COLS["brand_name"],
                    MAPPING_COLS["ingredient"], MAPPING_COLS["drugbank_id"]]],
            left_on=DL_COLS["drugbank_id"],
            right_on=MAPPING_COLS["drugbank_id"],
            how="inner"
        )
        dl_mapped["kg_prediction"] = False
        dl_mapped["dl_prediction"] = True
        dl_mapped["source"] = "TxGNN Deep Learning Model"

        # Rename columns to match KG format
        dl_mapped = dl_mapped.rename(columns={
            MAPPING_COLS["license_id"]: "license_id",
            MAPPING_COLS["brand_name"]: "brand_name",
            MAPPING_COLS["ingredient"]: "drug_ingredient",
        })

        print(f"    DL-only mapped to local products: {len(dl_mapped):,}")

        # Combine
        unified = pd.concat([
            kg_unified[["license_id", "brand_name", "drug_ingredient", "drugbank_id",
                       "potential_indication", "kg_prediction", "dl_prediction", "dl_score", "source"]],
            dl_mapped[["license_id", "brand_name", "drug_ingredient", "drugbank_id",
                      "potential_indication", "kg_prediction", "dl_prediction", "dl_score", "source"]]
        ], ignore_index=True)
    else:
        unified = kg_unified[["license_id", "brand_name", "drug_ingredient", "drugbank_id",
                              "potential_indication", "kg_prediction", "dl_prediction", "dl_score", "source"]]

    # Add confidence level
    print("  Computing confidence levels...")

    # Fill NaN in dl_score for comparison
    dl_score_filled = unified["dl_score"].fillna(0)

    conditions = [
        (unified["kg_prediction"] & unified["dl_prediction"] & (dl_score_filled >= 0.9)),
        (unified["kg_prediction"] & unified["dl_prediction"]),
        (~unified["kg_prediction"] & unified["dl_prediction"] & (dl_score_filled >= 0.9)),
        (~unified["kg_prediction"] & unified["dl_prediction"] & (dl_score_filled >= 0.7)),
        (~unified["kg_prediction"] & unified["dl_prediction"]),
        (unified["kg_prediction"] & ~unified["dl_prediction"]),
    ]
    choices = ["very_high", "high", "high", "medium", "low", "medium"]
    unified["confidence"] = np.select(conditions, choices, default="low")

    # Update source column
    unified.loc[unified["kg_prediction"] & unified["dl_prediction"], "source"] = "KG + DL"
    unified.loc[unified["kg_prediction"] & ~unified["dl_prediction"], "source"] = "KG"
    unified.loc[~unified["kg_prediction"] & unified["dl_prediction"], "source"] = "DL"

    # Sort by confidence and dl_score
    confidence_order = {"very_high": 0, "high": 1, "medium": 2, "low": 3}
    unified["_conf_order"] = unified["confidence"].map(confidence_order)
    unified["_dl_score"] = unified["dl_score"].fillna(0)
    unified = unified.sort_values(
        ["_conf_order", "_dl_score"],
        ascending=[True, False]
    ).drop(columns=["_conf_order", "_dl_score"])

    return unified


def print_statistics(unified: pd.DataFrame):
    """Print integration statistics."""
    print("\n" + "=" * 60)
    print("Integration Statistics")
    print("=" * 60)

    print(f"\nTotal predictions: {len(unified):,}")
    print(f"Unique drugs: {unified['drugbank_id'].nunique():,}")
    print(f"Unique indications: {unified['potential_indication'].nunique():,}")
    print(f"Unique products: {unified['license_id'].nunique():,}")

    print("\nBy source:")
    for source, count in unified["source"].value_counts().items():
        print(f"  {source}: {count:,}")

    print("\nBy confidence level:")
    for conf, count in unified["confidence"].value_counts().sort_index().items():
        print(f"  {conf}: {count:,}")

    # High confidence predictions
    high_conf = unified[unified["confidence"].isin(["very_high", "high"])]
    print(f"\nHigh/Very High confidence predictions: {len(high_conf):,}")
    print(f"  Drugs: {high_conf['drugbank_id'].nunique():,}")
    print(f"  Indications: {high_conf['potential_indication'].nunique():,}")


def save_results(unified: pd.DataFrame):
    """Save integration results."""
    print(f"\nSaving results to {OUTPUT_FILE}...")
    unified.to_csv(OUTPUT_FILE, index=False)
    print(f"  Saved {len(unified):,} predictions")

    # Save statistics as JSON
    stats = {
        "total_predictions": len(unified),
        "unique_drugs": int(unified["drugbank_id"].nunique()),
        "unique_indications": int(unified["potential_indication"].nunique()),
        "unique_products": int(unified["license_id"].nunique()),
        "by_source": unified["source"].value_counts().to_dict(),
        "by_confidence": unified["confidence"].value_counts().to_dict(),
    }

    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print(f"  Saved statistics to {STATS_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Integrate KG and DL predictions")
    parser.add_argument(
        "--dl-threshold",
        type=float,
        default=0.5,
        help="DL score threshold (default: 0.5)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run without saving results"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("BrTxGNN Prediction Integration")
    print("=" * 60)

    # Load data
    kg = load_kg_predictions()
    dl = load_dl_predictions(score_threshold=args.dl_threshold)
    mapping = load_drug_mapping()

    # Integrate
    unified = integrate_predictions(kg, dl, mapping)

    # Statistics
    print_statistics(unified)

    # Save
    if not args.dry_run:
        save_results(unified)
    else:
        print("\n[Dry run - results not saved]")

    print("\nDone!")


if __name__ == "__main__":
    main()
