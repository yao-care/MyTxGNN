#!/usr/bin/env python3
"""Generate FHIR R4 resources for MyTxGNN

Generate FHIR-formatted resources from drug repurposing predictions.

Usage:
    uv run python scripts/generate_fhir_resources.py

Prerequisites:
    Run run_kg_prediction.py first

Output files:
    docs/fhir/metadata
    docs/fhir/MedicationKnowledge/*.json
    docs/fhir/ClinicalUseDefinition/*.json
"""

import json
from pathlib import Path
from datetime import datetime

import pandas as pd


# Malaysia configuration
BASE_URL = "https://mytxgnn.yao.care"

JURISDICTION = {
    "coding": [{
        "system": "urn:iso:std:iso:3166",
        "code": "MY",
        "display": "Malaysia"
    }]
}


def generate_capability_statement() -> dict:
    """Generate CapabilityStatement (metadata)"""
    return {
        "resourceType": "CapabilityStatement",
        "id": "mytxgnn-fhir-server",
        "url": f"{BASE_URL}/fhir/metadata",
        "version": "1.0.0",
        "name": "MyTxGNNFHIRServer",
        "status": "active",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "MyTxGNN Project",
        "description": "Malaysia drug repurposing predictions using TxGNN",
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [{
            "mode": "server",
            "resource": [
                {
                    "type": "MedicationKnowledge",
                    "interaction": [{"code": "read"}, {"code": "search-type"}]
                },
                {
                    "type": "ClinicalUseDefinition",
                    "interaction": [{"code": "read"}, {"code": "search-type"}]
                }
            ]
        }]
    }


def generate_medication_knowledge(drug_id: str, drug_name: str, evidence_level: str) -> dict:
    """Generate MedicationKnowledge resource"""
    slug = drug_id.lower().replace(" ", "-")
    return {
        "resourceType": "MedicationKnowledge",
        "id": slug,
        "status": "active",
        "code": {
            "coding": [{
                "system": "https://www.drugbank.ca",
                "code": drug_id,
                "display": drug_name
            }]
        },
        "intendedJurisdiction": [JURISDICTION],
        "extension": [{
            "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
            "valueCode": evidence_level
        }]
    }


def generate_clinical_use_definition(
    drug_id: str,
    drug_name: str,
    indication: str,
    disease_id: str,
    evidence_level: str
) -> dict:
    """Generate ClinicalUseDefinition resource"""
    drug_slug = drug_id.lower()
    # Sanitize: replace spaces and slashes
    indication_slug = indication.lower().replace(" ", "-").replace("/", "-").replace("\\", "-")[:50]
    resource_id = f"{drug_slug}-{indication_slug}"

    return {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "type": "indication",
        "subject": [{"reference": f"MedicationKnowledge/{drug_slug}"}],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {
                    "coding": [{
                        "system": f"{BASE_URL}/diseases",
                        "code": disease_id if disease_id else indication_slug,
                        "display": indication
                    }],
                    "text": indication
                }
            }
        },
        "extension": [
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
                "valueCode": evidence_level
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/source",
                "valueString": "TxGNN Knowledge Graph"
            }
        ]
    }


def main():
    print("=" * 60)
    print("Generating FHIR R4 Resources for MyTxGNN")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    fhir_dir = base_dir / "docs" / "fhir"

    # Create directories
    (fhir_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "Bundle").mkdir(parents=True, exist_ok=True)

    # 1. Generate CapabilityStatement
    print("1. Generating CapabilityStatement...")
    metadata = generate_capability_statement()
    with open(fhir_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    # 2. Load prediction results
    print("2. Loading prediction results...")
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv.gz"

    if not candidates_path.exists():
        print(f"   Error: Prediction results not found: {candidates_path}")
        print("   Please run run_kg_prediction.py first")
        return

    candidates = pd.read_csv(candidates_path)
    print(f"   Loaded {len(candidates)} predictions")

    # 3. Generate MedicationKnowledge resources
    print("3. Generating MedicationKnowledge resources...")
    drugs = candidates[["drugbank_id", "ingredient"]].drop_duplicates()
    drugs = drugs[drugs["drugbank_id"].notna()]

    drug_count = 0
    for _, row in drugs.iterrows():
        drug_id = row["drugbank_id"]
        drug_name = row["ingredient"]
        evidence_level = "L5"  # Level 5: Computational prediction
        resource = generate_medication_knowledge(drug_id, drug_name, evidence_level)
        slug = drug_id.lower()
        with open(fhir_dir / "MedicationKnowledge" / f"{slug}.json", "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        drug_count += 1

    print(f"   Generated {drug_count} MedicationKnowledge resources")

    # 4. Generate ClinicalUseDefinition resources
    print("4. Generating ClinicalUseDefinition resources...")
    count = 0
    for _, row in candidates.iterrows():
        drug_id = row.get("drugbank_id", "")
        drug_name = row.get("ingredient", "")
        indication = row.get("disease_name", "")
        disease_id = row.get("disease_id", "")
        evidence_level = "L5"

        if pd.notna(drug_id) and pd.notna(indication) and drug_id and indication:
            resource = generate_clinical_use_definition(
                drug_id, drug_name, indication,
                disease_id if pd.notna(disease_id) else "",
                evidence_level
            )
            drug_slug = drug_id.lower()
            # Sanitize filename: replace spaces, slashes, and other problematic characters
            indication_slug = indication.lower().replace(" ", "-").replace("/", "-").replace("\\", "-")[:50]
            filename = f"{drug_slug}-{indication_slug}.json"
            with open(fhir_dir / "ClinicalUseDefinition" / filename, "w", encoding="utf-8") as f:
                json.dump(resource, f, indent=2, ensure_ascii=False)
            count += 1

    print(f"   Generated {count} ClinicalUseDefinition resources")

    print()
    print("Done!")
    print(f"FHIR resources saved to: {fhir_dir}")


if __name__ == "__main__":
    main()
