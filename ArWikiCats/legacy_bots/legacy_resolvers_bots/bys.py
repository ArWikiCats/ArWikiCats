"""
Label helpers for categories that use the word ``by``.

TODO: need refactoring

"""

from __future__ import annotations

import functools

from ...helps import getLogger

logger = getLogger(__name__)
from ...new_resolvers import all_new_resolvers
from ...new_resolvers.bys_new import resolve_by_labels
from ...translations import People_key
from ...translations.funcs import get_from_new_p17_final
from ..utils.regex_hub import BY_MATCH_PATTERN, DUAL_BY_PATTERN
from .bot_2018 import get_pop_All_18


def find_dual_by_keys(normalized: str) -> str:
    resolved = ""
    match = DUAL_BY_PATTERN.match(normalized)

    if not match:
        return ""

    first_key, second_key = match.groups()
    first_label = resolve_by_labels(first_key.lower())
    second_label = resolve_by_labels(second_key.lower())

    logger.debug(f"<<lightred>>>> by:{first_key},lab:{first_label}.")
    logger.debug(f"<<lightred>>>> by:{second_key},lab:{second_label}.")

    if first_label and second_label:
        resolved = f"حسب {first_label} و{second_label}"
        logger.debug(f"<<lightblue>>>> ^^^^^^^^^ make_by_label lab:{resolved}.")

    return resolved


def by_people_bot(key: str) -> str:
    """Return the Arabic label for a person-related key.

    Args:
        key: The key representing a person-related category.
    Returns:
        The Arabic label corresponding to the key, or an empty string if not found.
    """
    resolved = ""
    if key.lower().startswith("by "):
        candidate = key[3:]
        label = People_key.get(candidate, "")
        if label:
            resolved = f"بواسطة {label}"
            logger.debug(f"matched people label, {key=}, {resolved=}")

    return resolved


@functools.lru_cache(maxsize=10000)
def make_new_by_label(category: str) -> str:
    """Return the Arabic label for ``category`` that starts with ``by``.

    Args:
        category: Category name that is expected to start with the word ``by``.

    Returns:
        Resolved label or an empty string when the category is unknown.
    """

    normalized = category.strip()
    logger.info(f"Resolving by-label, category: {normalized=}")
    logger.info(f"<<lightred>>>> vvvvvvvvvvvv make_by_label start, cate:{category} vvvvvvvvvvvv ")
    resolved = ""

    if normalized.lower().startswith("by "):
        candidate = normalized[3:]
        film_label = "" or all_new_resolvers(candidate) or People_key.get(candidate)
        if film_label:
            resolved = f"بواسطة {film_label}"
            logger.debug(f"Matched film label, category: {normalized}, label: {resolved}")

    if not resolved:
        resolved = find_dual_by_keys(normalized)

    logger.info("<<lightblue>>>> ^^^^^^^^^ make_by_label end ^^^^^^^^^ ")
    return resolved


@functools.lru_cache(maxsize=10000)
def make_by_label(category: str) -> str:
    return by_people_bot(category) or make_new_by_label(category) or ""


@functools.lru_cache(maxsize=10000)
def get_by_label(category: str) -> str:
    """
    Compose an Arabic label for a category that contains a "by" clause.

    Parameters:
        category (str): Full category string expected to include " by " separating an entity and a suffix.

    Returns:
        str: The composed Arabic label (e.g., "<entity_label> <by_label>") or an empty string if resolution fails.
    """
    if " by " not in category:
        return ""

    label = ""
    logger.info(f"<<lightyellow>>>>get_by_label {category=}")

    match = BY_MATCH_PATTERN.match(category)
    if not match:
        return ""

    first_part, by_section = match.groups()
    by_section = by_section.lower()

    first_part_cleaned = first_part.strip().lower()
    if first_part_cleaned.startswith("the "):
        first_part_cleaned = first_part_cleaned[4:]

    first_label = get_from_new_p17_final(first_part_cleaned) or get_pop_All_18(first_part_cleaned, "") or ""
    by_label = resolve_by_labels(by_section)

    logger.debug(f"<<lightyellow>>>>frist:{first_part=}, {by_section=}")

    if first_label and by_label:
        label = f"{first_label} {by_label}"
        logger.info(f"<<lightyellow>>>>get_by_label lab {label=}")

    return label


__all__ = [
    "get_by_label",
    "make_by_label",
]
