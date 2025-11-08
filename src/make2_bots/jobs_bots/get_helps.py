"""Utility helpers for extracting country labels from category names."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Tuple

from .utils import cached_lookup, log_debug

GET_COUNTRY_CACHE: dict[str, Tuple[str, str]] = {}


def _match_prefix(category: str, key: str, *, category_type: str) -> Tuple[str, str]:
    """Attempt to match a prefix for a single key.

    Args:
        category: Raw category string to inspect.
        key: Candidate key from the lookup table.
        category_type: Type of category, e.g. ``"nat"``.

    Returns:
        A tuple containing the trimmed category suffix and the detected key.
        Empty strings are returned when the prefix does not match.
    """

    candidate_prefixes: dict[int, str] = {2: f"{key.lower()} "}
    if category_type == "nat":
        candidate_prefixes[1] = f"{key.lower().strip()} people "
    if key.startswith("the "):
        candidate_prefixes[3] = key[len("the ") :]

    category_suffix = ""
    for option_index in [1, 2, 3, 4]:
        prefix_candidate = candidate_prefixes.get(option_index)
        if not prefix_candidate:
            continue
        if category.lower().startswith(prefix_candidate.lower()):
            category_suffix = category[len(prefix_candidate) :].strip()
            log_debug(
                '<<lightyellow>>>>>> get_con_3 start_th key_:%s "%s", fo_3:"%s",contry_start:"%s"',
                option_index,
                prefix_candidate,
                category_suffix,
                key,
            )
            return category_suffix, key
    return "", ""


def get_con_3(
    category: str,
    keys: Iterable[str],
    category_type: str,
) -> Tuple[str, str]:
    """Retrieve country information based on category and keys.

    Args:
        category: The category string to be processed.
        keys: Candidate prefixes used to derive the country name.
        category_type: The type of information being processed, e.g., ``"nat"``.

    Returns:
        A tuple containing the remaining category string and the detected
        country prefix. Empty strings are returned if nothing matches.
    """

    def _compute() -> Tuple[str, str]:
        category_suffix = ""
        country_prefix = ""
        for key in keys:
            category_suffix, country_prefix = _match_prefix(category, key, category_type=category_type)
            if category_suffix:
                break
        if category_suffix and country_prefix:
            log_debug(
                '<<lightpurple>>>>>> test_4.py contry_start:"%s",get_con_3 fo_3:"%s",Type:%s',
                country_prefix,
                category_suffix,
                category_type,
            )
        return category_suffix, country_prefix

    return cached_lookup(GET_COUNTRY_CACHE, (category, category_type), _compute)
