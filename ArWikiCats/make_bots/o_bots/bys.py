"""Label helpers for categories that use the word ``by``."""

from __future__ import annotations

import re
import functools
from ...helps.log import logger
from ...translations import By_orginal2, By_table, By_table_orginal, get_from_new_p17_final
from ..lazy_data_bots.bot_2018 import pop_All_2018
from ..media_bots.films_bot import te_films
from ...translations.sports_formats_national.sport_lab_nat import sport_lab_nat_load_new


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
            nationality_label = sport_lab_nat_load_new(candidate)
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


@functools.lru_cache(maxsize=10000)
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
    logger.info(f"<<lightyellow>>>>get_by_label {category}")

    match = re.match(r"^(.*?) (by .*)$", category, flags=re.IGNORECASE)
    if not match:
        return ""

    first_part, by_section = match.groups()
    by_section = by_section.lower()

    first_part_cleaned = first_part.strip().lower()
    if first_part_cleaned.startswith("the "):
        first_part_cleaned = first_part_cleaned[4:]

    first_label = get_from_new_p17_final(first_part_cleaned) or pop_All_2018.get(first_part_cleaned, "")
    by_label = By_table.get(by_section, "") or By_table_orginal.get(by_section, "")

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
    if " and " not in category:
        return ""

    logger.info(f"<<lightyellow>>>>get_and_label {category}")
    logger.info(f"Resolving get_and_label, {category=}")
    match = re.match(r"^(.*?) and (.*)$", category, flags=re.IGNORECASE)

    if not match:
        logger.debug(f"<<lightyellow>>>> No match found for get_and_label: {category}")
        return ""

    first_part, last_part = match.groups()
    first_part = first_part.lower()
    last_part = last_part.lower()

    logger.debug(f"<<lightyellow>>>> get_and_label(): {first_part=}, {last_part=}")

    first_label = get_from_new_p17_final(first_part, None) or pop_All_2018.get(first_part)
    last_label = get_from_new_p17_final(last_part, None) or pop_All_2018.get(last_part)

    logger.debug(f"<<lightyellow>>>> get_and_label(): {first_label=}, {last_label=}")

    label = ""
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
