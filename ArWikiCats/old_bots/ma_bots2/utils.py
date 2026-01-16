#!/usr/bin/python3
"""
This module provides functions for processing and generating labels for country names based on separators.
"""

from typing import Tuple

from ...helps import logger


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
