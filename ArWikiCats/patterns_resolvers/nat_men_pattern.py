"""
This module provides functionality to translate category titles
that follow a nationality pattern. It uses a pre-configured
bot to handle the translation logic.

"""

import re
import functools
from .categories_patterns.NAT_males import NAT_DATA_MALES
from ..helps import logger, dump_data
from ..translations import All_Nat, all_country_with_nat
from ..translations_formats import FormatDataV2
from ..new_resolvers.nats_as_country_names import nats_keys_as_country_names_bad_keys

countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]


def fix_keys(category: str) -> str:
    category = category.replace("category:", "").replace("'", "").lower()
    category = re.sub(r"\bthe\b", "", category)
    category = re.sub(r"\s+", " ", category)

    replacements = {
        "expatriates": "expatriate",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    return category.strip()


@functools.lru_cache(maxsize=1)
def _bot_new() -> FormatDataV2:
    formatted_data = dict(NAT_DATA_MALES)
    formatted_data = {fix_keys(k): v for k, v in formatted_data.items()}
    formatted_data.update(
        {
            "{en_nat} diaspora": "شتات {male}",
        }
    )

    nats_data = {
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
        text_after=" people",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
# @dump_data(1)
def resolve_nat_men_pattern_new(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_nat_men_pattern_new: {category=}")

    normalized_category = fix_keys(category)

    if normalized_category in nats_keys_as_country_names_bad_keys or normalized_category in countries_en_keys:
        logger.info(f"<<yellow>> skip mens_resolver_labels: {category=}, [result=]")
        return ""

    yc_bot = _bot_new()
    result = yc_bot.create_label(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    logger.info_if_or_debug(f"<<yellow>> end resolve_nat_men_pattern_new: {category=}, {result=}", result)

    return result or ""


__all__ = [
    "resolve_nat_men_pattern_new",
]
