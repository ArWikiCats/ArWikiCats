"""

Usage:
from ...matables_bots.table1_bot import table1get, get_KAKO

"""
import functools
from typing import Dict
from ..lazy_data_bots.bot_2018 import pop_All_2018
from ...helps.print_bot import output_test
from .bot import Films_O_TT, players_new_keys

from .bot import All_P17
from ...ma_lists import (
    pf_keys2,
    Music_By_table,
    Films_key_man,
    By_table,
    Jobs_new,           # to be removed from players_new_keys
    jobs_mens_data,      # to be  removed from players_new_keys
)

KAKO: Dict[str, Dict[str, str]] = {
    "pf_keys2": pf_keys2,
    "pop_All_2018": pop_All_2018,
    "Music_By_table": Music_By_table,
    "Films_key_man": Films_key_man,
    "All_P17": All_P17,
    "By_table": By_table,
    "Films_O_TT": Films_O_TT,
    "players_new_keys": players_new_keys,
    "jobs_mens_data": jobs_mens_data,
    "Jobs_new": Jobs_new,
}


@functools.lru_cache(maxsize=None)
def get_KAKO(text: str) -> str:
    for table_name, table_data in KAKO.items():
        resolved_label = table_data.get(text, "")
        if resolved_label:
            output_test(f'>> get_KAKO_({table_name}) for ["{text}"] = "{resolved_label}"')
            return resolved_label
    return ""
