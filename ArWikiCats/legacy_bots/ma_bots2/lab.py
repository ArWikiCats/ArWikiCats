#!/usr/bin/python3
"""
Arabic Label Builder Module
"""

import functools
import re
from typing import Tuple

from ...helps import logger
from ...legacy_bots.common_resolver_chain import get_lab_for_country2
from ...new_resolvers import all_new_resolvers
from ...sub_new_resolvers import team_work
from ...translations import (
    RELIGIOUS_KEYS_PP,
    New_female_keys,
    get_from_new_p17_final,
    get_from_pf_keys2,
    religious_entries,
)
from .. import tmp_bot
from ..ma_bots.country_bot import fetch_country_term_label, get_country
from ..make_bots.bot_2018 import get_pop_All_18
from ..o_bots import bys


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


def _handle_special_type_cases(type_lower: str, normalized_preposition: str) -> Tuple[str, bool]:
    """Handle special cases for type labels.

    Args:
        type_lower: Lowercase type string
        normalized_preposition: Normalized separator/preposition

    Returns:
        Tuple of (label, should_append_in_label)
    """
    # Special case: "women" with "from" preposition
    if type_lower == "women" and normalized_preposition == "from":
        logger.info('>> >> >> Make label="نساء".')
        return "نساء", True

    # Special case: "women of"
    if type_lower == "women of":
        logger.info('>> >> >> Make label="نساء من".')
        return "نساء من", True

    # Check for type with preposition in Type_with_preposition_mappings
    type_with_prep = type_lower.strip()
    if not type_with_prep.endswith(f" {normalized_preposition}"):
        type_with_prep = f"{type_lower.strip()} {normalized_preposition}"

    Type_with_preposition_mappings = {
        "sport in": "الرياضة في",
    }

    label = Type_with_preposition_mappings.get(type_with_prep, "")
    if label:
        logger.info(f"<<<< {type_with_prep=}, {label=}")
        return label, False

    return "", True


def _lookup_religious_males(type_lower: str) -> str:
    """Look up religious keys for males."""
    return RELIGIOUS_KEYS_PP.get(type_lower, {}).get("males", "")


def _lookup_country_with_by(country_lower: str) -> str:
    """Handle country labels with 'by' prefix or infix."""
    if country_lower.startswith("by "):
        return bys.make_by_label(country_lower)

    if " by " in country_lower:
        return bys.get_by_label(country_lower)

    return ""


def _lookup_country_with_in_prefix(country_lower: str) -> str:
    """Handle country labels with 'in ' prefix."""
    if not country_lower.strip().startswith("in "):
        return ""

    inner_country = country_lower.strip()[len("in ") :].strip()
    country_label = get_country(inner_country)

    if not country_label:
        country_label = get_lab_for_country2(inner_country)

    if country_label:
        return f"في {country_label}"

    return ""


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

    # Handle special cases first
    label, should_append_in_label = _handle_special_type_cases(type_lower, normalized_preposition)

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
            "fetch_country_term_label": lambda t: fetch_country_term_label(t, normalized_preposition, lab_type="type_label"),
            "get_lab_for_country2": get_lab_for_country2,
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


@functools.lru_cache(maxsize=10000)
def get_con_lab(separator: str, country: str, start_get_country2: bool = False) -> str:
    """Retrieve the corresponding label for a given country.

    Args:
        separator: The separator/delimiter.
        country: The country part of the category.
        start_get_country2: Whether to use the secondary country lookup.

    Returns:
        The Arabic label for the country.
    """
    separator = separator.strip()
    country_lower = country.strip().lower()
    country_no_dash = country_lower.replace("-", " ")

    for_table = {
        "for national teams": "للمنتخبات الوطنية",
        "for member-of-parliament": "لعضوية البرلمان",
    }

    label = get_pop_All_18(country_no_dash, "") or get_pop_All_18(country_lower, "")
    if label:
        logger.info(f"?????? get_con_lab early return: {country_lower=}, {label=}")
        return label

    lookup_chain = {
        "all_new_resolvers": lambda t: all_new_resolvers(t),
        "get_from_new_p17_final": lambda c: get_from_new_p17_final(c),
        "pf_keys2": lambda c: get_from_pf_keys2(c),
        "_lookup_country_with_by": _lookup_country_with_by,
        "for_table": lambda c: for_table.get(c, "") if separator.lower() == "for" else "",
        "_lookup_country_with_in_prefix": _lookup_country_with_in_prefix,
        "team_work.resolve_clubs_teams_leagues": lambda c: team_work.resolve_clubs_teams_leagues(c.strip()),
        "fetch_country_term_label": lambda c: fetch_country_term_label(
            c, separator, start_get_country2=start_get_country2
        ),
        "tmp_bot.Work_Templates": tmp_bot.Work_Templates,
        "get_lab_for_country2": get_lab_for_country2,
    }
    label = ""

    for name, lookup_func in lookup_chain.items():
        label = lookup_func(country_lower)
        if label:
            logger.debug(f"get_con_lab({country_lower}): Found label '{label}' via {name}")
            break

    logger.info(f"?????? get_con_lab: {country_lower=}, {label=}")
    logger.info(f"?????? get_con_lab: {start_get_country2=}, {country=}, {separator=}")

    return label


__all__ = [
    "get_type_lab",
    "get_con_lab",
    "get_type_country",
]
