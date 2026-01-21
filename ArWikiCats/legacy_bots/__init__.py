"""
Wrapper for legacy category resolvers.

This module coordinates several older resolution strategies to provide
backward compatibility for category translation logic.

The resolvers are organized in a pipeline pattern, where each resolver
is tried in priority order and the first non-empty result is returned.
"""

from __future__ import annotations

import functools
from typing import Callable, List

from ..sub_new_resolvers import university_resolver
from .legacy_resolvers_bots import country_bot, event_lab_bot, general_resolver, with_years_bot, year_or_typeo

# Type alias for resolver functions
ResolverFunc = Callable[[str], str]

# Pipeline of resolver functions in priority order
# Each resolver accepts a category string and returns a string (or empty string if no match)
RESOLVER_PIPELINE: List[ResolverFunc] = [
    university_resolver.resolve_university_category,
    country_bot.event2_d2,
    with_years_bot.wrap_try_with_years,
    year_or_typeo.label_for_startwith_year_or_typeo,
    event_lab_bot.event_Lab,
    general_resolver.translate_general_category,
]


def _run_pipeline(category: str, pipeline: List[ResolverFunc]) -> str:
    """
    Execute resolver functions in order and return the first non-empty result.

    Parameters:
        category (str): The category name to resolve.
        pipeline (List[ResolverFunc]): List of resolver functions to try.

    Returns:
        str: The first non-empty result from a resolver, or empty string if none match.
    """
    for resolver in pipeline:
        result = resolver(category)
        if result:
            return result
    return ""


@functools.lru_cache(maxsize=None)
def legacy_resolvers(changed_cat: str) -> str:
    """
    Resolve a category label using the legacy resolver chain in priority order.

    This function uses a pipeline pattern to try multiple resolver strategies
    and returns the first successful match. The resolvers are defined in
    RESOLVER_PIPELINE and can be extended or modified as needed.

    Parameters:
        changed_cat (str): Category name or identifier to resolve.

    Returns:
        str: The resolved category label, or an empty string if no
             legacy resolver produces a value.
    """
    return _run_pipeline(changed_cat, RESOLVER_PIPELINE)


__all__ = [
    "legacy_resolvers",
    "RESOLVER_PIPELINE",
]
