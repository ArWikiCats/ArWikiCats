"""

This module provides functionality to translate category titles
that follow a 'country-year' pattern. It uses a pre-configured
bot (`yc_bot`) to handle the translation logic.
"""

import functools

from ..translations import Nat_mens
from ..translations_formats import FormatData
from .categories_patterns.NAT import NAT_DATA


@functools.lru_cache(maxsize=1)
def _bot() -> FormatData:
    Nat_mens_new = {x: v for x, v in Nat_mens.items() if "-american" not in x}

    return FormatData(
        formatted_data=NAT_DATA,
        data_list=Nat_mens_new,
        key_placeholder="{en_nat}",
        value_placeholder="{nat_men1}",
        text_after="",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def get_label(category: str) -> str:
    yc_bot = _bot()

    result = yc_bot.search(category)
    if not result:
        normalized_category = category.lower().replace("category:", "")
        # Only call again if the string is different after normalization
        if normalized_category != category:
            result = yc_bot.search(normalized_category)
    return result or ""
