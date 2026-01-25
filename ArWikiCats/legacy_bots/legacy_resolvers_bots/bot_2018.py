#!/usr/bin/python3
"""Bot module for population and label lookups from 2018 data.

This module provides functionality to look up Arabic labels for categories
using population data from 2018 and other mapping tables.
"""

import functools
from typing import Dict

from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...new_resolvers.bys_new import resolve_by_labels
from ...translations import (
    SPORTS_KEYS_FOR_LABEL,
    Clubs_key_2,
    Jobs_new,
    films_mslslat_tab,
    jobs_mens_data,
    pf_keys2,
    pop_final_5,
    sub_teams_new,
)
from ...translations.funcs import get_from_new_p17_final, open_json_file

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


@functools.lru_cache(maxsize=10000)
def _get_pop_All_18(key: str, default: str = "") -> str:
    """
    Lookup a population label in the cached 2018 dataset.

    Parameters:
        key (str): Lookup key to search in the in-memory 2018 population mapping.
        default (str): Value to return if `key` is not present.

    Returns:
        str: The label mapped to `key`, or `default` if no mapping exists.
    """
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


@functools.lru_cache(maxsize=10000)
def get_pop_all_18_wrap(key: str, default: str = "") -> str:
    """
    Resolve an Arabic population or category label for a given key using layered lookup sources.

    Parameters:
        key (str): Lookup key; a leading "the " is ignored.
        default (str): Value returned when no label is found.

    Returns:
        str: The found Arabic label, or `default` if no match is found.
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


@functools.lru_cache(maxsize=10000)
def get_pop_All_18(key: str, default: str = "") -> str:
    """
    Lookup an Arabic label for `key` using layered 2018 population and alias sources.

    If no label is found for `key` as given, the function retries once with hyphens replaced by spaces.

    Parameters:
        key (str): The lookup key or category name.
        default (str): Value to return when no label is found.

    Returns:
        str: The resolved label string if found, `default` otherwise.
    """
    result = get_pop_all_18_wrap(key, default)

    if not result and "-" in key:
        result = get_pop_all_18_wrap(key.replace("-", " "), default)

    return result


def Add_to_pop_All_18(tab: Dict[str, str]) -> None:
    """
    Add or update mappings in the cached 2018 population label table.

    Updates the module-level `pop_All_2018` dictionary in place by inserting all key→label pairs from `tab`. Existing keys are overwritten.

    Parameters:
        tab (Dict[str, str]): Mapping of keys to labels to merge into the cached population data.
    """
    for key, lab in tab.items():
        pop_All_2018[key] = lab
