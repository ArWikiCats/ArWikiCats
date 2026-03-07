"""
copied from ArWikiCats/new_resolvers/jobs_resolvers/mens.py

"""

import functools
import logging

from ...translations import (
    RELIGIOUS_KEYS_PP,
    All_Nat,
    all_country_with_nat,
    countries_en_as_nationality_keys,
    jobs_mens_data,
)
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from ..nats_as_country_names import nats_keys_as_country_names
from ..jobs_resolvers.utils import fix_keys, nat_and_gender_keys

logger = logging.getLogger(__name__)
countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]

jobs_mens_data_f = dict(jobs_mens_data.items())

keys_not_jobs = [
    "women",
    "men",
]

NAT_DATA_MALES = {
    # males with ذكور
    "{en_nat} male swimmers": "سباحون ذكور {males}",  # 101
    "{en_nat} male freestyle swimmers": "سباحو تزلج حر ذكور {males}",  # 121
    "{en_nat} male sprinters": "عداؤون سريعون ذكور {males}",  # 71
    # males without ذكور
    "{en_nat} male martial artists": "ممارسو فنون قتالية ذكور {males}",  # 137
    "{en_nat} male boxers": "ملاكمون ذكور {males}",  # 136
    "{en_nat} male athletes": "لاعبو قوى ذكور {males}",  # 81
    "{en_nat} male actors": "ممثلون ذكور {males}",  # 91
    "{en_nat} male singers": "مغنون ذكور {males}",  # 85
    "{en_nat} male writers": "كتاب ذكور {males}",  # 86
    "{en_nat} male film actors": "ممثلو أفلام ذكور {males}",  # 80
}


def is_false_key(key: str, value: str) -> bool:
    if ("mens" in key.lower() or "men's" in key.lower()) and "رجالية" in value:
        return True

    if RELIGIOUS_KEYS_PP.get(key):
        return True

    if key in keys_not_jobs:
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
def _load_formatted_data() -> dict:
    formatted_data_jobs_with_nat = {
        # [Category:Turkish expatriate sports-people] : "تصنيف:رياضيون أتراك مغتربون"
        "{en_nat} expatriate {en_job}": "{ar_job} {males} مغتربون",

        # "Category:Pakistani expatriate male actors": "تصنيف:ممثلون ذكور باكستانيون مغتربون",
        "{en_nat} expatriate male {en_job}": "{ar_job} ذكور {males} مغتربون",

        "male {en_nat}": "{males} ذكور",
    }

    # { "{en_nat} male emigrants": "{males} مهاجرون ذكور", "{en_nat} emigrants male": "{males} مهاجرون ذكور", "male {en_nat} emigrants": "{males} مهاجرون ذكور" }
    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "emigrants", "male", "{males} مهاجرون ذكور"))
    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "expatriate", "male", "{males} مغتربون ذكور"))
    formatted_data_jobs_with_nat.update(NAT_DATA_MALES)

    formatted_data_jobs = {
        # base keys
        "{en_job}": "{ar_job}",
        "male {en_job}": "{ar_job} ذكور",

        # expatriate keys
        "expatriate {en_job}": "{ar_job} مغتربون",
        "expatriate male {en_job}": "{ar_job} ذكور مغتربون",
    }
    formatted_data_jobs.update(nat_and_gender_keys("{en_job}", "emigrants", "male", "{ar_job} مهاجرون ذكور"))
    formatted_data_jobs.update(nat_and_gender_keys("{en_job}", "expatriate", "male", "{ar_job} مغتربون ذكور"))

    formatted_data = dict(formatted_data_jobs)
    formatted_data.update(
        {
            f"{{en_nat}} {x}": f"{v} {{males}}"
            for x, v in formatted_data_jobs.items()
            if "{en_nat}" not in x and "{males}" not in v
        }
    )

    formatted_data.update(formatted_data_jobs_with_nat)

    formatted_data_final = {x.replace("'", ""): v for x, v in formatted_data.items()}

    return formatted_data_final


@functools.lru_cache(maxsize=1)
def _load_jobs_data() -> dict[str, str]:
    # all keys without any word from not_in_keys
    data = {
        x: {"ar_job": v} for x, v
        in jobs_mens_data_f.items()
        if not is_false_key(x, v)
    }
    len_diff = len(set(jobs_mens_data_f.keys()) - set(data.keys()))

    if len_diff:
        logger.warning(f" mens before fix: {len(data):,}, is_false_key diff: {len_diff:,}")

    data = {x.replace("'", "").replace("australian rules", "australian-rules"): v for x, v in data.items()}

    data.update({
        "philosophers and theologians": {"ar_job": "فلاسفة ولاهوتيون"},
    })
    return data


@functools.lru_cache(maxsize=1)
def _load_nat_data() -> dict[str, str]:
    # nats_data: dict[str, str] = {x: v for x, v in all_country_with_nat_ar.items()}  # 342
    nats_data: dict[str, str] = dict(All_Nat.items())  # 342

    nats_data.update(dict(nats_keys_as_country_names.items()))

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
    logger.debug(f"jobs_data_enhanced mens: {len(jobs_data_enhanced):,}")

    formatted_data = _load_formatted_data()

    logger.debug(f"_load_formatted_data mens: {len(formatted_data):,}")

    nats_data = _load_nat_data()
    return format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        data_list2=jobs_data_enhanced,
        key2_placeholder="{en_job}",
        text_after=" people",
        text_before="the ",
        use_other_formatted_data=True,
        search_first_part=True,
    )


@functools.lru_cache(maxsize=10000)
def _mens_resolver_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start {category=}")
    category = fix_keys(category).replace("australian rules", "australian-rules")

    _bot = load_bot()
    result = _bot.search_all_category(category)

    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


@functools.lru_cache(maxsize=10000)
def males_resolver_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start {category=}")
    category = fix_keys(category).replace("australian rules", "australian-rules")

    if category in countries_en_as_nationality_keys or category in countries_en_keys:
        logger.info(f"<<yellow>> skip : {category=}, [result=]")
        return ""

    result = _mens_resolver_labels(category)
    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result
