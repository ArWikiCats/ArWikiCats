"""
Wrapper for legacy category resolvers.
This module coordinates several older resolution strategies to provide
backward compatibility for category translation logic.
"""

from __future__ import annotations

import functools
from typing import Callable

from ..sub_new_resolvers import university_resolver
from .legacy_resolvers_bots import country_bot, event_lab_bot, general_resolver, with_years_bot, year_or_typeo

# Define the resolver pipeline in priority order
# Each resolver is a callable that takes a category string and returns a label or empty string
RESOLVER_PIPELINE: list[Callable[[str], str]] = [
    university_resolver.resolve_university_category,
    country_bot.event2_d2,
    with_years_bot.wrap_try_with_years,
    year_or_typeo.label_for_startwith_year_or_typeo,
    event_lab_bot.event_Lab,
    general_resolver.translate_general_category,
]


@functools.lru_cache(maxsize=None)
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
    "RESOLVER_PIPELINE",
]
