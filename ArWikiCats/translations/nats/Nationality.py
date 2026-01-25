#!/usr/bin/python3
"""
Nationality system with full refactoring and full type hints.
All comments are in English only.
"""

from __future__ import annotations

from typing import Any, Dict

from ..helps import len_print
from ..data_builders.build_nationalities import (
    NationalityEntry,
    build_american_forms,
    build_lookup_tables,
    load_sources,
    normalize_aliases,
)
from ..utils import open_json_file

AllNatDict = Dict[str, NationalityEntry]
LookupTable = Dict[str, str]


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


# =====================================================================
# Main Execution (same logic as before)
# =====================================================================

raw_nats_as_en_key: Dict[str, Any] = open_json_file("nationalities/all_nat_as_en.json") or {}

raw_all_nat_o: AllNatDict = open_json_file("nationalities/nationalities_data.json") or {}
nat_directions_mapping: AllNatDict = open_json_file("nationalities/nationalities_data_with_directions.json") or {}

raw_uu_nats: AllNatDict = open_json_file("nationalities/sub_nats_with_ar_or_en.json") or {}
raw_sub_nat: AllNatDict = open_json_file("nationalities/sub_nats.json") or {}
continents: AllNatDict = open_json_file("nationalities/continents.json") or {}

nationalities_data: Dict[str, NationalityEntry] = load_sources(
    raw_all_nat_o,
    nat_directions_mapping,
    raw_uu_nats,
    raw_sub_nat,
    continents,
    raw_sub_nat_additional,
    countries_en_as_nationality_keys,
    raw_nats_as_en_key,
)


nationalities_data = normalize_aliases(nationalities_data, True)

All_Nat: AllNatDict = {k.lower(): v for k, v in nationalities_data.items()}

American_nat = build_american_forms(nationalities_data)
# All_Nat.update(American_nat)

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
