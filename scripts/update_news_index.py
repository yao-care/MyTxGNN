#!/usr/bin/env python3
"""Update news-index.json for the website.

Converts latest_news.json to the format expected by docs/data/news-index.json.

Key logic: News must match BOTH drug AND indication to be included.
When an indication is matched, the system finds related drugs that can treat it.

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


def build_indication_to_drugs_map(keywords_path: Path) -> dict:
    """Build a mapping from indication to list of related drugs.

    Uses drug_disease_pairs from keywords.json to create:
    indication_name -> [(drug_name, drug_slug), ...]
    """
    if not keywords_path.exists():
        return {}

    with open(keywords_path, encoding="utf-8") as f:
        keywords = json.load(f)

    indication_to_drugs = {}

    # Process drug_disease_pairs
    for pair in keywords.get("drug_disease_pairs", []):
        drug_name = pair.get("drug", "")
        disease = pair.get("disease", "").lower()

        if not drug_name or not disease:
            continue

        # Create slug from drug name
        drug_slug = slugify(drug_name)

        if disease not in indication_to_drugs:
            indication_to_drugs[disease] = []

        # Avoid duplicates
        drug_entry = {"name": drug_name.title(), "slug": drug_slug}
        if drug_entry not in indication_to_drugs[disease]:
            indication_to_drugs[disease].append(drug_entry)

    # Also map disease_keywords to their related drugs
    disease_keywords = keywords.get("disease_keywords", {})
    for disease_name, disease_info in disease_keywords.items():
        disease_lower = disease_name.lower()
        # Check if any drug_disease_pairs contain this disease
        for pair in keywords.get("drug_disease_pairs", []):
            pair_disease = pair.get("disease", "").lower()
            # Partial match: if the disease keyword is contained in a pair's disease
            if disease_lower in pair_disease or pair_disease in disease_lower:
                drug_name = pair.get("drug", "")
                drug_slug = slugify(drug_name)

                if disease_lower not in indication_to_drugs:
                    indication_to_drugs[disease_lower] = []

                drug_entry = {"name": drug_name.title(), "slug": drug_slug}
                if drug_entry not in indication_to_drugs[disease_lower]:
                    indication_to_drugs[disease_lower].append(drug_entry)

    return indication_to_drugs


def match_drug_keywords(text: str, drugs_lookup: dict, synonyms: dict) -> list:
    """Match drug names in text."""
    text_lower = text.lower()
    matched = []
    seen = set()

    # First check all 508 drug names from drugs_lookup
    for drug_name_lower, slug in drugs_lookup.items():
        # Only match if drug name is at least 4 chars to avoid false positives
        if len(drug_name_lower) >= 4 and drug_name_lower in text_lower:
            if drug_name_lower not in seen:
                matched.append({
                    "type": "drug",
                    "name": drug_name_lower.title(),
                    "slug": slug
                })
                seen.add(drug_name_lower)

    # Also check drug synonyms (brand names, local names)
    drug_synonyms = synonyms.get("drug_synonyms", {})
    for drug_name, syns in drug_synonyms.items():
        if drug_name.lower() in seen:
            continue
        for syn in syns:
            # Only match synonyms with 4+ chars
            if len(syn) >= 4 and syn.lower() in text_lower:
                slug = drugs_lookup.get(drug_name.lower())
                if slug:
                    matched.append({
                        "type": "drug",
                        "name": drug_name.title(),
                        "slug": slug
                    })
                    seen.add(drug_name.lower())
                break

    return matched, seen


def match_indication_keywords(text: str, synonyms: dict, indication_to_drugs: dict, drugs_lookup: dict) -> tuple:
    """Match indication/disease names in text and find related drugs.

    Returns:
        (indication_matches, related_drug_matches)
    """
    text_lower = text.lower()
    indication_matched = []
    related_drugs = []
    seen_indications = set()
    seen_drugs = set()

    indication_synonyms = synonyms.get("indication_synonyms", {})
    for indication, syns in indication_synonyms.items():
        all_names = [indication] + syns
        for name in all_names:
            if name.lower() in text_lower:
                if indication not in seen_indications:
                    indication_matched.append({
                        "type": "indication",
                        "name": indication.title(),
                        "keyword": name,
                        "slug": slugify(indication)
                    })
                    seen_indications.add(indication)

                    # Find related drugs for this indication
                    indication_lower = indication.lower()
                    if indication_lower in indication_to_drugs:
                        for drug_info in indication_to_drugs[indication_lower]:
                            drug_slug = drug_info["slug"]
                            if drug_slug not in seen_drugs:
                                # Check if drug exists in drugs_lookup
                                drug_name_lower = drug_info["name"].lower()
                                if drug_name_lower in drugs_lookup or drug_slug in [v for v in drugs_lookup.values()]:
                                    related_drugs.append({
                                        "type": "drug",
                                        "name": drug_info["name"],
                                        "slug": drug_slug,
                                        "via_indication": indication.title()
                                    })
                                    seen_drugs.add(drug_slug)
                break

    return indication_matched, related_drugs, seen_drugs


def convert_news_item(item: dict, drugs_lookup: dict, synonyms: dict, indication_to_drugs: dict) -> dict:
    """Convert a news item to website format.

    A news item is only included if it has BOTH drug AND indication matches.
    When an indication is matched, related drugs are also added.
    """
    text = f"{item.get('title', '')} {item.get('summary', '')}"

    # Match direct drug keywords
    direct_drug_keywords, seen_direct_drugs = match_drug_keywords(text, drugs_lookup, synonyms)

    # Match indication keywords and get related drugs
    indication_keywords, related_drug_keywords, seen_related_drugs = match_indication_keywords(
        text, synonyms, indication_to_drugs, drugs_lookup
    )

    # Combine drug keywords (direct + related from indications)
    all_drug_keywords = direct_drug_keywords.copy()
    for drug in related_drug_keywords:
        # Avoid duplicates
        if drug["slug"] not in seen_direct_drugs:
            all_drug_keywords.append(drug)

    # Combine all keywords
    keywords = all_drug_keywords + indication_keywords

    return {
        "title": item.get("title", ""),
        "published": item.get("published", ""),
        "sources": [
            {
                "name": item.get("source", ""),
                "link": item.get("url", "")
            }
        ],
        "keywords": keywords,
        "_has_drug": len(all_drug_keywords) > 0,
        "_has_indication": len(indication_keywords) > 0
    }


def main():
    print("=" * 60)
    print("Updating News Index for Website")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    latest_news_path = base_dir / "data" / "news" / "latest_news.json"
    synonyms_path = base_dir / "data" / "news" / "synonyms.json"
    keywords_path = base_dir / "data" / "news" / "keywords.json"
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

    print("4. Building indication-to-drugs mapping...")
    indication_to_drugs = build_indication_to_drugs_map(keywords_path)
    print(f"   Built mapping for {len(indication_to_drugs)} indications")

    # Convert news items
    print("5. Converting news items...")
    news_items = []
    drug_only_count = 0
    indication_only_count = 0
    both_count = 0

    for item in latest_news.get("items", []):
        converted = convert_news_item(item, drugs_lookup, synonyms, indication_to_drugs)

        has_drug = converted.pop("_has_drug", False)
        has_indication = converted.pop("_has_indication", False)

        # Only include items that have BOTH drug AND indication
        if has_drug and has_indication:
            news_items.append(converted)
            both_count += 1
        elif has_drug:
            drug_only_count += 1
        elif has_indication:
            indication_only_count += 1

    print(f"   Drug + Indication (included): {both_count}")
    print(f"   Drug only (excluded): {drug_only_count}")
    print(f"   Indication only (excluded): {indication_only_count}")

    # Create output
    output = {
        "news": news_items,
        "last_updated": datetime.now().isoformat() + "Z",
        "sources": ["CodeBlue", "The Star", "Malay Mail", "NST", "FMT"]
    }

    # Save
    print("6. Saving news index...")
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
        for item in news_items[:5]:
            drugs = [k["name"] for k in item.get("keywords", []) if k["type"] == "drug"]
            indications = [k["name"] for k in item.get("keywords", []) if k["type"] == "indication"]
            print(f"  - {item['title'][:60]}...")
            print(f"    Drugs: {', '.join(drugs)}")
            print(f"    Indications: {', '.join(indications)}")


if __name__ == "__main__":
    main()
