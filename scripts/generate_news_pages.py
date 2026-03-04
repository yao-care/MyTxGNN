#!/usr/bin/env python3
"""Generate news keyword pages for drugs and indications.

Creates individual pages in docs/_news/ for each drug and indication
so users can view news filtered by keyword.

Usage:
    uv run python scripts/generate_news_pages.py
"""

import json
import re
from pathlib import Path


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'[^\w-]', '', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def generate_drug_page(drug: dict, synonyms: list) -> str:
    """Generate markdown content for a drug news page."""
    name = drug.get("name", "")
    slug = drug.get("slug", "")
    drugbank_id = drug.get("drugbank_id", "")

    synonyms_yaml = "\n".join([f'  - "{s}"' for s in synonyms]) if synonyms else ""

    return f"""---
layout: news
title: "Berita: {name}"
keyword: "{name}"
slug: "{slug}"
drugbank_id: "{drugbank_id}"
type: drug
synonyms:
{synonyms_yaml}
---
"""


def generate_indication_page(indication: str, synonyms: list) -> str:
    """Generate markdown content for an indication news page."""
    slug = slugify(indication)
    title = indication.title()

    synonyms_yaml = "\n".join([f'  - "{s}"' for s in synonyms]) if synonyms else ""

    return f"""---
layout: news
title: "Berita: {title}"
keyword: "{title}"
slug: "{slug}"
type: indication
synonyms:
{synonyms_yaml}
---
"""


def main():
    print("=" * 60)
    print("Generating News Keyword Pages")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    drugs_dir = base_dir / "docs" / "_drugs"
    news_dir = base_dir / "docs" / "_news"
    synonyms_path = base_dir / "data" / "news" / "synonyms.json"

    # Create news directory
    news_dir.mkdir(parents=True, exist_ok=True)

    # Load synonyms
    print("1. Loading synonyms...")
    if synonyms_path.exists():
        with open(synonyms_path, encoding="utf-8") as f:
            synonyms_data = json.load(f)
        drug_synonyms = synonyms_data.get("drug_synonyms", {})
        indication_synonyms = synonyms_data.get("indication_synonyms", {})
        print(f"   Loaded {len(drug_synonyms)} drug synonyms")
        print(f"   Loaded {len(indication_synonyms)} indication synonyms")
    else:
        drug_synonyms = {}
        indication_synonyms = {}
        print("   No synonyms file found")

    # Generate drug pages from _drugs collection
    print("2. Generating drug news pages...")
    drug_count = 0

    if drugs_dir.exists():
        for drug_file in drugs_dir.glob("*.md"):
            # Read front matter to get drug info
            content = drug_file.read_text(encoding="utf-8")

            # Parse front matter
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    front_matter = parts[1]

                    # Extract fields
                    name = ""
                    slug = ""
                    drugbank_id = ""

                    for line in front_matter.split("\n"):
                        if line.startswith("title:"):
                            name = line.split(":", 1)[1].strip().strip('"')
                        elif line.startswith("drugbank_id:"):
                            drugbank_id = line.split(":", 1)[1].strip().strip('"')
                        elif line.startswith("permalink:"):
                            # Extract slug from permalink like /drugs/omeprazole/
                            plink = line.split(":", 1)[1].strip().strip('"')
                            parts = plink.strip("/").split("/")
                            if len(parts) >= 2:
                                slug = parts[-1]

                    if name and slug:
                        drug = {
                            "name": name,
                            "slug": slug,
                            "drugbank_id": drugbank_id
                        }
                        syns = drug_synonyms.get(name.lower(), [])

                        page_content = generate_drug_page(drug, syns)
                        page_path = news_dir / f"{slug}.md"
                        page_path.write_text(page_content, encoding="utf-8")
                        drug_count += 1

    print(f"   Generated {drug_count} drug news pages")

    # Generate indication pages
    print("3. Generating indication news pages...")
    indication_count = 0

    for indication, syns in indication_synonyms.items():
        if indication.startswith("_"):
            continue

        slug = slugify(indication)
        page_content = generate_indication_page(indication, syns)
        page_path = news_dir / f"{slug}.md"

        # Don't overwrite drug pages
        if not page_path.exists():
            page_path.write_text(page_content, encoding="utf-8")
            indication_count += 1

    print(f"   Generated {indication_count} indication news pages")

    print()
    print(f"Total news pages: {drug_count + indication_count}")
    print(f"Output directory: {news_dir}")


if __name__ == "__main__":
    main()
