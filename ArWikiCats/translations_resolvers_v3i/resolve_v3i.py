#!/usr/bin/python3
"""
TODO: use this code in flowworks
"""
import re
import functools
from ..make_bots.ma_bots.country2_lab import get_lab_for_country2
from ..helps import logger
from ..translations_formats import FormatDataFrom, MultiDataFormatterYearAndFrom
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

formatted_data = {
    "{year1} {country1}": "{country1} في {year1}",
    "{year1} deaths from {country1}": "وفيات بسبب {country1} في {year1}",
}


def get_job_label(text: str) -> str:
    return (
        jobs_part_labels.get(text) or
        new_jobs_resolver_label(text) or
        get_lab_for_country2(text) or
        ""
    )


def get_label_new(text: str) -> str:
    """Get the Arabic label for a 'job from country' category."""
    text = text.lower().replace(" the ", " ").strip()
    match = FROM_REGEX.match(text)
    logger.debug(f"get_label_new: {text=}")

    if not match:
        print(f"get_label_new: no match: {text=}")
        return get_lab_for_country2(text) or ""

    job_part = match.group(1)
    from_part = match.group(2)
    logger.debug(f"get_label_new: {job_part=}, {from_part=}")

    job_label = get_job_label(job_part)
    from_label = get_lab_for_country2(from_part)

    logger.debug(f"get_label_new: {job_label=}, {from_label=}")

    if job_label and from_label:
        return f"{job_label} من {from_label}"

    return ""


def match_key_callback(text: str) -> str:
    """Match the country part from 'job from country'."""
    # replace all formatted_data keys from text
    # text = text.replace("{year1} deaths from", "").replace("{year1}", "")

    keys_to_replace = [x.replace("{country1}", "").strip() for x in formatted_data.keys() if x.replace("{country1}", "").strip()]
    # sort by len
    keys_to_replace = sorted(
        keys_to_replace,
        key=lambda k: (-k.count(" "), -len(k)),
    )
    for key in keys_to_replace:
        if key in text:
            return text.replace(key, "").strip()
    return text.strip()


@functools.lru_cache(maxsize=1)
def multi_bot_v4() -> MultiDataFormatterYearAndFrom:

    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        search_callback=get_label_new,
        match_key_callback=match_key_callback,
    )
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
