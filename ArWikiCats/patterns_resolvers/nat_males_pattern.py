"""
This module provides functionality to translate category titles
that follow a nationality pattern. It uses a pre-configured
bot to handle the translation logic.

"""

import functools
import re

import logging
from ..translations import (
    RELIGIOUS_KEYS_PP,
    All_Nat,
    all_country_with_nat,
    countries_en_as_nationality_keys,
)
from ..translations_formats import FormatDataV2
from .categories_patterns.NAT_males import NAT_DATA_MALES

logger = logging.getLogger(__name__)

countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]


def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "").replace("'", "")
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
    nats_data.update(
        {
            x: {
                "males": v["males"],
                "females": v["females"],
            }
            for x, v in RELIGIOUS_KEYS_PP.items()
            if x not in nats_data and v.get("males")
        }
    )

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        text_after=" people",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def resolve_nat_males_pattern(category: str) -> str:
    logger.debug(f"<<yellow>> start: {category=}")

    normalized_category = fix_keys(category)

    if normalized_category in countries_en_as_nationality_keys or normalized_category in countries_en_keys:
        logger.info(f"<<yellow>> skip resolve_nat_males_pattern: {category=}, [result=]")
        return ""

    yc_bot = _bot_new()
    result = yc_bot.create_label(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    logger.info(f"<<yellow>> end: {category=}, {result=}")

    return result or ""


__all__ = [
    "resolve_nat_males_pattern",
]
