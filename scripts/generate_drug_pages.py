#!/usr/bin/env python3
"""
Generate individual drug pages for MyTxGNN Jekyll site.

This script reads the prediction data and generates markdown files
for each drug in the _drugs collection.
"""

import json
import os
from pathlib import Path

import pandas as pd


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    return (
        text.lower()
        .replace(" ", "-")
        .replace("_", "-")
        .replace("/", "-")
        .replace("\\", "-")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .replace("'", "")
    )


def generate_drug_page(drug_data: dict, output_dir: Path) -> None:
    """Generate a single drug page."""
    drug_name = drug_data["drug_name"]
    drugbank_id = drug_data["drugbank_id"]
    slug = slugify(drug_name)

    # Create markdown content
    content = f"""---
layout: drug
title: "{drug_name}"
drugbank_id: "{drugbank_id}"
drug_name: "{drug_name}"
kg_predictions: {drug_data.get("kg_predictions", 0)}
dl_predictions: {drug_data.get("dl_predictions", 0)}
evidence_level: "{drug_data.get("evidence_level", "L5")}"
indication_count: {drug_data.get("kg_predictions", 0)}
brands: {json.dumps(drug_data.get("brands", []))}
permalink: /drugs/{slug}/
---

# {drug_name}

## Quick Overview

| Attribute | Value |
|-----------|-------|
| **Drug Name** | {drug_name} |
| **DrugBank ID** | [{drugbank_id}](https://go.drugbank.com/drugs/{drugbank_id}) |
| **KG Predictions** | {drug_data.get("kg_predictions", 0)} |
| **DL Predictions (≥0.7)** | {drug_data.get("dl_predictions", 0)} |
| **Evidence Level** | {drug_data.get("evidence_level", "L5")} |
| **NPRA Status** | Approved |

---

## Sample Brand Names in Malaysia

{chr(10).join(f"- {brand}" for brand in drug_data.get("brands", ["N/A"])[:5])}

---

## Predicted Indications

This drug has **{drug_data.get("kg_predictions", 0)}** knowledge graph predictions and **{drug_data.get("dl_predictions", 0)}** high-confidence deep learning predictions.

### Top KG Predictions

| Indication | Source |
|------------|--------|
{generate_indication_table(drug_data.get("top_indications", []))}

---

## FHIR Resources

Access drug data via FHIR R4 API:

- **MedicationKnowledge**: [`/fhir/MedicationKnowledge/{drugbank_id}`](/fhir/MedicationKnowledge/{drugbank_id}.json)

---

## Related Resources

| Resource | Link |
|----------|------|
| DrugBank | [View on DrugBank](https://go.drugbank.com/drugs/{drugbank_id}) |
| PubMed | [Search PubMed](https://pubmed.ncbi.nlm.nih.gov/?term={drug_name.replace(" ", "+")}) |
| ClinicalTrials.gov | [Search Trials](https://clinicaltrials.gov/search?intr={drug_name.replace(" ", "+")}) |

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Drug repurposing predictions are for research purposes only. These predictions have not been clinically validated and should not be used for medical decisions. Always consult healthcare professionals.
</div>
"""

    # Write file
    output_file = output_dir / f"{slug}.md"
    output_file.write_text(content, encoding="utf-8")
    print(f"Generated: {output_file}")


def generate_indication_table(indications: list) -> str:
    """Generate markdown table rows for indications."""
    if not indications:
        return "| *Evidence collection in progress* | - |"

    rows = []
    for ind in indications[:10]:
        disease = ind.get("disease_name", "Unknown")
        source = ind.get("source", "KG")
        rows.append(f"| {disease} | {source} |")

    return "\n".join(rows) if rows else "| *Evidence collection in progress* | - |"


def main():
    """Main function to generate all drug pages."""
    # Paths
    project_root = Path(__file__).parent.parent
    data_dir = project_root / "data" / "processed"
    output_dir = project_root / "docs" / "_drugs"
    stats_file = project_root / "docs" / "_data" / "drug_stats.json"

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load prediction data
    kg_file = data_dir / "repurposing_candidates.csv.gz"
    dl_file = data_dir / "txgnn_checkpoint.csv"

    if not kg_file.exists():
        print(f"Error: {kg_file} not found")
        return

    # Read KG predictions
    print(f"Reading {kg_file}...")
    kg_df = pd.read_csv(kg_file)

    # Aggregate by drug
    drug_kg_stats = (
        kg_df.groupby(["drugbank_id", "ingredient"])
        .agg(
            kg_predictions=("disease_name", "count"),
            top_diseases=("disease_name", lambda x: list(x.head(10))),
        )
        .reset_index()
    )

    # Read DL predictions if available
    dl_stats = {}
    if dl_file.exists():
        print(f"Reading {dl_file}...")
        dl_df = pd.read_csv(dl_file)
        # Filter high confidence predictions
        dl_high = dl_df[dl_df["txgnn_score"] >= 0.7]
        dl_stats = dl_high.groupby("drugbank_id").size().to_dict()

    # Get brand names from NPRA data
    npra_file = data_dir / "npra_drugs.json"
    brands_by_drug = {}
    if npra_file.exists():
        with open(npra_file, encoding="utf-8") as f:
            npra_data = json.load(f)
        for item in npra_data:
            ingredient = item.get("ingredients_normalized", "").upper()
            brand = item.get("product", "")
            if ingredient and brand:
                if ingredient not in brands_by_drug:
                    brands_by_drug[ingredient] = []
                if brand not in brands_by_drug[ingredient]:
                    brands_by_drug[ingredient].append(brand)

    # Load existing stats if available
    if stats_file.exists():
        with open(stats_file, encoding="utf-8") as f:
            stats_data = json.load(f)
    else:
        stats_data = []

    # Generate pages
    print(f"Generating {len(drug_kg_stats)} drug pages...")

    for _, row in drug_kg_stats.iterrows():
        drugbank_id = row["drugbank_id"]
        drug_name = row["ingredient"]

        # Get DL predictions count
        dl_count = dl_stats.get(drugbank_id, 0)

        # Get brand names
        brands = brands_by_drug.get(drug_name.upper(), [])[:5]

        # Prepare top indications
        top_indications = [
            {"disease_name": d, "source": "KG"} for d in row["top_diseases"]
        ]

        drug_data = {
            "drug_name": drug_name.title(),
            "drugbank_id": drugbank_id,
            "kg_predictions": int(row["kg_predictions"]),
            "dl_predictions": int(dl_count),
            "evidence_level": "L5",  # Default, can be updated later
            "brands": brands,
            "top_indications": top_indications,
        }

        generate_drug_page(drug_data, output_dir)

    print(f"\nDone! Generated {len(drug_kg_stats)} drug pages in {output_dir}")


if __name__ == "__main__":
    main()
