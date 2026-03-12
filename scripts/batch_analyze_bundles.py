#!/usr/bin/env python3
"""Batch analyze drug bundles and update drug pages.

This script analyzes collected bundles and determines evidence levels
based on clinical trial phases and literature.

Usage:
    uv run python scripts/batch_analyze_bundles.py
"""

import json
import re
from datetime import datetime
from pathlib import Path


def determine_evidence_level(indication: dict) -> tuple[str, str]:
    """Determine evidence level for an indication.

    Returns:
        (evidence_level, recommendation)
    """
    trials = indication.get("clinical_trials", [])
    articles = indication.get("pubmed_articles", [])

    # Count trials by phase
    phase3 = 0
    phase2 = 0
    phase4 = 0
    phase1 = 0

    for trial in trials:
        phase = trial.get("phase", "").upper()
        if "PHASE3" in phase or "PHASE 3" in phase:
            phase3 += 1
        elif "PHASE4" in phase or "PHASE 4" in phase:
            phase4 += 1
        elif "PHASE2" in phase or "PHASE 2" in phase:
            phase2 += 1
        elif "PHASE1" in phase or "PHASE 1" in phase:
            phase1 += 1

    # Count article types
    reviews = 0
    rcts = 0
    for article in articles:
        pub_types = article.get("pub_types", [])
        for pt in pub_types:
            pt_lower = pt.lower()
            if "review" in pt_lower or "meta-analysis" in pt_lower:
                reviews += 1
                break
            if "randomized controlled trial" in pt_lower:
                rcts += 1
                break

    # Determine level
    # L1: Multiple Phase 3 OR Phase 3 + reviews
    if phase3 >= 3 or (phase3 >= 1 and reviews >= 2) or phase4 >= 3:
        return "L1", "Go"

    # L2: Phase 3 exists OR multiple Phase 2 OR RCT articles
    if phase3 >= 1 or phase2 >= 3 or rcts >= 2:
        return "L2", "Research Question"

    # L3: Phase 2 exists OR Phase 1 trials
    if phase2 >= 1 or phase1 >= 2:
        return "L3", "Research Question"

    # L4: Has some trials or articles
    if len(trials) > 0 or len(articles) >= 5:
        return "L4", "Hold"

    # L5: AI prediction only
    return "L5", "Hold"


def analyze_bundle(bundle_path: Path) -> dict:
    """Analyze a drug bundle and return evidence summary."""
    with open(bundle_path, encoding="utf-8") as f:
        bundle = json.load(f)

    drug_name = bundle["drug"]["name"]
    drugbank_id = bundle["drug"].get("drugbank_id")

    indications_analysis = []
    best_level = "L5"
    level_order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}

    for pi in bundle["drug"]["predicted_indications"]:
        level, rec = determine_evidence_level(pi)

        trials = pi.get("clinical_trials", [])
        articles = pi.get("pubmed_articles", [])

        # Count phases
        phase3 = sum(1 for t in trials if "PHASE3" in t.get("phase", "").upper() or "PHASE 3" in t.get("phase", "").upper())
        phase2 = sum(1 for t in trials if "PHASE2" in t.get("phase", "").upper() or "PHASE 2" in t.get("phase", "").upper())
        phase4 = sum(1 for t in trials if "PHASE4" in t.get("phase", "").upper() or "PHASE 4" in t.get("phase", "").upper())

        indications_analysis.append({
            "disease": pi["disease_name"],
            "evidence_level": level,
            "recommendation": rec,
            "trials": len(trials),
            "articles": len(articles),
            "phase3": phase3,
            "phase2": phase2,
            "phase4": phase4,
        })

        if level_order.get(level, 5) < level_order.get(best_level, 5):
            best_level = level

    # Get NPRA count
    npra_count = len(bundle.get("npra", {}).get("records", []))

    return {
        "drug": drug_name,
        "drugbank_id": drugbank_id,
        "best_level": best_level,
        "npra_count": npra_count,
        "indications": indications_analysis,
    }


def create_evidence_pack(analysis: dict, output_dir: Path) -> None:
    """Create evidence pack JSON and MD files."""
    drug_slug = analysis["drug"].lower().replace(" ", "_")
    pack_dir = output_dir / drug_slug
    pack_dir.mkdir(parents=True, exist_ok=True)

    # Create JSON
    evidence_pack = {
        "meta": {
            "version": "v1",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "analyzed_by": "Claude (batch)"
        },
        "drug": {
            "name": analysis["drug"],
            "drugbank_id": analysis["drugbank_id"],
        },
        "overall": {
            "best_evidence_level": analysis["best_level"],
            "npra_products": analysis["npra_count"],
        },
        "indications": analysis["indications"],
    }

    with open(pack_dir / f"{drug_slug}_drug_evidence_pack.json", "w", encoding="utf-8") as f:
        json.dump(evidence_pack, f, indent=2, ensure_ascii=False)

    # Create MD
    md_lines = [
        f"# {analysis['drug']} Drug Repurposing Analysis",
        "",
        "## Summary",
        f"- **Best Evidence Level**: {analysis['best_level']}",
        f"- **NPRA Products**: {analysis['npra_count']}",
        "",
        "## Indications",
        "| Indication | Level | Trials | Articles | Phase 3 | Recommendation |",
        "|------------|-------|--------|----------|---------|----------------|",
    ]

    for ind in analysis["indications"]:
        md_lines.append(
            f"| {ind['disease']} | {ind['evidence_level']} | {ind['trials']} | "
            f"{ind['articles']} | {ind['phase3']} | {ind['recommendation']} |"
        )

    with open(pack_dir / f"{drug_slug}_drug_evidence_pack.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))


def update_drug_page(analysis: dict, drugs_dir: Path) -> bool:
    """Update drug page with evidence analysis."""
    drug_slug = analysis["drug"].lower().replace(" ", "-")
    drug_file = drugs_dir / f"{drug_slug}.md"

    if not drug_file.exists():
        # Try underscore version
        drug_slug = analysis["drug"].lower().replace(" ", "_")
        drug_file = drugs_dir / f"{drug_slug}.md"

    if not drug_file.exists():
        print(f"  Warning: Drug page not found for {analysis['drug']}")
        return False

    content = drug_file.read_text(encoding="utf-8")

    # Update evidence_level in front matter
    content = re.sub(
        r'evidence_level:\s*"?L\d"?',
        f'evidence_level: "{analysis["best_level"]}"',
        content
    )

    # Update indication_count
    content = re.sub(
        r'indication_count:\s*\d+',
        f'indication_count: {len(analysis["indications"])}',
        content
    )

    # Update Evidence Level in table if exists
    content = re.sub(
        r'\|\s*\*\*Evidence Level\*\*\s*\|\s*L\d\s*\|',
        f'| **Evidence Level** | {analysis["best_level"]} |',
        content
    )

    drug_file.write_text(content, encoding="utf-8")
    return True


def main():
    print("=" * 60)
    print("Batch Drug Bundle Analysis")
    print("=" * 60)

    base_dir = Path(__file__).parent.parent
    bundles_dir = base_dir / "data" / "bundles"
    evidence_packs_dir = base_dir / "data" / "evidence_packs"
    drugs_dir = base_dir / "docs" / "_drugs"

    # Find all bundles
    bundle_files = sorted(bundles_dir.glob("*/drug_bundle.json"))
    print(f"\nFound {len(bundle_files)} bundles to analyze\n")

    results = []

    for i, bundle_path in enumerate(bundle_files, 1):
        drug_slug = bundle_path.parent.name
        print(f"[{i}/{len(bundle_files)}] Analyzing {drug_slug}...")

        try:
            analysis = analyze_bundle(bundle_path)

            # Create evidence pack
            create_evidence_pack(analysis, evidence_packs_dir)

            # Update drug page
            updated = update_drug_page(analysis, drugs_dir)

            results.append({
                "drug": analysis["drug"],
                "level": analysis["best_level"],
                "indications": len(analysis["indications"]),
                "updated": updated,
            })

            print(f"  → {analysis['best_level']} ({len(analysis['indications'])} indications)")

        except Exception as e:
            print(f"  Error: {e}")
            results.append({
                "drug": drug_slug,
                "level": "ERROR",
                "error": str(e),
            })

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    level_counts = {}
    for r in results:
        level = r.get("level", "ERROR")
        level_counts[level] = level_counts.get(level, 0) + 1

    print("\nEvidence Level Distribution:")
    for level in sorted(level_counts.keys()):
        print(f"  {level}: {level_counts[level]} drugs")

    print(f"\nTotal: {len(results)} drugs analyzed")
    print(f"Evidence packs saved to: {evidence_packs_dir}")


if __name__ == "__main__":
    main()
