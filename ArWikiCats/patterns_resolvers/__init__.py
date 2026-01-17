"""
"""
import functools

from ..helps import logger

from . import nat_men_pattern, country_time_pattern


@functools.lru_cache(maxsize=None)
def all_patterns_resolvers(category: str) -> str:
    logger.debug(f">> all_patterns_resolvers: {category}")
    category_lab = (
        country_time_pattern.resolve_country_time_pattern(category)
        or nat_men_pattern.resolve_nat_men_pattern_new(category)
        or ""
    )
    logger.debug(f"<< all_patterns_resolvers: {category} => {category_lab}")
    return category_lab
