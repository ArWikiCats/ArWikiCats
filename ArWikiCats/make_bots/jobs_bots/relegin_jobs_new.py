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

    formatted_data = {
        "female {job_en}": "{job_ar}",
        "female {rele_en}": "{rele_ar}",

        "female {rele_en} {job_en}": "{job_ar} {rele_ar}",
        "female {job_en} {rele_en}": "{job_ar} {rele_ar}",

        "{rele_en} {job_en}": "{job_ar} {rele_ar}",
        "{job_en} {rele_en}": "{job_ar} {rele_ar}",

        "{rele_en} eugenicists": "عالمات {rele_ar} متخصصات في تحسين النسل",
        "{rele_en} female politicians who committed suicide": "سياسيات {rele_ar} أقدمن على الانتحار",
        "{rele_en} female contemporary artists": "فنانات {rele_ar} معاصرات",
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


@functools.lru_cache(maxsize=1)
def _load_mens_bot() -> MultiDataFormatterBase:
    relegins_data = {x: v["mens"] for x, v in RELIGIOUS_KEYS_PP.items() if v.get("mens")}

    formatted_data = {
        "{rele_en} {job_en}": "{job_ar} {rele_ar}",
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
