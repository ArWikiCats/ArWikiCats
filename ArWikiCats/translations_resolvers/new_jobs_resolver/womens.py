"""
This module provides functionality to translate category titles
compare with womens_prefixes_work
"""
import functools
import re
from ...helps import len_print, logger
from ...translations import Nat_Womens, jobs_womens_data, RELIGIOUS_KEYS_PP, FEMALE_JOBS_BASE
from ...translations_formats import format_multi_data, MultiDataFormatterBase
from ...translations_resolvers_v2.nats_as_country_names import nats_keys_as_country_names

from .utils import one_Keys_more_2, nat_and_gender_keys, filter_and_replace_gender_terms


def _load_formatted_data() -> dict:
    formatted_data_jobs_with_nat = {
        "{en_nat} {women} actresses": "ممثلات {ar_nat}",
        "{en_nat} actresses": "ممثلات {ar_nat}",

        "{en_nat} expatriate {women} {en_job}": "{ar_job} {ar_nat} مغتربات",
        "{en_nat}-american {women} people": "أمريكيات {ar_nat}",

        "{en_nat} {women} eugenicists": "عالمات {ar_nat} متخصصات في تحسين النسل",
        "{en_nat} {women} politicians who committed suicide": "سياسيات {ar_nat} أقدمن على الانتحار",
        "{en_nat} {women} contemporary artists": "فنانات {ar_nat} معاصرات",

        # base keys
        "{women} {en_nat} people": "{ar_nat}",
        "{en_nat} {women} people": "{ar_nat}",
    }

    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "expatriate", "{women}", "{ar_nat} مغتربات"))
    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "emigrants", "{women}", "{ar_nat} مهاجرات"))

    formatted_data_jobs = {
        # jobs
        # NOTE: "{en_job}": "{ar_job}", Should be used in males bot: [yemeni singers] : "تصنيف:مغنون يمنيون"
        # NOTE: "{en_job}": "{ar_job}", Should used here to handel womens jobs like: [yemeni actresses] : "تصنيف:ممثلات يمنيات"

        # base keys
        "{en_job}": "{ar_job}",
        "{women} {en_job}": "{ar_job}",

        "{women} {en_job} people": "{ar_job}",
        # "{en_job} people": "أعلام {ar_job}",
        "{en_job} people": "{ar_job}",

        # expatriate keys
        "{women} expatriate {en_job}": "{ar_job} مغتربات",
        "expatriate {women} {en_job}": "{ar_job} مغتربات",
        "expatriate {en_job}": "{ar_job} مغتربات",

        # emigrants keys
        "{women} emigrants {en_job}": "{ar_job} مهاجرات",
        "emigrants {women} {en_job}": "{ar_job} مهاجرات",
        "emigrants {en_job}": "{ar_job} مهاجرات",
    }

    formatted_data_jobs.update(nat_and_gender_keys("{en_job}", "expatriate", "{women}", "{ar_job} مغتربات"))
    formatted_data_jobs.update(nat_and_gender_keys("{en_job}", "emigrants", "{women}", "{ar_job} مهاجرات"))

    formatted_data = dict(formatted_data_jobs)
    formatted_data.update({
        f"{{en_nat}} {x}": f"{v} {{ar_nat}}" for x, v in formatted_data_jobs.items()
        if "{en_nat}" not in x and "{ar_nat}" not in v
    })

    formatted_data.update({
        f"{{en_nat}}-american {x}" : f"{v} أمريكيات {{ar_nat}}" for x, v in formatted_data_jobs.items()
    })

    genders_keys: dict[str, str] = {
        "blind": "مكفوفات",
        "deaf": "صم",
        "deafblind": "صم ومكفوفات",
        "killed-in-action": "قتلن في عمليات قتالية",
        "killed in action": "قتلن في عمليات قتالية",
        "murdered abroad": "قتلن في الخارج",
    }

    for x, v in genders_keys.items():
        formatted_data.update(
            one_Keys_more_2(x, v, add_women=True)
        )
    formatted_data.update(formatted_data_jobs_with_nat)

    # formatted_data.update({ "{en_nat} {women} film directors": "مخرجات أفلام {ar_nat}"})
    formatted_data_final = filter_and_replace_gender_terms(formatted_data)

    return formatted_data_final


def _load_jobs_data() -> dict[str, str]:
    not_in_keys = [
        "expatriate",
        "immigrants",
    ]
    # all keys without any word from not_in_keys
    data = {
        x: v
        for x, v in jobs_womens_data.items()
        if not any(word in x for word in not_in_keys)
        and not RELIGIOUS_KEYS_PP.get(x)
    }
    data.update({
        "actresses": "ممثلات",
    })
    data.update(FEMALE_JOBS_BASE)
    return data


@functools.lru_cache(maxsize=1)
def load_bot() -> MultiDataFormatterBase:
    jobs_data_enhanced = _load_jobs_data()
    logger.info(f"jobs_data_enhanced womens: {len(jobs_data_enhanced):,}")

    formatted_data = _load_formatted_data()
    logger.info(f"_load_formatted_data womens: {len(formatted_data):,}")

    nats_data = {
        x: v for x, v in Nat_Womens.items()
        if "-american" not in x
    }

    nats_data.update({
        x: v.get("females") for x, v in nats_keys_as_country_names.items()
        if v.get("females")
    })

    return format_multi_data(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        value_placeholder="{ar_nat}",
        data_list2=jobs_data_enhanced,
        key2_placeholder="{en_job}",
        value2_placeholder="{ar_job}",
        text_after="",
        text_before="the ",
        use_other_formatted_data=True,
        search_first_part=True,
    )


REGEX_WOMENS = re.compile(r"\b(womens|women)\b", re.I)


def fix_keys(category: str) -> str:
    category = category.replace("'", "").lower()
    category = category.replace("expatriates", "expatriate")
    category = REGEX_WOMENS.sub("female", category)
    return category


@functools.lru_cache(maxsize=10000)
def womens_resolver_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start womens_resolver_labels: {category=}")
    category = fix_keys(category)

    if category in nats_keys_as_country_names:
        logger.debug(f"<<yellow>> end womens_resolver_labels: {category=}, [result=]")
        return ""

    _bot = load_bot()
    result = _bot.search_all_category(category)
    logger.debug(f"<<yellow>> end womens_resolver_labels: {category=}, {result=}")
    return result


formatted_data = _load_formatted_data()
len_print.data_len("womens.py", {
    "formatted_data": formatted_data,
})
