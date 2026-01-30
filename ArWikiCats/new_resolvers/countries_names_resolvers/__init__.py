"""
Package for resolving country names in category titles.
This package provides specialized resolvers for matching and translating
country names and related geographic entities (like US states) into Arabic.
"""

import functools
import logging

from . import (  # countries_names_double_v2,
    countries_names,
    countries_names_v2,
    geo_names_formats,
    medalists_resolvers,
    us_states,
)

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_countries_names_resolvers(normalized_category: str) -> str:
    """
    Orchestrates resolution of an Arabic label for geographic category strings using a prioritized sequence of resolvers.

    The input is normalized by stripping whitespace, converting to lowercase, and removing a leading "category:" before resolution.

    Parameters:
        normalized_category (str): Category string to resolve; it will be normalized as described above.

    Returns:
        str: Resolved Arabic label, or an empty string if no resolver produces a match.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {normalized_category=}")

    resolved_label = (
        # NOTE: order matters here
        # resolve_by_countries_names_v2 must be before resolve_by_countries_names, to avoid mis-resolving like:
        # incorrect:    [Category:Zimbabwe political leader] : "تصنيف:قادة زيمبابوي السياسيون",
        # correct:      [Category:Zimbabwe political leader] : "تصنيف:قادة سياسيون زيمبابويون",
        countries_names_v2.resolve_by_countries_names_v2(normalized_category)
        or countries_names.resolve_by_countries_names(normalized_category)
        or medalists_resolvers.resolve_countries_names_medalists(normalized_category)
        or us_states.resolve_us_states(normalized_category)
        or geo_names_formats.resolve_by_geo_names(normalized_category)
        # or countries_names_double_v2.resolve_countries_names_double(normalized_category)
        or ""
    )

    logger.info(f"<<yellow>> end {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "main_countries_names_resolvers",
]
