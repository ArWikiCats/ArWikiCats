"""Utilities for normalizing year placement within Arabic labels."""

from __future__ import annotations

import functools
import re

import logging

logger = logging.getLogger(__name__)
# Pattern for matching years in Arabic text (including BCE dates and century/millennium references)
YEARS_REGEX_AR = (
    r"\d+[−–\-]\d+"
    # r"|\d+\s*(ق[\s\.]م|قبل الميلاد)*"
    r"|(?:عقد|القرن|الألفية)*\s*\d+\s*(ق[\s\.]م|قبل الميلاد)*"
)

# Precompiled Regex Patterns
REGEX_WHITESPACE = re.compile(r"\s+", re.IGNORECASE)
REGEX_QM = re.compile(r"\bق\.م\b", re.IGNORECASE)

REGEX_YEAR_IN_SECOND_PART = re.compile(r"^(?P<subject>.*)\sحسب\s(?P<by>[\s\w]+)$", re.IGNORECASE)

REGEX_BY_DATE_PATTERN = re.compile(
    rf"^(?P<first_part>.*)\sحسب\s(?P<by_part>[\s\w]+)\sفي\s(?P<date>{YEARS_REGEX_AR})$",
    re.IGNORECASE,
)
REGEX_YEAR_FIRST_PATTERN = re.compile(
    rf"^(?P<first_part>{YEARS_REGEX_AR})\sفي\s(?P<second_part>[^0-9]*)$", re.IGNORECASE
)


# @dump_data(1, compare_with_output="text_str")
def move_by_in(text_str: str) -> str:
    """
    A function that takes in a string and searches for a specific pattern within it. The function replaces underscores in the string with spaces and then uses a regular expression to search for a pattern of the form '{first_part} حسب {by_part} في {date}'.

    Parameters:
    - text_str (str): The input string.

    Returns:
    - str: The modified string if a match is found, otherwise the original string.
    """
    # تصنيف:اتحاد الرجبي حسب البلد في 1989
    text_normalized = text_str.replace("_", " ")
    new_text = text_normalized
    result = REGEX_BY_DATE_PATTERN.search(text_normalized)

    if not result:
        logger.debug(f"no match for {text_str}")
        return text_str

    # [[تصنيف:اتحاد الرجبي في 1989 حسب البلد]]
    first_part = result.group("first_part")
    by_part = result.group("by_part")
    date = result.group("date")
    new_text = f"{first_part} في {date} حسب {by_part}"
    logger.debug(f"{new_text=}")

    new_text = REGEX_WHITESPACE.sub(" ", new_text)
    new_text = REGEX_QM.sub("ق م", new_text)
    new_text = new_text.replace(" في في ", " في ")

    return new_text


# @dump_data(1, compare_with_output="text_str")
def move_years_first(text_str: str) -> str:
    """Move leading year fragments to the end of the label when applicable.

    Args:
        text_str: Raw label text.

    Returns:
        A normalized string with the year moved after the subject.
    """
    # return text_str
    new_text = text_str
    match = REGEX_YEAR_FIRST_PATTERN.match(text_str)

    if not match:
        logger.debug(f'no match for "{text_str}"')
        return text_str

    first_part = match.group("first_part").strip()
    second_part = match.group("second_part").strip()
    logger.debug(f"first_part={first_part} second_part={second_part}")
    skip_it = [
        "أفلام",
        "الأفلام",
    ]
    if second_part in skip_it:
        return text_str
    if " في x" in second_part:
        logger.debug("skipping due to nested preposition")
        return text_str

    new_text = f"{second_part} في {first_part}"
    if result := REGEX_YEAR_IN_SECOND_PART.search(second_part):
        logger.debug("found حسب clause")
        subject = result.group("subject")
        by_part = result.group("by")
        new_text = f"{subject} في {first_part} حسب {by_part}"

    new_text = REGEX_WHITESPACE.sub(" ", new_text)
    new_text = REGEX_QM.sub("ق م", new_text)
    new_text = new_text.replace(" في في ", " في ")
    return new_text


@functools.lru_cache(maxsize=10000)
def move_years(text_str: str) -> str:
    """Normalize the placement of year fragments within the label.

    Args:
        text_str: Raw label text.

    Returns:
        The normalized label with category namespace preserved.
    """

    text_str = text_str.replace("_", " ").strip()
    is_category_namespace = text_str.startswith("تصنيف:")

    if is_category_namespace:
        text_str = text_str.replace("تصنيف:", "")

    new_text = move_years_first(text_str)
    if new_text == text_str:
        new_text = move_by_in(text_str)

    if is_category_namespace:
        new_text = f"تصنيف:{new_text}"

    return new_text


__all__ = [
    "move_by_in",
    "move_years",
    "move_years_first",
]
