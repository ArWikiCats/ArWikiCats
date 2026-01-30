"""
Resolver for job-related category labels with gender-specific logic.
This module provides functions to translate categories combining jobs,
nationalities, and genders into idiomatic Arabic.
"""

import functools
import re

import logging
from ...translations import SPORT_KEY_RECORDS_BASE, All_Nat
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from .utils import fix_keys

logger = logging.getLogger(__name__)


def generate_jobs_data_dict() -> dict[str, dict[str, str]]:
    """
    Map English job identifiers to Arabic masculine, feminine, and inclusive labels.

    Each mapping value is a dictionary with keys `job_males`, `job_females`, and `both_jobs`, each holding the corresponding Arabic string for that job category.

    Returns:
        jobs_data (dict[str, dict[str, str]]): Mapping from an English job identifier (e.g., "actors") to a dict with Arabic forms under `job_males`, `job_females`, and `both_jobs`.
    """
    # "[ا-ي]+ون* و[ا-ي]+ات"
    jobs_data_new = {
        "bobsledders": {
            "job_males": "متزلجون جماعيون",
            "job_females": "متزلجات جماعيات",
            "both_jobs": "متزلجون ومتزلجات جماعيون",
        },
        "models": {"job_males": "عارضو أزياء", "job_females": "عارضات أزياء", "both_jobs": "عارضو وعارضات أزياء"},
        "actors": {"job_males": "ممثلون", "job_females": "ممثلات", "both_jobs": "ممثلون وممثلات"},
        "boxers": {"job_males": "ملاكمون", "job_females": "ملاكمات", "both_jobs": "ملاكمون وملاكمات"},
        "classical composers": {
            "job_males": "ملحنون كلاسيكيون",
            "job_females": "ملحنات كلاسيكيات",
            "both_jobs": "ملحنون وملحنات كلاسيكيون",
        },
        "composers": {"job_males": "ملحنون", "job_females": "ملحنات", "both_jobs": "ملحنون وملحنات"},
        "cyclists": {"job_males": "دراجون", "job_females": "دراجات", "both_jobs": "دراجون ودراجات"},
        "film actors": {"job_males": "ممثلو أفلام", "job_females": "ممثلات أفلام", "both_jobs": "ممثلو وممثلات أفلام"},
        "guitarists": {
            "job_males": "عازفو قيثارة",
            "job_females": "عازفات قيثارة",
            "both_jobs": "عازفو وعازفات قيثارة",
        },
        "singers": {"job_males": "مغنون", "job_females": "مغنيات", "both_jobs": "مغنون ومغنيات"},
        "television actors": {
            "job_males": "ممثلو تلفاز",
            "job_females": "ممثلات تلفاز",
            "both_jobs": "ممثلو وممثلات تلفاز",
        },
    }
    # TODO: Load from jobs_data_multi_one_word.json
    # jobs_data_new.update(open_json_file("jobs_data_multi_one_word.json"))

    return jobs_data_new


@functools.lru_cache(maxsize=1)
def generate_formatted_data() -> dict[str, str]:
    """
    Provide a mapping from English category patterns to Arabic template strings for gendered job and nationality phrases.

    Returns:
        dict[str, str]: Mapping where keys are English patterns containing placeholders (e.g., `{en_nat}`, `{job_en}`) and values are Arabic template strings using placeholders such as `{males}`, `{females}`, `{job_males}`, `{job_females}`, and `{both_jobs}`.
    """
    formatted_data = {
        "actresses": "ممثلات",
        "{en_nat} actresses": "ممثلات {females}",
        # [guitarists] = "عازفو وعازفات قيثارة"
        "{job_en}": "{both_jobs}",
        # [male guitarists] = "عازفو قيثارة"
        "male {job_en}": "{job_males}",
        # [american guitarists] = "عازفو وعازفات قيثارة أمريكيون"
        "{en_nat} {job_en}": "{both_jobs} {males}",
        # [american male guitarists] = "عازفو قيثارة أمريكيون"
        "{en_nat} male {job_en}": "{job_males} {males}",
        "male {en_nat} {job_en}": "{job_males} {males}",
        # [female guitarists] = "عازفات قيثارة"
        "female {job_en}": "{job_females}",
        # [american female guitarists] = "عازفات قيثارة أمريكيات"
        "{en_nat} female {job_en}": "{job_females} {females}",
        "female {en_nat} {job_en}": "{job_females} {females}",
        # test to add classical
        "classical {job_en}": "{both_jobs} كلاسيكيون",
        "male classical {job_en}": "{job_males} كلاسيكيون",
        "female classical {job_en}": "{job_females} كلاسيكيات",
        "{en_nat} classical {job_en}": "{both_jobs} كلاسيكيون {males}",
        "{en_nat} male classical {job_en}": "{job_males} كلاسيكيون {males}",
        "{en_nat} female classical {job_en}": "{job_females} كلاسيكيات {females}",
    }

    return formatted_data


@functools.lru_cache(maxsize=1)
def _job_bot() -> MultiDataFormatterBaseV2:
    jobs_data_new = generate_jobs_data_dict()

    nats_data = {
        x: {
            "males": v["males"],
            "females": v["females"],
        }
        for x, v in All_Nat.items()
        if v.get("males")
    }
    formatted_data = generate_formatted_data()

    return format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        data_list2=jobs_data_new,
        key2_placeholder="{job_en}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )


@functools.lru_cache(maxsize=10000)
def genders_jobs_resolver(category: str) -> str:
    normalized_category = fix_keys(category)
    logger.debug(f"<<yellow>> start: {normalized_category=}")

    job_bot = _job_bot()
    result = job_bot.search_all_other_first(normalized_category)
    result = job_bot.prepend_arabic_category_prefix(category, result)

    logger.info(f"<<yellow>> end: {category=}, {result=}")

    return result


__all__ = [
    "genders_jobs_resolver",
]
