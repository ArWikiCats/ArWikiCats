"""

This module provides functionality to translate category titles
that follow a 'country-year' pattern. It uses a pre-configured
bot (`yc_bot`) to handle the translation logic.
"""

import functools
from ..translations import Nat_women
from ..translations_formats import format_year_country_data

NAT_YEAR_DATA = {
    "{year1} {en_nat} films": "أفلام {ar_nat} في {year1}",
}

yc_bot = format_year_country_data(
    formatted_data=NAT_YEAR_DATA,
    data_list=Nat_women,
    key_placeholder="{en_nat}",
    value_placeholder="{ar_nat}",
    key2_placeholder="{year1}",
    value2_placeholder="{year1}",
    text_after="",
    text_before="the ",
)


@functools.lru_cache(maxsize=10000)
def get_label(category: str) -> str:
    normalized_category = category.lower().replace("category:", "")
    result = yc_bot.create_label(normalized_category)
    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result
    return result or ""
