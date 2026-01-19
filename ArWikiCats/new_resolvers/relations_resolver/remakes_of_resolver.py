#!/usr/bin/python3
""" """

import functools

from ArWikiCats.translations_formats.DataModel.model_data_v2 import MultiDataFormatterBaseV2

from ...helps import logger
from ...translations import All_Nat
from ...translations_formats import format_multi_data_v2

formatted_data = {
    # American remakes of Argentine films
    "{en_1} remakes of {en_2} films": "أفلام {female_1} مأخوذة من أفلام {female_2}",
    "{en_1} remakes of {en_2} television series": "مسلسلات تلفزيونية {female_1} مأخوذة من مسلسلات تلفزيونية {female_2}",
    "television remakes of films": "مسلسلات تلفزيونية مأخوذة من أفلام",
}


nats_data_1 = {x: {"female_1": v["female"]} for x, v in All_Nat.items()}
nats_data_2 = {x: {"female_2": v["female"]} for x, v in All_Nat.items()}


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    _bot = format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=nats_data_1,
        data_list2=nats_data_2,
        key_placeholder="{en_1}",
        key2_placeholder="{en_2}",
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
def resolve_remakes_of_resolver(category: str) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start resolve_remakes_of_resolver: {category=}")

    # Handling special case: "television remakes of films"
    if category == "television remakes of films":
        return "مسلسلات تلفزيونية مأخوذة من أفلام"

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)
    logger.info_if_or_debug(f"<<yellow>> end resolve_remakes_of_resolver: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_remakes_of_resolver",
]
