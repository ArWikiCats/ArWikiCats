#!/usr/bin/python3
"""
!
"""

import functools
from typing import Dict

from ...helps import len_print
from ...translations import Clubs_key_2, find_teams_2025, pop_All_2018_bot, pop_final_5


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


@functools.lru_cache(maxsize=None)
def get_pop_All_18(key: str, default: str = "") -> str:
    """Fetch a population label, falling back to sports team lookups."""
    result = _get_pop_All_18(key, default) or find_teams_2025(key, default) or Clubs_key_2.get(key) or pop_final_5.get(key) or default
    return result


pop_All_2018 = {}  # 524266


len_print.data_len(
    "make2_bots.matables_bots/bot_2018.py",
    {
        # "pop_All_2018" : 524266
        "pop_All_2018": lazy_load()
    },
)
