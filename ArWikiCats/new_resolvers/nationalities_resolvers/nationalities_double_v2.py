#!/usr/bin/python3
"""
"""
import functools

from ...helps import logger
from ...translations import countries_en_as_nationality_keys, All_Nat
from ...translations_formats import FormatDataDoubleV2
from ..nats_as_country_names import nats_keys_as_country_names

formatted_data = {
    # "jewish persian": "فرس يهود",
    "{en}": "{males}",

    # north american-jewish culture
    "{en} surnames": "ألقاب {female}",
    "{en} culture": "ثقافة {female}",
    "{en} families": "عائلات {female}",
    "{en} wars": "حروب {female}",
    "{en} television series": "مسلسلات تلفزيونية {female}",

    "{en} literature": "أدب {male}",
    "{en} history": "تاريخ {male}",
    "{en} cuisine": "مطبخ {male}",
    "{en} descent": "أصل {male}",
    "{en} diaspora": "شتات {male}",
}

nats_data = {
    x: v for x, v in All_Nat.items()
}
nats_data.update({
    x: v for x, v in nats_keys_as_country_names.items()
})


@functools.lru_cache(maxsize=1)
def double_bot() -> FormatDataDoubleV2:
    # Template data with both nationality and sport placeholders
    # "german jewish history": "تاريخ يهودي ألماني",

    # Create an instance of the FormatDataDoubleV2 class with the formatted data and data list
    _bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en}",
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
def resolve_by_nats_double_v2(category: str) -> str:
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
    "resolve_by_nats_double_v2",
]
