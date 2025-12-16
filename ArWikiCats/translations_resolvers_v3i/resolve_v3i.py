#!/usr/bin/python3
"""
TODO: use this code in flowworks
"""
import functools
from ..helps import logger
from ..translations_formats import YearFormatData, FormatDataFrom, MultiDataFormatterYearAndFrom
from ..translations_resolvers.new_jobs_resolver.mens import mens_resolver_labels

from ..new.time_to_arabic import (
    convert_time_to_arabic,
    match_time_en_first,
)


def get_label(text: str) -> str:
    data = {
        "writers from Hong Kong" : "كتاب من هونغ كونغ",
        "writers from yemen" : "كتاب من اليمن",
        "writers from Crown of Aragon" : "كتاب من تاج أرغون",
        "writers gg yemen" : "كتاب من اليمن",
    }
    logger.debug(f"search: {text=}")
    return data.get(text, "")


@functools.lru_cache(maxsize=1)
def multi_bot_v3() -> MultiDataFormatterYearAndFrom:

    formatted_data = {
        "{year1} {country1}": "{country1} في {year1}",
    }
    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        search_callback=get_label,
        match_key_callback=lambda x: x.replace("{year1}", "").strip()
    )

    year_bot = YearFormatData(
        key_placeholder="{year1}",
        value_placeholder="{year1}",
    )
    return MultiDataFormatterYearAndFrom(
        country_bot=country_bot,
        year_bot=year_bot,
        other_key_first=True,
    )


@functools.lru_cache(maxsize=1)
def multi_bot_v4() -> MultiDataFormatterYearAndFrom:

    formatted_data = {
        "{year1} {country1}": "{country1} في {year1}",
    }
    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        search_callback=get_label,
        match_key_callback=lambda x: x.replace("{year1}", "").strip()
    )
    year_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{year1}",
        value_placeholder="{year1}",
        search_callback=lambda x: convert_time_to_arabic(x),
        match_key_callback=lambda x: match_time_en_first(x),
    )
    return MultiDataFormatterYearAndFrom(
        country_bot=country_bot,
        year_bot=year_bot,
        other_key_first=True,
    )


def resolve_job_from_countries(category: str) -> str:
    """Resolve job from countries using the provided multi_bot_v3.country_bot."""
    _bot = multi_bot_v3()
    return _bot.country_bot.search_all(category)


def resolve_year_job_from_countries(category: str) -> str:
    """Resolve year and job from countries using multi_bot_v3."""
    _bot = multi_bot_v3()
    return _bot.search_all(category)
