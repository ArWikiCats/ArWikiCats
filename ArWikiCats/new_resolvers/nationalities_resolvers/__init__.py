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
def main_nationalities_resolvers(normalized_category) -> str:
    """
    Resolve a category string into a nationalities category label.

    Parameters:
        normalized_category (str): Category string to resolve.

    Returns:
        str: Matched nationalities category label, or empty string if no resolver matches.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying nationalities_resolvers resolvers for: {normalized_category=}")

    resolved_label = (
        nationalities_v2.resolve_by_nats(normalized_category)
        or nationalities_time_v2.resolve_nats_time_v2(normalized_category)
        or ministers_resolver.resolve_secretaries_labels(normalized_category)
        or ""
    )

    logger.info_if_or_debug(
        f"<<yellow>> end nationalities_resolvers: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "main_nationalities_resolvers",
]
