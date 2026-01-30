#!/usr/bin/python3
"""
!
"""

import functools
import logging
import re

from ...translations import RELIGIOUS_KEYS_PP, jobs_mens_data, jobs_womens_data
from ...translations_formats import MultiDataFormatterBase, format_multi_data

logger = logging.getLogger(__name__)

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
    """
    Builds and returns a MultiDataFormatterBase configured for male-focused religion and job category translations.

    The formatter maps English category patterns that reference male gender or male-specific groupings to their Arabic equivalents, using the module's male religion entries and male job dataset. It includes predefined templates, entries derived from NAT_BEFORE_OCC_BASE when present in the male jobs data, and a small manual extension for philosophers and theologians.

    Returns:
        MultiDataFormatterBase: Formatter that resolves English male/religion/job category patterns to Arabic strings.
    """
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


@functools.lru_cache(maxsize=10000)
def womens_result(category: str) -> str:
    """
    Resolve a female-focused translation for the given job or religious category.

    Parameters:
        category (str): Category key to match against the female-oriented job/religion translations.

    Returns:
        str: The matched translation string, or an empty string if no match is found.
    """
    logger.debug(f"\t xx start: <<lightred>> >> <<lightpurple>> {category=}")

    nat_bot = _load_womens_bot()
    return nat_bot.search_all_category(category)


@functools.lru_cache(maxsize=10000)
def mens_result(category: str) -> str:
    """
    Resolve a category into its male-gendered job/religion translation using the module's male formatter.

    Parameters:
        category (str): Category key or label to look up and format.

    Returns:
        str: The formatted translation for the given category, or an empty string if no match is found.
    """
    logger.debug(f"\t xx start: <<lightred>> >> <<lightpurple>> {category=}")

    nat_bot = _load_mens_bot()
    return nat_bot.search_all_category(category)


def fix_keys(category: str) -> str:
    """
    Normalize and standardize a category key string.

    Performs normalization by removing single quotes, converting to lowercase,
    replacing known plural forms and gender variants (e.g., "expatriates" -> "expatriate",
    "women"/"womens" -> "female"), and trimming surrounding whitespace.

    Parameters:
        category (str): The raw category key to normalize.

    Returns:
        str: The normalized category key.
    """
    category = category.replace("'", "").lower()

    replacements = {
        "expatriates": "expatriate",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    category = REGEX_WOMENS.sub("female", category)
    return category.strip()


@functools.lru_cache(maxsize=10000)
def new_religions_jobs_with_suffix(category: str) -> str:
    """
    Resolve a translated Arabic label for a religious job category, preferring male-specific forms before female-specific forms.

    Parameters:
        category (str): Category key to translate; the input is normalized (lowercased, certain tokens replaced, and whitespace trimmed) before lookup.

    Returns:
        Translated Arabic category string if a match is found, otherwise an empty string.
    """
    category = fix_keys(category)
    logger.debug(f"\t xx start: <<lightred>> >> <<lightpurple>> {category=}")

    return mens_result(category) or womens_result(category)


__all__ = [
    "new_religions_jobs_with_suffix",
    "mens_result",
    "womens_result",
]
