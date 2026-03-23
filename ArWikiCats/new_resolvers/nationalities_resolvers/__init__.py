"""
Package for resolving nationality-related categories.
This package provides specialized resolvers for matching and translating
nationalities, often combined with occupations or time periods.
"""

import functools
import logging

from . import (
    ministers_resolver,
    nationalities_time_v2,
    nationalities_v2,
)

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_nationalities_resolvers(category) -> str:
    """
    Resolve a category string into a nationalities category label.

    Parameters:
        category (str): Category string to resolve.

    Returns:
        str: Matched nationalities category label, or empty string if no resolver matches.
    """
    category = category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {category=}")

    result = (
        nationalities_v2.resolve_by_nats(category)
        or nationalities_time_v2.resolve_nats_time_v2(category)
        or ministers_resolver.resolve_secretaries_labels(category)
        or ""
    )

    logger.log(20 if result else 10, f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "main_nationalities_resolvers",
]
