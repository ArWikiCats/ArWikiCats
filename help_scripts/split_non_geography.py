from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Tuple

base_dir = Path(__file__).parent.parent
jsons_dir = base_dir / 'ArWikiCats' / 'translations' / 'jsons'


NON_GEO_KEYWORDS = {
    # Education
    "university", "college", "school", "academy", "institute", "faculty",

    # Medical
    "hospital", "clinic", "medical center",

    # Business
    "company", "corporation", "ltd", "inc", "limited", "enterprise", "brand",

    # Infrastructure
    "bridge", "tunnel", "airport", "station", "highway", "road", "railway", "canal", "pipeline", "dam",

    # Organizations
    "association", "organisation", "organization", "foundation", "society", "agency",

    # Culture
    "museum", "library", "gallery", "opera", "novel", "book", "film", "movie",
    "series", "episode", "soundtrack", "theater", "theatre", "poem", "play",

    # Sports
    "club", "team", "fc", "sc", "league", "tournament", "stadium", "arena",

    # Politics / Law
    "government", "ministry", "court", "constitution", "policy", "election",
    "presidential", "parliament", "senate",

    # Media / Technology
    "software", "protocol", "video game", "algorithm", "language",

    # Biology / Scientific
    "virus", "bacteria", "species", "genus", "family", "order", "mammal",
    "bird", "fish", "fungus", "plant",

    # People / Roles
    "king", "queen", "prince", "president", "minister", "lord", "sir",

}

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
    "phyceae",
    "phycidae",
)


def has_non_geo_keyword(label: str) -> bool:
    lowered = label.lower()
    for keyword in NON_GEO_KEYWORDS:
        pattern = rf"\b{re.escape(keyword)}\b"
        if re.search(pattern, lowered):
            return True
    return False


def looks_like_taxon(label: str) -> bool:
    lowered = label.lower()
    return any(lowered.endswith(suffix) for suffix in TAXON_SUFFIXES)


def looks_like_person(label: str) -> bool:
    lowered = label.lower()
    # Heuristic: titles containing commas that denote roles (e.g., "king of", "queen of")
    role_markers = ("king", "queen", "president", "chancellor", "minister", "lord", "sir")
    return any(re.search(rf"\b{marker}\b", lowered) for marker in role_markers)


def is_non_geographic(key: str, value: str) -> bool:
    # Arabic patterns in value

    if has_non_geo_keyword(key) or looks_like_taxon(key) or looks_like_person(key):
        return True

    arabic_patterns = [
        "جامعة", "كلية", "معهد", "نادي", "شركة", "مستشفى", "متحف",
        "جمعية", "فندق", "ملعب", "جسر", "قناة", "محطة", "مطار"
    ]

    for pattern in arabic_patterns:
        if pattern in value:
            return True

    return False


def classify_entries(entries: Dict[str, str]) -> Tuple[Dict[str, str], Dict[str, str]]:
    non_geo = {}
    geo = {}

    for key, value in entries.items():
        if is_non_geographic(key, value):
            non_geo[key] = value
        else:
            geo[key] = value
    return geo, non_geo


def filter_file(input_path: Path, geo_out: Path, non_geo_out: Path) -> None:
    """Read → classify → write outputs."""
    data = json.loads(input_path.read_text(encoding="utf-8"))
    geo, non_geo = classify_entries(data)

    # Write output files
    with open(geo_out, 'w', encoding='utf-8') as f:
        json.dump(geo, f, ensure_ascii=False, indent=4, sort_keys=True)

    with open(non_geo_out, 'w', encoding='utf-8') as f:
        json.dump(non_geo, f, ensure_ascii=False, indent=4, sort_keys=True)

    print(f"Total: {len(data)} | Geographic: {len(geo)} | Non-Geographic: {len(non_geo)}")


def main() -> None:

    SOURCE_FILE = jsons_dir / "cities/yy2.json"
    NEW_FILE = jsons_dir / "cities/yy2_new.json"
    NON_GEO_FILE = jsons_dir / "cities/yy2_non_cities.json"
    filter_file(SOURCE_FILE, NEW_FILE, NON_GEO_FILE)

    SOURCE_FILE2 = jsons_dir / "geography/P17_2_final_ll.json"
    NEW_FILE2 = jsons_dir / "geography/P17_2_final_ll_new.json"
    NON_GEO_FILE2 = jsons_dir / "geography/P17_2_final_ll_non_geographic.json"
    filter_file(SOURCE_FILE2, NEW_FILE2, NON_GEO_FILE2)


if __name__ == "__main__":
    main()
