"""

Usage:
from ...matables_bots.table1_bot import table1get, get_KAKO

"""

import functools
from typing import Dict

from ...helps.log import logger
from ...translations import Jobs_new  # to be removed from players_new_keys
from ...translations import jobs_mens_data  # to be  removed from players_new_keys
from ...translations import (
    By_table,
    Films_key_man,
    Music_By_table,
    pf_keys2,
)
from ..lazy_data_bots.bot_2018 import pop_All_2018
from .bot import All_P17, Films_O_TT, players_new_keys

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


from ...helps.jsonl_dump import dump_data


# @dump_data()
@functools.lru_cache(maxsize=None)
def get_KAKO(text: str) -> str:
    """Look up the Arabic label for a term across several mapping tables."""
    for table_name, table_data in KAKO.items():
        resolved_label = table_data.get(text, "")
        if not resolved_label:
            continue

        # If not a string → also an error
        if not isinstance(resolved_label, str):
            raise TypeError(f"Resolver '{table_name}' returned non-string type {type(resolved_label)}: {resolved_label}")

        logger.debug(f'>> get_KAKO_({table_name}) for ["{text}"] = "{resolved_label}"')

        return resolved_label

    return ""
