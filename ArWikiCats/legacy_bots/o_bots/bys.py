"""
Label helpers for categories that use the word ``by``.

TODO: need refactoring

"""

from __future__ import annotations

import functools
import re

from ...helps import dump_data, logger
from ...new_resolvers.bys_new import resolve_by_labels
from ...new_resolvers.sports_resolvers.sport_lab_nat import sport_lab_nat_load_new
from ...translations import People_key, get_from_new_p17_final
from ..films_and_others_bot import te_films
from ..make_bots.bot_2018 import get_pop_All_18

DUAL_BY_PATTERN = re.compile(r"^by (.*?) and (.*?)$", flags=re.IGNORECASE)
BY_MATCH_PATTERN = re.compile(r"^(.*?) (by .*)$", flags=re.IGNORECASE)
AND_PATTERN = re.compile(r"^(.*?) and (.*)$", flags=re.IGNORECASE)


# @dump_data(1)
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
# @dump_data(1)
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
        film_label = te_films(candidate)
        if film_label:
            resolved = f"بواسطة {film_label}"
            logger.debug(f"Matched film label, category: {normalized}, label: {resolved}")

        if not resolved:
            nationality_label = sport_lab_nat_load_new(candidate)
            if nationality_label:
                resolved = f"بواسطة {nationality_label}"
                logger.debug(f"Matched nationality label, category: {normalized}, label: {resolved}")

    if not resolved:
        resolved = find_dual_by_keys(normalized)

    logger.info("<<lightblue>>>> ^^^^^^^^^ make_by_label end ^^^^^^^^^ ")
    return resolved


@functools.lru_cache(maxsize=10000)
def make_by_label(category: str) -> str:
    return by_people_bot(category) or make_new_by_label(category) or ""


@functools.lru_cache(maxsize=10000)
# @dump_data(1)
def get_by_label(category: str) -> str:
    """Return the label for a category in the form ``<entity> by <suffix>``.

    Args:
        category: Full category string that contains a "by" clause.

    Returns:
        The composed Arabic label or an empty string when the lookup fails.
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


@functools.lru_cache(maxsize=10000)
# @dump_data(1)
def get_and_label(category: str) -> str:
    """Return the label for ``<entity> and <entity>`` categories.

    Args:
        category: Category string that joins two entities with "and".

    Returns:
        The combined Arabic label or an empty string when either entity is
        missing from the lookup tables.
    """
    if " and " not in category:
        return ""

    logger.info(f"<<lightyellow>>>>get_and_label {category}")
    logger.info(f"Resolving get_and_label, {category=}")
    match = AND_PATTERN.match(category)

    if not match:
        logger.debug(f"<<lightyellow>>>> No match found for get_and_label: {category}")
        return ""

    first_part, last_part = match.groups()
    first_part = first_part.lower()
    last_part = last_part.lower()

    logger.debug(f"<<lightyellow>>>> get_and_label(): {first_part=}, {last_part=}")

    first_label = get_from_new_p17_final(first_part, None) or get_pop_All_18(first_part) or ""

    last_label = get_from_new_p17_final(last_part, None) or get_pop_All_18(last_part) or ""

    logger.debug(f"<<lightyellow>>>> get_and_label(): {first_label=}, {last_label=}")

    label = ""
    if first_label and last_label:
        label = f"{first_label} و{last_label}"
        logger.info(f"<<lightyellow>>>>get_and_label lab {label}")

    return label


__all__ = [
    "get_and_label",
    "get_by_label",
    "make_by_label",
]
