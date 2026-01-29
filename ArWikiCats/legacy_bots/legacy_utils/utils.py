#!/usr/bin/python3
"""
This module provides functions for processing and generating labels for country names based on separators.
"""

import functools
import re
from typing import Tuple

from ...helps import getLogger

logger = getLogger(__name__)


def split_text_by_separator(separator: str, country: str) -> Tuple[str, str]:
    """
    Split a title-like string into two logical parts around a separator.

    Rules:
    - Case-insensitive search for the separator.
    - If the separator appears once:
        * Return both parts in lowercase (trimmed).
        * Apply special rules for "by" and "of"/"-of".
    - If the separator appears more than once:
        * Return both parts in original casing:
          - part_1: everything before the first separator (with " of" if needed).
          - part_2: everything after the first separator as a single block
                    (with leading "by " if needed).
    """

    # Normalize and short-circuit
    country = country.strip()
    if not country:
        return "", ""

    norm_country = country.lower()
    norm_sep = separator.lower()

    if norm_sep not in norm_country:
        return "", ""

    # Locate first occurrence (case-insensitive) and slice using original indices
    first_idx = norm_country.find(norm_sep)
    after_idx = first_idx + len(norm_sep)

    before_raw = country[:first_idx]
    after_raw = country[after_idx:]

    # Default parts: normalized lowercase (single-occurrence path)
    part_1 = before_raw.lower().strip()
    part_2 = after_raw.lower().strip()

    # Original-case slices (used when we detect multiple separators)
    type_t = before_raw.strip()
    country_t = after_raw.strip()

    # Does the separator appear more than once?
    has_multiple = norm_country.count(norm_sep) > 1
    base_sep = norm_sep.strip()

    # Apply special rules on the original-case variant first
    if base_sep == "by":
        country_t = f"by {country_t}".strip()

    if base_sep in {"of", "-of"}:
        type_t = f"{type_t} of".strip()

    if has_multiple:
        # Multi-occurrence path: keep original casing and group everything
        # after the first separator as one logical block.
        logger.info(
            "split_text_by_separator(multi): %r -> (%r, %r) [sep=%r]",
            country,
            type_t,
            country_t,
            separator,
        )
        return type_t, country_t

    # Single-occurrence path: apply special rules on normalized parts
    if base_sep == "by":
        part_2 = f"by {part_2}".strip()

    if base_sep in {"of", "-of"}:
        part_1 = f"{part_1} of".strip()

    logger.info(
        "split_text_by_separator(single): %r -> (%r, %r) [sep=%r]",
        country,
        part_1,
        part_2,
        separator,
    )
    return part_1, part_2


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
    text_strip = text.strip()

    if is_type:
        # Adjustments for type (separator should be at the end)
        if separator_stripped == "of" and not text_strip.endswith(separator_ends):
            return f"{text_strip} of"
        # elif separator_stripped == "spies for" and not text_strip.endswith(" spies"):
        #     return f"{text_strip} spies"
    else:
        # Adjustments for country (separator should be at the start)
        if separator_stripped == "by" and not text_strip.startswith(separator_starts):
            return f"by {text_strip}"
        elif separator_stripped == "for" and not text_strip.startswith(separator_starts):
            return f"for {text_strip}"

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
