#!/usr/bin/python3
"""

"""

import functools

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import (
    tyty_data,
    television_keys,
)


@functools.lru_cache(maxsize=None)
@dump_data(1)
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

        prefix = normalized_identifier[: -len(suffix)].strip() + " {tyty_en}"
        logger.debug(f'<<lightblue>> {prefix=}, endswith:"{suffix}" ')
        prefix_label = tyty_data.get(prefix.strip(), "")

        if prefix_label and "{tyty}" in prefix_label:
            resolved_label = prefix_label.format(tyty=suffix_translation)
            logger.info(f'<<lightblue>> get_Films_key_CAO: new {resolved_label=} ')
            return resolved_label

    return ""
