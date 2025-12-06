# Scripts

This directory contains utility scripts for maintaining the ArWikiCats project.

## filter_non_geographic.py

Filters non-geographic entries from `P17_2_final_ll.json` into a separate file.

### Purpose

The `P17_2_final_ll.json` file is intended to contain geographic translations (countries, cities, regions, etc.). However, over time, non-geographic entries (universities, bridges, associations, companies, sports clubs, etc.) have been added to the file.

This script identifies and separates these non-geographic entries based on keywords into a new file called `P17_2_final_ll_non_geographic.json`.

### Usage

```bash
python scripts/filter_non_geographic.py
```

### What it does

1. Creates a backup of the original file (`.backup`)
2. Reads `P17_2_final_ll.json`
3. Identifies non-geographic entries based on:
   - English keywords: university, college, bridge, fc, club, company, museum, association, etc.
   - Arabic keywords: جامعة, كلية, نادي, جسر, شركة, متحف, جمعية, etc.
4. Splits the entries into two files:
   - `P17_2_final_ll.json` - Geographic entries only (updated in place)
   - `P17_2_final_ll_non_geographic.json` - Non-geographic entries (new file)

### Example Output

```
Total entries: 1720
Geographic entries: 1606
Non-geographic entries: 114
```

### Patterns Detected

The script detects the following types of non-geographic entities:

- **Educational institutions**: universities, colleges, schools, institutes
- **Infrastructure**: bridges, highways, railways, airports, stations
- **Organizations**: associations, societies, foundations
- **Sports entities**: football clubs (FC), sports teams
- **Companies**: corporations, limited companies
- **Medical facilities**: hospitals, clinics
- **Cultural institutions**: museums, galleries, libraries, theaters
- **Sports venues**: stadiums, arenas
- **Hospitality**: hotels, resorts
