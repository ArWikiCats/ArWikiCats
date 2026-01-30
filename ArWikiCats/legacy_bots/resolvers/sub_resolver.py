#!/usr/bin/python3
"""
Sub-resolver module for general category translation.

This module provides utility functions for translating categories using
multiple lookup sources. It is extracted from the legacy circular_dependency
package to break the import cycle.
"""

from __future__ import annotations

import functools
import re

from ...helps import getLogger
from ...time_formats import time_to_arabic
from ...translations import Jobs_new, jobs_mens_data
from ...utils import get_value_from_any_table
from ..legacy_resolvers_bots.bot_2018 import get_pop_All_18
from ..make_bots import Films_O_TT, players_new_keys

logger = getLogger(__name__)

en_literes = "[a-z]"


@functools.lru_cache(maxsize=10000)
def sub_translate_general_category(category_r: str) -> str:
    """
    Translate a general category using multiple lookup sources.

    This function attempts to resolve a category label by checking:
    1. Population data (get_pop_All_18)
    2. Films lookup table (Films_O_TT)
    3. Players/jobs tables
    4. Time conversion

    Parameters:
        category_r: The category string to translate.

    Returns:
        The Arabic label if found, otherwise an empty string.

    Example:
        >>> sub_translate_general_category("Category:20th-century musicians")
        "موسيقيون في القرن 20"
    """
    category = category_r.replace("_", " ").lower()
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    logger.info(f"<<lightyellow>>>> ^^^^^^^^^ sub_translate_general_category start ^^^^^^^^^ ({category}) ")
    logger.debug(f"<<lightyellow>>>>>> {category_r=}")

    arlabel = (
        ""
        or get_pop_All_18(category, "")
        or Films_O_TT.get(category, "")
        or get_value_from_any_table(category, [players_new_keys, jobs_mens_data, Jobs_new])
        or time_to_arabic.convert_time_to_arabic(category)
    )

    if arlabel:
        logger.debug(f"<<lightyellow>>>> sub_translate_general_category {arlabel=}  ")

    logger.debug("<<lightyellow>>>> ^^^^^^^^^ sub_translate_general_category end ^^^^^^^^^ ")

    return arlabel


__all__ = [
    "sub_translate_general_category",
]
