#!/usr/bin/python3
"""

Helper utilities for resolving film- and media-related categories.

TODO: replaced by resolve_films
"""

import functools

from ...helps.log import logger
from ...make_bots.jobs_bots.get_helps import get_suffix_with_keys
from ...translations import (
    All_Nat,
    Films_key_333,
    Films_key_CAO,
    Films_key_CAO_new_format,
    Films_key_For_nat,
    Nat_mens,
    Nat_women,
    en_is_nat_ar_is_women,
    television_keys,
)
from .resolve_films_labels import get_films_key_tyty_new
from .resolve_films_labels_and_time import get_films_key_tyty_new_and_time


@functools.lru_cache(maxsize=None)
def get_Films_key_CAO(country_identifier: str) -> str:
    """
    Resolve labels for composite television keys used in film lookups.
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


@functools.lru_cache(maxsize=None)
def films_with_nat(country_start: str, category_without_nat: str) -> str:
    """
    Resolve film labels based on nationality.
    Example:
        - country_start='yemeni', category_without_nat='science fiction film series endings'
        - result='سلاسل أفلام خيال علمي يمنية انتهت في'
    """
    country_name = Nat_mens[country_start] if category_without_nat == "people" else Nat_women[country_start]
    country_label = en_is_nat_ar_is_women.get(category_without_nat.strip(), "")

    result = ""
    if country_label:
        result = country_label.format(country_name)
        logger.debug(f"<<lightblue>> bot_te_4:Films: new {result=} ")

    if not result:
        country_label = (
            Films_key_CAO.get(category_without_nat)
            or get_Films_key_CAO(category_without_nat)
            or get_films_key_tyty_new_and_time(category_without_nat)
            or get_films_key_tyty_new(category_without_nat)
            or ""
        )
        if country_label:
            result = f"{country_label} {country_name}"
            if category_without_nat in Films_key_CAO_new_format:
                result = Films_key_CAO_new_format[category_without_nat].format(country_name)
            logger.debug(f"<<lightblue>> bot_te_4:Films: new {result=} , {category_without_nat=} ")

    if not result:
        country_label = Films_key_For_nat.get(category_without_nat, "")
        if country_label and "{}" in country_label:
            result = country_label.format(country_name)
            logger.debug(f"<<lightblue>> Films_key_For_nat:Films: new {result=} ")

    logger.info_if_or_debug(
        f"<<yellow>> end films_with_nat:{country_start=}, {category_without_nat=}, {result=}", result
    )
    return result


@functools.lru_cache(maxsize=None)
def Films(category: str) -> str:
    """Resolve the Arabic label for a given film category."""

    result = Films_key_CAO.get(category, "") or get_Films_key_CAO(category) or get_films_key_tyty_new(category) or ""

    logger.info_if_or_debug(f"<<yellow>> end Films: {category=}, {result=}", result)
    return result


@functools.lru_cache(maxsize=None)
def resolve_films_with_nat(category: str) -> str:
    """
    TODO: use class method
    """
    normalized_category = category.lower().replace("_", " ").replace("-", " ")

    logger.debug(f"<<yellow>> start resolve_films: {normalized_category=}")

    suffix, nat = get_suffix_with_keys(normalized_category, All_Nat, "nat")

    country_label = ""
    if suffix and nat:
        country_label = films_with_nat(nat, suffix)

    logger.info_if_or_debug(f"<<yellow>> end resolve_films:{category=}, {country_label=}", country_label)
    return country_label or ""


@functools.lru_cache(maxsize=None)
def resolve_films(category: str) -> str:
    """
    TODO: use class method
    """
    normalized_category = category.lower().replace("_", " ").replace("-", " ")

    logger.debug(f"<<yellow>> start resolve_films: {normalized_category=}")

    suffix, nat = get_suffix_with_keys(normalized_category, All_Nat, "nat")

    if suffix and nat:
        country_label = films_with_nat(nat, suffix)
    else:
        country_label = Films(normalized_category)

    logger.info_if_or_debug(f"<<yellow>> end resolve_films:{category=}, {country_label=}", country_label)
    return country_label or ""


__all__ = [
    "Films",
    "resolve_films",
]
