#!/usr/bin/python3
"""
Shared Resolver Functions Module

This module contains resolver functions that were previously causing circular
import dependencies between country_bot and ar_lab_bot. By placing them in a
shared location, we break the circular dependency chain:
    country_bot -> general_resolver -> ar_lab_bot -> country_bot

Functions moved here:
- Get_country2: Resolve Arabic labels for country names
- event2_d2: Determine category labels based on input strings
"""

from __future__ import annotations

import functools
import re

from ...config import app_settings
from ...fix import fixtitle
from ...helps import logger
from ..common_resolver_chain import get_lab_for_country2
from ..legacy_resolvers_bots.bot_2018 import get_pop_All_18
from ..make_bots import get_KAKO


@functools.lru_cache(maxsize=None)
def Get_country2(country: str) -> str:
    """
    Resolve the Arabic label for a country name using layered resolution and normalization.

    This function is imported by both country_bot and ar_lab_bot, so it needs to be
    in a shared location to avoid circular imports.

    Parameters:
        country (str): The country name to resolve.

    Returns:
        str: The Arabic label for the country if found, otherwise an empty string.
            The returned label is post-processed for title fixes and normalized whitespace.
    """
    # Import here to avoid circular dependency
    from . import general_resolver
    from .country2_label_bot import country_2_title_work

    normalized_country = country.lower().strip()
    logger.info(f'>> Get_country2 "{normalized_country}":')

    resolved_label = (
        country_2_title_work(country, with_years=True)
        or get_lab_for_country2(country)
        or get_KAKO(country)
        or get_pop_All_18(country)
        or general_resolver.translate_general_category(normalized_country, start_get_country2=False, fix_title=False)
        or get_pop_All_18(normalized_country.lower(), "")
        or ""
    )

    if resolved_label:
        resolved_label = fixtitle.fixlabel(resolved_label, en=normalized_country)

    resolved_label = " ".join(resolved_label.strip().split())

    logger.info(f'>> Get_country2 "{normalized_country}": cnt_la: {resolved_label}')

    return resolved_label


def event2_d2(category_r: str) -> str:
    """Determine the category label based on the input string.

    This function is called by ar_lab_bot.wrap_event2, so it needs to be in a
    shared location to avoid circular imports.

    Args:
        category_r: The raw category string to process

    Returns:
        The processed category label or an empty string if not found
    """
    # Import here to avoid circular dependency at module level
    from .country_bot import get_country

    cat3 = category_r.lower().replace("category:", "").strip()

    logger.info(f'<<lightred>>>>>> category33:"{cat3}" ')

    # TODO: THIS NEED REVIEW
    # Reject strings that contain common English prepositions
    blocked = ("in", "of", "from", "by", "at")
    if any(f" {word} " in cat3.lower() for word in blocked):
        return ""

    category_lab = ""
    if re.sub(r"^\d", "", cat3) == cat3:
        category_lab = get_country(cat3)

    return category_lab


__all__ = [
    "Get_country2",
    "event2_d2",
]
