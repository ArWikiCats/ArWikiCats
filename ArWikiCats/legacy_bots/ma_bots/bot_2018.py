#!/usr/bin/python3
"""Bot module for population and label lookups from 2018 data.

This module provides functionality to look up Arabic labels for categories
using population data from 2018 and other mapping tables.
"""

import functools
from typing import Dict

from ...helps import len_print, logger
from ...new_resolvers import all_new_resolvers
from ...new_resolvers.bys_new import resolve_by_labels
from ...translations import (
    SPORTS_KEYS_FOR_LABEL,
    Clubs_key_2,
    Jobs_new,
    films_mslslat_tab,
    get_from_new_p17_final,
    jobs_mens_data,
    open_json_file,
    pf_keys2,
    pop_final_5,
    sub_teams_new,
)

pop_All_2018 = open_json_file("population/pop_All_2018.json")  # 524266

pop_All_2018.update(
    {
        "establishments": "تأسيسات",
        "disestablishments": "انحلالات",
    }
)

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
    """
    Retrieve an Arabic label for a key by probing multiple alias tables and fallback sources.

    Parameters:
        key (str): The lookup key; the function will try the original key and a lowercase variant.

    Returns:
        The label string if found, otherwise an empty string.
    """
    sources = {
        "pf_keys2": lambda k: pf_keys2.get(k),
        "Jobs_new": lambda k: Jobs_new.get(k),
        "jobs_mens_data": lambda k: jobs_mens_data.get(k),
        "films_mslslat_tab": lambda k: films_mslslat_tab.get(k),
        "resolve_by_labels": lambda k: resolve_by_labels(k),
        "sub_teams_new": lambda k: sub_teams_new.get(k),
    }

    for x, source in sources.items():
        result = source(key) or source(key.lower())
        if result:
            logger.debug(f"Found key in {x}: {key} -> {result}")
            return result

    result = get_from_new_p17_final(key.lower())

    if not result:
        result = SPORTS_KEYS_FOR_LABEL.get(key) or SPORTS_KEYS_FOR_LABEL.get(key.lower(), "")
    return result


@functools.lru_cache(maxsize=None)
def get_pop_All_18(key: str, default: str = "") -> str:
    """
    Lookup an Arabic population or category label for `key` using multiple fallback sources and return `default` if not found.

    Parameters:
        key (str): The lookup key; leading "the " is ignored when present.
        default (str): Value to return if no label is found.

    Returns:
        str: The found label if any, otherwise `default`.
    """
    result = first_data.get(key.lower(), "") or ""

    if result:
        return result

    if key.startswith("the "):
        key = key[len("the ") :]

    call_ables = {
        "all_new_resolvers": all_new_resolvers,
        "_get_pop_All_18": _get_pop_All_18,
        "_get_from_alias": _get_from_alias,
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
    """
    Add or update mappings in the cached 2018 population label table.

    Updates the module-level `pop_All_2018` dictionary in place by inserting all key→label pairs from `tab`. Existing keys are overwritten.

    Parameters:
        tab (Dict[str, str]): Mapping of keys to labels to merge into the cached population data.
    """
    for key, lab in tab.items():
        pop_All_2018[key] = lab


len_print.data_len(
    "make_bots.matables_bots/bot_2018.py",
    {
        # "pop_All_2018" : 524266
        "pop_All_2018": pop_All_2018
    },
)
