"""
Package for resolving country names in category titles.
This package provides specialized resolvers for matching and translating
country names and related geographic entities (like US states) into Arabic.
"""

import functools

from ...helps import logger
from . import (  # countries_names_double_v2,
    countries_names,
    countries_names_v2,
    geo_names_formats,
    medalists_resolvers,
    us_states,
)


@functools.lru_cache(maxsize=None)
def main_countries_names_resolvers(normalized_category: str) -> str:
    """Orchestrate country name resolution for a category string.

    This function tries multiple country-related resolvers in a prioritized
    order to find an Arabic translation for geographic category elements.

    Args:
        normalized_category: The normalized category string to resolve.

    Returns:
        The resolved Arabic label or an empty string.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")
    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> Trying countries_names_resolvers for: {normalized_category=}")

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

    logger.info_if_or_debug(
        f"<<yellow>> end countries_names_resolvers: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "main_countries_names_resolvers",
]
