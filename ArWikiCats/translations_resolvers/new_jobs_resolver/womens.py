"""
This module provides functionality to translate category titles
compare with womens_prefixes_work
"""
import functools
from ...translations import Nat_Womens, jobs_womens_data, RELIGIOUS_KEYS_PP
from ...translations_formats import format_multi_data, MultiDataFormatterBase


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

        # TODO: ADD DATA FROM RELIGIOUS_KEYS_PP
        "{en_nat} {women} shia muslims": "{ar_nat} مسلمات شيعيات",
        "{women} {en_nat} shia muslims": "{ar_nat} مسلمات شيعيات",
    }

    for x, v in RELIGIOUS_KEYS_PP.items():
        label = f"{{ar_nat}} {v['females']}"

        # "Yemeni muslims": "تصنيف:يمنيون مسلمون"
        # formatted_data_jobs_with_nat[f"{{en_nat}} {x}"] = label
        # formatted_data_jobs_with_nat[f"{x} {{en_nat}}"] = label

        # "Yemeni women's muslims": "تصنيف:يمنيات مسلمات"
        formatted_data_jobs_with_nat[f"{{en_nat}} {{women}} {x}"] = label

        # "women's Yemeni muslims": "تصنيف:يمنيات مسلمات"
        formatted_data_jobs_with_nat[f"{{women}} {{en_nat}} {x}"] = label

        # "Yemeni women's muslims": "تصنيف:يمنيات مسلمات"
        formatted_data_jobs_with_nat[f"{{en_nat}} {{women}} {x}"] = label

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

    formatted_data = dict(formatted_data_jobs)
    formatted_data.update({
        f"{{en_nat}} {x}": f"{v} {{ar_nat}}" for x, v in formatted_data_jobs.items()
        if "{en_nat}" not in x and "{ar_nat}" not in v
    })

    formatted_data.update({
        f"{{en_nat}}-american {x}" : f"{v} أمريكيات {{ar_nat}}" for x, v in formatted_data_jobs.items()
    })

    genders_keys: dict[str, str] = {
        "{en} blind": "{ar} مكفوفات",
        "{en} deaf": "{ar} صم",
        "{en} deafblind": "{ar} صم ومكفوفات",
        "{en} killed-in-action": "{ar} قتلن في عمليات قتالية",
        "{en} killed in action": "{ar} قتلن في عمليات قتالية",
        "{en} murdered abroad": "{ar} قتلن في الخارج",
    }

    for x, v in genders_keys.items():
        # writers blind
        formatted_data[x.format(en="{en_job}")] = v.format(ar="{ar_job}")

        # greek blind
        formatted_data[x.format(en="{en_nat}")] = v.format(ar="{ar_nat}")

        # female greek blind
        formatted_data[x.format(en="{women} {en_nat}")] = v.format(ar="{ar_nat}")

        # female writers blind
        formatted_data[x.format(en="{women} {en_job}")] = v.format(ar="{ar_job}")

        # greek writers blind
        formatted_data[x.format(en="{en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")

        # female greek writers blind
        formatted_data[x.format(en="{women} {en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")

        # writers greek blind
        formatted_data[x.format(en="{en_job} {en_nat}")] = v.format(ar="{ar_job} {ar_nat}")

        # writers female greek blind
        formatted_data[x.format(en="{en_job} {women} {en_nat}")] = v.format(ar="{ar_job} {ar_nat}")

        # female writers greek blind
        formatted_data[x.format(en="{women} {en_job} {en_nat}")] = v.format(ar="{ar_job} {ar_nat}")

    formatted_data.update(formatted_data_jobs_with_nat)

    formatted_data_women = {x: v for x, v in formatted_data.items() if "{women}" in x}

    formatted_data_final = {x: v for x, v in formatted_data.items() if "{women}" not in x}

    for x, v in formatted_data_women.items():
        formatted_data_final[x.replace("{women}", "women")] = v
        formatted_data_final[x.replace("{women}", "womens")] = v
        formatted_data_final[x.replace("{women}", "female")] = v

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
    }
    data.update({
        "actresses": "ممثلات",
    })
    return data


@functools.lru_cache(maxsize=1)
def load_bot() -> MultiDataFormatterBase:
    jobs_data_enhanced = _load_jobs_data()
    print(f"jobs_data_enhanced womens: {len(jobs_data_enhanced):,}")

    formatted_data = _load_formatted_data()
    print(f"_load_formatted_data womens: {len(formatted_data):,}")

    nats_new = {
        x: v for x, v in Nat_Womens.items()
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
        text_after="",
        text_before="the ",
        use_other_formatted_data=True,
        search_first_part=True,
    )


def womens_resolver_labels(category: str) -> str:
    _bot = load_bot()

    category = category.replace("'", "").lower()
    category = category.replace("expatriates", "expatriate")

    return _bot.search_all_category(category)
