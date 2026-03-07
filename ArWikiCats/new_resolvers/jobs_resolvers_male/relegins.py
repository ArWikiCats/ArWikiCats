#!/usr/bin/python3
"""
copied from ArWikiCats/new_resolvers/jobs_resolvers/relegin_jobs_new.py
"""

import functools
import logging

from ...translations import RELIGIOUS_KEYS_PP, jobs_mens_data
from ...translations_formats import MultiDataFormatterBase, format_multi_data

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=1)
def _load_mens_bot() -> MultiDataFormatterBase:
    """
    Builds and returns a MultiDataFormatterBase configured for male-focused religion and job category translations.

    The formatter maps English category patterns that reference male gender or male-specific groupings to their Arabic equivalents, using the module's male religion entries and male job dataset. It includes predefined templates, entries derived from NAT_BEFORE_OCC_BASE when present in the male jobs data, and a small manual extension for philosophers and theologians.

    Returns:
        MultiDataFormatterBase: Formatter that resolves English male/religion/job category patterns to Arabic strings.
    """
    religions_data = {x: v["males"] for x, v in RELIGIOUS_KEYS_PP.items() if v.get("males")}

    # moved to ArWikiCats/new_resolvers/jobs_resolvers_male/relegins.py
    formatted_data = {
        "{job_en}": "{job_ar}",
        "male {job_en}": "{job_ar} ذكور",

        "{rele_en}": "{rele_ar}",
        "male {rele_en}": "{rele_ar} ذكور",

        "{rele_en} {job_en}": "{job_ar} {rele_ar}",
        "{rele_en} male {job_en}": "{job_ar} ذكور {rele_ar}",

        "{job_en} {rele_en}": "{job_ar} {rele_ar}",
        "{job_en} male {rele_en}": "{job_ar} ذكور {rele_ar}",
    }

    jobs_data = dict(jobs_mens_data)

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

    return category.strip()


@functools.lru_cache(maxsize=10000)
def new_religions_jobs_for_males(category: str) -> str:
    """
    Resolve a translated Arabic label for a religious job category, preferring male-specific forms before female-specific forms.

    Parameters:
        category (str): Category key to translate; the input is normalized (lowercased, certain tokens replaced, and whitespace trimmed) before lookup.

    Returns:
        Translated Arabic category string if a match is found, otherwise an empty string.
    """
    category = fix_keys(category)
    logger.debug(f"\t xx start: <<lightred>> >> <<lightpurple>> {category=}")

    nat_bot = _load_mens_bot()
    return nat_bot.search_all_category(category)


__all__ = [
    "new_religions_jobs_for_males",
]
