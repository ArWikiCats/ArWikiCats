#!/usr/bin/python3
"""
"""
import functools

from ...helps import logger
from ...translations import countries_en_as_nationality_keys, All_Nat
from ...translations_formats import FormatDataDouble
from ..nats_as_country_names import nats_keys_as_country_names

female_data = {
    # north american-jewish culture
    "{en} jewish surnames": "ألقاب يهودية {female}",
    "{en}-jewish surnames": "ألقاب يهودية {female}",
    "{en}-jewish culture": "ثقافة يهودية {female}",
    "{en} jewish culture": "ثقافة يهودية {female}",
}

formatted_data = {
    "{en} literature": "أدب {male}",
    "{en} history": "تاريخ {male}",
    "{en} cuisine": "مطبخ {male}",
    "{en} descent": "أصل {male}",
    "{en} diaspora": "شتات {male}",
}

# film_keys_for_female
nats_data = {
    "german": "ألماني",
    "jewish": "يهودي",
}

nats_data = {
    x: v.get("male") for x, v in All_Nat.items() if v.get("male")
}
nats_data.update({
    x: v.get("male") for x, v in nats_keys_as_country_names.items()if v.get("male")
})


@functools.lru_cache(maxsize=1)
def double_bot() -> FormatDataDouble:
    # Template data with both nationality and sport placeholders
    # "german jewish history": "تاريخ يهودي ألماني",

    # Create an instance of the FormatDataDouble class with the formatted data and data list
    _bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en}",
        value_placeholder="{male}",
        splitter=r"[ \-]",
        sort_ar_labels=True,
    )

    return _bot


def fix_keys(category: str) -> str:
    """Fix known issues in category keys before searching.

    Args:
        category: The original category key.
    """
    # Fix specific known issues with category keys
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")
    return category.strip()


@functools.lru_cache(maxsize=10000)
def resolve_by_nats_double(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_by_nats: {category=}")

    if category in countries_en_as_nationality_keys:  # or category in countries_en_keys:
        logger.info(f"<<yellow>> skip resolve_by_nats: {category=}, [result=]")
        return ""

    category = fix_keys(category)
    nat_bot = double_bot()
    result = nat_bot.search_all_category(category)
    logger.info_if_or_debug(f"<<yellow>> end resolve_by_nats: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_by_nats_double",
]
