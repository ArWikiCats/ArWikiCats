"""
This module provides functionality to translate category titles
"""

import functools

from ...translations import Nat_mens, jobs_mens_data
from ...translations_formats import format_multi_data, MultiDataFormatterBase

Mens_suffix: dict[str, str] = {
    "{en} male deaf": "{ar} صم ذكور",
    "{en} blind": "{ar} مكفوفون",
    "{en} deafblind": "{ar} صم ومكفوفون",
    "{en} deaf": "{ar} صم",
    "{en} killed-in-action": "{ar} قتلوا في عمليات قتالية",
    "{en} killed in action": "{ar} قتلوا في عمليات قتالية",
    "{en} murdered abroad": "{ar} قتلوا في الخارج",
}

formatted_data_jobs = {
    "expatriate {en_job}": "{ar_job} مغتربون",
    "{en_job}": "{ar_job}",
    "{en_job} people": "{ar_job}",
    "male {en_job}": "{ar_job} ذكور",
    "expatriate male {en_job}": "{ar_job} مغتربون ذكور",
}

formatted_data_nats = {
    f"{{en_nat}} {x}": f"{v} {{ar_nat}}" for x, v in formatted_data_jobs.items()
}

formatted_data = dict(formatted_data_jobs) | formatted_data_nats
formatted_data.update({
    f"{{en_nat}}-american {x}" : f"{v} أمريكيون {{ar_nat}}" for x, v in formatted_data_jobs.items()
})

formatted_data.update({
    "{en_nat} people": "{ar_nat}",  # 187
})

for x, v in Mens_suffix.items():
    formatted_data[x.format(en="{en_job}")] = v.format(ar="{ar_job}")
    formatted_data[x.format(en="{en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")


@functools.lru_cache(maxsize=1)
def _bot_multi() -> MultiDataFormatterBase:
    Nat_mens_new = {x: v for x, v in Nat_mens.items() if "-american" not in x}
    return format_multi_data(
        formatted_data=formatted_data,
        data_list=Nat_mens_new,
        key_placeholder="{en_nat}",
        value_placeholder="{ar_nat}",
        data_list2=jobs_mens_data,
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
