#!/usr/bin/python3
"""
Utility helpers for extracting country labels from category names.

TODO: refactor the code
"""

import functools
from typing import Dict, Tuple

from ...helps.log import logger
from ...translations import RELIGIOUS_KEYS_PP, All_Nat, Nat_women, contries_from_nat

keys_data = {
    "nat": All_Nat,
    "Nat_women": Nat_women,
    "All_P17": {},
    "contries_from_nat": contries_from_nat,
    "religions": list(RELIGIOUS_KEYS_PP.keys()),
}


def get_keys(category_type: str):
    """Return the lookup table associated with the requested category type."""
    return keys_data.get(category_type, [])


def get_suffix_with_keys(cate: str, data_keys, category_type: str = "", check_the: bool = False) -> Tuple[str, str]:
    """Fast and optimized version of get_suffix.

    This function identifies a matching prefix from the given keys and
    extracts the remaining suffix while preserving the original behavior.
    All comments are in English only as required.
    """
    # Pre-lower cate once for speed
    cate_lower = cate.lower()

    category_suffix: str = ""
    country_prefix: str = ""

    cate2 = cate[4:] if cate.startswith("the ") else cate

    cate_lower2 = cate_lower[4:] if cate_lower.startswith("the ") else cate_lower

    for key in data_keys:
        if category_suffix:
            # A match has already been found; exit early
            break

        # Pre-lower key only once
        key_lower = key.lower().strip()

        # Build minimal prefix options
        # Index meanings are kept exactly as original logic
        candidate_prefixes: Dict[int, str] = {
            2: f"{key_lower} ",
        }

        # Add "people" pattern only when category_type == "nat"
        if category_type in ["nat", "Nat_women"]:
            candidate_prefixes[1] = f"{key_lower} people "

        # Add the "the <country>" special case
        if key.startswith("the "):
            candidate_prefixes[3] = key[4:].lower()

        # Try each prefix option in fixed order
        for option_index in (1, 2, 3, 4, 5):
            prefix_candidate = candidate_prefixes.get(option_index)
            if not prefix_candidate:
                continue

            if cate_lower.startswith(prefix_candidate):
                country_prefix = key
                category_suffix = cate[len(prefix_candidate) :].strip()

                logger.debug(
                    f"<<lightyellow>>>>>> get_suffix {prefix_candidate=}, {category_suffix=}, {country_prefix=}"
                )

                break

            if check_the and cate_lower2.startswith(prefix_candidate):
                country_prefix = key
                category_suffix = cate2[len(prefix_candidate) :].strip()

                logger.debug(
                    f"<<lightyellow>>>>>> get_suffix {prefix_candidate=}, {category_suffix=}, {country_prefix=}"
                )

                break

    # Logging final result if match found
    if category_suffix and country_prefix:
        logger.debug(f'<<lightpurple>>>>>> get_helps.py {country_prefix=}, "{category_suffix=}, {category_type=}')

    return category_suffix, country_prefix


@functools.lru_cache(maxsize=None)
def get_suffix(cate: str, category_type: str, check_the: bool = False) -> Tuple[str, str]:
    keys = get_keys(category_type)
    return get_suffix_with_keys(cate, keys, category_type, check_the)


__all__ = [
    "get_suffix_with_keys",
    "get_suffix",
]
