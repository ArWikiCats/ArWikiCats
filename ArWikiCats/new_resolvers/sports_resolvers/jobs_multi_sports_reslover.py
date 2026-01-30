#!/usr/bin/python3
"""
Bot for translating job-related and nationality-based categories.

This module provides functionality for matching and translating categories
related to jobs, nationalities, and multi-sports topics from English to Arabic.

"""

import functools

import logging
from ...translations_formats import FormatDataFrom, MultiDataFormatterYearAndFrom
from ..countries_names_resolvers.medalists_resolvers import medalists_data
from ..jobs_resolvers import main_jobs_resolvers

logger = logging.getLogger(__name__)

medalists_data = dict(
    sorted(
        medalists_data.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)
formatted_data = {
    "{game} {en_job}": "{ar_job} في {game}",
}


@functools.lru_cache(maxsize=10000)
def match_key_callback(text: str) -> str:
    orgtext = text
    text = text.replace("{game} ", "")
    logger.debug(f" match_key_callback: processed {orgtext=} into {text=}")
    return text.strip()


def get_game_label(text: str) -> str:
    label = medalists_data.get(text.lower(), "")
    logger.debug(f" get_game_label: for {text=} found {label=}")
    return label


def match_game_key(category_lower: str) -> str:
    logger.debug(f" match_game_key: category_lower: {category_lower}")
    for sport_prefix, sport_label in medalists_data.items():
        prefix_pattern = f"{sport_prefix} ".lower()
        if category_lower.startswith(prefix_pattern):
            logger.debug(
                f'jobs_in_multi_sports match: prefix="{prefix_pattern}", '
                f'label="{sport_label}", sport_prefix="{sport_prefix}"'
            )
            return sport_prefix
    return ""


@functools.lru_cache(maxsize=1)
def multi_bot_v4() -> MultiDataFormatterYearAndFrom:
    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{en_job}",
        value_placeholder="{ar_job}",
        search_callback=main_jobs_resolvers,
        match_key_callback=match_key_callback,
    )
    game_bot = FormatDataFrom(
        formatted_data={},
        key_placeholder="{game}",
        value_placeholder="{game}",
        search_callback=get_game_label,
        match_key_callback=match_game_key,
    )
    return MultiDataFormatterYearAndFrom(
        country_bot=country_bot,
        year_bot=game_bot,
        other_key_first=True,
    )


@functools.lru_cache(maxsize=10000)
def jobs_in_multi_sports(category: str) -> str:
    category = category.lower().replace("category:", "")
    category = category.replace("_", " ").lower()
    category = category.replace("olympics", "olympic")

    logger.debug(f"<<yellow>> start: {category=}")
    yc_bot = multi_bot_v4()

    result = yc_bot.search_all_category(category)

    logger.info(f"<<yellow>> end: {category=}, {result=}")
    return result or ""


__all__ = [
    "jobs_in_multi_sports",
]
