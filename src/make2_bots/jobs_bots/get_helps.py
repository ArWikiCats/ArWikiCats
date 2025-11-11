#!/usr/bin/python3
"""Utility helpers for extracting country labels from category names."""

from typing import Dict, Tuple, List

from ...helps.print_bot import output_test4


GET_COUNTRY_CACHE: Dict[Tuple[str, str], Tuple[str, str]] = {}


def get_con_3(cate: str, keys: List[str], category_type: str) -> Tuple[str, str]:
    """Retrieve country information based on category and keys.

    Args:
        cate: The category string to be processed.
        keys: Candidate prefixes used to derive the country name.
        category_type: The type of information being processed, e.g., "nat".

    Returns:
        A tuple containing the remaining category string and the detected
        country prefix. Empty strings are returned if nothing matches.
    """

    cache_key = (cate, category_type)
    if cache_key in GET_COUNTRY_CACHE:
        return GET_COUNTRY_CACHE[cache_key]

    category_suffix: str = ""
    country_prefix: str = ""

    for key in keys:
        candidate_prefixes: Dict[int, str] = {}
        if category_suffix:
            break

        candidate_prefixes[2] = f"{key.lower()} "

        if category_type == "nat":
            candidate_prefixes[1] = f"{key.lower().strip()} people "

        if key.startswith("the "):
            candidate_prefixes[3] = key[len("the ") :]

        for option_index in [1, 2, 3, 4]:
            prefix_candidate = candidate_prefixes.get(option_index)
            if not prefix_candidate:
                continue

            if cate.lower().startswith(prefix_candidate.lower()):
                country_prefix = key
                category_suffix = cate[len(prefix_candidate) :].strip()
                output_test4(
                    f'<<lightyellow>>>>>> get_con_3 start_th key_:{option_index} "{prefix_candidate}", '
                    f'fo_3:"{category_suffix}",country_start:"{country_prefix}"'
                )
                break

    GET_COUNTRY_CACHE[cache_key] = (category_suffix, country_prefix)

    if category_suffix and country_prefix:
        output_test4(
            f'<<lightpurple>>>>>> test_4.py country_start:"{country_prefix}",' \
            f'get_con_3 fo_3:"{category_suffix}",Type:{category_type}'
        )

    return category_suffix, country_prefix
