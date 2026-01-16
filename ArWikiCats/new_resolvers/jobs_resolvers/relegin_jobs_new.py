#!/usr/bin/python3
"""
!
"""

import functools
import re

from ...helps import logger
from ...translations import RELIGIOUS_KEYS_PP, jobs_mens_data, jobs_womens_data
from ...translations_formats import MultiDataFormatterBase, format_multi_data

REGEX_WOMENS = re.compile(r"\b(womens|women)\b", re.I)

NAT_BEFORE_OCC_BASE = [
    "murdered abroad",
    "contemporary",
    "tour de france stage winners",
    "deafblind",
    "deaf",
    "blind",
    "jews",
    # "women's rights activists",
    "human rights activists",
    "imprisoned",
    "imprisoned abroad",
    "conservationists",
    "expatriate",
    "defectors",
    "scholars of islam",
    "scholars-of-islam",
    "amputees",
    "executed abroad",
    "executed",
    "emigrants",
]


@functools.lru_cache(maxsize=1)
def _load_womens_bot() -> MultiDataFormatterBase:
    religions_data = {x: v["females"] for x, v in RELIGIOUS_KEYS_PP.items() if v.get("females")}

    female_formatted_data = {
        "female {job_en}": "{job_ar}",
        "people female {rele_en}": "{rele_ar}",
        "female {rele_en}": "{rele_ar}",
        "female {rele_en} {job_en}": "{job_ar} {rele_ar}",
        "female {job_en} {rele_en}": "{job_ar} {rele_ar}",
        "{rele_en} female {job_en}": "{job_ar} {rele_ar}",
        "{job_en} female {rele_en}": "{job_ar} {rele_ar}",
        "{rele_en} female saints": "قديسات {rele_ar}",
        "{rele_en} female eugenicists": "عالمات {rele_ar} متخصصات في تحسين النسل",
        "{rele_en} female politicians who committed suicide": "سياسيات {rele_ar} أقدمن على الانتحار",
        "{rele_en} female contemporary artists": "فنانات {rele_ar} معاصرات",
    }

    return format_multi_data(
        formatted_data=female_formatted_data,
        data_list=religions_data,
        key_placeholder="{rele_en}",
        value_placeholder="{rele_ar}",
        data_list2=jobs_womens_data,
        key2_placeholder="{job_en}",
        value2_placeholder="{job_ar}",
        text_after="",
        search_first_part=True,
    )


@functools.lru_cache(maxsize=1)
def _load_mens_bot() -> MultiDataFormatterBase:
    religions_data = {x: v["males"] for x, v in RELIGIOUS_KEYS_PP.items() if v.get("males")}

    formatted_data = {
        "people {job_en}": "{job_ar}",
        "{job_en}": "{job_ar}",
        "people {rele_en}": "{rele_ar}",
        "{rele_en}": "{rele_ar}",
        "{rele_en} expatriate": "{rele_ar} مغتربون",
        # "{rele_en} {job_en}": "{job_ar} {rele_ar}",
        # "{job_en} {rele_en}": "{job_ar} {rele_ar}",
        "{rele_en} {job_en}": "{job_ar} {rele_ar}",
        "{job_en} {rele_en}": "{job_ar} {rele_ar}",
        "male {job_en}": "{job_ar} ذكور",
        "male {rele_en}": "{rele_ar} ذكور",
        "{rele_en} male {job_en}": "{job_ar} ذكور {rele_ar}",
        "{job_en} male {rele_en}": "{job_ar} ذكور {rele_ar}",
        "fictional {rele_en} religious workers": "عمال دينيون {rele_ar} خياليون",
        "{rele_en} religious workers": "عمال دينيون {rele_ar}",
        "{rele_en} emigrants": "{rele_ar} مهاجرون",
        "{rele_en} saints": "قديسون {rele_ar}",
        "{rele_en} eugenicists": "علماء {rele_ar} متخصصون في تحسين النسل",
        "{rele_en} politicians who committed suicide": "سياسيون {rele_ar} أقدموا على الانتحار",
        "{rele_en} contemporary artists": "فنانون {rele_ar} معاصرون",
        # TODO: ADD DATA FROM NAT_BEFORE_OCC_BASE
        "{rele_en} scholars of islam": "{rele_ar} باحثون عن الإسلام",
        "{rele_en} female rights activists": "{rele_ar} ناشطون في حقوق المرأة",
    }

    for x in NAT_BEFORE_OCC_BASE:
        if jobs_mens_data.get(x):
            formatted_data[f"{{rele_en}} {x}"] = f"{{rele_ar}} {jobs_mens_data[x]}"
            formatted_data[f"{x} {{rele_en}}"] = f"{{rele_ar}} {jobs_mens_data[x]}"

    jobs_data = dict(jobs_mens_data)
    jobs_data.update(
        {
            "philosophers and theologians": "فلاسفة ولاهوتيون",
        }
    )

    return format_multi_data(
        formatted_data=formatted_data,
        data_list=religions_data,
        key_placeholder="{rele_en}",
        value_placeholder="{rele_ar}",
        data_list2=jobs_data,
        key2_placeholder="{job_en}",
        value2_placeholder="{job_ar}",
        search_first_part=True,
    )


@functools.lru_cache(maxsize=None)
def womens_result(category: str) -> str:
    """ """
    logger.debug(f"\t xx start: <<lightred>>womens_result >> <<lightpurple>> {category=}")

    nat_bot = _load_womens_bot()
    return nat_bot.search_all_category(category)


@functools.lru_cache(maxsize=None)
def mens_result(category: str) -> str:
    """ """
    logger.debug(f"\t xx start: <<lightred>>mens_result >> <<lightpurple>> {category=}")

    nat_bot = _load_mens_bot()
    return nat_bot.search_all_category(category)


def fix_keys(category: str) -> str:
    category = category.replace("'", "").lower()

    replacements = {
        "expatriates": "expatriate",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    category = REGEX_WOMENS.sub("female", category)
    return category.strip()


@functools.lru_cache(maxsize=None)
def new_religions_jobs_with_suffix(category: str) -> str:
    """
    Resolves jobs for religious groups, handling both male and female variations.
    This function attempts to find a translation for a given category by checking
    against male-specific job/religion combinations first, and then female-specific
    combinations if no male-specific match is found.
    Args:
        category: The category string to translate.
    Returns:
        The translated Arabic category string, or an empty string if no match is found.
    """
    category = fix_keys(category)
    logger.debug(f"\t xx start: <<lightred>>new_religions_jobs_with_suffix >> <<lightpurple>> {category=}")

    return mens_result(category) or womens_result(category)


__all__ = [
    "new_religions_jobs_with_suffix",
    "mens_result",
    "womens_result",
]
