#!/usr/bin/python3
"""
!
"""

import functools

from ...helps.log import logger
from ...translations import RELIGIOUS_KEYS_PP, jobs_mens_data
from ...translations_formats import format_multi_data, MultiDataFormatterBase


@functools.lru_cache(maxsize=1)
def _load_multi_bot() -> MultiDataFormatterBase:
    relegins_data = {x: v["mens"] for x, v in RELIGIOUS_KEYS_PP.items() if v.get("mens")}

    formatted_data = {
        "{rele_en} {job_en}": "{rele_ar} {job_ar}",
    }

    return format_multi_data(
        formatted_data=formatted_data,
        data_list=relegins_data,
        key_placeholder="{rele_en}",
        value_placeholder="{rele_ar}",
        data_list2=jobs_mens_data,
        key2_placeholder="{job_en}",
        value2_placeholder="{job_ar}",
    )


@functools.lru_cache(maxsize=1000)
def get_en_ar_is_p17_label_multi(category: str) -> str:
    nat_bot = _load_multi_bot()
    return nat_bot.search(category)


@functools.lru_cache(maxsize=None)
def new_relegins_jobs_with_suffix(cate: str) -> str:
    """
    """
    logger.debug(f"\t xx start: <<lightred>>try_relegins_jobs_with_suffix >> <<lightpurple>> {cate=}")

    nat_bot = _load_multi_bot()
    return nat_bot.search(cate)
