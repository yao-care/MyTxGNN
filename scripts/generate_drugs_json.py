#!/usr/bin/env python3
"""Generate drugs.json for the news page drug list.

Creates docs/data/drugs.json from the _drugs collection.

Usage:
    uv run python scripts/generate_drugs_json.py
"""

import json
import re
from pathlib import Path


def main():
    print("=" * 60)
    print("Generating drugs.json")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    drugs_dir = base_dir / "docs" / "_drugs"
    output_path = base_dir / "docs" / "data" / "drugs.json"

    drugs = []

    print("1. Reading drug files...")
    for drug_file in sorted(drugs_dir.glob("*.md")):
        content = drug_file.read_text(encoding="utf-8")

        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                front_matter = parts[1]

                name = ""
                slug = ""
                drugbank_id = ""

                for line in front_matter.split("\n"):
                    if line.startswith("title:"):
                        name = line.split(":", 1)[1].strip().strip('"')
                    elif line.startswith("drugbank_id:"):
                        drugbank_id = line.split(":", 1)[1].strip().strip('"')
                    elif line.startswith("permalink:"):
                        plink = line.split(":", 1)[1].strip().strip('"')
                        parts = plink.strip("/").split("/")
                        if len(parts) >= 2:
                            slug = parts[-1]

                if name and slug:
                    drugs.append({
                        "name": name,
                        "slug": slug,
                        "drugbank_id": drugbank_id
                    })

    print(f"   Found {len(drugs)} drugs")

    # Sort by name
    drugs.sort(key=lambda x: x["name"])

    # Save
    print("2. Saving drugs.json...")
    output = {
        "drugs": drugs,
        "total": len(drugs),
        "last_updated": "2026-03-04"
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print()
    print(f"Saved to: {output_path}")
    print(f"Total drugs: {len(drugs)}")


if __name__ == "__main__":
    main()
