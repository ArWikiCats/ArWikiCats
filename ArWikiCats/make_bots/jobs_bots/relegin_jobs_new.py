#!/usr/bin/python3
"""
!
"""

import functools

from ...helps.log import logger
from ...translations import RELIGIOUS_KEYS_PP, jobs_mens_data
from ...translations_formats import format_multi_data, MultiDataFormatterBase


@functools.lru_cache(maxsize=1)
def _load_womens_bot() -> MultiDataFormatterBase:
    relegins_data = {x: v["womens"] for x, v in RELIGIOUS_KEYS_PP.items() if v.get("womens")}

    female_formatted_data = {
        "female {job_en}": "{job_ar}",
        "female {rele_en}": "{rele_ar}",

        "female {rele_en} {job_en}": "{job_ar} {rele_ar}",
        "female {job_en} {rele_en}": "{job_ar} {rele_ar}",

        "{rele_en} female {job_en}": "{job_ar} {rele_ar}",
        "{job_en} female {rele_en}": "{job_ar} {rele_ar}",

        "{rele_en} female eugenicists": "عالمات {rele_ar} متخصصات في تحسين النسل",
        "{rele_en} female politicians who committed suicide": "سياسيات {rele_ar} أقدمن على الانتحار",
        "{rele_en} female contemporary artists": "فنانات {rele_ar} معاصرات",
    }

    formatted_data = {}

    for x, v in female_formatted_data.items():
        formatted_data[x] = v
        if "female" in x:
            formatted_data[x.replace("female", "womens")] = v
            formatted_data[x.replace("female", "women's")] = v

    return format_multi_data(
        formatted_data=formatted_data,
        data_list=relegins_data,
        key_placeholder="{rele_en}",
        value_placeholder="{rele_ar}",
        data_list2=jobs_mens_data,
        key2_placeholder="{job_en}",
        value2_placeholder="{job_ar}",
        search_first_part=True
    )


@functools.lru_cache(maxsize=1)
def _load_mens_bot() -> MultiDataFormatterBase:
    relegins_data = {x: v["mens"] for x, v in RELIGIOUS_KEYS_PP.items() if v.get("mens")}

    formatted_data = {
        "{job_en}": "{job_ar}",
        "{rele_en}": "{rele_ar}",
        "{rele_en} expatriates": "{rele_ar} مغتربون",

        # "{rele_en} {job_en}": "{job_ar} {rele_ar}",
        # "{job_en} {rele_en}": "{job_ar} {rele_ar}",
        "{rele_en} {job_en}": "{job_ar} {rele_ar}",
        "{job_en} {rele_en}": "{job_ar} {rele_ar}",

        "male {job_en}": "{job_ar} ذكور",
        "male {rele_en}": "{rele_ar} ذكور",

        "{rele_en} male {job_en}": "{job_ar} ذكور {rele_ar}",
        "{job_en} male {rele_en}": "{job_ar} ذكور {rele_ar}",

        "{rele_en} scholars of islam": "{rele_ar} باحثون عن الإسلام",
        "{rele_en} convicted-of-murder": "{rele_ar} أدينوا بالقتل",
        "{rele_en} women's rights activists": "{rele_ar} ناشطون في حقوق المرأة",
        "{rele_en} eugenicists": "علماء {rele_ar} متخصصون في تحسين النسل",
        "{rele_en} politicians who committed suicide": "سياسيون {rele_ar} أقدموا على الانتحار",
        "{rele_en} contemporary artists": "فنانون {rele_ar} معاصرون",
    }
    return format_multi_data(
        formatted_data=formatted_data,
        data_list=relegins_data,
        key_placeholder="{rele_en}",
        value_placeholder="{rele_ar}",
        data_list2=jobs_mens_data,
        key2_placeholder="{job_en}",
        value2_placeholder="{job_ar}",
        search_first_part=True
    )


@functools.lru_cache(maxsize=None)
def womens_result(category: str) -> str:
    """
    """
    logger.debug(f"\t xx start: <<lightred>>mens_result >> <<lightpurple>> {category=}")

    nat_bot = _load_womens_bot()
    return nat_bot.search_all(category)


@functools.lru_cache(maxsize=None)
def mens_result(category: str) -> str:
    """
    """
    logger.debug(f"\t xx start: <<lightred>>mens_result >> <<lightpurple>> {category=}")

    nat_bot = _load_mens_bot()
    return nat_bot.search_all(category)


@functools.lru_cache(maxsize=None)
def new_relegins_jobs_with_suffix(category: str) -> str:
    """
    """
    logger.debug(f"\t xx start: <<lightred>>try_relegins_jobs_with_suffix >> <<lightpurple>> {category=}")

    return mens_result(category) or womens_result(category)
