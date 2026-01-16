#!/usr/bin/python3
"""

"""

import functools

from ...helps import logger
from ...translations import (
    Films_key_333,
    television_keys,
)


@functools.lru_cache(maxsize=None)
def get_Films_key_CAO(country_identifier: str) -> str:
    """
    Resolve an Arabic label for a composite television-style film key.

    Given a country or category identifier that may be composed of a prefix and a known television suffix, match the suffix, look up the prefix label, and combine them into a localized Arabic label.

    Parameters:
        country_identifier (str): The input identifier (e.g., a composite television/category key) to resolve.

    Returns:
        str: The resolved Arabic label when a matching suffix and prefix are found, or an empty string if no resolution is possible.
    """

    logger.debug(f"<<lightblue>> get_Films_key_CAO : {country_identifier=} ")
    normalized_identifier = country_identifier.lower().strip()

    resolved_label = ""

    for suffix, suffix_translation in television_keys.items():
        if not normalized_identifier.endswith(suffix.lower()):
            continue

        prefix = normalized_identifier[: -len(suffix)].strip()
        logger.debug(f'<<lightblue>> {prefix=}, endswith:"{suffix}" ')

        prefix_label = Films_key_333.get(prefix.strip(), "")

        if not prefix_label:
            continue

        logger.debug(f"<<lightblue>> get_Films_key_CAO : {prefix=} ")

        resolved_label = f"{suffix_translation} {prefix_label}"

        if resolved_label:
            logger.info(f"<<lightblue>> get_Films_key_CAO: new {resolved_label=} ")
            break

    logger.info_if_or_debug(
        f"<<yellow>> end get_Films_key_CAO:{country_identifier=}, {resolved_label=}", resolved_label
    )
    return resolved_label


__all__ = [
    "get_Films_key_CAO",
]
