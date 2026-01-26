"""
Wrapper for legacy category resolvers.
This module coordinates several older resolution strategies to provide
backward compatibility for category translation logic.
"""

from __future__ import annotations

import functools
from typing import Callable

from ..fix import fixtitle
from .circular_dependency import country_bot, general_resolver, sub_general_resolver
from .legacy_resolvers_bots import event_lab_bot, with_years_bot, year_or_typeo
from .resolvers import event_based_resolver
# Define the resolver pipeline in priority order
# Each resolver is a callable that takes a category string and returns a label or empty string
#
# RESOLVER_PIPELINE: Ordered list of resolver functions
#
# The resolvers are tried in the order listed below. The first resolver to return
# a non-empty string wins. This ordering is significant:
#
# 2. country_bot.event2_d2 - Country and event-based resolution
# 3. with_years_bot.wrap_try_with_years - Year-based category resolution
# 4. year_or_typeo.label_for_startwith_year_or_typeo - Year prefix patterns and typo handling
# 5. event_lab_bot.event_Lab - General event labeling
# 6. general_resolver.translate_general_category - Catch-all general resolution (lowest priority)
#
# To add a new resolver:
# 1. Import the resolver function at the top of this file
# 2. Insert it into RESOLVER_PIPELINE at the appropriate priority position
# 3. Document its purpose in this docstring
#
# To modify priority:
# 1. Reorder entries in the list
# 2. Update this docstring to reflect the new order


def translate_general_category_wrap(category: str) -> str:
    arlabel = (
        ""
        or sub_general_resolver.sub_translate_general_category(category)
        or general_resolver.work_separator_names(category)
    )
    if arlabel:
        arlabel = fixtitle.fixlabel(arlabel, en=category)

    return arlabel


RESOLVER_PIPELINE: list[Callable[[str], str]] = [
    event_based_resolver.event2_d2,
    with_years_bot.wrap_try_with_years,
    year_or_typeo.label_for_startwith_year_or_typeo,
    event_lab_bot.event_Lab,
    translate_general_category_wrap,
]


@functools.lru_cache(maxsize=50000)
def legacy_resolvers(changed_cat: str) -> str:
    """
    Resolve a category label using the legacy resolver chain in priority order.

    This function implements a pipeline pattern, iterating through registered
    resolvers until one returns a non-empty result. The resolvers are tried
    in the order defined in RESOLVER_PIPELINE.

    Parameters:
        changed_cat (str): Category name or identifier to resolve.

    Returns:
        category_label (str): The resolved category label, or an empty string
            if no legacy resolver produces a value.
    """
    for resolver in RESOLVER_PIPELINE:
        category_lab = resolver(changed_cat)
        if category_lab:
            return category_lab

    return ""


__all__ = [
    "legacy_resolvers",
]
