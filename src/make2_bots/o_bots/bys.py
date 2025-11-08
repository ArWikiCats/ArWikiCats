"""Label helpers for categories that use the word ``by``."""

from __future__ import annotations

import re
from typing import Callable, Dict

from ...helps.log import logger
from ...ma_lists import By_orginal2, By_table, By_table_orginal, New_P17_Finall
from ..matables_bots.bot_2018 import pop_All_2018
from ..media_bots.films_bot import test_films
from ..p17_bots.nats import find_nat_others
from .utils import first_non_empty

LabelLookup = Callable[[str], str]


def _lookup_entity(key: str, *tables: Dict[str, str]) -> str:
    """Return the first non-empty label for ``key`` from ``tables``."""

    lower_key = key.lower()
    return first_non_empty(lower_key, list(tables))


def make_by_label(category: str) -> str:
    """Return the Arabic label for ``category`` that starts with ``by``.

    Args:
        category: Category name that is expected to start with the word ``by``.

    Returns:
        Resolved label or an empty string when the category is unknown.
    """

    logger.info(
        f"<<lightred>>>> vvvvvvvvvvvv make_by_label start, cate:{category} vvvvvvvvvvvv "
    )
    resolved_label = ""

    if category.startswith("by "):
        category_label = test_films(category.replace("by ", ""))
        if category_label:
            resolved_label = f"بواسطة {category_label}"
        else:
            category_label = find_nat_others(category.replace("by ", ""))
            if category_label:
                resolved_label = f"بواسطة {category_label}"

    match = re.match(r"^by (.*?) and (.*?)$", category.lower())
    if not resolved_label and match:
        first_key = match.group(1)
        second_key = match.group(2)

        first_label = By_orginal2.get(first_key, "")
        second_label = By_orginal2.get(second_key, "")

        logger.debug(f"<<lightred>>>> by:{first_key},lab:{first_label}.")
        logger.debug(f"<<lightred>>>> by:{second_key},lab:{second_label}.")

        if second_label and first_label:
            resolved_label = f"حسب {first_label} و{second_label}"

    if resolved_label:
        logger.debug(
            f"<<lightblue>>>> ^^^^^^^^^ make_by_label lab:{resolved_label}."
        )

    logger.info("<<lightblue>>>> ^^^^^^^^^ make_by_label end ^^^^^^^^^ ")
    return resolved_label


def _lookup_prefixed_label(part: str, lookup: LabelLookup) -> str:
    """Return the label for ``part`` using ``lookup`` with normalisation."""

    cleaned = part.strip().lower()
    if cleaned.startswith("the "):
        cleaned = cleaned[4:]
    return lookup(cleaned)


def get_by_label(category: str) -> str:
    """Return the label for a category in the form ``<entity> by <suffix>``.

    Args:
        category: Full category string that contains a "by" clause.

    Returns:
        The composed Arabic label or an empty string when the lookup fails.
    """

    label = ""
    by_section = ""
    first_part = ""

    logger.info(f"<<lightyellow>>>>get_by_label {category}")

    first_label = ""
    by_label = ""

    if match_info := re.match(r"^(.*?) (by .*)$", category, flags=re.IGNORECASE):
        first_part = match_info.group(1)
        by_section = match_info.group(2)

        logger.debug(f"<<lightyellow>>>>frist:{first_part},by:{by_section}")

    if first_part.startswith("the "):
        first_part = first_part[len("the ") :]

    if first_part:
        if not first_label:
            first_label = New_P17_Finall.get(first_part.lower(), "")

        if not first_label:
            first_label = pop_All_2018.get(first_part.lower(), "")

    if by_section:
        if not by_label:
            by_label = By_table.get(by_section.lower(), "")

        if not by_label:
            by_label = By_table_orginal.get(by_section.lower(), "")

    if first_label and by_label:
        label = f"{first_label} {by_label}"
        logger.info(f"<<lightyellow>>>>get_by_label lab {label}")

    return label


def get_and_label(category: str) -> str:
    """Return the label for ``<entity> and <entity>`` categories.

    Args:
        category: Category string that joins two entities with "and".

    Returns:
        The combined Arabic label or an empty string when either entity is
        missing from the lookup tables.
    """

    label = ""
    first_part = ""
    last_part = ""

    logger.info(f"<<lightyellow>>>>get_and_label {category}")

    first_label = ""
    last_label = ""

    if match_info := re.match(r"(.*?) and (.*)", category, flags=re.IGNORECASE):
        first_part = match_info.group(1)
        last_part = match_info.group(2)

        logger.debug(f"<<lightyellow>>>>frist:{first_part},last:{last_part}")

    if first_part:
        if not first_label:
            first_label = New_P17_Finall.get(first_part.lower(), "")

        if not first_label:
            first_label = pop_All_2018.get(first_part.lower(), "")

    if last_part:
        if not last_label:
            last_label = New_P17_Finall.get(last_part.lower(), "")

        if not last_label:
            last_label = pop_All_2018.get(last_part.lower(), "")

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
