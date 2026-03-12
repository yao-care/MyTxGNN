#!/usr/bin/env python3
"""Collect clinical evidence for drug repurposing predictions.

Searches ClinicalTrials.gov and PubMed for each drug's top predicted indications
and saves the evidence to data/evidence/.

Usage:
    uv run python scripts/collect_evidence.py [--drug DRUG_NAME] [--limit N]
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mytxgnn.collectors.clinicaltrials import ClinicalTrialsCollector
from mytxgnn.collectors.pubmed import PubMedCollector


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'[^\w-]', '', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


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

        # Parse front matter
        drug = {"file": drug_file}
        for line in front_matter.split("\n"):
            if line.startswith("title:"):
                drug["name"] = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("drugbank_id:"):
                drug["drugbank_id"] = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("evidence_level:"):
                drug["evidence_level"] = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("kg_predictions:"):
                drug["kg_predictions"] = int(line.split(":", 1)[1].strip())

        if "name" in drug:
            drugs.append(drug)

    return drugs


def extract_top_indications(drug_file: Path, max_indications: int = 5) -> list[str]:
    """Extract top predicted indications from a drug file."""
    content = drug_file.read_text(encoding="utf-8")

    # Find the predictions table
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


def determine_evidence_level(trials: list[dict], articles: list[dict]) -> tuple[str, dict]:
    """Determine evidence level based on collected evidence.

    Returns:
        (evidence_level, evidence_summary)
    """
    summary = {
        "phase3_trials": 0,
        "phase2_trials": 0,
        "phase1_trials": 0,
        "other_trials": 0,
        "rct_articles": 0,
        "review_articles": 0,
        "other_articles": 0,
        "total_trials": len(trials),
        "total_articles": len(articles),
    }

    # Analyze trials
    for trial in trials:
        phase = trial.get("phase", "").lower()
        if "phase 3" in phase or "phase3" in phase:
            summary["phase3_trials"] += 1
        elif "phase 2" in phase or "phase2" in phase:
            summary["phase2_trials"] += 1
        elif "phase 1" in phase or "phase1" in phase:
            summary["phase1_trials"] += 1
        else:
            summary["other_trials"] += 1

    # Analyze articles
    for article in articles:
        pub_types = [pt.lower() for pt in article.get("pub_types", [])]

        if any("randomized controlled trial" in pt for pt in pub_types):
            summary["rct_articles"] += 1
        elif any("review" in pt or "meta-analysis" in pt for pt in pub_types):
            summary["review_articles"] += 1
        else:
            summary["other_articles"] += 1

    # Determine level
    # L1: Multiple Phase 3 RCTs or systematic reviews
    if summary["phase3_trials"] >= 2 or (summary["phase3_trials"] >= 1 and summary["review_articles"] >= 1):
        return "L1", summary

    # L2: Single RCT or multiple Phase 2 trials
    if summary["phase3_trials"] >= 1 or summary["phase2_trials"] >= 2 or summary["rct_articles"] >= 1:
        return "L2", summary

    # L3: Phase 1/2 trials or observational studies
    if summary["phase2_trials"] >= 1 or summary["phase1_trials"] >= 1:
        return "L3", summary

    # L4: Case reports or preclinical evidence
    if summary["total_articles"] >= 3 or summary["other_trials"] >= 1:
        return "L4", summary

    # L5: AI prediction only
    return "L5", summary


def collect_evidence_for_drug(
    drug: dict,
    ct_collector: ClinicalTrialsCollector,
    pm_collector: PubMedCollector,
    output_dir: Path,
    delay: float = 1.0,
) -> dict:
    """Collect evidence for a single drug.

    Returns:
        Evidence summary dict
    """
    drug_name = drug["name"]
    drug_slug = slugify(drug_name)

    print(f"\n{'='*60}")
    print(f"Collecting evidence for: {drug_name}")
    print(f"{'='*60}")

    # Get top indications
    indications = extract_top_indications(drug["file"])

    if not indications:
        print(f"  No indications found for {drug_name}")
        return {"drug": drug_name, "evidence_level": "L5", "indications": []}

    print(f"  Found {len(indications)} top indications")

    all_trials = []
    all_articles = []
    indication_evidence = []

    for indication in indications:
        print(f"\n  Searching: {drug_name} + {indication}")

        # Search ClinicalTrials.gov
        time.sleep(delay)
        ct_result = ct_collector.search(drug_name, indication)
        trials = ct_result.data if ct_result.success else []
        print(f"    ClinicalTrials.gov: {len(trials)} trials")

        # Search PubMed
        time.sleep(delay)
        pm_result = pm_collector.search(drug_name, indication)
        articles = pm_result.data.get("results", []) if pm_result.success else []
        print(f"    PubMed: {len(articles)} articles")

        all_trials.extend(trials)
        all_articles.extend(articles)

        # Determine evidence level for this indication
        level, summary = determine_evidence_level(trials, articles)

        indication_evidence.append({
            "indication": indication,
            "evidence_level": level,
            "trials": len(trials),
            "articles": len(articles),
            "summary": summary,
        })

        print(f"    Evidence level: {level}")

    # Determine overall evidence level (best among all indications)
    best_level = "L5"
    level_order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}

    for ie in indication_evidence:
        if level_order.get(ie["evidence_level"], 5) < level_order.get(best_level, 5):
            best_level = ie["evidence_level"]

    print(f"\n  Overall evidence level: {best_level}")

    # Save evidence
    evidence = {
        "drug": drug_name,
        "drugbank_id": drug.get("drugbank_id", ""),
        "evidence_level": best_level,
        "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "indications": indication_evidence,
        "total_trials": len(all_trials),
        "total_articles": len(all_articles),
        "trials": all_trials[:20],  # Limit stored data
        "articles": all_articles[:20],
    }

    # Save to file
    output_file = output_dir / f"{drug_slug}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(evidence, f, indent=2, ensure_ascii=False)

    print(f"  Saved to: {output_file}")

    return evidence


def main():
    parser = argparse.ArgumentParser(description="Collect clinical evidence for drug predictions")
    parser.add_argument("--drug", type=str, help="Specific drug name to process")
    parser.add_argument("--limit", type=int, default=10, help="Max drugs to process (default: 10)")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between API calls in seconds")
    args = parser.parse_args()

    print("=" * 60)
    print("Evidence Collection for MyTxGNN")
    print("=" * 60)

    base_dir = Path(__file__).parent.parent
    drugs_dir = base_dir / "docs" / "_drugs"
    output_dir = base_dir / "data" / "evidence"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize collectors
    ct_collector = ClinicalTrialsCollector(max_results=20)
    pm_collector = PubMedCollector(max_results=10)

    # Load drugs
    print("\n1. Loading drug list...")
    drugs = load_drug_list(drugs_dir)
    print(f"   Found {len(drugs)} drugs")

    # Filter if specific drug requested
    if args.drug:
        drugs = [d for d in drugs if d["name"].lower() == args.drug.lower()]
        if not drugs:
            print(f"   Drug '{args.drug}' not found")
            return

    # Prioritize drugs with more predictions
    drugs.sort(key=lambda d: d.get("kg_predictions", 0), reverse=True)

    # Limit number of drugs
    drugs = drugs[:args.limit]

    print(f"\n2. Processing {len(drugs)} drugs...")

    results = []
    for i, drug in enumerate(drugs, 1):
        print(f"\n[{i}/{len(drugs)}] Processing {drug['name']}...")

        try:
            evidence = collect_evidence_for_drug(
                drug, ct_collector, pm_collector, output_dir, args.delay
            )
            results.append(evidence)
        except Exception as e:
            print(f"  Error: {e}")
            results.append({
                "drug": drug["name"],
                "evidence_level": "L5",
                "error": str(e),
            })

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    level_counts = {"L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0}
    for r in results:
        level = r.get("evidence_level", "L5")
        level_counts[level] = level_counts.get(level, 0) + 1

    for level, count in sorted(level_counts.items()):
        print(f"  {level}: {count} drugs")

    # Save summary
    summary_file = output_dir / "_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump({
            "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "total_drugs": len(results),
            "level_counts": level_counts,
            "drugs": [{"drug": r["drug"], "level": r.get("evidence_level", "L5")} for r in results],
        }, f, indent=2, ensure_ascii=False)

    print(f"\nSummary saved to: {summary_file}")


if __name__ == "__main__":
    main()
