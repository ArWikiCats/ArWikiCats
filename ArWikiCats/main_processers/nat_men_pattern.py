"""
This module provides functionality to translate category titles
that follow a nationality pattern. It uses a pre-configured
bot to handle the translation logic.

"""

import functools
from ..patterns_resolvers.categories_patterns.NAT_males import NAT_DATA_MALES
from ..helps import logger
from ..translations import All_Nat
from ..new_resolvers.translations_formats import FormatDataV2


@functools.lru_cache(maxsize=1)
def _bot_new() -> FormatDataV2:

    formatted_data = dict(NAT_DATA_MALES)
    formatted_data.update({
        "{en_nat} diaspora": "شتات {male}",
    })

    nats_data={
        x: {
            "males": v["males"],
            "male": v["male"],
            "females": v["females"],
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
def resolve_nat_men_pattern_new(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_nat_men_pattern_new: {category=}")
    yc_bot=_bot_new()

    normalized_category=category.lower().replace("category:", "")
    result=yc_bot.create_label(normalized_category)

    if result and category.lower().startswith("category:"):
        result="تصنيف:" + result
    logger.debug(f"<<yellow>> end resolve_nat_men_pattern_new: {category=}, {result=}")

    return result or ""


__all__=[
    "resolve_nat_men_pattern_new",
]
