"""
This module provides functionality to translate category titles
compare with womens_prefixes_work
"""
import functools
from ...translations import Nat_Womens, jobs_womens_data
from .job_resolve import NatJobsResolver

womens_prefixes = {
    "{en} blind": "{ar} مكفوفات",
    "{en} deaf": "{ar} صم",
    "{en} deafblind": "{ar} صم ومكفوفات",
}

formatted_data_jobs = {
    # jobs
    "{en_job}": "{ar_job}",
    "female {en_job} people": "{ar_job}",
    # "{en_job} people": "أعلام {ar_job}",
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
    f"{{en_nat}} {x}": f"{v} {{ar_nat}}" for x, v in formatted_data_jobs.items()
}

formatted_data = dict(formatted_data_jobs) | formatted_data_nats
formatted_data.update({
    f"{{en_nat}}-american {x}" : f"{v} أمريكيات {{ar_nat}}" for x, v in formatted_data_jobs.items()
})

for x, v in womens_prefixes.items():
    formatted_data[x.format(en="{en_job}")] = v.format(ar="{ar_job}")
    formatted_data[x.format(en="{en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")

formatted_data.update({
    "{en_nat} female actresses": "ممثلات {ar_nat}",
    "{en_nat} actresses": "ممثلات {ar_nat}",

    "{en_nat} expatriate female {en_job}": "{ar_job} {ar_nat} مغتربات",
    "{en_nat} expatriate women's {en_job}": "{ar_job} {ar_nat} مغتربات",
    "female {en_nat} people": "{ar_nat}",
    "women's {en_nat} people": "{ar_nat}",
    "{en_nat} female people": "{ar_nat}",
    "{en_nat}-american female people": "أمريكيات {ar_nat}",

    "{en_nat} female eugenicists": "عالمات {ar_nat} متخصصات في تحسين النسل",
    "{en_nat} female politicians who committed suicide": "سياسيات {ar_nat} أقدمن على الانتحار",
    "{en_nat} female contemporary artists": "فنانات {ar_nat} معاصرات",
})

nat_womens_new = {x: v for x, v in Nat_Womens.items() if "-american" not in x}
jobs_womens = dict(jobs_womens_data)
jobs_womens.update({
    "actresses": "ممثلات",
})

womens_resolver = NatJobsResolver(jobs_womens, formatted_data, nat_womens_new)

get_label = womens_resolver.get_label


@functools.lru_cache(maxsize=1)
def load_bot() -> NatJobsResolver:
    return NatJobsResolver(jobs_womens, formatted_data, nat_womens_new)


def womens_resolver_label(category: str) -> str:
    _bot = load_bot()
    return _bot.search_all_category(category)
