"""
Package for resolving language-related categories.
This package provides resolvers for categories involving languages,
including films and books in specific languages, with optional time components.


TODO: use it instead of langs_w.py after adding
    jobs_mens_data,
    Films_key_For_nat,
    Lang_work,

"""

import functools

from ...helps import getLogger
from ...new.handle_time_with_callback import handle_year_at_first
from .resolve_languages import _resolve_languages_labels
from .resolve_languages_films import resolve_films_languages_labels

logger = getLogger(__name__)


def fix_keys(category: str) -> str:
    """Normalize language-related category keys by lowercasing and standardizing suffixes.

    Args:
        category: The raw category string.

    Returns:
        The normalized category string.
    """
    category = category.lower().replace("category:", "").replace("'", "")
    category = category.replace("-language ", " language ")
    return category


@functools.lru_cache(maxsize=10000)
def resolve_languages_labels(category: str) -> str:
    category = fix_keys(category)

    result = _resolve_languages_labels(category) or resolve_films_languages_labels(category) or ""

    return result


@functools.lru_cache(maxsize=10000)
def resolve_languages_labels_with_time(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_languages_labels_with_time: {category=}")
    category = fix_keys(category)

    result = handle_year_at_first(
        category=category,
        callback=resolve_languages_labels,
        result_format="{sub_result} في {arabic_time}",
    )

    logger.info_if_or_debug(f"<<yellow>> end resolve_languages_labels_with_time: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_languages_labels",
    "resolve_languages_labels_with_time",
]
