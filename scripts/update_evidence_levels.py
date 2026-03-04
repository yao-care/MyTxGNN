#!/usr/bin/env python3
"""Update drug pages with collected evidence levels.

Reads evidence from data/evidence/ and updates the drug pages in docs/_drugs/.

Usage:
    uv run python scripts/update_evidence_levels.py
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


def update_front_matter(content: str, updates: dict) -> str:
    """Update front matter fields in markdown content.

    Args:
        content: Full markdown content
        updates: Dict of field -> new value

    Returns:
        Updated markdown content
    """
    if not content.startswith("---"):
        return content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return content

    front_matter_lines = parts[1].strip().split("\n")
    new_lines = []
    updated_fields = set()

    for line in front_matter_lines:
        field_match = re.match(r'^(\w+):\s*', line)
        if field_match:
            field_name = field_match.group(1)
            if field_name in updates:
                new_value = updates[field_name]
                if isinstance(new_value, str):
                    new_lines.append(f'{field_name}: "{new_value}"')
                else:
                    new_lines.append(f'{field_name}: {new_value}')
                updated_fields.add(field_name)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    # Add any new fields that weren't in original
    for field, value in updates.items():
        if field not in updated_fields:
            if isinstance(value, str):
                new_lines.append(f'{field}: "{value}"')
            else:
                new_lines.append(f'{field}: {value}')

    return f"---\n{chr(10).join(new_lines)}\n---{parts[2]}"


def update_evidence_badge(content: str, new_level: str) -> str:
    """Update the evidence level in the Quick Overview table."""
    # Update in table: | **Evidence Level** | L5 |
    content = re.sub(
        r'\|\s*\*\*Evidence Level\*\*\s*\|\s*L\d\s*\|',
        f'| **Evidence Level** | {new_level} |',
        content
    )
    return content


def main():
    print("=" * 60)
    print("Updating Drug Evidence Levels")
    print("=" * 60)

    base_dir = Path(__file__).parent.parent
    evidence_dir = base_dir / "data" / "evidence"
    drugs_dir = base_dir / "docs" / "_drugs"

    if not evidence_dir.exists():
        print("No evidence data found. Run collect_evidence.py first.")
        return

    # Load all evidence files
    print("\n1. Loading evidence data...")
    evidence_data = {}

    for evidence_file in evidence_dir.glob("*.json"):
        if evidence_file.name.startswith("_"):
            continue

        with open(evidence_file, encoding="utf-8") as f:
            data = json.load(f)

        drug_name = data.get("drug", "")
        if drug_name:
            evidence_data[drug_name.lower()] = data

    print(f"   Loaded evidence for {len(evidence_data)} drugs")

    # Update drug pages
    print("\n2. Updating drug pages...")
    updated_count = 0
    level_changes = {"L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0}

    for drug_file in sorted(drugs_dir.glob("*.md")):
        content = drug_file.read_text(encoding="utf-8")

        if not content.startswith("---"):
            continue

        # Extract drug name from front matter
        drug_name = ""
        current_level = "L5"

        for line in content.split("---", 2)[1].split("\n"):
            if line.startswith("title:"):
                drug_name = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("evidence_level:"):
                current_level = line.split(":", 1)[1].strip().strip('"')

        if not drug_name:
            continue

        # Check if we have evidence for this drug
        evidence = evidence_data.get(drug_name.lower())

        if not evidence:
            continue

        new_level = evidence.get("evidence_level", "L5")

        # Only update if level changed
        if new_level == current_level:
            continue

        print(f"   {drug_name}: {current_level} → {new_level}")

        # Update front matter
        updated_content = update_front_matter(content, {"evidence_level": new_level})

        # Update evidence badge in content
        updated_content = update_evidence_badge(updated_content, new_level)

        # Write back
        drug_file.write_text(updated_content, encoding="utf-8")
        updated_count += 1
        level_changes[new_level] = level_changes.get(new_level, 0) + 1

    print(f"\n3. Updated {updated_count} drug pages")

    if updated_count > 0:
        print("\n   Level distribution of changes:")
        for level, count in sorted(level_changes.items()):
            if count > 0:
                print(f"     {level}: {count}")

    # Show summary of all levels
    print("\n4. Checking current level distribution...")
    all_levels = {"L1": 0, "L2": 0, "L3": 0, "L4": 0, "L5": 0}

    for drug_file in drugs_dir.glob("*.md"):
        content = drug_file.read_text(encoding="utf-8")
        level_match = re.search(r'evidence_level:\s*"?(L\d)"?', content)
        if level_match:
            level = level_match.group(1)
            all_levels[level] = all_levels.get(level, 0) + 1

    print("\n   Current distribution:")
    for level, count in sorted(all_levels.items()):
        print(f"     {level}: {count} drugs")


if __name__ == "__main__":
    main()
