#!/usr/bin/env python3
"""
Unified classifier for geographic vs non-geographic labels.

This script merges:
- Rich keyword taxonomy from split_non_geography.py
- Arabic/English pattern detection from filter_non_geographic.py
- Taxon detection (biological names)
- Person-role detection (king, queen, president...)
- Cultural/media keywords
- Multi-layer rule-based classification for maximum accuracy

"""

import json
import re
from pathlib import Path
from typing import Dict, Tuple
from collections import defaultdict
base_dir = Path(__file__).parent.parent
jsons_dir = base_dir / 'ArWikiCats' / 'translations' / 'jsons'


# -------------------------------------------------------------
# 1) Robust Keyword Sets (merged + expanded)
# -------------------------------------------------------------
NON_GEO_KEYWORDS_EN = {
    "Education": [
        "university", "college", "school", "academy", "institute", "faculty",
        "journal"
    ],
    "Medical": ["hospital", "clinic", "medical center"],
    "Business": [
        "company", "corporation", "ltd", "inc", "limited", "enterprise",
        "brand", "product", "bank", "airlines", "airways",
        "restaurant", "hotel"
    ],
    "Infrastructure": [
        "bridge", "tunnel", "airport", "station", "highway", "road",
        "railway", "canal", "pipeline", "dam", "dike", "circuit",
        "center", "centre", "park", "garden", "zoo"
    ],
    "Religious / Cultural Buildings": [
        "church", "cathedral", "mosque", "temple", "synagogue",
        "abbey", "monastery"
    ],
    "Organizations / Groups": [
        "association", "organisation", "organization", "foundation",
        "society", "agency", "council", "union", "movement",
        "army", "navy", "air force"
    ],
    "Tv": [
        "film", "tv series", "tv show", "television", "channel", "episode", "series"
    ],
    "Culture / Media": [
        "museum", "library", "gallery", "opera", "novel", "book",
        "movie", "season", "soundtrack",
        "theater", "theatre", "poem", "play", "album", "song",
        "single", "ballet", "musical",
        "magazine", "newspaper", "script", "studios", "music",
        "festival", "band"
    ],
    "Sports": [
        "club", "team", "fc", "sc", "league", "tournament", "stadium",
        "arena", "championship", "cup", "race", "grand prix",
        "clubs"
    ],
    "Politics / Law": [
        "government", "ministry", "court", "constitution", "policy",
        "election", "presidential", "parliament", "senate", "law",
        "legal", "case", "presidential election",
        "politics", "assembly", "treaty", "party"
    ],
    "Media / Technology": [
        "software", "protocol", "video game", "algorithm",
        "language", "operating system", "board game"
    ],
    "Biology / Scientific": [
        "virus", "bacteria", "species", "genus", "family", "order",
        "mammal", "bird", "fish", "fungus", "plant", "animal", "insect"
    ],
    "People / Roles": [
        "king", "queen", "prince", "emperor", "president", "minister",
        "lord", "sir", "judge", "politician",
        "artist", "actor", "actress", "singer", "writer", "author",
        "poet", "philosopher", "scientist", "musician",
        "composer", "director", "producer", "footballer",
        "basketball player", "baseball player", "coach",
        "businessman", "businesswoman",
        "people"
    ],
    "Mythology / Religion": [
        "mythology", "goddess", "god", "mythical", "religion",
        "sect", "liturgy"
    ],
    "Historical / Societal Concepts": [
        "clan", "dynasty", "empire", "kingdom", "tribe", "war",
        "battle", "front"
    ],
    "Awards / Recognition": [
        "award", "medal", "prize", "trophy"
    ],
    "Departments / Institutions / Other": [
        "department", "dialect", "military", "police", "prison"
    ]
}

# -------------------------------------------------------------
# 2) Arabic pattern detection
# -------------------------------------------------------------

NON_GEO_KEYWORDS_AR=[
    "جامعة", "كلية", "معهد", "نادي", "شركة", "مستشفى", "متحف",
    "جمعية", "فندق", "ملعب", "جسر", "قناة", "محطة", "مطار"
]

# -------------------------------------------------------------
# 3) Biological suffixes
# -------------------------------------------------------------

TAXON_SUFFIXES=(
    "aceae",
    "ales",
    "ineae",
    "phyta",
    "phyceae",
    "mycetes",
    "mycota",
    "formes",
    "idae",
    "inae",
    "oidea",
    "morpha",
    "cetes",
    "phycidae",
)


# -------------------------------------------------------------
# Detection Helpers
# -------------------------------------------------------------

def detect_english_keywords(label: str) -> bool:
    """Return True if English keyword matches exactly or by token."""
    lowered=label.lower()
    for name, keywords in NON_GEO_KEYWORDS_EN.items():
        for keyword in keywords:
            pattern=rf"\b{re.escape(keyword)}\b"
            if re.search(pattern, lowered):
                return True, name
    return False, ""


def detect_arabic_keywords(value: str) -> bool:
    """Return True if target Arabic keyword appears."""
    for keyword in NON_GEO_KEYWORDS_AR:
        if keyword in value:
            return True
    return False


def detect_taxon(label: str) -> bool:
    """Detect biological taxon names by suffix."""
    lowered=label.lower()
    return any(lowered.endswith(suffix) for suffix in TAXON_SUFFIXES)


def detect_person_like(label: str) -> bool:
    """Detect if label refers to persons/titles."""
    lowered=label.lower()
    # Heuristic: titles containing commas that denote roles (e.g., "king of", "queen of")
    roles=("king", "queen", "president", "chancellor", "minister", "lord", "sir", "prince")
    return any(re.search(rf"\b{role}\b", lowered) for role in roles)

# -------------------------------------------------------------
# Filtering Logic
# -------------------------------------------------------------


def classify_entries(entries: Dict[str, str]) -> Tuple[Dict[str, str], Dict[str, str]]:
    """Split entries into geographic and non-geographic."""
    geo = {}
    non_geo = {}
    typies = defaultdict(lambda: defaultdict(int))
    for key, value in entries.items():

        # Layer 1: English keyword detection
        isa, name = detect_english_keywords(key)
        if isa:
            non_geo[key] = value
            typies[name][key] = value

        # Layer 2: Arabic keyword detection
        elif detect_arabic_keywords(value):
            non_geo[key] = value
            typies["arabic"][key] = value

        # Layer 3: Biological taxon detection
        elif detect_taxon(key):
            non_geo[key] = value
            typies["taxons"][key] = value

        # Layer 4: Person role detection
        elif detect_person_like(key):
            non_geo[key] = value
            typies["persons"][key] = value
        else:
            geo[key] = value

    typies = dict(sorted(typies.items(), key=lambda item: len(item[1]), reverse=True))

    print(f"Total: {len(entries)} | Geographic: {len(geo)} | Non-Geographic: {len(non_geo)}")
    print(" - Detected\n\t| " + "\n\t| ".join([f" {k}: {len(v)}" for k, v in typies.items()]))

    return geo, typies


def filter_file(input_path: Path, geo_out: Path, non_geo_out: Path) -> None:
    """Read → classify → write outputs."""
    data=json.loads(input_path.read_text(encoding="utf-8"))
    geo, non_geo=classify_entries(data)

    # Write output files
    with open(geo_out, 'w', encoding='utf-8') as f:
        json.dump(geo, f, ensure_ascii=False, indent=4, sort_keys=True)

    with open(non_geo_out, 'w', encoding='utf-8') as f:
        json.dump(non_geo, f, ensure_ascii=False, indent=4, sort_keys=True)


def main() -> None:

    SOURCE_FILE=jsons_dir / "cities/yy2.json"
    NEW_FILE=jsons_dir / "cities/yy2_new.json"
    NON_GEO_FILE=jsons_dir / "cities/yy2_non_cities.json"
    filter_file(SOURCE_FILE, NEW_FILE, NON_GEO_FILE)

    SOURCE_FILE2=jsons_dir / "geography/P17_2_final_ll.json"
    NEW_FILE2=jsons_dir / "geography/P17_2_final_ll_new.json"
    NON_GEO_FILE2=jsons_dir / "geography/P17_2_final_ll_non_geographic.json"
    filter_file(SOURCE_FILE2, NEW_FILE2, NON_GEO_FILE2)


if __name__ == "__main__":
    main()
