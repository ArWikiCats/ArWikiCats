#!/usr/bin/python3
"""

Helper utilities for resolving film- and media-related categories.

TODO: refactor the code
"""

import functools

from ...helps.log import logger
from ...translations import (
    Films_key_333,
    Films_key_CAO,
    Films_key_CAO_new_format,
    Films_key_For_nat,
    Nat_mens,
    Nat_women,
    en_is_nat_ar_is_women,
    television_keys_female,
)


@functools.lru_cache(maxsize=None)
def get_Films_key_CAO(country_identifier: str) -> str:
    """
    Resolve labels for composite television keys used in film lookups.
    """

    logger.debug(f'<<lightblue>> get_Films_key_CAO : {country_identifier=} ')
    normalized_identifier = country_identifier.lower().strip()
    resolved_label = ""

    for suffix, suffix_translation in television_keys_female.items():
        if not normalized_identifier.endswith(suffix.lower()):
            continue

        prefix = normalized_identifier[: -len(suffix)].strip()
        logger.debug(f'<<lightblue>> {prefix=}, endswith:"{suffix}" ')
        prefix_label = Films_key_333.get(prefix.strip(), "")

        if not prefix_label:
            continue

        logger.debug(f'<<lightblue>> get_Films_key_CAO : {prefix=} ')

        if "{}" in prefix_label:
            resolved_label = prefix_label.format(tyty=suffix_translation)
        else:
            resolved_label = f"{suffix_translation} {prefix_label}"

        if resolved_label:
            logger.info(f'<<lightblue>> get_Films_key_CAO: new {resolved_label=} ')
            break

    return resolved_label


@functools.lru_cache(maxsize=None)
def Films(category: str, country_start: str, country_code: str) -> str:
    """Resolve the Arabic label for a given film category."""

    result = ""
    if country_code:
        country_name = Nat_mens[country_start] if country_code == "people" else Nat_women[country_start]
        country_label = en_is_nat_ar_is_women.get(country_code.strip(), "")

        if country_label:
            result = country_label.format(country_name)
            logger.debug(f'<<lightblue>> bot_te_4:Films: new {result=} ')

        if not result:
            country_label = Films_key_CAO.get(country_code, get_Films_key_CAO(country_code))
            if country_label:
                result = f"{country_label} {country_name}"
                if country_code in Films_key_CAO_new_format:
                    result = Films_key_CAO_new_format[country_code].format(country_name)
                logger.debug(f'<<lightblue>> bot_te_4:Films: new {result=} , {country_code=} ')

        if not result:
            country_label = Films_key_For_nat.get(country_code, "")
            if country_label:
                result = country_label.format(country_name)
                logger.debug(f'<<lightblue>> Films_key_For_nat:Films: new {result=} ')

    if not result:
        category_label = Films_key_CAO.get(category, "")
        if category_label:
            result = category_label
            logger.debug(f'<<lightblue>> test Films: {result=} ')

    if not result:
        result = get_Films_key_CAO(category)
        if result:
            logger.debug(f'<<lightblue>> test Films: new {result=} ')

    return result
