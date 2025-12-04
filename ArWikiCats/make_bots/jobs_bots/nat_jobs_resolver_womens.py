"""
This module provides functionality to translate category titles
compare with Women_s_priffix_work
"""

import functools

from ...translations import Nat_Womens, jobs_womens_data
from ...translations_formats import format_multi_data, MultiDataFormatterBase

Women_s_priffix = {
    "{en} blind": "{ar} مكفوفات",
    "{en} deaf": "{ar} صم",
    "{en} deafblind": "{ar} صم ومكفوفات",
}

formatted_data_jobs = {
    # jobs
    "{en_job}": "{ar_job}",
    "female {en_job} people": "{ar_job}",
    "{en_job} people": "{ar_job}",

    "female expatriate {en_job}": "{ar_job} مغتربات",
    "expatriate female {en_job}": "{ar_job} مغتربات",
    "expatriate women's {en_job}": "{ar_job} مغتربات",

    "female {en_job}": "{ar_job}",
    "women {en_job}": "{ar_job}",
    "women's {en_job}": "{ar_job}",
    "womens {en_job}": "{ar_job}",
}

formatted_data_nats = {
    f"{{en_nat}} {x}" : f"{v} {{ar_nat}}" for x, v in formatted_data_jobs.items()
}

formatted_data = dict(formatted_data_jobs) | formatted_data_nats
formatted_data.update({
    f"{{en_nat}}-american {x}" : f"{v} أمريكيات {{ar_nat}}" for x, v in formatted_data_jobs.items()
})

formatted_data.update({
    "{en_nat} expatriate female {en_job}": "{ar_job} {ar_nat} مغتربات",
    "{en_nat} expatriate women's {en_job}": "{ar_job} {ar_nat} مغتربات",
    "female {en_nat} people": "{ar_nat}",
    "women's {en_nat} people": "{ar_nat}",
    "{en_nat} female actresses": "ممثلات {ar_nat}",
    "{en_nat} actresses": "ممثلات {ar_nat}",
    "{en_nat} people": "{ar_nat}",
    "{en_nat}-american people": "أمريكيات {ar_nat}",
})

for x, v in Women_s_priffix.items():
    formatted_data[x.format(en="{en_job}")] = v.format(ar="{ar_job}")
    formatted_data[x.format(en="{en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")


@functools.lru_cache(maxsize=1)
def _bot_multi() -> MultiDataFormatterBase:
    nat_womens_new = {x: v for x, v in Nat_Womens.items() if "-american" not in x}
    jobs_womens = dict(jobs_womens_data)
    jobs_womens.update({
        "actresses": "ممثلات",
    })
    return format_multi_data(
        formatted_data=formatted_data,
        data_list=nat_womens_new,
        key_placeholder="{en_nat}",
        value_placeholder="{ar_nat}",
        data_list2=jobs_womens,
        key2_placeholder="{en_job}",
        value2_placeholder="{ar_job}",
        text_after="",
        text_before="the ",
        use_other_formatted_data=True,
    )


@functools.lru_cache(maxsize=10000)
def get_label(category: str) -> str:
    nat_bot = _bot_multi()
    result = nat_bot.search_all(category)
    return result
