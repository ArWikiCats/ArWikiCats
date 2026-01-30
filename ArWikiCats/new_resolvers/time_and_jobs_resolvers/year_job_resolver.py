#!/usr/bin/python3
"""
TODO: use this code in flowworks

Examples:
    - en: 18th-century nobility
    - bad arabic: (نبلاء القرن 18)
    - good arabic: (نبلاء في القرن 18)
More examples:
    "Category:21st-century yemeni writers": "تصنيف:كتاب يمنيون في القرن 21",
    "Category:21st-century New Zealand writers": "تصنيف:كتاب نيوزيلنديون في القرن 21",

"""

import functools

import logging
from ...time_formats.time_to_arabic import convert_time_to_arabic, match_time_en_first
from ...translations_formats import FormatDataFrom, MultiDataFormatterYearAndFrom
from ..jobs_resolvers import main_jobs_resolvers

logger = logging.getLogger(__name__)

jobs_part_labels = {
    "lgbtq people": "أعلام إل جي بي تي كيو",
    "princes": "أمراء",
    "people": "أشخاص",
    "women": "نساء",
    "womens": "نساء",
    "women's": "نساء",
    "female": "نساء",
}

formatted_data = {
    "{year1} {country1}": "{country1} في {year1}",
}


@functools.lru_cache(maxsize=10000)
def get_job_label(text: str) -> str:
    text = normalize_text(text)
    result = jobs_part_labels.get(text) or main_jobs_resolvers(text) or ""

    return result


def normalize_text(text):
    text = text.lower().replace("category:", "")
    text = text.replace("sportspeople", "sports-people")
    text = text.replace(" the ", " ")
    # text = text.replace("republic of", "republic-of")
    text = text.removeprefix("the ")
    return text.strip()


@functools.lru_cache(maxsize=10000)
def match_key_callback(text: str) -> str:
    """Match the country part from 'job from country'."""
    # replace all formatted_data keys from text
    # text = text.replace("{year1} deaths from", "").replace("{year1}", "")

    keys_to_replace = [
        x.replace("{country1}", "").strip() for x in formatted_data.keys() if x.replace("{country1}", "").strip()
    ]
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
        search_callback=get_job_label,
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


@functools.lru_cache(maxsize=10000)
def resolve_year_job_countries(category: str) -> str:
    """Resolve year and job from countries using multi_bot_v4."""
    logger.debug(f"<<yellow>> start {category=}")

    category = normalize_text(category)

    _bot = multi_bot_v4()
    result = _bot.create_label(category)

    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "resolve_year_job_countries",
]
