#!/usr/bin/env python3
"""Generate news monitoring keywords from synonyms and predictions.

Creates keyword patterns for monitoring health news in Malaysia.

Usage:
    uv run python scripts/generate_news_keywords.py

Output:
    data/news/keywords.json
"""

import json
from pathlib import Path
from datetime import datetime

import pandas as pd


def load_synonyms(path: Path) -> dict:
    """Load disease and drug synonyms."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_top_predictions(path: Path, top_n: int = 100) -> pd.DataFrame:
    """Load top drug repurposing predictions."""
    df = pd.read_csv(path)
    # Get unique drug-disease pairs
    df = df.drop_duplicates(subset=["drugbank_id", "disease_name"])
    return df.head(top_n)


def generate_keywords(synonyms: dict, predictions: pd.DataFrame) -> dict:
    """Generate keyword patterns for news monitoring.

    Returns:
        Dictionary with keyword patterns
    """
    keywords = {
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "description": "News monitoring keywords for MyTxGNN",
        "disease_keywords": {},
        "drug_keywords": {},
        "drug_disease_pairs": [],
    }

    # Disease keywords from synonyms
    indication_synonyms = synonyms.get("indication_synonyms", {})
    for disease, terms in indication_synonyms.items():
        if disease.startswith("_"):
            continue
        all_terms = [disease] + terms
        keywords["disease_keywords"][disease] = {
            "primary": disease,
            "synonyms": terms,
            "patterns": [
                # Basic patterns
                f'"{disease}"',
                # With treatment context
                f'"{disease}" AND (treatment OR therapy OR drug OR medicine)',
                f'"{disease}" AND (breakthrough OR discovery OR trial)',
            ],
        }

    # Drug keywords from synonyms
    drug_synonyms = synonyms.get("drug_synonyms", {})
    for drug, terms in drug_synonyms.items():
        if drug.startswith("_"):
            continue
        keywords["drug_keywords"][drug] = {
            "primary": drug,
            "synonyms": terms,
            "patterns": [
                f'"{drug}"',
                f'"{drug}" AND (repurposing OR "new use" OR indication)',
            ],
        }

    # Drug-disease pairs from predictions
    for _, row in predictions.iterrows():
        drug_id = row.get("drugbank_id", "")
        ingredient = row.get("ingredient", "")
        disease = row.get("disease_name", "")

        if pd.notna(ingredient) and pd.notna(disease):
            # Get synonyms for this pair
            disease_terms = indication_synonyms.get(disease, [disease])
            drug_terms = drug_synonyms.get(ingredient.lower(), [ingredient])

            keywords["drug_disease_pairs"].append({
                "drugbank_id": drug_id,
                "drug": ingredient,
                "drug_synonyms": drug_terms[:3],  # Limit synonyms
                "disease": disease,
                "disease_synonyms": disease_terms[:3],
                "patterns": [
                    f'"{ingredient}" AND "{disease}"',
                    f'"{ingredient}" AND ({" OR ".join(disease_terms[:2])})',
                ],
            })

    return keywords


def main():
    print("=" * 60)
    print("Generating News Monitoring Keywords")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    synonyms_path = base_dir / "data" / "news" / "synonyms.json"
    predictions_path = base_dir / "data" / "processed" / "repurposing_candidates.csv.gz"
    output_path = base_dir / "data" / "news" / "keywords.json"

    # Load data
    print("1. Loading synonyms...")
    synonyms = load_synonyms(synonyms_path)
    print(f"   Loaded {len(synonyms.get('indication_synonyms', {}))} disease synonyms")
    print(f"   Loaded {len(synonyms.get('drug_synonyms', {}))} drug synonyms")

    print("2. Loading predictions...")
    if predictions_path.exists():
        predictions = load_top_predictions(predictions_path, top_n=100)
        print(f"   Loaded {len(predictions)} top predictions")
    else:
        predictions = pd.DataFrame()
        print("   No predictions found (skipping)")

    # Generate keywords
    print("3. Generating keywords...")
    keywords = generate_keywords(synonyms, predictions)

    # Save
    print("4. Saving keywords...")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(keywords, f, indent=2, ensure_ascii=False)

    print()
    print("Summary:")
    print(f"  Disease keywords: {len(keywords['disease_keywords'])}")
    print(f"  Drug keywords: {len(keywords['drug_keywords'])}")
    print(f"  Drug-disease pairs: {len(keywords['drug_disease_pairs'])}")
    print()
    print(f"Keywords saved to: {output_path}")


if __name__ == "__main__":
    main()
