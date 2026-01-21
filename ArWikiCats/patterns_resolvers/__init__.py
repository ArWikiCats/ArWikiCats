"""
Pattern-based category resolvers for the ArWikiCats project.
This package provides resolvers that use complex regex patterns to match
and translate categories with structured temporal or nationality components.
"""

import functools

from ..helps import logger
from . import (
    country_time_pattern,
    nat_males_pattern,
    time_patterns_resolvers,
    country_nat_pattern,
)


@functools.lru_cache(maxsize=None)
def all_patterns_resolvers(category: str) -> str:
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
