"""Label helpers for categories that use the word ``by``."""

from __future__ import annotations

import re
import functools
from typing import Callable, Dict

from ...helps.log import logger
from ...translations import By_orginal2, By_table, By_table_orginal, New_P17_Finall
from ..lazy_data_bots.bot_2018 import pop_All_2018
from ..media_bots.films_bot import te_films
from ..p17_bots.nats_other import find_nat_others
from .utils import first_non_empty

LabelLookup = Callable[[str], str]


def _lookup_entity(key: str, *tables: Dict[str, str]) -> str:
    """Return the first non-empty label for ``key`` from ``tables``."""

    lower_key = key.lower()
    return first_non_empty(lower_key, list(tables))


@functools.lru_cache(maxsize=10000)
def make_by_label(category: str) -> str:
    """Return the Arabic label for ``category`` that starts with ``by``.

    Args:
        category: Category name that is expected to start with the word ``by``.

    Returns:
        Resolved label or an empty string when the category is unknown.
    """

    normalized = category.strip()
    logger.info(f"Resolving by-label, category: {normalized}")
    logger.info(f"<<lightred>>>> vvvvvvvvvvvv make_by_label start, cate:{category} vvvvvvvvvvvv ")
    resolved = ""
    if normalized.lower().startswith("by "):
        candidate = normalized[3:]
        film_label = te_films(candidate)
        if film_label:
            resolved = f"بواسطة {film_label}"
            logger.debug(f"Matched film label, category: {normalized}, label: {resolved}")

        if not resolved:
            nationality_label = find_nat_others(candidate)
            if nationality_label:
                resolved = f"بواسطة {nationality_label}"
                logger.debug(f"Matched nationality label, category: {normalized}, label: {resolved}")
    if not resolved:
        match = re.match(r"^by (.*?) and (.*?)$", normalized, flags=re.IGNORECASE)
        if match:
            first_key, second_key = match.groups()
            first_label = By_orginal2.get(first_key.lower(), "")
            second_label = By_orginal2.get(second_key.lower(), "")

            logger.debug(f"<<lightred>>>> by:{first_key},lab:{first_label}.")
            logger.debug(f"<<lightred>>>> by:{second_key},lab:{second_label}.")

            if first_label and second_label:
                resolved = f"حسب {first_label} و{second_label}"
                logger.debug(f"<<lightblue>>>> ^^^^^^^^^ make_by_label lab:{resolved}.")

    logger.info("<<lightblue>>>> ^^^^^^^^^ make_by_label end ^^^^^^^^^ ")
    return resolved


def _lookup_prefixed_label(part: str, lookup: LabelLookup) -> str:
    """Return the label for ``part`` using ``lookup`` with normalisation."""

    cleaned = part.strip().lower()
    if cleaned.startswith("the "):
        cleaned = cleaned[4:]
    return lookup(cleaned)


@functools.lru_cache(maxsize=10000)
def get_by_label(category: str) -> str:
    """Return the label for a category in the form ``<entity> by <suffix>``.

    Args:
        category: Full category string that contains a "by" clause.

    Returns:
        The composed Arabic label or an empty string when the lookup fails.
    """

    label = ""
    logger.info(f"<<lightyellow>>>>get_by_label {category}")

    match = re.match(r"^(.*?) (by .*)$", category, flags=re.IGNORECASE)
    if not match:
        return ""

    first_part, by_section = match.groups()
    first_label = _lookup_prefixed_label(first_part, lambda key: _lookup_entity(key, New_P17_Finall, pop_All_2018))

    by_label = _lookup_entity(by_section, By_table, By_table_orginal)

    logger.debug(f"<<lightyellow>>>>frist:{first_part},by:{by_section}")

    if first_label and by_label:
        label = f"{first_label} {by_label}"
        logger.info(f"<<lightyellow>>>>get_by_label lab {label}")

    return label


@functools.lru_cache(maxsize=10000)
def get_and_label(category: str) -> str:
    """Return the label for ``<entity> and <entity>`` categories.

    Args:
        category: Category string that joins two entities with "and".

    Returns:
        The combined Arabic label or an empty string when either entity is
        missing from the lookup tables.
    """

    label = ""
    logger.info(f"<<lightyellow>>>>get_and_label {category}")
    logger.info(f"Resolving get_and_label, {category=}")
    match = re.match(r"(.*?) and (.*)", category, flags=re.IGNORECASE)
    if not match:
        return ""

    first_part, last_part = match.groups()

    logger.debug(f"<<lightyellow>>>>frist:{first_part},last:{last_part}")

    first_label = _lookup_entity(first_part, New_P17_Finall, pop_All_2018)
    last_label = _lookup_entity(last_part, New_P17_Finall, pop_All_2018)

    if first_label and last_label:
        label = f"{first_label} و{last_label}"
        logger.info(f"<<lightyellow>>>>get_and_label lab {label}")

    return label


# Backwards compatibility ----------------------------------------------------------------------
make_By_lab = make_by_label  # type: ignore
Make_By_lab = make_by_label
Get_by_label = get_by_label
Get_and_label = get_and_label

__all__ = [
    "get_and_label",
    "get_by_label",
    "make_by_label",
    "Get_and_label",
    "Get_by_label",
    "Make_By_lab",
    "make_By_lab",
]
