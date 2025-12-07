"""
This module provides functionality to translate category titles
"""

from ...translations import Nat_mens, jobs_mens_data
from .job_resolve import NatJobsResolver

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
    "{en_job} people": "أعلام {ar_job}",
    "male {en_job}": "{ar_job} ذكور",
    "expatriate male {en_job}": "{ar_job} مغتربون ذكور",
}

formatted_data_nats = {
    f"{{en_nat}} {x}": f"{v} {{ar_nat}}" for x, v in formatted_data_jobs.items()
}

formatted_data = dict(formatted_data_jobs) | formatted_data_nats
# formatted_data.update({ f"{{en_nat}}-american {x}" : f"{v} أمريكيون {{ar_nat}}" for x, v in formatted_data_jobs.items() })

for x, v in Mens_suffix.items():
    formatted_data[x.format(en="{en_job}")] = v.format(ar="{ar_job}")
    formatted_data[x.format(en="{en_nat} {en_job}")] = v.format(ar="{ar_job} {ar_nat}")

formatted_data.update({
    "{en_nat}-american": "{ar_nat} أمريكيون",
    "{en_nat}": "{ar_nat}",
    "{en_nat} people": "أعلام {ar_nat}",
    "{en_nat} eugenicists": "علماء {ar_nat} متخصصون في تحسين النسل",
    "{en_nat} politicians who committed suicide": "سياسيون {ar_nat} أقدموا على الانتحار",
    "{en_nat} contemporary artists": "فنانون {ar_nat} معاصرون",
})

Nat_mens_new = {x: v for x, v in Nat_mens.items() if "-american" not in x}

mens_resolver = NatJobsResolver(jobs_mens_data, formatted_data, Nat_mens_new)

get_label = mens_resolver.get_label
