"""
This module provides functionality to translate category titles
"""
import functools

from ...helps import logger, len_print
from ...translations import Nat_mens, jobs_mens_data, RELIGIOUS_KEYS_PP
from ...translations_formats import format_multi_data, MultiDataFormatterBase
from ..translations_resolvers_v2.nats_as_country_names import nats_keys_as_country_names, nats_keys_as_country_names_bad_keys

from .utils import one_Keys_more_2, nat_and_gender_keys


def _load_formatted_data() -> dict:
    formatted_data_jobs_with_nat = {
        # base keys
        "{en_nat}": "{ar_nat}",
        "{en_nat} people": "أعلام {ar_nat}",
        # "{en_nat} people": "{ar_nat}",

        "{en_nat}-american coaches of canadian-football": "مدربو كرة قدم كندية أمريكيون {ar_nat}",
        "{en_nat} coaches of canadian-football": "مدربو كرة قدم كندية {ar_nat}",

        "{en_nat}-american": "{ar_nat} أمريكيون",
        "{en_nat} eugenicists": "علماء {ar_nat} متخصصون في تحسين النسل",
        "{en_nat} politicians who committed suicide": "سياسيون {ar_nat} أقدموا على الانتحار",
        "{en_nat} contemporary artists": "فنانون {ar_nat} معاصرون",

        # [Category:Turkish expatriate sports-people] : "تصنيف:رياضيون أتراك مغتربون"
        "{en_nat} expatriate {en_job}": "{ar_job} {ar_nat} مغتربون",

        # "Category:Pakistani expatriate male actors": "تصنيف:ممثلون ذكور باكستانيون مغتربون",
        "{en_nat} expatriate male {en_job}": "{ar_job} ذكور {ar_nat} مغتربون",

        # [Category:Turkish immigrants sports-people] : "تصنيف:رياضيون أتراك مهاجرون"
        "{en_nat} immigrants {en_job}": "{ar_job} {ar_nat} مهاجرون",

        "{en_nat} films people": "أعلام أفلام {ar_nat}",
        "{en_nat} film people": "أعلام أفلام {ar_nat}",
        "male {en_nat}": "{ar_nat} ذكور",

        # emigrants keys
        # "{en_nat} emigrants": "{ar_job} مهاجرون",
        "{en_nat} emigrants {en_job}": "{ar_job} {ar_nat} مهاجرون",
        "emigrants {en_nat} {en_job}": "{ar_job} مهاجرون",

    }

    # { "{en_nat} male emigrants": "{ar_nat} مهاجرون ذكور", "{en_nat} emigrants male": "{ar_nat} مهاجرون ذكور", "male {en_nat} emigrants": "{ar_nat} مهاجرون ذكور" }
    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "emigrants", "male", "{ar_nat} مهاجرون ذكور"))
    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "expatriate", "male", "{ar_nat} مغتربون ذكور"))

    formatted_data_jobs = {

        # base keys
        "{en_job}": "{ar_job}",
        "{en_job} people": "أعلام {ar_job}",
        "male {en_job}": "{ar_job} ذكور",

        # expatriate keys
        "expatriate {en_job}": "{ar_job} مغتربون",
        "expatriate male {en_job}": "{ar_job} ذكور مغتربون",

        # emigrants keys
        "emigrants {en_job}": "{ar_job} مهاجرون",
    }
    formatted_data_jobs.update(nat_and_gender_keys("{en_job}", "emigrants", "male", "{ar_job} مهاجرون ذكور"))
    formatted_data_jobs.update(nat_and_gender_keys("{en_job}", "expatriate", "male", "{ar_job} مغتربون ذكور"))

    formatted_data = dict(formatted_data_jobs)
    formatted_data.update({
        f"{{en_nat}} {x}": f"{v} {{ar_nat}}" for x, v in formatted_data_jobs.items()
        if "{en_nat}" not in x and "{ar_nat}" not in v
    })

    # formatted_data.update({
    #     f"{{en_nat}}-american {x}" : f"{v} أمريكيون {{ar_nat}}" for x, v in formatted_data_jobs.items()
    # })

    genders_keys: dict[str, str] = {
        "male deaf": "صم ذكور",
        "blind": "مكفوفون",
        "deaf": "صم",
        "deafblind": "صم ومكفوفون",
        "killed-in-action": "قتلوا في عمليات قتالية",
        "killed in action": "قتلوا في عمليات قتالية",
        "murdered abroad": "قتلوا في الخارج",
    }

    for x, v in genders_keys.items():
        # formatted_data.update( one_Keys_more_2(x, v, add_women=False) )
        formatted_data.update(
            one_Keys_more_2(x, v, add_women=False)
        )

    formatted_data.update(formatted_data_jobs_with_nat)
    formatted_data.update({
        "{en_nat} emigrants": "{ar_nat} مهاجرون",
        "fictional {en_nat} religious workers": "عمال دينيون {ar_nat} خياليون",
        "{en_nat} religious workers": "عمال دينيون {ar_nat}",

        # TODO: ADD DATA FROM NAT_BEFORE_OCC_BASE
        # "{en_nat} saints": "{ar_nat} قديسون",
        "{en_nat} eugenicists": "علماء {ar_nat} متخصصون في تحسين النسل",
        "{en_nat} politicians who committed suicide": "سياسيون {ar_nat} أقدموا على الانتحار",
        "{en_nat} contemporary artists": "فنانون {ar_nat} معاصرون",

        "{en_nat} scholars of islam": "{ar_nat} باحثون عن الإسلام",
        "{en_nat} convicted-of-murder": "{ar_nat} أدينوا بالقتل",
        "{en_nat} womens rights activists": "{ar_nat} ناشطون في حقوق المرأة",
    })

    return formatted_data


def _load_jobs_data() -> dict[str, str]:
    not_in_keys = [
        "expatriate",
        "immigrants",
    ]
    # all keys without any word from not_in_keys
    data = {
        x: v
        for x, v in jobs_mens_data.items()
        if not any(word in x for word in not_in_keys)
        and not RELIGIOUS_KEYS_PP.get(x)
    }

    return data


@functools.lru_cache(maxsize=1)
def load_bot() -> MultiDataFormatterBase:
    jobs_data_enhanced = _load_jobs_data()
    logger.debug(f"jobs_data_enhanced mens: {len(jobs_data_enhanced):,}")

    formatted_data = _load_formatted_data()

    logger.debug(f"_load_formatted_data mens: {len(formatted_data):,}")

    nats_data: dict[str, str] = {
        x: v for x, v in Nat_mens.items()
        if "-american" not in x
    }

    nats_data.update({
        x: v.get("males") for x, v in nats_keys_as_country_names.items()
        if v.get("males")
    })

    return format_multi_data(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        value_placeholder="{ar_nat}",
        data_list2=jobs_data_enhanced,
        key2_placeholder="{en_job}",
        value2_placeholder="{ar_job}",
        text_after=" people",
        text_before="the ",
        use_other_formatted_data=True,
        search_first_part=True,
    )


def fix_keys(category: str) -> str:
    category = category.replace("'", "").lower()

    replacements = {
        "expatriates": "expatriate",
        "canadian football": "canadian-football",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    return category


@functools.lru_cache(maxsize=10000)
def mens_resolver_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start mens_resolver_labels: {category=}")

    category = fix_keys(category)
    if category in nats_keys_as_country_names_bad_keys:
        logger.debug(f"<<yellow>> end mens_resolver_labels: {category=}, [result=]")
        return ""

    _bot = load_bot()
    result = _bot.search_all_category(category)

    logger.debug(f"<<yellow>> end mens_resolver_labels: {category=}, {result=}")
    return result

# len_print.data_len("mens.py", {"formatted_data": _load_formatted_data()})
