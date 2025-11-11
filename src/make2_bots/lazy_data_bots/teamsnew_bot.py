#!/usr/bin/python3
"""
Usage:
"""
import functools
from typing import Dict
from ...helps import len_print
from ...ma_lists.sports_formats_2025.teams_new_data import load_teams_new


@functools.lru_cache(maxsize=1)
def lazy_load() -> Dict[str, str]:
    return load_teams_new()


@functools.lru_cache(maxsize=None)
def get_teams_new(key: str, default: str = "") -> str:
    data = lazy_load()
    return data.get(key, default)


len_print.data_len("make2_bots.matables_bots/teamsnew_bot.py", {
    "Teams_new" : lazy_load()
    # "Teams_new" : 352946
})

__all__ = [
    "get_teams_new"
]
