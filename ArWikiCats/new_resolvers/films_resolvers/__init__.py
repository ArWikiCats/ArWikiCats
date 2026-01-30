"""
Package for resolving film and television related categories.
This package provides specialized resolvers for film genres, production years,
and television series, often combined with geographic elements.
"""

import functools
import logging
import re

from ...translations import TELEVISION_KEYS, Films_key_CAO
from .resolve_films_labels import get_films_key_tyty_new
from .resolve_films_labels_and_time import get_films_key_tyty_new_and_time

logger = logging.getLogger(__name__)


def legacy_label_check(normalized_category: str) -> str:
    """
    Resolve legacy labels or return a numeric category string.

    Parameters:
        normalized_category (str): Normalized category text to check.

    Returns:
        str: Arabic label for known legacy terms, the numeric string if the input is all digits, or an empty string if no match.
    """
    label = ""
    if re.match(r"^\d+$", normalized_category.strip()):
        label = normalized_category.strip()

    if normalized_category == "people":
        label = "أشخاص"
    return label


@functools.lru_cache(maxsize=10000)
def main_films_resolvers(normalized_category) -> str:
    """
    Resolve a film nationalities label from a category string.

    Normalizes the input by trimming whitespace, converting to lowercase, and removing a leading "category:" prefix, then queries a sequence of film-label resolvers and returns the first non-empty result.

    Parameters:
        normalized_category (str): Category text to resolve; may include a leading "category:" prefix.

    Returns:
        str: The resolved label if any resolver finds a match, otherwise an empty string.
    """
    normalized_category = normalized_category.strip().lower().replace("category:", "")

    logger.debug("--" * 20)
    logger.debug(f"<><><><><><> <<green>> {normalized_category=}")

    resolved_label = (
        legacy_label_check(normalized_category)
        or get_films_key_tyty_new_and_time(normalized_category)
        or TELEVISION_KEYS.get(normalized_category)
        or Films_key_CAO.get(normalized_category)
        or get_films_key_tyty_new(normalized_category)
        or ""
    )

    logger.info(f"<<yellow>> end {normalized_category=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "main_films_resolvers",
    "get_films_key_tyty_new",
    "get_films_key_tyty_new_and_time",
]
