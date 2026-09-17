#!/usr/bin/env python3
"""
Generate unified search index for drug lookup feature.

This script creates a JSON index file that supports:
1. Drug name search (English INN + Chinese brand names)
2. Indication/disease search
3. Bidirectional lookup (drug → indications, indication → drugs)
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import date

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUNDLES_DIR = PROJECT_ROOT / "data" / "bundles"
OUTPUT_FILE = PROJECT_ROOT / "docs" / "data" / "search-index.json"


def calculate_evidence_level(indication: dict) -> str:
    """Calculate evidence level based on clinical trials and papers."""
    trials = indication.get("clinical_trials", [])
    articles = indication.get("pubmed_articles", [])

    phase3_4_count = 0
    phase2_count = 0
    phase1_count = 0

    for trial in trials:
        phase = trial.get("phase", "").upper()
        if "PHASE3" in phase or "PHASE4" in phase or "PHASE 3" in phase or "PHASE 4" in phase:
            phase3_4_count += 1
        elif "PHASE2" in phase or "PHASE 2" in phase:
            phase2_count += 1
        elif "PHASE1" in phase or "PHASE 1" in phase:
            phase1_count += 1

    total_articles = len(articles)

    if phase3_4_count >= 2:
        return "L1"
    elif phase3_4_count >= 1 or phase2_count >= 2:
        return "L2"
    elif phase2_count >= 1 or phase1_count >= 1 or len(trials) >= 1:
        return "L3"
    elif total_articles >= 1:
        return "L4"
    else:
        return "L5"


def extract_brand_names(bundle: dict) -> list:
    """Extract Chinese brand names from TFDA data."""
    brand_names = set()

    tfda = bundle.get("tfda", {})
    licenses = tfda.get("licenses", [])

    for license_info in licenses:
        name = license_info.get("name", "")
        if name:
            # Extract Chinese characters only
            chinese_name = re.sub(r'[^\u4e00-\u9fff]', '', name)
            if chinese_name and len(chinese_name) >= 2:
                brand_names.add(chinese_name)

    return list(brand_names)[:5]  # Limit to 5 brand names


def get_original_indication(bundle: dict) -> str:
    """Get original indication from bundle."""
    drug = bundle.get("drug", {})
    original = drug.get("original_indications", [])
    if original:
        return original[0][:50] + "..." if len(original[0]) > 50 else original[0]
    return ""


def load_all_bundles() -> list:
    """Load all drug bundles."""
    bundles = []

    for drug_dir in BUNDLES_DIR.iterdir():
        if not drug_dir.is_dir():
            continue

        bundle_file = drug_dir / "drug_bundle.json"
        if not bundle_file.exists():
            continue

        try:
            with open(bundle_file, "r", encoding="utf-8") as f:
                bundle = json.load(f)
                bundle["_slug"] = drug_dir.name
                bundles.append(bundle)
        except Exception as e:
            print(f"Error loading {bundle_file}: {e}")

    return bundles


def build_search_index(bundles: list) -> dict:
    """Build the search index from all bundles."""
    drugs = []
    indication_map = defaultdict(list)  # indication -> list of drugs

    level_order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}

    for bundle in bundles:
        drug_data = bundle.get("drug", {})
        slug = bundle.get("_slug", "")
        name = drug_data.get("inn", slug.replace("_", " ").title())

        # Get brand names
        brand_names = extract_brand_names(bundle)

        # Get original indication
        original_indication = get_original_indication(bundle)

        # Get predicted indications
        predicted = drug_data.get("predicted_indications", [])
        indications = []
        best_level = "L5"

        for ind in predicted:
            ind_name = ind.get("disease_name", "")
            score = ind.get("txgnn_score", 0)
            level = calculate_evidence_level(ind)

            indications.append({
                "name": ind_name,
                "score": round(score * 100, 2),
                "level": level
            })

            # Track best evidence level
            if level_order.get(level, 5) < level_order.get(best_level, 5):
                best_level = level

            # Add to indication map for reverse lookup
            indication_map[ind_name].append({
                "name": name,
                "slug": slug,
                "score": round(score * 100, 2),
                "level": level,
                "original": original_indication
            })

        drugs.append({
            "name": name,
            "slug": slug,
            "brands": brand_names,
            "original": original_indication,
            "level": best_level,
            "indications": indications
        })

    # Build indication index
    indications = []
    for ind_name, ind_drugs in indication_map.items():
        # Sort drugs by evidence level, then by score
        sorted_drugs = sorted(
            ind_drugs,
            key=lambda x: (level_order.get(x["level"], 5), -x["score"])
        )

        best_level = sorted_drugs[0]["level"] if sorted_drugs else "L5"

        indications.append({
            "name": ind_name,
            "count": len(sorted_drugs),
            "level": best_level,
            "drugs": sorted_drugs
        })

    # Sort indications by drug count (descending)
    indications.sort(key=lambda x: -x["count"])

    return {
        "generated": date.today().isoformat(),
        "drug_count": len(drugs),
        "indication_count": len(indications),
        "drugs": drugs,
        "indications": indications
    }


def main():
    print("=" * 60)
    print("Generating Search Index")
    print("=" * 60)

    # Load all bundles
    bundles = load_all_bundles()
    print(f"Loaded {len(bundles)} drug bundles")

    # Build search index
    index = build_search_index(bundles)
    print(f"Built index with {index['drug_count']} drugs and {index['indication_count']} indications")

    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Write output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"Output written to: {OUTPUT_FILE}")

    # Show sample data
    print("\nSample drugs:")
    for drug in index["drugs"][:3]:
        print(f"  - {drug['name']} ({drug['level']}): {len(drug['indications'])} indications")
        if drug['brands']:
            print(f"    Brands: {', '.join(drug['brands'])}")

    print("\nSample indications:")
    for ind in index["indications"][:3]:
        print(f"  - {ind['name']} ({ind['level']}): {ind['count']} drugs")


def _prune_search_index():
    """把 docs/_drugs 裡不存在、或自己標了 search_exclude 的頁面，從搜尋索引移除。

    索引是由 data/processed 的預測檔生成的，跟頁面是否存在無關，所以會出現
    指向不存在頁面的 entry（死連結），以及薄內容頁佔據搜尋結果。這裡在寫檔後
    以頁面為準做一次收斂。
    """
    import json as _json
    import re as _re
    from pathlib import Path as _Path

    idx_path = _Path("docs/data/search-index.json")
    drugs_dir = _Path("docs/_drugs")
    if not idx_path.exists() or not drugs_dir.is_dir():
        return

    try:
        idx = _json.loads(idx_path.read_text(encoding="utf-8"))
    except Exception:
        return
    if not isinstance(idx, dict) or not isinstance(idx.get("drugs"), list):
        return

    _cache = {}

    def _visible(slug):
        if not slug:
            return False
        if slug in _cache:
            return _cache[slug]
        page = drugs_dir / f"{slug}.md"
        ok = page.exists()
        if ok:
            head = page.read_text(encoding="utf-8", errors="replace")[:2000]
            if _re.search(r"^search_exclude:\s*true", head, _re.M | _re.I):
                ok = False
        _cache[slug] = ok
        return ok

    before = len(idx["drugs"])
    idx["drugs"] = [d for d in idx["drugs"] if _visible(d.get("slug"))]

    inds = idx.get("indications")
    if isinstance(inds, list):
        kept = []
        for ind in inds:
            refs = ind.get("drugs")
            if isinstance(refs, list):
                refs = [r for r in refs if _visible(r.get("slug"))]
                if not refs:
                    continue
                ind["drugs"] = refs
                ind["drug_count"] = len(refs)
            kept.append(ind)
        idx["indications"] = kept
        idx["indication_count"] = len(kept)

    idx["drug_count"] = len(idx["drugs"])
    idx_path.write_text(_json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  Pruned search index: {before} -> {len(idx['drugs'])} drugs")


_main_before_prune = main


def main():
    _main_before_prune()
    _prune_search_index()


if __name__ == "__main__":
    main()
