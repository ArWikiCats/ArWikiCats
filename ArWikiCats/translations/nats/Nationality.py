#!/usr/bin/python3
"""
Nationality system with full refactoring and full type hints.
All comments are in English only.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple, TypedDict

from ...helps import len_print
from ..utils.json_dir import open_json_file

regex_line = r"""
"male": "([^"]+)?",
\s+"males": "([^"]+)?",
\s+"female": "([^"]+)?",
\s+"females": "([^"]+)?",
\s+"the_male": "([^"]+)?",
\s+"the_female": "([^"]+)?",
\s+"en": "([^"]+)?",
\s+"ar": "([^"]+)?"

"male": "$1",
"males": "$2",
"female": "$3",
"females": "$4",
"the_male": "$5",
"the_female": "$6",
"en": "$7",
"ar": "$8"
"""
# =====================================================================
# Type aliases
# =====================================================================

countries_en_as_nationality_keys = [
    "antigua and barbuda",
    "botswana",
    "central african republic",
    "chinese taipei",
    "democratic republic of congo",
    "democratic-republic-of-congo",
    "dominican republic",
    "federated states of micronesia",
    "federated states-of micronesia",
    "georgia (country)",
    "hong kong",
    "ireland",
    "kiribati",
    "kyrgyz",
    "lesotho",
    "liechtenstein",
    "new zealand",
    "northern ireland",
    "republic of congo",
    "republic of ireland",
    "republic-of ireland",
    "republic-of-congo",
    "são toméan",
    "trinidad and tobago",
    "turkmen",
    "turkmenistan",
    "uzbek",
    "vatican",
    "west india",
]


class NationalityEntry(TypedDict):
    """Represents one nationality block with all fields always present as strings."""

    male: str
    males: str
    female: str
    females: str
    the_male: str
    the_female: str
    en: str
    ar: str


AllNatDict = Dict[str, NationalityEntry]
LookupTable = Dict[str, str]


def build_nationality_structure(val):
    return {
        "male": val.get("male", ""),
        "males": val.get("males", ""),
        "female": val.get("female", ""),
        "females": val.get("females", ""),
        "the_female": val.get("the_female", ""),
        "the_male": val.get("the_male", ""),
        "en": val.get("en", ""),
        "ar": val.get("ar", ""),
    }


# =====================================================================
# Section 1: Load and prepare JSON sources
# =====================================================================


raw_sub_nat_additional_to_check = {
    "muslims": {
        "male": "مسلم",
        "males": "مسلمون",
        "female": "مسلمة",
        "females": "مسلمات",
        "the_male": "المسلم",
        "the_female": "المسلمة",
        "en": "",
        "ar": "الإسلام",
    },
    "muslim": {
        "male": "مسلم",
        "males": "مسلمون",
        "female": "مسلمة",
        "females": "مسلمات",
        "the_male": "المسلم",
        "the_female": "المسلمة",
        "en": "muslims",
        "ar": "الإسلام",
    },
}

raw_sub_nat_additional = {
    "jews": {
        "male": "يهودي",
        "males": "يهود",
        "female": "يهودية",
        "females": "يهوديات",
        "the_male": "اليهودي",
        "the_female": "اليهودية",
        "en": "",
        "ar": "اليهودية",
    },
    "sufi": {
        "male": "صوفي",
        "males": "صوفيون",
        "female": "صوفية",
        "females": "صوفيات",
        "the_male": "الصوفي",
        "the_female": "الصوفية",
        "en": "",
        "ar": "الصوفية",
    },
    "christian": {
        "male": "مسيحي",
        "males": "مسيحيون",
        "female": "مسيحية",
        "females": "مسيحيات",
        "the_male": "المسيحي",
        "the_female": "المسيحية",
        "en": "",
        "ar": "المسيحية",
    },
}


def load_sources(
    raw_nats_as_en_key: Dict[str, Dict[str, str]] | None = None,
) -> Dict[str, NationalityEntry]:
    """
    Load nationality JSON data and merge nationalities_data + sub_nats.
    Ensures all entries follow the NationalityEntry structure (string values only).

    """
    data_to_review = {
        "people from jerusalem": {
            "male": "مقدسي",
            "males": "مقدسيون",
            "female": "مقدسية",
            "females": "مقدسيات",
            "en": "jerusalem",
            "ar": "القدس",
            "the_female": "المقدسية",
            "the_male": "المقدسي",
        },
    }

    raw_all_nat_o: AllNatDict = open_json_file("nationalities/nationalities_data.json") or {}
    nationality_directions_mapping: AllNatDict = (
        open_json_file("nationalities/nationalities_data_with_directions.json") or {}
    )

    raw_uu_nats: AllNatDict = open_json_file("nationalities/sub_nats_with_ar_or_en.json") or {}
    raw_sub_nat: AllNatDict = open_json_file("nationalities/sub_nats.json") or {}
    continents: AllNatDict = open_json_file("nationalities/continents.json") or {}

    raw_all_nat_o.update(nationality_directions_mapping)

    if raw_nats_as_en_key:
        raw_all_nat_o.update(build_en_nat_entries(raw_nats_as_en_key))
        raw_all_nat_o.update(raw_nats_as_en_key)

    data = {}

    # Merge JSONs into nationalities_data
    data.update(raw_uu_nats)

    data.update(raw_sub_nat)
    data.update(continents)
    data.update(raw_sub_nat_additional)
    # for key, val in raw_sub_nat.items(): raw_all_nat_o[key] = val

    data.update(raw_all_nat_o)

    # Convert everything to NationalityEntry ensuring all fields exist
    normalized: Dict[str, NationalityEntry] = {}

    for key, val in data.items():
        # Build guaranteed structure
        val = val if isinstance(val, dict) else {}
        entry: NationalityEntry = build_nationality_structure(val)
        normalized[key] = entry

        # Special cases like "Category:Antigua and Barbuda writers" which use country names as nationalities
        en_key = entry["en"].lower()
        if en_key in countries_en_as_nationality_keys and en_key != key.lower():
            normalized[en_key] = entry

    return normalized


def build_en_nat_entries(raw_data: AllNatDict) -> AllNatDict:
    data: AllNatDict = {}
    if not raw_data:
        return {}
    for _, v in raw_data.items():
        if v.get("en_nat"):
            data[v["en_nat"]] = build_nationality_structure(v)

    return data


# =====================================================================
# Section 2: Normalize aliases
# =====================================================================


def normalize_aliases(all_nat_o: Dict[str, NationalityEntry], _print=False) -> Dict[str, NationalityEntry]:
    """
    Apply alias equivalence and one-off corrections.
    Ensures the resulting dictionary keys all map to NationalityEntry.
    """

    alias_map: Dict[str, str] = {
        "turkish cypriot": "northern cypriot",
        "luxembourg": "luxembourgish",
        "ancient romans": "ancient-romans",
        "ancient-roman": "ancient-romans",
        "arabian": "arab",
        "argentinean": "argentine",
        "argentinian": "argentine",
        "austro-hungarian": "austrianhungarian",
        "bangladesh": "bangladeshi",
        "barbadian_2": "barbadian",
        "belizian": "belizean",
        "bosnia and herzegovina": "bosnian",
        "burkinabé": "burkinabe",
        "burkinese": "burkinabe",
        "canadians": "canadian",
        "caribbean": "caribbeans",
        "comoran": "comorian",
        "democratic-republic-of-congo": "democratic republic of congo",
        "dominican republic": "dominican republic",
        "republic of congo": "republic of congo",
        "republic-of ireland": "irish",
        "republic-of-congo": "republic of congo",
        "emiri": "emirati",
        "emirian": "emirati",
        "equatorial guinean": "equatoguinean",
        "ivoirian": "ivorian",
        "kosovar": "kosovan",
        "lao": "laotian",
        "monacan": "monegasque",
        "monégasque": "monegasque",
        "mosotho": "lesotho",
        "nepali": "nepalese",
        "roman": "romanian",
        "russians": "russian",
        "salvadoran": "salvadorean",
        "saudi": "saudiarabian",
        "singapore": "singaporean",
        "slovakian": "slovak",
        "slovene": "slovenian",
        "somali": "somalian",
        "south ossetian": "ossetian",
        "trinidadian": "trinidad and tobago",
        "trinidadians": "trinidad and tobago",
        "vietnamesei": "vietnamese",
        "yemenite": "yemeni",
        "jewish": "jews",
        "native american": "native americans",
    }

    # Apply simple alias redirection
    for alias, target in alias_map.items():
        if alias == target:
            continue  # skip self-aliases

        if target in all_nat_o:
            all_nat_o[alias] = build_nationality_structure(all_nat_o[target])
        else:
            if _print:
                print(f"Alias({alias}) target ({target}) not found in nationality data")

    # NOTE: "papua new guinean" has same values as "guinean"
    all_nat_o["papua new guinean x"] = {
        "male": "غيني",
        "males": "غينيون",
        "female": "غينية",
        "females": "غينيات",
        "the_male": "الغيني",
        "the_female": "الغينية",
        "en": "papua new guinea",
        "ar": "بابوا غينيا الجديدة",
    }

    # Handle Georgia (country)
    if "georgian" in all_nat_o:
        all_nat_o["georgia (country)"] = build_nationality_structure(all_nat_o["georgian"])
        all_nat_o["georgia (country)"]["en"] = "georgia (country)"

    return all_nat_o


# =====================================================================
# Section 3: Build American forms
# =====================================================================


def build_american_forms(all_nat_o: Dict[str, NationalityEntry]) -> AllNatDict:
    """
    Build '-american' and 'x american' nationality forms.
    Returns: (updated_all_nat, count_of_added_items)
    """

    American_nat = {}

    for nat_key, entry in all_nat_o.items():
        male = entry["male"]
        males = entry["males"]
        female, females = entry["female"], entry["females"]

        if not any([male, males, female, females]):
            continue  # skip if no gender fields present

        the_female, the_male = entry.get("the_female", ""), entry.get("the_male", "")

        new_entry: NationalityEntry = {
            "male": f"أمريكي {male}" if male else "",
            "males": f"أمريكيون {males}" if males else "",
            "female": f"أمريكية {female}" if female else "",
            "females": f"أمريكيات {females}" if females else "",
            "en": "",
            "ar": "",
            "the_female": f"الأمريكية {the_female}" if the_female else "",
            "the_male": f"الأمريكي {the_male}" if the_male else "",
        }

        key_lower = nat_key.lower()
        American_nat[f"{key_lower}-american"] = new_entry

        # Special case
        if key_lower == "jewish":
            American_nat[f"{key_lower} american"] = new_entry

    return American_nat


# =====================================================================
# Section 4: Build lookup tables
# =====================================================================


def build_lookup_tables(all_nat: AllNatDict) -> Dict[str, Any]:
    """
    Build all nationality lookup tables used throughout the system.
    """

    Nat_men: LookupTable = {}
    Nat_mens: LookupTable = {}
    Nat_women: LookupTable = {}
    Nat_Womens: LookupTable = {}

    Nat_the_female: LookupTable = {}
    Nat_the_male: LookupTable = {}

    ar_Nat_men: LookupTable = {}
    countries_from_nat: LookupTable = {}

    all_country_ar: LookupTable = {}
    all_country_with_nat: AllNatDict = {}
    all_country_with_nat_ar: AllNatDict = {}
    countries_nat_en_key: Dict[str, NationalityEntry] = {}
    en_nats_to_ar_label: LookupTable = {}

    for nat_key, entry in all_nat.items():
        en: str = entry["en"].lower()
        ar: str = entry["ar"]
        en_norm: str = en[4:] if en.startswith("the ") else en

        if entry.get("male"):
            Nat_men[nat_key] = entry["male"]
            ar_Nat_men[entry["male"]] = nat_key

        if entry.get("males"):
            Nat_mens[nat_key] = entry["males"]

        if entry.get("female"):
            Nat_women[nat_key] = entry["female"]

        if entry.get("females"):
            Nat_Womens[nat_key] = entry["females"]

        if entry.get("the_female"):
            Nat_the_female[nat_key] = entry["the_female"]

        if entry.get("the_male"):
            Nat_the_male[nat_key] = entry["the_male"]

        # English → Arabic country mapping
        if en and ar:
            all_country_ar[en_norm] = ar
            countries_from_nat[en_norm] = ar

            if en_norm.startswith("the "):
                countries_from_nat[en_norm[4:]] = ar

        # Full nationality entry mapping
        if ar:
            all_country_with_nat_ar[nat_key] = entry
            en_nats_to_ar_label[nat_key] = ar

        if en:
            all_country_with_nat[nat_key] = entry
            countries_nat_en_key[en_norm] = entry

    # Special case: Iran
    if "iranian" in all_nat:
        countries_nat_en_key["islamic republic of iran"] = all_nat["iranian"]

    countries_from_nat.update(
        {
            "serbia and montenegro": "صربيا والجبل الأسود",
            "serbia-and-montenegro": "صربيا والجبل الأسود",
        }
    )

    return {
        "Nat_men": Nat_men,
        "Nat_mens": Nat_mens,
        "Nat_women": Nat_women,
        "Nat_Womens": Nat_Womens,
        "ar_Nat_men": ar_Nat_men,
        "countries_from_nat": countries_from_nat,
        "all_country_ar": all_country_ar,
        "all_country_with_nat": all_country_with_nat,
        "all_country_with_nat_ar": all_country_with_nat_ar,
        "countries_nat_en_key": countries_nat_en_key,
        "en_nats_to_ar_label": en_nats_to_ar_label,
        "Nat_the_male": Nat_the_male,
        "Nat_the_female": Nat_the_female,
    }


# =====================================================================
# Main Execution (same logic as before)
# =====================================================================

raw_nats_as_en_key: Dict[str, Any] = open_json_file("nationalities/all_nat_as_en.json") or {}

nationalities_data: Dict[str, NationalityEntry] = load_sources(raw_nats_as_en_key)

nationalities_data = normalize_aliases(nationalities_data, True)

All_Nat: AllNatDict = {k.lower(): v for k, v in nationalities_data.items()}

American_nat = build_american_forms(nationalities_data)
All_Nat.update(American_nat)
result_tables = build_lookup_tables(All_Nat)

Nat_men: LookupTable = result_tables["Nat_men"]
Nat_mens: LookupTable = result_tables["Nat_mens"]
Nat_women: LookupTable = result_tables["Nat_women"]
Nat_Womens: LookupTable = result_tables["Nat_Womens"]

Nat_the_male: LookupTable = result_tables["Nat_the_male"]
Nat_the_female: LookupTable = result_tables["Nat_the_female"]

ar_Nat_men: LookupTable = result_tables["ar_Nat_men"]
countries_from_nat: LookupTable = result_tables["countries_from_nat"]
all_country_ar: LookupTable = result_tables["all_country_ar"]

all_country_with_nat: AllNatDict = result_tables["all_country_with_nat"]
all_country_with_nat_ar: AllNatDict = result_tables["all_country_with_nat_ar"]
countries_nat_en_key: Dict[str, NationalityEntry] = result_tables["countries_nat_en_key"]

en_nats_to_ar_label: LookupTable = result_tables["en_nats_to_ar_label"]

nats_to_add = {}

all_nat_sorted = dict(
    sorted(
        All_Nat.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)

len_result = {
    "raw_nats_as_en_key": 17,
    "ar_Nat_men": 711,
    "Nat_men": 841,
    "Nat_mens": 843,
    "Nat_women": 843,
    "Nat_Womens": 843,
    "All_Nat": 843,
    "Nat_the_male": 843,
    "Nat_the_female": 843,
    "all_country_ar": 285,
    "countries_from_nat": 287,
    "all_country_with_nat_ar": 342,
    "en_nats_to_ar_label": 342,
    "all_country_with_nat": 336,
    "American_nat": 422,
    "countries_nat_en_key": 286,
}
len_print.data_len(
    "nationality.py",
    {
        "raw_nats_as_en_key": raw_nats_as_en_key,
        "ar_Nat_men": ar_Nat_men,
        "Nat_men": Nat_men,
        "Nat_mens": Nat_mens,
        "Nat_women": Nat_women,
        "Nat_Womens": Nat_Womens,
        "all_country_ar": all_country_ar,
        "countries_from_nat": countries_from_nat,
        "All_Nat": All_Nat,
        "all_country_with_nat_ar": all_country_with_nat_ar,
        "all_country_with_nat": all_country_with_nat,
        "American_nat": American_nat,
        "countries_nat_en_key": countries_nat_en_key,
        "en_nats_to_ar_label": en_nats_to_ar_label,
        "Nat_the_male": Nat_the_male,
        "Nat_the_female": Nat_the_female,
    },
)
