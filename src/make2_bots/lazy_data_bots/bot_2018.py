#!/usr/bin/python3
"""
!
"""
import functools
from typing import Dict
from ...helps import len_print
from ...ma_lists import pop_All_2018_bot, find_teams_2025  # , teams_new_founder


@functools.lru_cache(maxsize=1)
def lazy_load() -> Dict[str, str]:
    return pop_All_2018_bot.load_pop_All_2018()


def Add_to_pop_All_18(tab: Dict[str, str]) -> None:
    pop_All_2018 = lazy_load()
    for key, lab in tab.items():
        pop_All_2018[key] = lab


@functools.lru_cache(maxsize=None)
def _get_pop_All_18(key: str, default: str = "") -> str:
    pop_All_2018 = lazy_load()
    result = pop_All_2018.get(key, default)
    return result


@functools.lru_cache(maxsize=None)
def get_pop_All_18(key: str, default: str = "") -> str:
    # ---
    result = _get_pop_All_18(key, default) or find_teams_2025(key, default)
    # ---
    return result


pop_All_2018 = {}  # 524266


len_print.data_len("make2_bots.matables_bots/bot_2018.py", {
    # "pop_All_2018" : 524266
    "pop_All_2018" : lazy_load()
})
