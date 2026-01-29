"""
Pattern-based category resolvers for the ArWikiCats project.
This package provides resolvers that use complex regex patterns to match
and translate categories with structured temporal or nationality components.
"""

import functools

from ..helps import getLogger

logger = getLogger(__name__)
from . import (
    country_nat_pattern,
    country_time_pattern,
    nat_males_pattern,
    time_patterns_resolvers,
)


@functools.lru_cache(maxsize=50000)
def all_patterns_resolvers(category: str) -> str:
    """
    Resolve a category name into a canonical label using pattern-based rules.

    Parameters:
        category (str): The category string to be analyzed and mapped.

    Returns:
        str: The resolved category label, or an empty string if no pattern matches.
    """
    logger.debug(f">> all_patterns_resolvers: {category}")
    category_lab = (
        country_time_pattern.resolve_country_time_pattern(category)
        or nat_males_pattern.resolve_nat_males_pattern(category)
        or time_patterns_resolvers.resolve_lab_from_years_patterns(category)
        or country_nat_pattern.resolve_country_nat_pattern(category)
        or ""
    )
    logger.debug(f"<< all_patterns_resolvers: {category} => {category_lab}")
    return category_lab
