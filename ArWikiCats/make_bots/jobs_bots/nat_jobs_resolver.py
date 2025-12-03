"""
This module provides functionality to translate category titles
"""

import functools

from ...translations import Nat_mens, jobs_mens_data
from ...translations_formats import format_multi_data, MultiDataFormatterBase


formatted_data = {
    "{en_job} people": "{ar_job}",
    "{en_nat} people": "{ar_nat}",  # 187
    "{en_nat} male {en_job}": "{ar_job} ذكور {ar_nat}",
    "{en_nat} {en_job}": "{ar_job} {ar_nat}",
}


@functools.lru_cache(maxsize=1)
def _bot_multi() -> MultiDataFormatterBase:
    Nat_mens_new = {x: v for x, v in Nat_mens.items() if "-american" not in x}
    return format_multi_data(
        formatted_data=formatted_data,
        data_list=Nat_mens_new,
        key_placeholder="{en_nat}",
        value_placeholder="{ar_nat}",
        data_list2=jobs_mens_data,
        key2_placeholder="{en_job}",
        value2_placeholder="{ar_job}",
        text_after="",
        text_before="the ",
        use_other_formatted_data=True,
    )


@functools.lru_cache(maxsize=10000)
def get_label(category: str) -> str:
    nat_bot = _bot_multi()
    result = nat_bot.search_all(category)
    return result
