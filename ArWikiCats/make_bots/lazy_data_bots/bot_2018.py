#!/usr/bin/python3
"""
!
"""

import functools
from typing import Dict

from ...helps import len_print, logger
from ...translations import (
    Clubs_key_2,
    find_teams_2025,
    pop_All_2018_bot,
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


@functools.lru_cache(maxsize=None)
def get_pop_All_18(key: str, default: str = "") -> str:
    """Fetch a population label, falling back to sports team lookups."""

    result = _get_pop_All_18(key) or find_teams_2025(key)

    if not result:
        sources = {
            "Clubs_key_2": Clubs_key_2,
            "pop_final_5": pop_final_5,
            "olympics": olympics,
            "pf_keys2": pf_keys2,
            "SPORTS_KEYS_FOR_LABEL": SPORTS_KEYS_FOR_LABEL,
            "Jobs_new": Jobs_new,
            "jobs_mens_data": jobs_mens_data,
            "films_mslslat_tab": films_mslslat_tab,
            "By_table": By_table,
            "sub_teams_new": sub_teams_new,
            "New_P17_Finall": New_P17_Finall,
        }
        for x, source in sources.items():
            if key in source or key.lower() in source:
                result = source.get(key) or source.get(key.lower())
                logger.debug(f"Found key in {x}: {key} -> {result}")
                break

    return result or default


@functools.lru_cache(maxsize=1)
def lazy_load() -> Dict[str, str]:
    """Load the 2018 population dataset once and cache the result."""
    return pop_All_2018_bot.load_pop_All_2018()


def Add_to_pop_All_18(tab: Dict[str, str]) -> None:
    """Merge additional mappings into the cached 2018 population data."""
    pop_All_2018 = lazy_load()
    for key, lab in tab.items():
        pop_All_2018[key] = lab


@functools.lru_cache(maxsize=None)
def _get_pop_All_18(key: str, default: str = "") -> str:
    """Return the cached population label for the given key or a default."""
    pop_All_2018 = lazy_load()
    result = pop_All_2018.get(key, default)
    return result


pop_All_2018 = {}  # 524266


len_print.data_len(
    "make_bots.matables_bots/bot_2018.py",
    {
        # "pop_All_2018" : 524266
        "pop_All_2018": lazy_load()
    },
)
