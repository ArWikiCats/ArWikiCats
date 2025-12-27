"""
This module provides functionality to translate category titles
"""
import functools

from ...helps import logger
from ...translations import all_country_with_nat_ar, jobs_mens_data, RELIGIOUS_KEYS_PP, all_country_with_nat
from ...translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ..nats_as_country_names import nats_keys_as_country_names, nats_keys_as_country_names_bad_keys
from .utils import one_Keys_more_2, nat_and_gender_keys

countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]


def _load_formatted_data() -> dict:
    formatted_data_jobs_with_nat = {
        # base keys
        "{en_nat}": "{males}",
        # "{en_nat} people": "أعلام {males}",
        # "{en_nat} people": "{males}",

        "{en_nat}-american coaches of canadian-football": "مدربو كرة قدم كندية أمريكيون {males}",
        "{en_nat} coaches of canadian-football": "مدربو كرة قدم كندية {males}",

        "{en_nat}-american": "{males} أمريكيون",
        "{en_nat} eugenicists": "علماء {males} متخصصون في تحسين النسل",
        "{en_nat} politicians who committed suicide": "سياسيون {males} أقدموا على الانتحار",
        "{en_nat} contemporary artists": "فنانون {males} معاصرون",

        # [Category:Turkish expatriate sports-people] : "تصنيف:رياضيون أتراك مغتربون"
        "{en_nat} expatriate {en_job}": "{ar_job} {males} مغتربون",

        # "Category:Pakistani expatriate male actors": "تصنيف:ممثلون ذكور باكستانيون مغتربون",
        "{en_nat} expatriate male {en_job}": "{ar_job} ذكور {males} مغتربون",

        # [Category:Turkish immigrants sports-people] : "تصنيف:رياضيون أتراك مهاجرون"
        "{en_nat} immigrants {en_job}": "{ar_job} {males} مهاجرون",

        "{en_nat} films people": "أعلام أفلام {males}",
        "{en_nat} film people": "أعلام أفلام {males}",
        "male {en_nat}": "{males} ذكور",

        # emigrants keys
        # "{en_nat} emigrants": "{ar_job} مهاجرون",
        "{en_nat} emigrants {en_job}": "{ar_job} {males} مهاجرون",
        "emigrants {en_nat} {en_job}": "{ar_job} مهاجرون",

        # "spouses of {en_nat} politicians": "قرينات سياسيون {males}",
        "spouses of {en_nat}": "قرينات {males}",
        "spouses of {en_nat} {en_job}": "قرينات {ar_job} {males}",

    }

    # { "{en_nat} male emigrants": "{males} مهاجرون ذكور", "{en_nat} emigrants male": "{males} مهاجرون ذكور", "male {en_nat} emigrants": "{males} مهاجرون ذكور" }
    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "emigrants", "male", "{males} مهاجرون ذكور"))
    formatted_data_jobs_with_nat.update(nat_and_gender_keys("{en_nat}", "expatriate", "male", "{males} مغتربون ذكور"))

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
        f"{{en_nat}} {x}": f"{v} {{males}}" for x, v in formatted_data_jobs.items()
        if "{en_nat}" not in x and "{males}" not in v
    })

    # formatted_data.update({
    #     f"{{en_nat}}-american {x}" : f"{v} أمريكيون {{males}}" for x, v in formatted_data_jobs.items()
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
            one_Keys_more_2(x, v, ar_nat_key="{males}", add_women=False)
        )

    formatted_data.update(formatted_data_jobs_with_nat)
    formatted_data.update({
        "{en_nat} emigrants": "{males} مهاجرون",
        "fictional {en_nat} religious workers": "عمال دينيون {males} خياليون",
        "{en_nat} religious workers": "عمال دينيون {males}",

        # TODO: ADD DATA FROM NAT_BEFORE_OCC_BASE
        # "{en_nat} saints": "{males} قديسون",
        "{en_nat} eugenicists": "علماء {males} متخصصون في تحسين النسل",
        "{en_nat} politicians who committed suicide": "سياسيون {males} أقدموا على الانتحار",
        "{en_nat} contemporary artists": "فنانون {males} معاصرون",

        "{en_nat} scholars of islam": "{males} باحثون عن الإسلام",
        "{en_nat} convicted-of-murder": "{males} أدينوا بالقتل",
        "{en_nat} womens rights activists": "{males} ناشطون في حقوق المرأة",
        "{en_nat} businesspeople": "شخصيات أعمال {female}",
    })

    return formatted_data


def _load_jobs_data() -> dict[str, str]:
    not_in_keys = [
        "expatriate",
        "immigrants",
    ]
    # all keys without any word from not_in_keys
    data = {
        x: {"ar_job": v}
        for x, v in jobs_mens_data.items()
        if not any(word in x for word in not_in_keys)
        and not RELIGIOUS_KEYS_PP.get(x)
    }

    return data


@functools.lru_cache(maxsize=1)
def load_bot() -> MultiDataFormatterBaseV2:
    jobs_data_enhanced = _load_jobs_data()
    logger.debug(f"jobs_data_enhanced mens: {len(jobs_data_enhanced):,}")

    formatted_data = _load_formatted_data()

    logger.debug(f"_load_formatted_data mens: {len(formatted_data):,}")

    nats_data: dict[str, str] = {
        x: v for x, v in all_country_with_nat_ar.items()
    }   # 342

    nats_data.update({
        x: v for x, v in nats_keys_as_country_names.items()
    })

    nats_data.update({
        "jewish american": {
            "male": "أمريكي يهودي",
            "males": "أمريكيون يهود",
            "female": "أمريكية يهودية",
            "females": "أمريكيات يهوديات",
            "en": "",
            "ar": "",
            "the_female": "الأمريكية اليهودية",
            "the_male": "الأمريكي اليهودي"
        }
    })
    return format_multi_data_v2(
        formatted_data=formatted_data,

        data_list=nats_data,
        key_placeholder="{en_nat}",
        # value_placeholder="{males}",

        data_list2=jobs_data_enhanced,
        key2_placeholder="{en_job}",
        # value2_placeholder="{ar_job}",

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

    return category.strip()


@functools.lru_cache(maxsize=10000)
def mens_resolver_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start mens_resolver_labels: {category=}")
    category = fix_keys(category)

    if category in nats_keys_as_country_names_bad_keys or category in countries_en_keys:
        logger.info(f"<<yellow>> skip mens_resolver_labels: {category=}, [result=]")
        return ""

    _bot = load_bot()
    result = _bot.search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end mens_resolver_labels: {category=}, {result=}", result)
    return result

# len_print.data_len("mens.py", {"formatted_data": _load_formatted_data()})
