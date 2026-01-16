#!/usr/bin/python3
"""
Utility helpers for extracting country/nationality labels from category names.

This module provides functions to identify nationality or country prefixes
in category strings and extract the remaining suffix for further processing.
"""

import functools
from dataclasses import dataclass
from typing import Iterable, Optional, Union

from ...helps import dump_data, logger
from ...translations import RELIGIOUS_KEYS_PP, All_Nat, Nat_women, countries_from_nat

# Type alias for keys data - can be dict or list
KeysDataType = Union[dict, list, Iterable[str]]

# Registry of category type to their corresponding lookup tables
CATEGORY_TYPE_REGISTRY: dict[str, KeysDataType] = {
    "nat": All_Nat,
    "Nat_women": Nat_women,
    "All_P17": {},
    "countries_from_nat": countries_from_nat,
    "religions": list(RELIGIOUS_KEYS_PP.keys()),
}

# Category types that support "people" suffix pattern
PEOPLE_SUFFIX_TYPES = frozenset({"nat", "Nat_women"})


@dataclass(frozen=True)
class PrefixMatch:
    """Represents a successful prefix match result."""

    country_prefix: str
    category_suffix: str

    def __bool__(self) -> bool:
        """Return True if both fields are non-empty."""
        return bool(self.country_prefix and self.category_suffix)


def get_keys(category_type: str) -> KeysDataType:
    """Return the lookup table associated with the requested category type.

    Args:
        category_type: The type of category lookup (e.g., 'nat', 'Nat_women').

    Returns:
        The corresponding lookup table, or empty list if not found.
    """
    return CATEGORY_TYPE_REGISTRY.get(category_type, [])


def _strip_the_prefix(text: str) -> str:
    """Remove 'the ' prefix from text if present.

    Args:
        text: The input text.

    Returns:
        Text without 'the ' prefix.
    """
    return text[4:] if text.startswith("the ") else text


def _build_candidate_prefixes(
    key_lower: str,
    key_original: str,
    category_type: str,
) -> list[str]:
    """Build a list of candidate prefixes to match against the category.

    The order of prefixes matters - more specific patterns come first.

    Args:
        key_lower: The lowercase version of the key.
        key_original: The original key (may have different casing).
        category_type: The type of category being processed.

    Returns:
        A list of candidate prefix patterns to try matching.
    """
    candidates = []

    # Pattern 1: "<nationality> people " (only for nationality types)
    if category_type in PEOPLE_SUFFIX_TYPES:
        candidates.append(f"{key_lower} people ")

    # Pattern 2: "<nationality> " (basic prefix)
    candidates.append(f"{key_lower} ")

    # Pattern 3: Handle "the <country>" special case
    if key_original.startswith("the "):
        candidates.append(key_original[4:].lower())

    return candidates


def _try_match_prefix(
    category_text: str,
    category_original: str,
    prefix: str,
    key: str,
) -> Optional[PrefixMatch]:
    """Try to match a prefix against the category text.

    Args:
        category_text: The lowercase category text to match against.
        category_original: The original category text (for suffix extraction).
        prefix: The prefix pattern to match.
        key: The original key associated with this prefix.

    Returns:
        PrefixMatch if successful, None otherwise.
    """
    if not category_text.startswith(prefix):
        return None

    suffix = category_original[len(prefix) :].strip()
    if not suffix:
        return None

    logger.debug(f"<<lightyellow>>>>>> get_suffix {prefix=}, " f"category_suffix={suffix}, country_prefix={key}")

    return PrefixMatch(country_prefix=key, category_suffix=suffix)


# @dump_data(1, input_keys=["category", "category_type", "check_the"])
def get_suffix_with_keys(
    category: str,
    data_keys: KeysDataType,
    category_type: str = "",
    check_the: bool = False,
) -> tuple[str, str]:
    """Extract nationality/country prefix and remaining suffix from a category.

    This function identifies a matching prefix from the given keys and
    extracts the remaining suffix. It tries multiple pattern variations
    to find a match.

    Args:
        category: The category string to analyze.
        data_keys: The collection of keys to match against.
        category_type: The type of category (affects matching patterns).
        check_the: If True, also try matching after stripping 'the ' prefix.

    Returns:
        A tuple of (category_suffix, country_prefix). Both empty if no match.

    Example:
        >>> get_suffix_with_keys("american actors", All_Nat, "nat")
        ("actors", "american")
    """
    category_lower = category.lower()

    # Prepare alternative versions without 'the ' prefix
    category_no_the = _strip_the_prefix(category)
    category_lower_no_the = _strip_the_prefix(category_lower)

    for key in data_keys:
        key_lower = key.lower().strip()
        candidate_prefixes = _build_candidate_prefixes(key_lower, key, category_type)

        for prefix in candidate_prefixes:
            # Try matching against the primary category
            match = _try_match_prefix(category_lower, category, prefix, key)
            if match:
                _log_final_match(match, category_type)
                return match.category_suffix, match.country_prefix

            # Try matching with 'the ' prefix stripped (if enabled)
            if check_the:
                match = _try_match_prefix(category_lower_no_the, category_no_the, prefix, key)
                if match:
                    _log_final_match(match, category_type)
                    return match.category_suffix, match.country_prefix

    return "", ""


def _log_final_match(match: PrefixMatch, category_type: str) -> None:
    """Log the final successful match.

    Args:
        match: The successful prefix match.
        category_type: The category type being processed.
    """
    logger.debug(
        f"<<lightpurple>>>>>> get_helps.py "
        f"country_prefix={match.country_prefix}, "
        f"category_suffix={match.category_suffix}, "
        f"{category_type=}"
    )


@functools.lru_cache(maxsize=None)
def get_suffix(
    category: str,
    category_type: str,
    check_the: bool = False,
) -> tuple[str, str]:
    """Cached wrapper for get_suffix_with_keys using registered keys.

    This function looks up the appropriate keys from the registry and
    delegates to get_suffix_with_keys.

    Args:
        category: The category string to analyze.
        category_type: The type of category (must be in CATEGORY_TYPE_REGISTRY).
        check_the: If True, also try matching after stripping 'the ' prefix.

    Returns:
        A tuple of (category_suffix, country_prefix). Both empty if no match.
    """
    keys = get_keys(category_type)
    return get_suffix_with_keys(category, keys, category_type, check_the)


__all__ = [
    "get_suffix_with_keys",
    "get_suffix",
    "get_keys",
    "CATEGORY_TYPE_REGISTRY",
]
