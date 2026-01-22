#!/usr/bin/python3
"""

"""

import functools
from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...sub_new_resolvers import team_work
from ...translations import (
    RELIGIOUS_KEYS_PP,
    New_female_keys,
    get_from_new_p17_final,
    religious_entries,
)
from .. import tmp_bot
from ..common_resolver_chain import get_lab_for_country2
from ..make_bots import get_KAKO
from .bot_2018 import get_pop_All_18


def _lookup_religious_males(type_lower: str) -> str:
    """Look up religious keys for males."""
    return RELIGIOUS_KEYS_PP.get(type_lower, {}).get("males", "")


@functools.lru_cache(maxsize=10000)
def get_type_lab(type_value: str) -> str:
    """Determine the type label based on input parameters.

    Args:
        type_value: The type part of the category.

    Returns:
        - label: The Arabic label for the type
    """
    logger.debug(f"get_type_lab, {type_value=}")

    type_lower = type_value.lower()

    if type_lower == "people":
        return "أشخاص"

    label = ""
    lookup_chain = {
        "get_from_new_p17_final": get_from_new_p17_final,
        "all_new_resolvers": all_new_resolvers,
        "_lookup_religious_males": _lookup_religious_males,
        "New_female_keys": lambda t: New_female_keys.get(t, ""),
        "religious_entries": lambda t: religious_entries.get(t, ""),
        "team_work.resolve_clubs_teams_leagues": team_work.resolve_clubs_teams_leagues,
        "tmp_bot.Work_Templates": tmp_bot.Work_Templates,
        "get_lab_for_country2": get_lab_for_country2,
        "get_pop_All_18": get_pop_All_18,
        "get_KAKO": get_KAKO,
    }

    for name, lookup_func in lookup_chain.items():
        label = lookup_func(type_lower)
        if label:
            logger.debug(f"get_type_lab({type_lower}): Found label '{label}' via {name}")
            break
    # Normalize whitespace in the label
    label = " ".join(label.strip().split())

    logger.info(f"?????? get_type_lab: {type_lower=}, {label=}")

    return label


__all__ = [
    "get_type_lab",
]
