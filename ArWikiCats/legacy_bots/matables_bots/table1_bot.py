"""

Usage:
from ...matables_bots.table1_bot import table1get, get_KAKO

"""

import functools
from typing import Dict

from ...helps import logger
from ...helps.jsonl_dump import dump_data
from ...new_resolvers.bys_new import resolve_by_labels
from ...translations import Jobs_new  # to be removed from players_new_keys
from ...translations import jobs_mens_data  # to be  removed from players_new_keys
from ...translations import (
    Films_key_man,
)
from ..make_bots.bot_2018 import pop_All_2018
from .bot import All_P17, Films_O_TT, players_new_keys

KAKO: Dict[str, Dict[str, str]] = {
    "pop_All_2018": pop_All_2018,  # 161
    "Films_key_man": Films_key_man,  # 74
    "All_P17": All_P17,  # 0
    "Films_O_TT": Films_O_TT,  # 0
    "players_new_keys": players_new_keys,  # 1,719
    "jobs_mens_data": jobs_mens_data,  # 96,552
    "Jobs_new": Jobs_new,  # 1,304
}


@functools.lru_cache(maxsize=None)
# @dump_data(1)
def _get_KAKO(text: str) -> str:
    """Look up the Arabic label for a term across several mapping tables."""
    resolved_label = resolve_by_labels(text)
    if resolved_label:
        return "resolve_by_labels", resolved_label

    for table_name, table_data in KAKO.items():
        resolved_label = table_data.get(text, "")
        if not resolved_label:
            continue

        # If not a string → also an error
        if not isinstance(resolved_label, str):
            raise TypeError(
                f"Resolver '{table_name}' returned non-string type {type(resolved_label)}: {resolved_label}"
            )

        logger.debug(f'>> get_KAKO_({table_name}) for ["{text}"] = "{resolved_label}"')

        return table_name, resolved_label

    return "", ""


@functools.lru_cache(maxsize=10000)
def get_KAKO(text: str) -> str:
    _, label = _get_KAKO(text)
    return label


__all__ = [
    "get_KAKO",
]
