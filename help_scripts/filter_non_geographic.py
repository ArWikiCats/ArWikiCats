#!/usr/bin/env python3
"""
Script to filter non-geographic entries from P17_2_final_ll.json.

This script identifies and separates entries that represent non-geographic entities
(universities, bridges, associations, companies, sports clubs, etc.) from geographic
entries (countries, cities, regions, etc.).
"""

import sys
import json
import shutil
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

base_dir = Path(__file__).parent.parent
jsons_dir = base_dir / 'ArWikiCats' / 'translations' / 'jsons'


def is_non_geographic(key: str, value: str) -> bool:
    """
    Determine if an entry is non-geographic based on keywords in key or value.

    Args:
        key: The English key (normalized to lowercase)
        value: The Arabic translation

    Returns:
        True if the entry is non-geographic, False otherwise
    """
    key_lower = key.lower()

    # Educational institutions
    educational_patterns = ['university', 'college', 'school', 'institute', 'academy']

    # Infrastructure (non-geographic)
    infrastructure_patterns = ['bridge', 'highway', 'railway', 'airport', 'station', 'road', 'tunnel']

    # Organizations and associations
    organization_patterns = ['association', 'society', 'organization', 'organisation', 'foundation']

    # Sports entities
    sports_patterns = ['fc', 'club', 'team']

    # Companies and businesses
    business_patterns = ['company', 'corporation', 'ltd', 'inc', 'limited']

    # Medical facilities
    medical_patterns = ['hospital', 'clinic', 'medical center']

    # Cultural institutions
    cultural_patterns = ['museum', 'gallery', 'library', 'theater', 'theatre']

    # Sports venues
    venue_patterns = ['stadium', 'arena']

    # Hospitality
    hospitality_patterns = ['hotel', 'resort']

    # All patterns combined
    all_patterns = (
        educational_patterns + infrastructure_patterns + organization_patterns +
        sports_patterns + business_patterns + medical_patterns +
        cultural_patterns + venue_patterns + hospitality_patterns
    )

    # Check English patterns in key
    for pattern in all_patterns:
        if pattern in key_lower:
            return True

    # Arabic patterns in value
    arabic_patterns = [
        'جامعة',  # university
        'كلية',   # college
        'معهد',   # institute
        'نادي',   # club
        'جسر',    # bridge
        'شركة',   # company
        'جمعية',  # association
        'مستشفى',  # hospital
        'متحف',   # museum
        'فندق',   # hotel
        'ملعب',   # stadium
    ]

    for pattern in arabic_patterns:
        if pattern in value:
            return True

    return False


def filter_json_file(input_file: Path, output_geo: Path, output_non_geo: Path) -> dict:
    """
    Filter a JSON file into geographic and non-geographic entries.

    Args:
        input_file: Path to the input JSON file
        output_geo: Path to save geographic entries
        output_non_geo: Path to save non-geographic entries

    Returns:
        Dictionary with statistics about the filtering
    """
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Separate entries
    geographic = {}
    non_geographic = {}

    for key, value in data.items():
        if is_non_geographic(key, value):
            non_geographic[key] = value
        else:
            geographic[key] = value

    # Write output files
    with open(output_geo, 'w', encoding='utf-8') as f:
        json.dump(geographic, f, ensure_ascii=False, indent=4, sort_keys=True)

    with open(output_non_geo, 'w', encoding='utf-8') as f:
        json.dump(non_geographic, f, ensure_ascii=False, indent=4, sort_keys=True)

    # Return statistics
    return {
        'total_entries': len(data),
        'geographic_entries': len(geographic),
        'non_geographic_entries': len(non_geographic),
    }


def one_file(SOURCE_FILE, NEW_FILE, NON_GEO_FILE):
    """Main execution function."""

    # Filter the file
    stats = filter_json_file(SOURCE_FILE, NEW_FILE, NON_GEO_FILE)

    # Print results
    print("\n" + "=" * 60)
    print("Filtering Results")
    print("=" * 60)
    print(f"Total entries: {stats['total_entries']}")
    print(f"Geographic entries: {stats['geographic_entries']}")
    print(f"Non-geographic entries: {stats['non_geographic_entries']}")
    print(f"Geographic entries saved to: {NEW_FILE}")
    print(f"Non-geographic entries saved to: {NON_GEO_FILE}")
    print("=" * 60)


def main() -> None:

    SOURCE_FILE = jsons_dir / "cities/yy2.json"
    NEW_FILE = jsons_dir / "cities/yy2_new.json"
    NON_GEO_FILE = jsons_dir / "cities/yy2_non_cities.json"
    one_file(SOURCE_FILE, NEW_FILE, NON_GEO_FILE)

    SOURCE_FILE2 = jsons_dir / "geography/P17_2_final_ll.json"
    NEW_FILE2 = jsons_dir / "geography/P17_2_final_ll_new.json"
    NON_GEO_FILE2 = jsons_dir / "geography/P17_2_final_ll_non_geographic.json"
    one_file(SOURCE_FILE2, NEW_FILE2, NON_GEO_FILE2)


if __name__ == '__main__':
    main()
