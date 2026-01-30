"""
Main entry point for resolving Arabic Wikipedia category names using multiple specialized resolvers.
This function orchestrates the resolution process by attempting to match a category string
against a series of specific resolvers in a predefined priority order to ensure accuracy
and avoid common linguistic conflicts (e.g., distinguishing between job titles and sports,
or nationalities and country names).

New resolvers for Arabic Wikipedia categories.
"""

from __future__ import annotations

import functools
from typing import Callable

import logging
from ..patterns_resolvers import all_patterns_resolvers
from ..sub_new_resolvers import main_other_resolvers
from ..time_formats import convert_time_to_arabic
from .countries_names_resolvers import main_countries_names_resolvers
from .countries_names_with_sports import main_countries_names_with_sports_resolvers
from .films_resolvers import main_films_resolvers
from .jobs_resolvers import main_jobs_resolvers
from .languages_resolves import resolve_languages_labels_with_time
from .nationalities_resolvers import main_nationalities_resolvers
from .relations_resolver import main_relations_resolvers
from .sports_resolvers import main_sports_resolvers
from .time_and_jobs_resolvers import time_and_jobs_resolvers_main

logger = logging.getLogger(__name__)

# Type alias for resolver functions
ResolverFn = Callable[[str], str]

# Define resolver chain in priority order
# Each tuple contains: (name, resolver_function, priority_notes)
_RESOLVER_CHAIN: list[tuple[str, ResolverFn, str]] = [
    (
        "Time to Arabic",
        convert_time_to_arabic,
        "Highest priority - handles year/century/millennium patterns",
    ),
    (
        "Pattern-based resolvers",
        all_patterns_resolvers,
        "Regex patterns for complex category structures",
    ),
    (
        "Jobs resolvers",
        main_jobs_resolvers,
        "Must be before sports to avoid mis-resolving job titles as sports",
    ),
    (
        "Time + Jobs resolvers",
        time_and_jobs_resolvers_main,
        "Combined time period and job titles",
    ),
    (
        "Sports resolvers",
        main_sports_resolvers,
        "Sports-specific category patterns",
    ),
    (
        "Nationalities resolvers",
        main_nationalities_resolvers,
        "Must be before countries to avoid conflicts (e.g., 'Italy political leader')",
    ),
    (
        "Countries names resolvers",
        main_countries_names_resolvers,
        "Country name patterns",
    ),
    (
        "Films resolvers",
        main_films_resolvers,
        "Film and television categories",
    ),
    (
        "Relations resolvers",
        main_relations_resolvers,
        "Complex relational categories (e.g., dual nationalities)",
    ),
    (
        "Countries with sports resolvers",
        main_countries_names_with_sports_resolvers,
        "Combined country and sport patterns",
    ),
    (
        "Languages resolvers",
        resolve_languages_labels_with_time,
        "Language-related categories with time periods",
    ),
    (
        "Other resolvers",
        main_other_resolvers,
        "Catch-all for remaining patterns",
    ),
]


@functools.lru_cache(maxsize=50000)
def all_new_resolvers(category: str) -> str:
    """Apply all new resolvers to translate a category string.

    The resolution follows a priority-based chain where each resolver is tried
    in order until one returns a non-empty result. The order is critical for
    correctness - see _RESOLVER_CHAIN for priority notes.

    Args:
        category (str): The category string to resolve.

    Returns:
        str: The resolved category label, or empty string if not resolved.
    """
    logger.info(f"<<purple>> all_new_resolvers: {category}")

    for name, resolver, _ in _RESOLVER_CHAIN:
        result = resolver(category)
        if result:
            logger.info(f"<<purple>> all_new_resolvers: {category} => {result} via {name}")
            return result

    logger.debug(f"<<purple>> all_new_resolvers: {category} => no match")
    return ""
