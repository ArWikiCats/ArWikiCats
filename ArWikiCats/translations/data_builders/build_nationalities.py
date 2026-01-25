#!/usr/bin/python3
"""
Nationality system with full refactoring and full type hints.
All comments are in English only.
"""

from __future__ import annotations

from typing import Any, Dict, List, TypedDict


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
    """
    Constructs a complete NationalityEntry mapping, ensuring all expected fields are present as strings.

    Parameters:
        val (Mapping[str, str]): Input mapping that may contain any subset of nationality fields.

    Returns:
        dict: A mapping with keys "male", "males", "female", "females", "the_female", "the_male", "en", and "ar"; each value is the corresponding string from `val` or an empty string if missing.
    """
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


def load_sources(
    raw_all_nat_o: AllNatDict,
    nationality_directions_mapping: AllNatDict,
    raw_uu_nats: AllNatDict,
    raw_sub_nat: AllNatDict,
    continents: AllNatDict,
    raw_sub_nat_additional: Dict[str, Dict[str, str]],
    countries_en_as_nationality_keys: List[str],
    raw_nats_as_en_key: Dict[str, Dict[str, str]] | None = None,
) -> Dict[str, NationalityEntry]:
    """
    Merge and normalize multiple nationality data sources into a consistent mapping of nationality keys to NationalityEntry objects.

    Parameters:
        raw_all_nat_o: Primary nationality entries keyed by identifier.
        nationality_directions_mapping: Additional nationality entries to merge into raw_all_nat_o.
        raw_uu_nats: United Nations or other global-sourced nationality entries to include.
        raw_sub_nat: Sub-national or regional nationality entries to include.
        continents: Continent-level entries to include.
        raw_sub_nat_additional: Extra sub-national entries (raw dict form) to include.
        countries_en_as_nationality_keys: List of English country names that should also be usable as nationality keys; when an entry's `en` lowercased matches a value here, an alias key is added.
        raw_nats_as_en_key: Optional raw entries where each entry's English-native name should be used as an additional key; when provided, entries built via build_en_nat_entries(raw_nats_as_en_key) and raw_nats_as_en_key are merged into the sources.

    Returns:
        Dict[str, NationalityEntry]: A normalized mapping where each key maps to a NationalityEntry with all fields present as strings. Entries whose `en` value matches an item in countries_en_as_nationality_keys will also be available under that English name (lowercased) as an alias.
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
    """
    Build a dictionary of nationality entries keyed by each entry's `en_nat` value.

    Parameters:
        raw_data (AllNatDict): Source mapping of nationality records; entries missing `en_nat` are ignored.

    Returns:
        AllNatDict: A mapping where each key is an entry's `en_nat` string and each value is a complete NationalityEntry. If `raw_data` is empty or contains no `en_nat` values, an empty dict is returned.
    """
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
    Add alias keys and apply one-off nationality corrections to the provided nationality mapping.

    Parameters:
        all_nat_o (Dict[str, NationalityEntry]): Mapping of nationality keys to NationalityEntry objects to augment.
        _print (bool): If True, print a diagnostic when an alias target is missing.

    Returns:
        Dict[str, NationalityEntry]: The input mapping augmented with alias keys and special-case entries.
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
    all_nat_o["papua_new_guinean!"] = {
        "male": "",  # غيني
        "males": "",  # غينيون
        "female": "",  # غينية
        "females": "",  # غينيات
        "the_male": "",  # الغيني
        "the_female": "",  # الغينية
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
    Create American-form nationality variants for entries that define gendered forms.

    Generates new NationalityEntry objects where Arabic gendered forms are prefixed with the Arabic adjectives for "American" and returns a mapping from new keys to those entries. For each input key X that has any of `male`, `males`, `female`, or `females`, a new entry is produced under the key "x-american" (lowercased). The special input key "jewish" also receives an additional alias "jewish american".

    Parameters:
        all_nat_o (Dict[str, NationalityEntry]): Mapping of existing nationality keys to their entries.

    Returns:
        AllNatDict: Mapping of generated keys to NationalityEntry objects. Each generated entry has:
            - Arabic gendered fields (`male`, `males`, `female`, `females`) prefixed with the appropriate Arabic word for "American" when the original field was present, otherwise empty strings.
            - `the_male` / `the_female` likewise prefixed when present.
            - `en` and `ar` left as empty strings.
    """

    data = {}

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
        data[f"{key_lower}-american"] = new_entry

        # Special case
        if key_lower == "jewish":
            data[f"{key_lower} american"] = new_entry

    return data


# =====================================================================
# Section 4: Build lookup tables
# =====================================================================


def build_lookup_tables(all_nat: AllNatDict) -> Dict[str, Any]:
    """
    Constructs lookup tables that map nationality keys and name variants to Arabic labels and full NationalityEntry records.

    Builds and returns a collection of tables including masculine/feminine forms, definite-form variants, English→Arabic country name mappings, and maps from nationality keys or normalized English names to NationalityEntry objects.

    Parameters:
        all_nat (AllNatDict): Mapping of nationality keys to NationalityEntry objects to index.

    Returns:
        Dict[str, Any]: A dictionary of lookup tables with the following keys:
            - "Nat_men": maps nat_key -> male form (Arabic string).
            - "Nat_mens": maps nat_key -> plural male form (Arabic string).
            - "Nat_women": maps nat_key -> female form (Arabic string).
            - "Nat_Womens": maps nat_key -> plural female form (Arabic string).
            - "ar_Nat_men": maps male Arabic form -> nat_key.
            - "countries_from_nat": maps normalized English country name -> Arabic country label.
            - "all_country_ar": maps normalized English country name -> Arabic country label (same as countries_from_nat for entries discovered).
            - "all_country_with_nat": maps nat_key -> full NationalityEntry for entries that include an English name.
            - "all_country_with_nat_ar": maps nat_key -> full NationalityEntry for entries that include an Arabic label.
            - "countries_nat_en_key": maps normalized English country name -> NationalityEntry.
            - "en_nats_to_ar_label": maps nat_key -> Arabic label (string).
            - "Nat_the_male": maps nat_key -> definite male form (Arabic string).
            - "Nat_the_female": maps nat_key -> definite female form (Arabic string).
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


__all__ = [
    "load_sources",
    "NationalityEntry",
    "build_american_forms",
    "build_lookup_tables",
    "normalize_aliases",
]
