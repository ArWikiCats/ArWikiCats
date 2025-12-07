#!/usr/bin/env python3
"""
Script to filter non-city entries from yy2.json.

This script uses the same logic as filter_non_geographic.py to identify and separate
non-city entries (universities, companies, museums, etc.) from actual city entries.
"""

import sys
import shutil
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from help_scripts.filter_non_geographic import filter_json_file


def main():
    """Main execution function for filtering cities file."""
    # Define paths
    base_dir = Path(__file__).parent.parent
    cities_dir = base_dir / 'ArWikiCats' / 'translations' / 'jsons' / 'cities'

    input_file = cities_dir / 'yy2.json'
    output_cities = cities_dir / 'yy2.json'
    output_non_cities = cities_dir / 'yy2_non_cities.json'

    # Backup the original file first
    backup_file = cities_dir / 'yy2.json.backup'
    if not backup_file.exists():
        shutil.copy2(input_file, backup_file)
        print(f"Created backup at: {backup_file}")

    # Filter the file
    stats = filter_json_file(input_file, output_cities, output_non_cities)

    # Print results
    print("\n" + "=" * 60)
    print("Filtering Results for yy2.json")
    print("=" * 60)
    print(f"Total entries: {stats['total_entries']}")
    print(f"City entries: {stats['geographic_entries']}")
    print(f"Non-city entries: {stats['non_geographic_entries']}")
    print(f"\nCity entries saved to: {output_cities}")
    print(f"Non-city entries saved to: {output_non_cities}")
    print("=" * 60)


if __name__ == '__main__':
    main()
