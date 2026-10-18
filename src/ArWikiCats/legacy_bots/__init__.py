"""
Wrapper for legacy category resolvers.
This module coordinates several older resolution strategies to provide
backward compatibility for category translation logic.

Architecture Note:
    The legacy `circular_dependency/` package has been replaced with the new
    `resolvers/` package which provides a clean, non-circular architecture.
    All imports now form a proper DAG (Directed Acyclic Graph).
"""

from __future__ import annotations

import functools
from typing import Callable, Protocol

# Import other legacy resolvers that are not part of the circular dependency
from .legacy_resolvers_bots import event_lab_bot, with_years_bot, year_or_typeo

# Import from the new resolvers package (no circular dependencies)
from .resolvers import event2_d2, initialize_resolvers, translate_general_category_wrap


class Resolver(Protocol):
    """Protocol for resolver functions that convert category names to Arabic labels."""

    def __call__(self, category: str) -> str:
        """
        Resolve a category name to an Arabic label.

        Parameters:
            category: The category name to resolve.

        Returns:
            The Arabic label, or an empty string if no resolution is found.
        """
        ...


# Initialize the resolver callbacks after all modules are loaded
initialize_resolvers()

# Define the resolver pipeline in priority order
# Each resolver is a callable that takes a category string and returns a label or empty string
#
# RESOLVER_PIPELINE: Ordered list of resolver functions
#
# The resolvers are tried in the order listed below. The first resolver to return
# a non-empty string wins. This ordering is significant:
#
# 1. event2_d2 - Country and event-based resolution
# 2. with_years_bot.wrap_try_with_years - Year-based category resolution
# 3. year_or_typeo.label_for_startwith_year_or_typeo - Year prefix patterns and typo handling
# 4. event_lab_bot.event_lab - General event labeling
# 5. translate_general_category_wrap - Catch-all general resolution (lowest priority)
#
# To add a new resolver:
# 1. Import the resolver function at the top of this file
# 2. Insert it into RESOLVER_PIPELINE at the appropriate priority position
# 3. Document its purpose in this docstring
#
# To modify priority:
# 1. Reorder entries in the list
# 2. Update this docstring to reflect the new order

RESOLVER_PIPELINE: list[Callable[[str], str]] = [
    event2_d2,
    with_years_bot.wrap_try_with_years,
    year_or_typeo.label_for_startwith_year_or_typeo,
    event_lab_bot.event_lab,
    translate_general_category_wrap,
]


@functools.lru_cache(maxsize=10000)
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
