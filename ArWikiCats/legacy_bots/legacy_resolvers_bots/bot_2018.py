#!/usr/bin/python3
"""Bot module for population and label lookups from 2018 data.

This module provides functionality to look up Arabic labels for categories
using population data from 2018 and other mapping tables.
"""

import functools

from ...helps import getLogger
from ...new_resolvers import all_new_resolvers
from ...new_resolvers.bys_new import resolve_by_labels
from ...translations.funcs import _get_from_alias, open_json_file

logger = getLogger(__name__)

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
    Retrieve the Arabic label for a key from the in-memory 2018 population mapping.

    Parameters:
        key (str): Lookup key to search in the mapping.
        default (str): Value to return if the key is not present.

    Returns:
        str: The label mapped to `key`, or `default` if no mapping exists.
    """
    result = pop_All_2018.get(key, default)
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
        "resolve_by_labels": resolve_by_labels,
        "_get_from_alias": _get_from_alias,
    }

    for name, func in call_ables.items():
        result = func(key)
        if result:
            logger.debug(f"get_pop_All_18: Found key in {name}: {key} -> {result}")
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
