#!/usr/bin/env python3
"""Batch collect drug bundles (without LLM calls).

This script collects drug bundles for multiple drugs.
It does NOT require an API key since it only collects data, no LLM generation.
Claude will analyze the bundles later during conversation.

Usage:
    # Collect top 10 drugs by prediction count
    uv run python scripts/batch_collect_bundles.py --limit 10

    # Collect specific drugs
    uv run python scripts/batch_collect_bundles.py --drugs "Prednisolone,Metformin"

    # Collect all drugs
    uv run python scripts/batch_collect_bundles.py --all --limit 100

    # Skip existing bundles
    uv run python scripts/batch_collect_bundles.py --limit 50 --skip-existing
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mytxgnn.collectors import DrugBundleAggregator
from mytxgnn.paths import get_bundles_dir, slugify


def load_drug_list(drugs_dir: Path) -> list[dict]:
    """Load drug list from _drugs collection."""
    drugs = []

    for drug_file in sorted(drugs_dir.glob("*.md")):
        content = drug_file.read_text(encoding="utf-8")

        if not content.startswith("---"):
            continue

        parts = content.split("---", 2)
        if len(parts) < 3:
            continue

        front_matter = parts[1]
        body = parts[2]

        # Parse front matter
        drug = {"file": drug_file}
        for line in front_matter.split("\n"):
            if line.startswith("title:"):
                drug["name"] = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("drugbank_id:"):
                drug["drugbank_id"] = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("kg_predictions:"):
                drug["kg_predictions"] = int(line.split(":", 1)[1].strip())
            elif line.startswith("evidence_level:"):
                drug["evidence_level"] = line.split(":", 1)[1].strip().strip('"')

        # Extract top indications from body
        drug["indications"] = extract_top_indications(body)

        if "name" in drug:
            drugs.append(drug)

    return drugs


def extract_top_indications(content: str, max_indications: int = 5) -> list[str]:
    """Extract top predicted indications from drug page content."""
    indications = []

    # Look for "Top KG Predictions" table
    table_match = re.search(
        r'### Top KG Predictions.*?\n\|.*?\n\|[-|\s]+\n(.*?)(?=\n---|\n##|\Z)',
        content,
        re.DOTALL
    )

    if table_match:
        rows = table_match.group(1).strip().split("\n")
        for row in rows[:max_indications]:
            # Extract indication from table row: | indication | source |
            parts = row.split("|")
            if len(parts) >= 2:
                indication = parts[1].strip()
                # Clean up indication name
                indication = re.sub(r'\s*\(disease\)\s*', '', indication)
                indication = re.sub(r'\s*\(disorder\)\s*', '', indication)
                if indication:
                    indications.append(indication)

    return indications


def collect_single_drug(
    drug: dict,
    aggregator: DrugBundleAggregator,
    delay: float = 1.0,
) -> dict:
    """Collect bundle for a single drug.

    Returns:
        dict with status, bundle_path, indication_count, error
    """
    result = {
        "drug": drug["name"],
        "drugbank_id": drug.get("drugbank_id"),
        "status": "pending",
        "bundle_path": None,
        "indication_count": 0,
        "error": None,
        "duration_seconds": 0,
    }

    start_time = time.time()

    try:
        # Collect bundle
        bundle = aggregator.collect(
            drug_name=drug["name"],
            drugbank_id=drug.get("drugbank_id"),
            indications=drug.get("indications", []),
        )

        # Save bundle
        bundle_path = bundle.save()

        # Get stats
        indication_count = len(bundle.drug.predicted_indications)
        total_trials = sum(
            len(pi.clinical_trials) + len(pi.ictrp_trials)
            for pi in bundle.drug.predicted_indications
        )
        total_articles = sum(
            len(pi.pubmed_articles)
            for pi in bundle.drug.predicted_indications
        )

        result.update({
            "status": "success",
            "bundle_path": str(bundle_path),
            "indication_count": indication_count,
            "total_trials": total_trials,
            "total_articles": total_articles,
            "npra_found": bundle.npra.get("found", False),
            "npra_count": len(bundle.npra.get("records", [])),
        })

        # Add delay between drugs to be nice to APIs
        time.sleep(delay)

    except Exception as e:
        result.update({
            "status": "error",
            "error": str(e),
        })

    result["duration_seconds"] = round(time.time() - start_time, 2)
    return result


def main():
    parser = argparse.ArgumentParser(description="Batch collect drug bundles")
    parser.add_argument("--drugs", type=str, help="Comma-separated list of drug names")
    parser.add_argument("--limit", type=int, help="Limit number of drugs to process")
    parser.add_argument("--offset", type=int, default=0, help="Start offset")
    parser.add_argument("--all", action="store_true", help="Process all drugs")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between drugs (seconds)")
    parser.add_argument("--output", type=str, help="Output JSON file for results")
    parser.add_argument("--skip-existing", action="store_true", help="Skip drugs with existing bundles")
    parser.add_argument("--max-indications", type=int, default=5, help="Max indications per drug")

    args = parser.parse_args()

    print("=" * 60)
    print("Batch Drug Bundle Collection")
    print("=" * 60)

    base_dir = Path(__file__).parent.parent
    drugs_dir = base_dir / "docs" / "_drugs"

    # Load drugs
    print("\n1. Loading drug list...")
    all_drugs = load_drug_list(drugs_dir)
    print(f"   Found {len(all_drugs)} drugs")

    # Filter by specific drugs if requested
    if args.drugs:
        drug_names = [d.strip().lower() for d in args.drugs.split(",")]
        drugs = [d for d in all_drugs if d["name"].lower() in drug_names]
        if not drugs:
            print(f"   No matching drugs found for: {args.drugs}")
            return
    else:
        drugs = all_drugs

    # Sort by prediction count (prioritize drugs with more predictions)
    drugs.sort(key=lambda d: d.get("kg_predictions", 0), reverse=True)

    # Apply offset
    if args.offset > 0:
        drugs = drugs[args.offset:]

    # Apply limit
    if args.limit:
        drugs = drugs[:args.limit]

    # Filter out existing bundles if requested
    if args.skip_existing:
        bundles_dir = get_bundles_dir()
        original_count = len(drugs)
        drugs = [
            d for d in drugs
            if not (bundles_dir / slugify(d["name"]) / "drug_bundle.json").exists()
        ]
        skipped = original_count - len(drugs)
        if skipped > 0:
            print(f"   Skipped {skipped} drugs with existing bundles")

    print(f"\n2. Processing {len(drugs)} drugs...")
    print("-" * 60)

    # Initialize aggregator
    aggregator = DrugBundleAggregator(save_collected=True)

    results = []
    for i, drug in enumerate(drugs, 1):
        print(f"[{i}/{len(drugs)}] {drug['name']}...", end=" ", flush=True)

        result = collect_single_drug(drug, aggregator, args.delay)
        results.append(result)

        if result["status"] == "success":
            print(
                f"✓ Ind:{result['indication_count']} "
                f"Trials:{result.get('total_trials', 0)} "
                f"Pub:{result.get('total_articles', 0)} "
                f"NPRA:{result.get('npra_count', 0)} "
                f"({result['duration_seconds']}s)"
            )
        else:
            print(f"✗ {result['error']}")

    # Summary
    print("-" * 60)
    success = sum(1 for r in results if r["status"] == "success")
    total_ind = sum(r.get("indication_count", 0) for r in results)
    total_trials = sum(r.get("total_trials", 0) for r in results)
    total_articles = sum(r.get("total_articles", 0) for r in results)

    print(f"\n3. Summary")
    print(f"   Completed: {success}/{len(drugs)}")
    print(f"   Total indications: {total_ind}")
    print(f"   Total trials: {total_trials}")
    print(f"   Total articles: {total_articles}")

    # Save results
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
        print(f"\n   Results saved to: {output_path}")
    else:
        # Save to default location
        output_path = get_bundles_dir() / "_collection_log.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps({
            "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_drugs": len(results),
            "success_count": success,
            "results": results,
        }, indent=2, ensure_ascii=False))
        print(f"\n   Collection log saved to: {output_path}")

    print("\n" + "=" * 60)
    print("Done! Bundles saved to: data/bundles/")
    print("Next step: Ask Claude to analyze the bundles")
    print("=" * 60)


if __name__ == "__main__":
    main()
