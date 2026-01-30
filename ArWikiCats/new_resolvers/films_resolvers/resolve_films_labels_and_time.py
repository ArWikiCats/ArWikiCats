#!/usr/bin/python3
""" """

import functools

from ...helps import getLogger
from ...time_formats.time_to_arabic import convert_time_to_arabic, match_time_en_first
from ...translations_formats import FormatDataFrom, MultiDataFormatterYearAndFrom
from .resolve_films_labels import get_films_key_tyty_new

logger = getLogger(__name__)

formatted_data = {
    "{year1} {en}": "{ar} في {year1}",
    "{year1} {en} debuts": "{ar} بدأ عرضها في {year1}",
    "{year1} {en} endings": "{ar} انتهت في {year1}",
    "{year1} {en}-endings": "{ar} انتهت في {year1}",
}


@functools.lru_cache(maxsize=10000)
def match_key_callback(text: str) -> str:
    """
    Extracts and normalizes the country/key component from a category-like text.

    Strips the suffixes " debuts", " endings", and "-endings", removes the "{year1} " placeholder, and trims surrounding whitespace.

    Parameters:
        text (str): Input category text potentially containing year and suffix tokens.

    Returns:
        str: The extracted and trimmed key component (e.g., country or category fragment).
    """
    # replace all formatted_data keys from text
    # text = text.replace("{year1} deaths from", "").replace("{year1}", "")
    orgtext = text
    text = text.removesuffix(" debuts").removesuffix(" endings").removesuffix("-endings")
    text = text.replace("{year1} ", "")

    logger.debug(f" match_key_callback: processed {orgtext=} into {text=}")
    return text.strip()


@functools.lru_cache(maxsize=1)
def multi_bot_v4() -> MultiDataFormatterYearAndFrom:
    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        search_callback=get_films_key_tyty_new,
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
def get_films_key_tyty_new_and_time(category: str) -> str:
    category = category.lower().replace("category:", "")
    # if category dosen't start with number, return ""
    if not category or not category[0].isdigit():
        logger.debug(f"<<yellow>> end get_films_key_tyty_new_and_time: {category=}, no digit start")
        return ""

    logger.debug(f"<<yellow>> start get_films_key_tyty_new_and_time: {category=}")
    yc_bot = multi_bot_v4()

    if category == match_time_en_first(category):
        logger.info_if_or_debug(f"<<yellow>> end get_films_key_tyty_new_and_time: {category=}, no time match", "")
        return ""

    result = yc_bot.search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end get_films_key_tyty_new_and_time: {category=}, {result=}", result)
    return result or ""


def fetch_films_by_category(category):
    result = get_films_key_tyty_new_and_time(category) or get_films_key_tyty_new(category)
    return result


__all__ = [
    "fetch_films_by_category",
    "get_films_key_tyty_new_and_time",
    "get_films_key_tyty_new",
]
