"""
Shared resolver functions to break circular imports.

This module contains resolver functions that were causing circular imports
between country_bot.py and ar_lab_bot.py. By extracting them here,
both modules can import from this central location instead of each other.
"""

from __future__ import annotations

import functools
from typing import TYPE_CHECKING

from ...sub_new_resolvers import university_resolver

if TYPE_CHECKING:
    pass


@functools.lru_cache(maxsize=10000)
def wrap_event2(category: str, separator: str = "") -> str:
    """
    Attempt to resolve a category label by trying several resolver functions in order.

    This function was moved from ar_lab_bot.py to break circular imports between
    ar_lab_bot, country_bot, and general_resolver.

    Parameters:
        category (str): The input category string to resolve.
        separator (str): Unused; kept for API compatibility.

    Returns:
        str: The first non-empty label returned by the resolvers, or an empty string if none match.
    """
    # Import here to avoid circular imports at module load time
    from ..legacy_resolvers_bots import country_bot, with_years_bot
    from ..legacy_resolvers_bots.year_or_typeo import label_for_startwith_year_or_typeo

    result = (
        university_resolver.resolve_university_category(category)
        or country_bot.event2_d2(category)
        or with_years_bot.wrap_try_with_years(category)
        or label_for_startwith_year_or_typeo(category)
        or ""
    )
    return result


__all__ = [
    "wrap_event2",
]
