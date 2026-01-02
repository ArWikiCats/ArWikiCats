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
from collections import defaultdict
from pathlib import Path
from typing import Dict, Tuple

base_dir = Path(__file__).parent.parent
jsons_dir = base_dir / "ArWikiCats" / "translations" / "jsons"


# -------------------------------------------------------------
# 1) Robust Keyword Sets (merged + expanded)
# -------------------------------------------------------------
CHECK_AR_ALSO = {
    "park": "بارك",
    "bridge": "بريدج",
}

NON_GEO_KEYWORDS_EN = {
    "education": ["university", "college", "school", "academy", "institute", "faculty", "journal"],
    "medical": ["hospital", "clinic", "medical center"],
    "business": [
        "company",
        "corporation",
        "ltd",
        "inc",
        "limited",
        "enterprise",
        "brand",
        "product",
        "bank",
        "airlines",
        "airways",
        "restaurant",
        "hotel",
    ],
    "Infrastructure": [
        "bridge",
        "tunnel",
        "airport",
        "station",
        "highway",
        "road",
        "railway",
        "canal",
        "pipeline",
        "dam",
        "dike",
        "circuit",
        "center",
        "centre",
        "park",
        "garden",
        "zoo",
    ],
    "religious_cultural_buildings": ["church", "cathedral", "mosque", "temple", "synagogue", "abbey", "monastery"],
    "organizations": [
        "association",
        "organisation",
        "organization",
        "foundation",
        "society",
        "agency",
        "council",
        "union",
        "movement",
    ],
    "military": [
        "army",
        "navy",
        "air force",
        "battalion",
        "regiment",
        "squadron",
    ],
    "Tv": ["film", "tv series", "tv show", "television", "channel", "episode", "series", "movie"],
    "culture_media": [
        "museum",
        "library",
        "gallery",
        "opera",
        "novel",
        "book",
        "movie",
        "season",
        "soundtrack",
        "theater",
        "theatre",
        "poem",
        "play",
        "album",
        "song",
        "single",
        "ballet",
        "musical",
        "magazine",
        "newspaper",
        "script",
        "studios",
        "music",
        "festival",
        "band",
    ],
    "sports": [
        "club",
        "team",
        "fc",
        "sc",
        "league",
        "tournament",
        "stadium",
        "arena",
        "championship",
        "cup",
        "race",
        "grand prix",
        "clubs",
        "f.c.",
        "نادي",
    ],
    "politics_law": [
        "government",
        "ministry",
        "court",
        "constitution",
        "policy",
        "election",
        "presidential",
        "parliament",
        "senate",
        "law",
        "legal",
        "case",
        "presidential election",
        "politics",
        "assembly",
        "treaty",
        "party",
    ],
    "media_technology": [
        "software",
        "protocol",
        "video game",
        "algorithm",
        "programming language",
        "operating system",
        "board game",
    ],
    "biology_scientific": [
        "virus",
        "bacteria",
        "species",
        "genus",
        "family",
        "order",
        "mammal",
        "bird",
        "fish",
        "fungus",
        "plant",
        "animal",
        "insect",
    ],
    "roles_people": [
        "king",
        "queen",
        "prince",
        "emperor",
        "president",
        "minister",
        "lord",
        "sir",
        "judge",
        "politician",
        "artist",
        "actor",
        "actress",
        "singer",
        "writer",
        "author",
        "poet",
        "philosopher",
        "scientist",
        "musician",
        "composer",
        "director",
        "producer",
        "footballer",
        "basketball player",
        "baseball player",
        "coach",
        "businessman",
        "businesswoman",
        "people",
    ],
    "mythology_religion": ["mythology", "goddess", "god", "mythical", "religion", "sect", "liturgy"],
    "historical_societal": [
        # "clan", "empire", "kingdom",
        "tribe",
        "war",
        "battle",
        "front",
    ],
    # "dynasty": [ "dynasty" ],
    "languages": ["language"],
    "awards": ["award", "medal", "prize", "trophy"],
    "institutions_other": ["department", "dialect", "police", "prison"],
    "others": [
        "history of",
        "culture of",
        "economy of",
        "demographics of",
        "transport in",
        "infrastructure of",
        "tourism in",
    ],
}

# -------------------------------------------------------------
# 2) Arabic pattern detection
# -------------------------------------------------------------

NON_GEO_KEYWORDS_AR = [
    "جامعة",
    "كلية",
    "معهد",
    "نادي",
    "شركة",
    "مستشفى",
    "متحف",
    "جمعية",
    "فندق",
    "ملعب",
    "جسر",
    "قناة",
    "محطة",
    "مطار",
]

# -------------------------------------------------------------
# 3) Biological suffixes
# -------------------------------------------------------------

TAXON_SUFFIXES = (
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


def detect_english_keywords(label: str, value: str) -> bool:
    """Return True if English keyword matches exactly or by token."""
    lowered = label.lower()
    for name, keywords in NON_GEO_KEYWORDS_EN.items():
        for keyword in keywords:
            # ----
            ar_word = CHECK_AR_ALSO.get(keyword)
            # ----
            # pattern = rf"\b{re.escape(keyword)}\b"
            pattern = rf"(?<!\w){re.escape(keyword)}(?!\w)"
            # ---
            if not re.search(pattern, lowered) and not re.search(pattern, value):
                continue
            # ---
            if not ar_word:
                return True, name
            # ---
            if ar_word:
                # ar_pattern = rf"\b{re.escape(ar_word)}\b"
                ar_pattern = rf"(?<!\w){re.escape(ar_word)}(?!\w)"

                if re.search(ar_pattern, value):
                    return False, ""
            # ---
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
    lowered = label.lower()
    return any(lowered.endswith(suffix) for suffix in TAXON_SUFFIXES)


def detect_person_like(label: str) -> bool:
    """Detect if label refers to persons/titles."""
    lowered = label.lower()
    # Heuristic: titles containing commas that denote roles (e.g., "king of", "queen of")
    roles = ("king", "queen", "president", "chancellor", "minister", "lord", "sir", "prince")
    return any(
        re.search(
            # rf"\b{role}\b",
            rf"(?<!\w){role}(?!\w)",
            lowered,
        )
        for role in roles
    )


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
        isa, name = detect_english_keywords(key, value)
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

    print(" - Detected\n\t| " + "\n\t| ".join([f" {k}: {len(v)}" for k, v in typies.items()]))

    return geo, typies


def filter_file(input_path: Path, geo_out: Path, non_geo_out: Path) -> str:
    """Read → classify → write outputs."""
    data = json.loads(input_path.read_text(encoding="utf-8"))
    geo, non_geo = classify_entries(data)
    non = len(data) - len(geo)
    if non:
        # Write output files
        with open(geo_out, "w", encoding="utf-8") as f:
            json.dump(geo, f, ensure_ascii=False, indent=4, sort_keys=True)

        with open(non_geo_out, "w", encoding="utf-8") as f:
            json.dump(non_geo, f, ensure_ascii=False, indent=4, sort_keys=True)

    return f"Total: {len(data):,} | Geographic: {len(geo):,} | Non-Geographic: {non:,}"


def main() -> None:
    files = [
        # jsons_dir / "geography/P17_2_final_ll.json",
        # jsons_dir / "cities/cities_full.json",
        # jsons_dir / "cities/yy2.json",
        # jsons_dir / "geography/popopo.json",
        jsons_dir
        / "geography/P17_PP.json",
    ]
    status = {}
    for file in files:
        print(f"Processing file: {file}")
        new_path = file.parent.parent / f"{file.parent.name}_new"
        new_path.mkdir(parents=True, exist_ok=True)

        NEW_FILE = new_path / file.name
        NON_GEO_FILE = new_path / f"{file.stem}_non.json"

        stat = filter_file(file, NEW_FILE, NON_GEO_FILE)
        status[file.name] = stat
    # ---
    for fname, stat in status.items():
        print(f"{fname} => {stat}")
    # ---
    print("Processing complete.")


if __name__ == "__main__":
    main()
