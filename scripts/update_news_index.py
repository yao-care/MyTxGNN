#!/usr/bin/env python3
"""Update news-index.json for the website.

Converts latest_news.json to the format expected by docs/data/news-index.json.

Usage:
    uv run python scripts/update_news_index.py
"""

import json
import re
from datetime import datetime
from pathlib import Path


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'[^\w\u4e00-\u9fff-]', '', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def load_drugs_list(path: Path) -> dict:
    """Load drugs list for keyword matching."""
    if not path.exists():
        return {}

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    # Create lookup by name
    drugs_lookup = {}
    for drug in data.get("drugs", []):
        name = drug.get("name", "").lower()
        slug = drug.get("slug", "")
        if name and slug:
            drugs_lookup[name] = slug

    return drugs_lookup


def match_drug_keywords(text: str, drugs_lookup: dict, synonyms: dict) -> list:
    """Match drug names in text."""
    text_lower = text.lower()
    matched = []
    seen = set()

    # Check drug synonyms
    drug_synonyms = synonyms.get("drug_synonyms", {})
    for drug_name, syns in drug_synonyms.items():
        all_names = [drug_name] + syns
        for name in all_names:
            if name.lower() in text_lower:
                slug = drugs_lookup.get(drug_name.lower())
                if slug and drug_name not in seen:
                    matched.append({
                        "type": "drug",
                        "name": drug_name.title(),
                        "slug": slug
                    })
                    seen.add(drug_name)
                break

    return matched


def match_indication_keywords(text: str, synonyms: dict) -> list:
    """Match indication/disease names in text."""
    text_lower = text.lower()
    matched = []
    seen = set()

    indication_synonyms = synonyms.get("indication_synonyms", {})
    for indication, syns in indication_synonyms.items():
        all_names = [indication] + syns
        for name in all_names:
            if name.lower() in text_lower:
                if indication not in seen:
                    matched.append({
                        "type": "indication",
                        "name": indication.title(),
                        "keyword": name,
                        "slug": slugify(indication)
                    })
                    seen.add(indication)
                break

    return matched


def convert_news_item(item: dict, drugs_lookup: dict, synonyms: dict) -> dict:
    """Convert a news item to website format."""
    text = f"{item.get('title', '')} {item.get('summary', '')}"

    # Match keywords
    drug_keywords = match_drug_keywords(text, drugs_lookup, synonyms)
    indication_keywords = match_indication_keywords(text, synonyms)
    keywords = drug_keywords + indication_keywords

    return {
        "title": item.get("title", ""),
        "published": item.get("published", ""),
        "sources": [
            {
                "name": item.get("source", ""),
                "link": item.get("url", "")
            }
        ],
        "keywords": keywords
    }


def main():
    print("=" * 60)
    print("Updating News Index for Website")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    latest_news_path = base_dir / "data" / "news" / "latest_news.json"
    synonyms_path = base_dir / "data" / "news" / "synonyms.json"
    drugs_path = base_dir / "docs" / "data" / "drugs.json"
    output_path = base_dir / "docs" / "data" / "news-index.json"

    # Load data
    print("1. Loading latest news...")
    if not latest_news_path.exists():
        print("   No latest news found. Run my_news.py first.")
        return

    with open(latest_news_path, encoding="utf-8") as f:
        latest_news = json.load(f)
    print(f"   Loaded {latest_news.get('total_items', 0)} news items")

    print("2. Loading synonyms...")
    if synonyms_path.exists():
        with open(synonyms_path, encoding="utf-8") as f:
            synonyms = json.load(f)
        print(f"   Loaded synonyms")
    else:
        synonyms = {}
        print("   No synonyms found")

    print("3. Loading drugs list...")
    drugs_lookup = load_drugs_list(drugs_path)
    print(f"   Loaded {len(drugs_lookup)} drugs")

    # Convert news items
    print("4. Converting news items...")
    news_items = []
    for item in latest_news.get("items", []):
        converted = convert_news_item(item, drugs_lookup, synonyms)
        # Only include items with keywords or from health sources
        if converted["keywords"] or "CodeBlue" in item.get("source", ""):
            news_items.append(converted)

    print(f"   Converted {len(news_items)} items with keywords")

    # Create output
    output = {
        "news": news_items,
        "last_updated": datetime.now().isoformat() + "Z",
        "sources": ["CodeBlue", "The Star", "Malay Mail", "NST", "FMT"]
    }

    # Save
    print("5. Saving news index...")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print()
    print(f"News index saved to: {output_path}")
    print(f"Total news items: {len(news_items)}")

    # Show sample
    if news_items:
        print()
        print("Sample items with keywords:")
        for item in news_items[:3]:
            kw_str = ", ".join([k["name"] for k in item.get("keywords", [])])
            print(f"  - {item['title'][:50]}...")
            if kw_str:
                print(f"    Keywords: {kw_str}")


if __name__ == "__main__":
    main()
