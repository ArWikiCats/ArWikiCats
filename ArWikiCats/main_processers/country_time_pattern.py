"""
"""

from ..translations import all_country_ar
from ..translations_formats import FormatYearCountryData

from .categories_patterns.COUNTRY_YEAR import COUNTRY_YEAR_DATA

yc_bot = FormatYearCountryData(
    formatted_data=COUNTRY_YEAR_DATA,
    data_list=all_country_ar,
    key_placeholder="{country1}",
    value_placeholder="{country1}",
    key2_placeholder="{year1}",
    value2_placeholder="{year1}",
    text_after="",
    text_before="the ",
)


def get_label(category) -> str:
    result = yc_bot.create_label(category)
    return result
