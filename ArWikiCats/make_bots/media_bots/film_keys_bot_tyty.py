#!/usr/bin/python3
"""

"""

import functools

from ...helps.log import logger
from ...translations import (
    film_Keys_for_female,
    Films_key_333,
    television_keys,
)

# sorted by len of " " in key
keys_female_sorted = dict(sorted(film_Keys_for_female.items(), key=lambda x: x[0].count(" "), reverse=True))

films_first = {
    "low-budget",
    "christmas",
    "lgbtq-related",
    "lgbt-related",
    "lgbtqrelated",
    "lgbtrelated",
    "upcoming",
}

search_multi_cache = {}


@functools.lru_cache(maxsize=None)
def search_multi(text: str) -> str:
    label = ""
    if search_multi_cache.get(text.lower()):
        return search_multi_cache[text.lower()]

    for second_part, second_label in keys_female_sorted.items():
        # ---
        if not text.endswith(second_part.lower()):
            continue
        # ---
        first_part = text[: -len(second_part)].strip()
        # ---
        second_key_lower = second_part.lower()
        first_key_lower = first_part.lower()
        # ---
        first_label = film_Keys_for_female.get(first_part, "")
        # ---
        logger.debug(f">??? search_multi: {first_part=} ({first_label}), {second_part=} ({second_label})")
        # ---
        if not first_label:
            continue

        paop_1 = f"{{tyty}} {first_label} {second_label}"

        # Adjust order for specific keywords
        if first_key_lower in films_first and second_key_lower not in films_first:
            paop_1 = f"{{tyty}} {second_label} {first_label}"

        search_multi_cache[f"{second_part} {first_part}"] = paop_1

        logger.info(f">??? search_multi: {paop_1=}")

        return paop_1

    return ""


@functools.lru_cache(maxsize=None)
# @dump_data(1)
def get_films_key_tyty(country_identifier: str) -> str:
    """
    Resolve labels for composite television keys used in film lookups.
    TODO: use FormatData
    """

    logger.debug(f'<<lightblue>> get_Films_key_CAO : {country_identifier=} ')
    normalized_identifier = country_identifier.lower().strip()

    for suffix, suffix_translation in television_keys.items():
        if not normalized_identifier.endswith(suffix.lower()):
            continue

        prefix = normalized_identifier[: -len(suffix)].strip()
        logger.debug(f'<<lightblue>> {prefix=}, endswith:"{suffix}" ')

        prefix_label = Films_key_333.get(prefix.strip())

        if prefix_label:
            resolved_label = f"{suffix_translation} {prefix_label}"
            logger.info(f'<<lightblue>> get_Films_key_CAO: new {resolved_label=} ')
            return resolved_label

        prefix_label = search_multi(prefix.strip())

        if prefix_label and "{tyty}" in prefix_label:
            resolved_label = prefix_label.format(tyty=suffix_translation)
            logger.info(f'<<lightblue>> get_Films_key_CAO: new {resolved_label=} ')
            return resolved_label

    return ""
