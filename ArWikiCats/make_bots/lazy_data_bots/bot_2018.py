#!/usr/bin/python3
"""
!
"""

import functools
from typing import Dict

from ...helps import len_print, logger
from ...translations import (
    open_json_file,
    Clubs_key_2,
    find_teams_2025,
    pop_final_5,
    Jobs_new,
    jobs_mens_data,
    New_P17_Finall,
    pf_keys2,
    sub_teams_new,
    By_table,
    SPORTS_KEYS_FOR_LABEL,
    films_mslslat_tab,
    olympics,
)


pop_All_2018 = open_json_file("population/pop_All_2018.json")  # 524266

first_data = {
    "by country": "حسب البلد",
    "in": "في",
    "films": "أفلام",
    "decades": "عقود",
    "women": "المرأة",
    "women in": "المرأة في",
    "medalists": "فائزون بميداليات",
    "gold medalists": "فائزون بميداليات ذهبية",
    "silver medalists": "فائزون بميداليات فضية",
    "bronze medalists": "فائزون بميداليات برونزية",
    "kingdom of": "مملكة",
    "kingdom-of": "مملكة",
    "country": "البلد",
}


@functools.lru_cache(maxsize=None)
def _get_pop_All_18(key: str, default: str = "") -> str:
    """Return the cached population label for the given key or a default."""
    result = pop_All_2018.get(key, default)
    return result


@functools.lru_cache(maxsize=10000)
def _get_from_alias(key: str) -> str:
    sources = {
        "pf_keys2": pf_keys2,
        "Jobs_new": Jobs_new,
        "jobs_mens_data": jobs_mens_data,
        "films_mslslat_tab": films_mslslat_tab,
        "By_table": By_table,
        "sub_teams_new": sub_teams_new,
        "New_P17_Finall": New_P17_Finall,
        "SPORTS_KEYS_FOR_LABEL": SPORTS_KEYS_FOR_LABEL,
    }
    for x, source in sources.items():
        if key in source or key.lower() in source:
            result = source.get(key) or source.get(key.lower())
            logger.debug(f"Found key in {x}: {key} -> {result}")
            return result or ""


@functools.lru_cache(maxsize=None)
def get_pop_All_18(key: str, default: str = "") -> str:
    """Fetch a population label, falling back to sports team lookups."""
    result = first_data.get(key.lower(), "") or olympics.get(key, "") or olympics.get(key.lower(), "")
    if result:
        return result

    call_ables = {
        "_get_pop_All_18": _get_pop_All_18,
        "_get_from_alias": _get_from_alias,
        "find_teams_2025": find_teams_2025,
    }

    for name, func in call_ables.items():
        result = func(key)
        if result:
            logger.debug(f"get_pop_All_18: Found key in {name}: {key} -> {result}")
            return result

    sources = {
        "Clubs_key_2": Clubs_key_2,
        "pop_final_5": pop_final_5,
    }
    for x, source in sources.items():
        result = source.get(key) or source.get(key.lower())
        if result:
            logger.debug(f"Found key in {x}: {key} -> {result}")
            return result

    return default


def Add_to_pop_All_18(tab: Dict[str, str]) -> None:
    """Merge additional mappings into the cached 2018 population data."""
    for key, lab in tab.items():
        pop_All_2018[key] = lab


len_print.data_len(
    "make_bots.matables_bots/bot_2018.py",
    {
        # "pop_All_2018" : 524266
        "pop_All_2018": pop_All_2018
    },
)
