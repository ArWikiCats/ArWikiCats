#!/usr/bin/python3
"""
TODO: use this code in flowworks
"""
import re
import functools
from ..make_bots.ma_bots.country2_lab import get_lab_for_country2
from ..helps import logger
from ..translations_formats import YearFormatData, FormatDataFrom, MultiDataFormatterYearAndFrom
from ..translations_resolvers.new_jobs_resolver import new_jobs_resolver_label

from ..new.time_to_arabic import convert_time_to_arabic, match_time_en_first

FROM_REGEX = re.compile(r"^(.*?) from (.*?)$", re.I)

jobs_part_labels = {
    "people": "أشخاص",
    "women": "نساء",
    "womens": "نساء",
    "women's": "نساء",
    "female": "نساء",
}


def get_label_new(text: str) -> str:
    """Get the Arabic label for a 'job from country' category."""
    text = text.lower()
    match = FROM_REGEX.match(text)
    logger.debug(f"get_label_new: {text=}")

    if not match:
        logger.debug("get_label_new: no match")
        return ""

    job_part = match.group(1)
    from_part = match.group(2)
    logger.debug(f"get_label_new: {job_part=}, {from_part=}")

    job_label = (
        jobs_part_labels.get(job_part) or
        new_jobs_resolver_label(job_part) or
        get_lab_for_country2(job_part) or
        ""
    )
    from_label = get_lab_for_country2(from_part)

    logger.debug(f"get_label_new: {job_label=}, {from_label=}")

    if job_label and from_label:
        return f"{job_label} من {from_label}"

    return ""


@functools.lru_cache(maxsize=1)
def multi_bot_v3() -> MultiDataFormatterYearAndFrom:

    formatted_data = {
        "{year1} {country1}": "{country1} في {year1}",
    }
    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        search_callback=get_label_new,
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
        search_callback=get_label_new,
        match_key_callback=lambda x: x.replace("{year1}", "").strip()
    )
    # year_bot = YearFormatData(key_placeholder="{year1}", value_placeholder="{year1}")
    year_bot = FormatDataFrom(
        formatted_data={},
        key_placeholder="{year1}",
        value_placeholder="{year1}",
        search_callback=convert_time_to_arabic,
        match_key_callback=match_time_en_first,
    )
    return MultiDataFormatterYearAndFrom(
        country_bot=country_bot,
        year_bot=year_bot,
        other_key_first=True,
    )


def resolve_job_from_countries(category: str) -> str:
    """Resolve job from countries using the provided multi_bot_v4.country_bot."""
    _bot = multi_bot_v4()
    return _bot.country_bot.search_all(category)


def resolve_year_job_from_countries(category: str) -> str:
    """Resolve year and job from countries using multi_bot_v4."""
    _bot = multi_bot_v4()
    return _bot.search_all(category)
