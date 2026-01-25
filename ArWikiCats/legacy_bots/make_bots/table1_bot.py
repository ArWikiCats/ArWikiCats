"""Table-based lookup bot for Arabic category labels.

This module provides functionality to look up Arabic labels for categories
using multiple mapping tables.

"""

import functools
from typing import Dict

from ...helps import logger
from ...new_resolvers.bys_new import resolve_by_labels
from ...translations import Jobs_new  # to be removed from players_new_keys
from ...translations import jobs_mens_data  # to be  removed from players_new_keys
from ...translations import Films_key_man
from .bot import Films_O_TT, players_new_keys

KAKO: Dict[str, Dict[str, str]] = {
    "Films_key_man": Films_key_man,  # 74
    "Films_O_TT": Films_O_TT,  # 0
    "players_new_keys": players_new_keys,  # 1,719
    "jobs_mens_data": jobs_mens_data,  # 96,552
    "Jobs_new": Jobs_new,  # 1,304
}


@functools.lru_cache(maxsize=5000)
def _get_KAKO(text: str) -> tuple[str, str]:
    """
    Look up the Arabic label for a term using resolve_by_labels and then the configured mapping tables.

    Parameters:
        text (str): Key to search for in the label resolvers and mapping tables.

    Returns:
        tuple: A pair (resolver_name, label) where `resolver_name` is the name of the resolver or table that produced `label` (empty string if none found), and `label` is the found Arabic label (empty string if none found).

    Raises:
        TypeError: If a resolver returns a non-string value for a found label.
    """
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
    """
    Return the Arabic label for a given term by consulting multiple mapping tables.

    Parameters:
        text (str): The term to look up.

    Returns:
        str: The Arabic label if found, otherwise an empty string.
    """
    _, label = _get_KAKO(text)
    return label


__all__ = [
    "get_KAKO",
]
