#!/usr/bin/python3
"""

"""

import functools

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import (
    film_Keys_For_female,
    television_keys,
    tyty_data,
)
from ...translations_formats import format_multi_data


class FilmKeysBot:
    """Thin wrapper to expose a search method for film key formatting."""

    def __init__(self) -> None:
        self.bot = format_multi_data(
            formatted_data={"{en1} {en2}":"<ar1> <ar2>"},
            data_list=film_Keys_For_female,
            data_list2=film_Keys_For_female,
            key_placeholder="{en1}",
            value_placeholder="<ar1>",
            key2_placeholder="{en2}",
            value2_placeholder="<ar2>",
        )

    def search(self, category: str) -> str:
        return self.bot.search(category)


@functools.lru_cache(maxsize=1)
def _load_bot():
    return FilmKeysBot()


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

        prefix = normalized_identifier[: -len(suffix)].strip()
        logger.debug(f'<<lightblue>> {prefix=}, endswith:"{suffix}" ')
        bot = _load_bot()
        prefix_label = bot.search(prefix.strip())

        if prefix_label and "{tyty}" in prefix_label:
            resolved_label = prefix_label.format(tyty=suffix_translation)
            logger.info(f'<<lightblue>> get_Films_key_CAO: new {resolved_label=} ')
            return resolved_label

    return ""
