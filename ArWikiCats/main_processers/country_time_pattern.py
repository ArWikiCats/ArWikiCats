"""

This module provides functionality to translate category titles
that follow a 'country-year' pattern. It uses a pre-configured
bot (`yc_bot`) to handle the translation logic.
"""

import functools
from ..translations import all_country_ar
from ..translations_formats import format_year_country_data, MultiDataFormatterBaseYear

from .categories_patterns.COUNTRY_YEAR import COUNTRY_YEAR_DATA


@functools.lru_cache(maxsize=1)
def _bot() -> MultiDataFormatterBaseYear:
    return format_year_country_data(
        formatted_data=COUNTRY_YEAR_DATA,
        data_list=all_country_ar,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        key2_placeholder="{year1}",
        value2_placeholder="{year1}",
        text_after="",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def get_label(category: str) -> str:
    yc_bot = _bot()
    result = yc_bot.create_label(category)
    if not result:
        normalized_category = category.lower().replace("category:", "")
        # Only call again if the string is different after normalization
        if normalized_category != category:
            result = yc_bot.create_label(normalized_category)
    return result or ""
