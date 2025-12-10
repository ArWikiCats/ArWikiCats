"""
This module provides functionality to translate category titles
that follow a nationality pattern. It uses a pre-configured
bot to handle the translation logic.

TODO: use resolve_nat_men_pattern_new to handle arabic nats keys like: (males, females, male, female, the_male, the_female) not only males


"""

import functools
from .categories_patterns.NAT_males import NAT_DATA_MALES
from ..translations import Nat_mens, All_Nat
from ..translations_formats import (
    FormatData,
    FormatDataV2,
)


@functools.lru_cache(maxsize=1)
def _bot() -> FormatData:
    # nat_mens_new = {x: v for x, v in Nat_mens.items() if "-american" not in x}

    return FormatData(
        formatted_data=NAT_DATA_MALES,
        data_list=Nat_mens,
        key_placeholder="{en_nat}",
        value_placeholder="{nat_men1}",
        text_after="",
        text_before="the ",
    )


@functools.lru_cache(maxsize=1)
def _bot_new() -> FormatDataV2:

    formatted_data = dict(NAT_DATA_MALES)

    nats_data = {
        x: {
            "nat_men1": v["males"]
        }
        for x, v in All_Nat.items()
        if v.get("males")
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        text_after="",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def resolve_nat_men_pattern(category: str) -> str:
    nat_bot = _bot()

    result = nat_bot.search(category)
    if not result:
        normalized_category = category.lower().replace("category:", "")
        # Only call again if the string is different after normalization
        if normalized_category != category:
            result = nat_bot.search(normalized_category)
    return result or ""


@functools.lru_cache(maxsize=10000)
def resolve_nat_men_pattern_new(category: str) -> str:
    yc_bot = _bot_new()

    normalized_category = category.lower().replace("category:", "")
    result = yc_bot.create_label(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    return result or ""


__all__ = [
    "resolve_nat_men_pattern",
    "resolve_nat_men_pattern_new",
]
