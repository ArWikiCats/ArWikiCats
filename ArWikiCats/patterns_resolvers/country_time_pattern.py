"""

This module provides functionality to translate category titles
that follow a 'country-year' pattern. It uses a pre-configured
bot (`yc_bot`) to handle the translation logic.
"""

import functools
import logging

from ..translations import COUNTRY_LABEL_OVERRIDES, US_STATES, all_country_ar
from ..translations_formats import MultiDataFormatterBaseYear, format_year_country_data
from .categories_patterns.COUNTRY_YEAR import COUNTRY_YEAR_DATA

logger = logging.getLogger(__name__)

# TODO: update countries_data with COUNTRY_LABEL_OVERRIDES after check any issues!


@functools.lru_cache(maxsize=1)
def load_bot() -> MultiDataFormatterBaseYear:
    countries_data = all_country_ar | US_STATES

    return format_year_country_data(
        formatted_data=COUNTRY_YEAR_DATA,
        data_list=countries_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        key2_placeholder="{year1}",
        value2_placeholder="{year1}",
        text_after="",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def resolve_country_time_pattern(category: str) -> str:
    logger.debug(f"<<yellow>> start {category=}")

    yc_bot = load_bot()
    result = yc_bot.search_all_category(category)

    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result or ""


__all__ = [
    "resolve_country_time_pattern",
]
