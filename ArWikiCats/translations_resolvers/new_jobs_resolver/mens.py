"""
This module provides functionality to translate category titles
"""
import functools
from ...translations import Nat_mens, jobs_mens_data, RELIGIOUS_KEYS_PP
from ...translations_formats import format_multi_data, MultiDataFormatterBase


def nat_and_gender_keys(nat_job_key, key, gender_key, gender_label) -> dict[str, str]:
    data = {}

    # "Yemeni male muslims": "تصنيف:يمنيون مسلمون ذكور"
    # "Yemeni women's muslims": "تصنيف:يمنيات مسلمات"
    data[f"{nat_job_key} {gender_key} {key}"] = gender_label

    # "Yemeni muslims male": "تصنيف:يمنيون مسلمون ذكور"
    data[f"{nat_job_key} {key} {gender_key}"] = gender_label

    # "male Yemeni muslims": "تصنيف:يمنيون مسلمون ذكور"
    # "women's Yemeni muslims": "تصنيف:يمنيات مسلمات"
    data[f"{gender_key} {nat_job_key} {key}"] = gender_label

    return data


def _load_formatted_data() -> dict:
    formatted_data_jobs_with_nat = {
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
        # base keys
        "{en_nat}": "{ar_nat}",
        "{en_nat} people": "أعلام {ar_nat}",
        "male {en_nat}": "{ar_nat} ذكور",

        # emigrants keys
        # "{en_nat} emigrants": "{ar_job} مهاجرون",
        "{en_nat} emigrants {en_job}": "{ar_job} {ar_nat} مهاجرون",
        "emigrants {en_nat} {en_job}": "{ar_job} مهاجرون",

    }

    # { '{en_nat} male emigrants': '{ar_nat} مهاجرون ذكور', '{en_nat} emigrants male': '{ar_nat} مهاجرون ذكور', 'male {en_nat} emigrants': '{ar_nat} مهاجرون ذكور' }
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
        "{en} male deaf": "{ar} صم ذكور",
        "{en} blind": "{ar} مكفوفون",
        "{en} deaf": "{ar} صم",
        "{en} deafblind": "{ar} صم ومكفوفون",
        "{en} killed-in-action": "{ar} قتلوا في عمليات قتالية",
        "{en} killed in action": "{ar} قتلوا في عمليات قتالية",
        "{en} murdered abroad": "{ar} قتلوا في الخارج",
    }

    for x, v in genders_keys.items():
        # writers blind
        formatted_data[x.format(en="{en_job}")] = v.format(ar="{ar_job}")

        # greek blind
        formatted_data[x.format(en="{en_nat}")] = v.format(ar="{ar_nat}")

        # greek writers blind
        formatted_data[x.format(en="{en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")

        # writers greek blind
        formatted_data[x.format(en="{en_job} {en_nat}")] = v.format(ar="{ar_job} {ar_nat}")

    formatted_data.update(formatted_data_jobs_with_nat)

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
    print(f"jobs_data_enhanced mens: {len(jobs_data_enhanced):,}")

    formatted_data = _load_formatted_data()
    print(f"_load_formatted_data mens: {len(formatted_data):,}")

    nats_new = {
        x: v for x, v in Nat_mens.items()
        if "-american" not in x
    }

    return format_multi_data(
        formatted_data=formatted_data,
        data_list=nats_new,
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


def mens_resolver_labels(category: str) -> str:
    _bot = load_bot()

    category = category.replace("'", "").lower()
    category = category.replace("expatriates", "expatriate")

    return _bot.search_all_category(category)
