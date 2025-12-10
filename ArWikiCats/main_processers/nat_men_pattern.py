"""
This module provides functionality to translate category titles
that follow a nationality pattern. It uses a pre-configured
bot to handle the translation logic.

TODO: create v2 code like (nats_time_v2.py) to handle arabic nats keys like: (males, females, male, female, the_male, the_female) not only males


"""

import functools

from ..translations import Nat_mens
from ..translations_formats import FormatData
from .categories_patterns.NAT_males import NAT_DATA_MALES


@functools.lru_cache(maxsize=1)
def _bot() -> FormatData:
    Nat_mens_new = {x: v for x, v in Nat_mens.items() if "-american" not in x}

    return FormatData(
        formatted_data=NAT_DATA_MALES,
        data_list=Nat_mens_new,
        key_placeholder="{en_nat}",
        value_placeholder="{nat_men1}",
        text_after="",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def get_label(category: str) -> str:
    nat_bot = _bot()

    result = nat_bot.search(category)
    if not result:
        normalized_category = category.lower().replace("category:", "")
        # Only call again if the string is different after normalization
        if normalized_category != category:
            result = nat_bot.search(normalized_category)
    return result or ""
