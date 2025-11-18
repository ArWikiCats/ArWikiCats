#!/usr/bin/python3
"""Utility helpers for extracting country labels from category names."""
import functools
from typing import Dict, Tuple

from ...helps.print_bot import output_test4
from ...translations import All_Nat, RELIGIOUS_KEYS_PP, Nat_women, contries_from_nat

keys_data = {
    "nat": All_Nat,
    "Nat_women": Nat_women,
    "All_P17": {},
    "contries_from_nat": contries_from_nat,
    "religions": list(RELIGIOUS_KEYS_PP.keys()),
}


def get_keys(category_type):
    return keys_data.get(category_type, [])


@functools.lru_cache(maxsize=None)
def get_con_3(cate: str, category_type: str) -> Tuple[str, str]:
    """Fast and optimized version of get_con_3.

    This function identifies a matching prefix from the given keys and
    extracts the remaining suffix while preserving the original behavior.
    All comments are in English only as required.
    """
    keys = get_keys(category_type)
    # Pre-lower cate once for speed
    cate_lower = cate.lower()

    category_suffix: str = ""
    country_prefix: str = ""

    for key in keys:
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
        for option_index in (1, 2, 3, 4):
            prefix_candidate = candidate_prefixes.get(option_index)
            if not prefix_candidate:
                continue

            if cate_lower.startswith(prefix_candidate):
                country_prefix = key
                category_suffix = cate[len(prefix_candidate):].strip()

                output_test4(
                    f'<<lightyellow>>>>>> get_con_3 start_th key_:{option_index} '
                    f'"{prefix_candidate}", fo_3:"{category_suffix}",'
                    f'country_start:"{country_prefix}"'
                )

                break

    # Logging final result if match found
    if category_suffix and country_prefix:
        output_test4(
            f'<<lightpurple>>>>>> bot_te_4.py country_start:"{country_prefix}",'
            f'get_con_3 fo_3:"{category_suffix}",Type:{category_type}'
        )

    return category_suffix, country_prefix
