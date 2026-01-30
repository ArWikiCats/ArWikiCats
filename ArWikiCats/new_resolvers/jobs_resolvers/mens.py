"""
Resolver for male-specific job and occupation category labels.
This module provides functionality to translate categories combining jobs,
nationalities, and descriptors for men into idiomatic Arabic.
"""

import functools
import re

from ...helps import getLogger, len_print
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping
from ...translations import (
    RELIGIOUS_KEYS_PP,
    All_Nat,
    all_country_with_nat,
    all_country_with_nat_ar,
    countries_en_as_nationality_keys,
    jobs_mens_data,
)
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from ..nats_as_country_names import nats_keys_as_country_names
from .utils import fix_keys, nat_and_gender_keys, one_Keys_more_2

logger = getLogger(__name__)
countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]

jobs_mens_data_f = dict(jobs_mens_data.items())
# jobs_mens_data_f.update({x: v["males"] for x, v in RELIGIOUS_KEYS_PP.items() if v.get("males")})

REGEX_THE = re.compile(r"\b(the)\b", re.I)

keys_not_jobs = [
    "women",
    "men",
]

Mens_prefix: dict[str, str] = {
    # "men": "رجال",
    # "expatriate male": "ذكور مغتربون",
    # "expatriate men's": "رجال مغتربون",
    # "male": "ذكور",
    # "male child": "أطفال ذكور",
    "amputee": "مبتورو أحد الأطراف",
    "blind": "مكفوفون",
    "child": "أطفال",
    "children": "أطفال",
    "deaf": "صم",
    "deafblind": "صم ومكفوفون",
    "expatriate": "مغتربون",
    "latin": "لاتينيون",
    "lgbt": "مثليون",
    "murdered": "قتلوا",
    "mythological": "أسطوريون",
    "nautical": "بحريون",
    "renaissance": "عصر النهضة",
    "romantic": "رومانسيون",
    "sunni muslim": "مسلمون سنة",
}

genders_keys_new_under_test: dict[str, str] = {
    "kidnapped": "مختطفون",
    "fictional": "خياليون",
    "disabled": "معاقون",
    "contemporary": "معاصرون",
    "latin": "لاتينيون",
    "child": "أطفال",
    "political": "سياسيون",
    "religious": "دينيون",
    # "military": "عسكريون", # NOTE: cause errors like: "British military": "بريطانيون عسكريون",
}

genders_keys: dict[str, str] = {
    "assassinated": "مغتالون",
    # "male deaf": "صم ذكور",
    "blind": "مكفوفون",
    "abolitionists": "مناهضون للعبودية",
    "deaf": "صم",
    "executed": "أعدموا",
    "executed abroad": "أعدموا في الخارج",
    "deafblind": "صم ومكفوفون",
    "killed-in-action": "قتلوا في عمليات قتالية",
    "killed in action": "قتلوا في عمليات قتالية",
    "murdered abroad": "قتلوا في الخارج",
}

genders_keys.update(genders_keys_new_under_test)


def is_false_key(key: str, value: str) -> bool:
    if ("mens" in key.lower() or "men's" in key.lower()) and "رجالية" in value:
        return True

    if key in genders_keys:  # NOTE: under test
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
        "political office-holders": "أصحاب مناصب سياسية",
        "{en_nat} political office-holders": "أصحاب مناصب سياسية {males}",
        # base keys
        "{en_nat} muslim scholars-of-islam": "باحثون عن الإسلام مسلمون {males}",
        "{en_nat} sunni muslim scholars-of-islam": "باحثون عن الإسلام مسلمون سنة {males}",
        "{en_nat} sunni muslim scholars of islam": "باحثون عن الإسلام مسلمون سنة {males}",
        "{en_nat} contemporary classical musicians": "موسيقيون كلاسيكيون معاصرون {males}",
        "{en_nat} contemporary classical composers": "ملحنون كلاسيكيون معاصرون {males}",
        "{en_nat}": "{males}",
        "{en_nat} muslims": "{males} مسلمون",
        "{en_nat} muslim": "{males} مسلمون",
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
        "men {en_nat}": "{males}",  # رجال
        "mens {en_nat}": "{males}",  # رجال
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
        "men {en_job}": "{ar_job}",  # رجال
        "mens {en_job}": "{ar_job}",  # رجال
        # expatriate keys
        "expatriate {en_job}": "{ar_job} مغتربون",
        "expatriate male {en_job}": "{ar_job} ذكور مغتربون",
        # emigrants keys
        "emigrants {en_job}": "{ar_job} مهاجرون",
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

    # formatted_data.update({
    #     f"{{en_nat}}-american {x}" : f"{v} أمريكيون {{males}}" for x, v in formatted_data_jobs.items()
    # })

    for x, v in genders_keys.items():
        keys_more = one_Keys_more_2(
            x,
            v,
            en_nat_key="{en_nat}",
            en_job_key="{en_job}",
            ar_nat_key="{males}",
            ar_job_key="{ar_job}",
            add_women=False,
        )
        formatted_data.update(keys_more)

    formatted_data.update(formatted_data_jobs_with_nat)
    formatted_data.update(
        {
            "fictional {en_nat} jews": "{males} يهود خياليون",
            "ancient {en_nat}": "{males} قدماء",
            "ancient {en_job}": "{ar_job} قدماء",
            "military {en_job}": "{ar_job} عسكريون",
            "{en_nat} emigrants": "{males} مهاجرون",
            "fictional {en_nat} religious workers": "عمال دينيون {males} خياليون",
            "{en_nat} religious workers": "عمال دينيون {males}",
            # TODO: ADD DATA FROM NAT_BEFORE_OCC_BASE
            # "{en_nat} saints": "{males} قديسون",
            "{en_nat} anti-communists": "{males} مناهضون للشيوعية",
            "{en_nat} disability rights activists": "{males} ناشطون في حقوق الإعاقة",
            # "executed {en_nat}": "{males} أعدموا",
            # "{en_nat} executed": "{males} أعدموا",
            # "{en_nat} executed abroad": "{males} أعدموا في الخارج",
            "{en_nat} eugenicists": "علماء {males} متخصصون في تحسين النسل",
            "{en_nat} politicians who committed suicide": "سياسيون {males} أقدموا على الانتحار",
            "{en_nat} contemporary artists": "فنانون {males} معاصرون",
            "{en_nat} scholars of islam": "{males} باحثون عن الإسلام",
            "{en_nat} womens rights activists": "{males} ناشطون في حقوق المرأة",
            "{en_nat} businesspeople": "شخصيات أعمال {female}",
        }
    )

    NAT_BEFORE_OCC_BASE = [
        "murdered abroad",
        "contemporary",
        "tour de france stage winners",
        "deafblind",
        "deaf",
        "blind",
        "jews",
        # "women's rights activists",
        "female rights activists",
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
        "emigrants",
    ]
    for x in NAT_BEFORE_OCC_BASE:
        if jobs_mens_data_f.get(x):
            formatted_data[f"{{en_nat}} {x}"] = f"{{males}} {jobs_mens_data_f[x]}"

    formatted_data_final = {x.replace("'", ""): v for x, v in formatted_data.items()}
    return formatted_data_final


@functools.lru_cache(maxsize=1)
def _load_jobs_data() -> dict[str, str]:
    # all keys without any word from not_in_keys
    data = {x: {"ar_job": v} for x, v in jobs_mens_data_f.items() if not is_false_key(x, v)}
    len_diff = len(set(jobs_mens_data_f.keys()) - set(data.keys()))

    if len_diff:
        logger.warning(f"_load_jobs_data mens before fix: {len(data):,}, is_false_key diff: {len_diff:,}")

    data.update(
        {
            "philosophers and theologians": {"ar_job": "فلاسفة ولاهوتيون"},
        }
    )

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
    logger.debug(f"jobs_data_enhanced mens: {len(jobs_data_enhanced):,}")

    formatted_data = _load_formatted_data()

    logger.debug(f"_load_formatted_data mens: {len(formatted_data):,}")

    nats_data = _load_nat_data()
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


@functools.lru_cache(maxsize=10000)
def _mens_resolver_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start mens_resolver_labels: {category=}")
    category = fix_keys(category).replace("australian rules", "australian-rules")

    _bot = load_bot()
    result = _bot.search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end mens_resolver_labels: {category=}, {result=}", result)
    return result


religious_data = {x: f"{{}} {v['males']}" for x, v in RELIGIOUS_KEYS_PP.items() if v.get("males")}

label_mappings_ends = dict(
    sorted(
        religious_data.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)


@functools.lru_cache(maxsize=10000)
def mens_resolver_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start mens_resolver_labels: {category=}")
    category = fix_keys(category).replace("australian rules", "australian-rules")

    if category in countries_en_as_nationality_keys or category in countries_en_keys:
        logger.info(f"<<yellow>> skip mens_resolver_labels: {category=}, [result=]")
        return ""

    result = _mens_resolver_labels(category) or resolve_sport_category_suffix_with_mapping(
        category=category,
        data=label_mappings_ends,
        callback=_mens_resolver_labels,
        format_key="{}",
    )
    logger.info_if_or_debug(f"<<yellow>> end mens_resolver_labels: {category=}, {result=}", result)
    return result


len_print.data_len(
    "mens.py",
    {
        "mens_formatted_data": _load_formatted_data(),
        "mens_jobs_data": _load_jobs_data(),
    },
)
