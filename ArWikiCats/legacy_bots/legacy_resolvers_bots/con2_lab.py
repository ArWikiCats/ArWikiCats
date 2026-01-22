#!/usr/bin/python3
"""
Arabic Label Builder Module
"""

import functools
import re
from typing import Tuple

from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...sub_new_resolvers import team_work
from ...translations import (
    RELIGIOUS_KEYS_PP,
    New_female_keys,
    get_from_new_p17_final,
    religious_entries,
)
from .. import tmp_bot
from ..circular_dependency import country_bot
from ..common_resolver_chain import get_lab_for_country2
from ..make_bots import get_KAKO
from .bot_2018 import get_pop_All_18


@functools.lru_cache(maxsize=10000)
def _split_category_by_separator(category: str, separator: str) -> Tuple[str, str]:
    """Split category into type and country parts using the separator.

    Args:
        category: The category string to split
        separator: The delimiter to use for splitting

    Returns:
        Tuple of (category_type, country)
    """
    if separator and separator in category:
        parts = category.split(separator, 1)
        category_type = parts[0]
        country = parts[1] if len(parts) > 1 else ""
    else:
        category_type = category
        country = ""

    return category_type, country.lower()


def _adjust_separator_position(text: str, separator_stripped: str, is_type: bool) -> str:
    """Adjust separator position for type or country based on separator value.

    Args:
        text: The text to adjust (either type or country)
        separator_stripped: The stripped separator
        is_type: True if adjusting type, False if adjusting country

    Returns:
        Adjusted text with proper separator positioning
    """
    separator_ends = f" {separator_stripped}"
    separator_starts = f"{separator_stripped} "

    if is_type:
        # Adjustments for type (separator should be at the end)
        if separator_stripped == "of" and not text.endswith(separator_ends):
            return f"{text} of"
        # elif separator_stripped == "spies for" and not text.endswith(" spies"):
        #     return f"{text} spies"
    else:
        # Adjustments for country (separator should be at the start)
        if separator_stripped == "by" and not text.startswith(separator_starts):
            return f"by {text}"
        elif separator_stripped == "for" and not text.startswith(separator_starts):
            return f"for {text}"

    return text


def _apply_regex_extraction(category: str, separator: str, category_type: str, country: str) -> Tuple[str, str, bool]:
    """Apply regex-based extraction when simple split is insufficient.

    Args:
        category: Original category string
        separator: The separator string
        category_type: Currently extracted type
        country: Currently extracted country

    Returns:
        Tuple of (type_regex, country_regex, should_use_regex)
    """
    separator_escaped = re.escape(separator) if separator else ""
    mash_pattern = f"^(.*?)(?:{separator_escaped}?)(.*?)$"

    test_remainder = category.lower()
    type_regex, country_regex = "", ""

    try:
        type_regex = re.sub(mash_pattern, r"\g<1>", category.lower())
        country_regex = re.sub(mash_pattern, r"\g<2>", category.lower())

        # Calculate what's left after removing extracted parts
        test_remainder = re.sub(re.escape(category_type.lower()), "", test_remainder)
        test_remainder = re.sub(re.escape(country.lower()), "", test_remainder)
        test_remainder = test_remainder.strip()

    except Exception as e:
        logger.info(f"<<lightred>>>>>> except test_remainder: {e}")
        return type_regex, country_regex, False

    # Determine if we should use regex results
    separator_stripped = separator.strip()
    should_use_regex = test_remainder and test_remainder != separator_stripped

    return type_regex, country_regex, should_use_regex


def _lookup_religious_males(type_lower: str) -> str:
    """Look up religious keys for males."""
    return RELIGIOUS_KEYS_PP.get(type_lower, {}).get("males", "")


@functools.lru_cache(maxsize=10000)
def get_type_country(category: str, separator: str) -> Tuple[str, str]:
    """Extract the type and country from a given category string.

    This function takes a category string and a delimiter (separator) to split
    the category into a type and a country. It processes the strings to
    ensure proper formatting and handles specific cases based on the value
    of separator.

    Args:
        category: The category string containing type and country information
        separator: The delimiter used to separate the type and country

    Returns:
        Tuple containing the processed type (str) and country (str)

    Example:
        >>> get_type_country("Military installations in Egypt", "in")
        ("Military installations", "egypt")
    """
    # Step 1: Initial split
    category_type, country = _split_category_by_separator(category, separator)

    # Step 2: Fix known typos
    separator_stripped = separator.strip()

    # Step 3: Apply initial separator adjustments
    category_type = _adjust_separator_position(category_type, separator_stripped, is_type=True)
    country = _adjust_separator_position(country, separator_stripped, is_type=False)

    logger.info(f'>xx>>> category_type: "{category_type.strip()}", country: "{country.strip()}", {separator=}')

    # Step 4: Check if regex extraction is needed
    type_regex, country_regex, should_use_regex = _apply_regex_extraction(category, separator, category_type, country)

    if not should_use_regex:
        logger.info(">>>> Using simple split results")
        return category_type, country

    # Step 5: Use regex results with separator adjustments
    logger.info(f">>>> Using regex extraction: {type_regex=}, {separator=}, {country_regex=}")

    # Apply typo fixes to regex results as well

    type_regex = _adjust_separator_position(type_regex, separator_stripped, is_type=True)
    country_regex = _adjust_separator_position(country_regex, separator_stripped, is_type=False)

    logger.info(f">>>> get_type_country: {type_regex=}, {country_regex=}")

    return type_regex, country_regex


@functools.lru_cache(maxsize=10000)
def get_type_lab(separator: str, type_value: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters.

    Args:
        separator: The separator/delimiter (preposition).
        type_value: The type part of the category.

    Returns:
        Tuple of (label, should_append_in_label)
            - label: The Arabic label for the type
            - should_append_in_label: Whether 'in' preposition should be appended
    """
    logger.debug(f"get_type_lab, {separator=}, {type_value=}")
    # get_type_lab, separator='by', type_value='new zealand non-fiction writers'

    normalized_preposition = separator.strip()
    type_lower = type_value.lower()

    if type_lower == "people":
        return "أشخاص", False

    should_append_in_label = True
    label = ""
    # Handle special cases first
    # label, should_append_in_label = _handle_special_type_cases(type_lower, normalized_preposition)

    # If no special case matched, proceed with lookup chain
    if not label:
        lookup_chain = {
            "get_from_new_p17_final": get_from_new_p17_final,
            "all_new_resolvers": all_new_resolvers,
            "_lookup_religious_males": _lookup_religious_males,
            "New_female_keys": lambda t: New_female_keys.get(t, ""),
            "religious_entries": lambda t: religious_entries.get(t, ""),
            "team_work.resolve_clubs_teams_leagues": team_work.resolve_clubs_teams_leagues,
            "tmp_bot.Work_Templates": tmp_bot.Work_Templates,
            "term_label": lambda t: country_bot.fetch_country_term_label(
                t, normalized_preposition, lab_type="type_label"
            ),
            "get_lab_for_country2": get_lab_for_country2,
            "get_pop_All_18": get_pop_All_18,
            "get_KAKO": get_KAKO,
        }

        for name, lookup_func in lookup_chain.items():
            label = lookup_func(type_lower)
            if label:
                logger.debug(f"get_type_lab({type_lower}): Found label '{label}' via {name}")
                break
    # Normalize whitespace in the label
    label = " ".join(label.strip().split())

    logger.info(f"?????? get_type_lab: {type_lower=}, {label=}")

    return label, should_append_in_label


__all__ = [
    "get_type_lab",
    "get_type_country",
]
