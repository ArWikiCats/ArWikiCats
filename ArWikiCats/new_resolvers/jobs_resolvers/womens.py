"""
Resolver for female-specific job and occupation category labels.
This module provides functionality to translate categories combining jobs,
nationalities, and descriptors for women into idiomatic Arabic.
"""

import functools
import logging
from ...helps import len_print
from ...translations import (
    FEMALE_JOBS_BASE_EXTENDED,
    RELIGIOUS_KEYS_PP,
    All_Nat,
    all_country_with_nat,
    all_country_with_nat_ar,
    countries_en_as_nationality_keys,
    jobs_womens_data,
)
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from ..nats_as_country_names import nats_keys_as_country_names
from .mens import mens_resolver_labels
from .utils import fix_keys, nat_and_gender_keys, one_Keys_more_2

logger = logging.getLogger(__name__)
countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]

keys_not_jobs = [
    "women",
    "men",
]


genders_keys_new_under_test: dict[str, str] = {
    # "kidnapped": "مختطفون",
    "fictional": "خياليات",
    # "disabled": "معاقون",
    # "contemporary": "معاصرون",
    # "latin": "لاتينيون",
    # "child": "أطفال",
    # "political": "سياسيون",
    # "religious": "دينيون",
    # "military": "عسكريون",
}
"""
"female {en_job} fictional": "{ar_job} خياليات",
"female {en_job} {en_nat} fictional": "{ar_job} {females} خياليات",
"female {en_nat} fictional": "{females} خياليات",
"female {en_nat} {en_job} fictional": "{ar_job} {females} خياليات",
"fictional {en_nat} female": "{females} خياليات",
"{en_job} female {en_nat} fictional": "{ar_job} {females} خياليات",
"{en_nat} female {en_job} fictional": "{ar_job} {females} خياليات",
"""
genders_keys: dict[str, str] = {
    "blind": "مكفوفات",
    "abolitionists": "مناهضات للعبودية",
    "deaf": "صم",
    "executed": "أعدمن",
    "executed abroad": "أعدمن في الخارج",
    "deafblind": "صم ومكفوفات",
    "killed-in-action": "قتلن في عمليات قتالية",
    "killed in action": "قتلن في عمليات قتالية",
    "murdered abroad": "قتلن في الخارج",
}

genders_keys.update(genders_keys_new_under_test)


def is_false_key(key: str, value: str) -> bool:
    if ("mens" in key.lower() or "men's" in key.lower()) and "رجالية" in value:
        return True

    if key in genders_keys:  # NOTE: under test
        return True

    if RELIGIOUS_KEYS_PP.get(key) or key in keys_not_jobs:
        return True

    not_in_keys = [
        "expatriate",
        "immigrants",
    ]

    # if any(word in key for word in not_in_keys) and not
    if any(word in key for word in not_in_keys):
        return True

    return False


@functools.lru_cache(maxsize=1)
def _load_formatted_data() -> tuple[dict[str, str], dict[str, str]]:
    formatted_data_jobs_with_nat = {
        "{en_nat} female actresses": "ممثلات {females}",
        "{en_nat} actresses": "ممثلات {females}",
        "{en_nat} expatriate female {en_job}": "{ar_job} {females} مغتربات",
        "{en_nat}-american female people": "أمريكيات {females}",
        "{en_nat} female eugenicists": "عالمات {females} متخصصات في تحسين النسل",
        "{en_nat} female politicians who committed suicide": "سياسيات {females} أقدمن على الانتحار",
        "{en_nat} female contemporary artists": "فنانات {females} معاصرات",
        # base keys
        "female {en_nat} people": "{females}",
        "{en_nat} female people": "{females}",
        "female {en_nat}": "{females}",
        "{en_nat} female": "{females}",
    }

    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "expatriate", "female", "{females} مغتربات"))
    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "emigrants", "female", "{females} مهاجرات"))

    formatted_data_jobs = {
        # jobs
        # NOTE: "{en_job}": "{ar_job}", Should be used in males bot: [yemeni singers] : "تصنيف:مغنون يمنيون"
        # NOTE: "{en_job}": "{ar_job}", Should be used here to handle womens jobs like: [yemeni actresses] : "تصنيف:ممثلات يمنيات"
        # base keys
        "{en_job}": "{ar_job}",
        "female {en_job}": "{ar_job}",
        "female {en_job} people": "{ar_job}",
        # "{en_job} people": "أعلام {ar_job}",
        "{en_job} people": "{ar_job}",
        # expatriate keys
        "female expatriate {en_job}": "{ar_job} مغتربات",
        "expatriate female {en_job}": "{ar_job} مغتربات",
        "expatriate {en_job}": "{ar_job} مغتربات",
        # emigrants keys
        "female emigrants {en_job}": "{ar_job} مهاجرات",
        "emigrants female {en_job}": "{ar_job} مهاجرات",
        "emigrants {en_job}": "{ar_job} مهاجرات",
    }

    formatted_data_jobs.update(nat_and_gender_keys("{en_job}", "expatriate", "female", "{ar_job} مغتربات"))
    formatted_data_jobs.update(nat_and_gender_keys("{en_job}", "emigrants", "female", "{ar_job} مهاجرات"))

    formatted_data = dict(formatted_data_jobs)
    formatted_data.update(
        {
            f"{{en_nat}} {x}": f"{v} {{females}}"
            for x, v in formatted_data_jobs.items()
            if "{en_nat}" not in x and "{females}" not in v
        }
    )

    formatted_data.update(
        {f"{{en_nat}}-american {x}": f"{v} أمريكيات {{females}}" for x, v in formatted_data_jobs.items()}
    )

    formatted_data_womens_jobs = {}

    for x, v in genders_keys.items():
        keys_more = one_Keys_more_2(
            x,
            v,
            en_nat_key="{en_nat}",
            en_job_key="{en_job}",
            ar_nat_key="{females}",
            ar_job_key="{ar_job}",
            women_key="female",
            add_women=True,
        )
        formatted_data.update(keys_more)
        formatted_data_womens_jobs.update(
            one_Keys_more_2(
                x,
                v,
                en_nat_key="{en_nat}",
                en_job_key="{en_job}",
                ar_nat_key="{females}",
                ar_job_key="{ar_job}",
                add_women=False,
            )
        )

    formatted_data.update(formatted_data_jobs_with_nat)

    # formatted_data.update({ "{en_nat} female film directors": "مخرجات أفلام {females}"})
    formatted_data.update(
        {
            "{en_nat} female abolitionists": "{females} مناهضات للعبودية",
        }
    )
    formatted_data_final = {x.replace("'", ""): v for x, v in formatted_data.items()}

    formatted_data_womens_jobs = {
        x.replace("'", ""): v for x, v in formatted_data_womens_jobs.items() if "{en_nat}" not in x
    }

    return formatted_data_final, formatted_data_womens_jobs


@functools.lru_cache(maxsize=1)
def _load_jobs_data() -> dict[str, str]:
    # all keys without any word from not_in_keys
    data = {x: {"ar_job": v} for x, v in jobs_womens_data.items() if not is_false_key(x, v)}
    len_diff = len(set(jobs_womens_data.keys()) - set(data.keys()))
    if len_diff:
        logger.warning(f"_load_jobs_data womens before fix: {len(data):,}, is_false_key diff: {len_diff:,}")

    # data.update({x: {"ar_job": v} for x, v in FEMALE_JOBS_BASE_EXTENDED.items()})

    data = {x.replace("'", "").replace("australian rules", "australian-rules"): v for x, v in data.items()}
    return data


@functools.lru_cache(maxsize=1)
def _load_nat_data() -> dict[str, str]:
    # nats_data: dict[str, str] = {x: v for x, v in all_country_with_nat_ar.items()}  # 342
    nats_data: dict[str, str] = {x: v for x, v in All_Nat.items()}  # 342

    nats_data.update({x: v for x, v in nats_keys_as_country_names.items()})

    nats_data.update(
        {
            "jewish american": {
                "male": "أمريكي يهودي",
                "males": "أمريكيون يهود",
                "female": "أمريكية يهودية",
                "females": "أمريكيات يهوديات",
                "the_male": "الأمريكي اليهودي",
                "the_female": "الأمريكية اليهودية",
                "en": "",
                "ar": "",
            }
        }
    )

    nats_data = {x.replace("'", ""): v for x, v in nats_data.items()}
    return nats_data


@functools.lru_cache(maxsize=1)
def load_bot() -> MultiDataFormatterBaseV2:
    jobs_data_enhanced = _load_jobs_data()
    logger.debug(f"jobs_data_enhanced womens: {len(jobs_data_enhanced):,}")

    formatted_data, _ = _load_formatted_data()

    logger.debug(f"_load_formatted_data formatted_data: {len(formatted_data):,}")

    nats_data = _load_nat_data()
    return format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        # value_placeholder="{females}",
        data_list2=jobs_data_enhanced,
        key2_placeholder="{en_job}",
        # value2_placeholder="{ar_job}",
        text_after=" people",
        text_before="the ",
        use_other_formatted_data=True,
        search_first_part=True,
    )


@functools.lru_cache(maxsize=1)
def load_bot_only_womens() -> MultiDataFormatterBaseV2:
    jobs_data = {x: {"ar_job": v} for x, v in FEMALE_JOBS_BASE_EXTENDED.items()}
    logger.debug(f"load_bot_only_womens: {len(jobs_data):,}")

    formatted_data, formatted_data_womens_jobs = _load_formatted_data()
    logger.debug(f"_load_formatted_data formatted_data_womens_jobs: {len(formatted_data_womens_jobs):,}")

    formatted_data_womens_jobs.update(formatted_data)

    nats_data = _load_nat_data()
    return format_multi_data_v2(
        formatted_data=formatted_data_womens_jobs,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        # value_placeholder="{females}",
        data_list2=jobs_data,
        key2_placeholder="{en_job}",
        # value2_placeholder="{ar_job}",
        text_after=" people",
        text_before="the ",
        use_other_formatted_data=True,
        search_first_part=True,
    )


@functools.lru_cache(maxsize=10000)
def _womens_resolver(category: str) -> str:
    logger.debug(f"<<yellow>> start _womens_resolver: {category=}")
    category = fix_keys(category).replace("australian rules", "australian-rules")

    result = load_bot().search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end _womens_resolver: {category=}, {result=}", result)
    return result


@functools.lru_cache(maxsize=10000)
def _womens_jobs_resolver(category: str) -> str:
    logger.debug(f"<<yellow>> start _womens_jobs_resolver: {category=}")
    category = fix_keys(category).replace("australian rules", "australian-rules")

    result = load_bot_only_womens().search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end _womens_jobs_resolver: {category=}, {result=}", result)
    return result


@functools.lru_cache(maxsize=10000)
def womens_resolver_labels(category: str) -> str:
    # logger.debug(f"<<yellow>> start womens_resolver_labels: {category=}")
    category = fix_keys(category).replace("australian rules", "australian-rules")

    if mens_label := mens_resolver_labels(category):
        logger.info(f"<<yellow>> skip womens_resolver_labels mens found: {category=}, {mens_label=}")
        return ""

    if category in countries_en_as_nationality_keys or category in countries_en_keys:
        logger.info(f"<<yellow>> skip womens_resolver_labels: {category=}, [result=]")
        return ""

    result = _womens_resolver(category) or _womens_jobs_resolver(category)

    # logger.info_if_or_debug(f"<<yellow>> end womens_resolver_labels: {category=}, {result=}", result)
    return result


len_print.data_len(
    "womens.py",
    {
        "womens_formatted_data": _load_formatted_data()[0],
        "formatted_data_womens_jobs": _load_formatted_data()[1],
        "womens_jobs_data_enhanced": _load_jobs_data(),
    },
)
