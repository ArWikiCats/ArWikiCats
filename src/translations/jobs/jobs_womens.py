"""
Build comprehensive gendered job label dictionaries.
"""

from __future__ import annotations
from typing import Dict

from ...helps import len_print

from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from .jobs_singers import FILMS_TYPE


FEMALE_JOBS_TO: Dict[str, str] = {}

for job_key, arabic_label in SPORTS_KEYS_FOR_JOBS.items():
    # Provide a category entry for women's players to preserve the legacy API.
    FEMALE_JOBS_TO[f"women's {job_key.lower()} players"] = f"لاعبات {arabic_label} نسائية"


FEMALE_JOBS_BASE: Dict[str, str] = {
    "nuns": "راهبات",
    "deafblind actresses": "ممثلات صم ومكفوفات",
    "deaf actresses": "ممثلات صم",
    "actresses": "ممثلات",
    "princesses": "أميرات",
    "video game actresses": "ممثلات ألعاب فيديو",
    "musical theatre actresses": "ممثلات مسرحيات موسيقية",
    "television actresses": "ممثلات تلفزيون",
    "stage actresses": "ممثلات مسرح",
    "voice actresses": "ممثلات أداء صوتي",
    "women in business": "سيدات أعمال",
    "women in politics": "سياسيات",
    "lesbians": "سحاقيات",
    "businesswomen": "سيدات أعمال",
}


def _build_female_jobs() -> Dict[str, str]:
    """Create the combined female job mapping with derived categories."""

    female_jobs = dict(FEMALE_JOBS_BASE)
    female_jobs2: Dict[str, str] = {}
    for film_category, film_labels in FILMS_TYPE.items():
        female_jobs2[f"{film_category} actresses"] = f"ممثلات {film_labels['womens']}"
    female_jobs2["sportswomen"] = "رياضيات"
    for key, label in FEMALE_JOBS_TO.items():
        female_jobs2[key] = label
    female_jobs.update(female_jobs2)
    return female_jobs


Female_Jobs = _build_female_jobs()
short_womens_jobs = Female_Jobs

_len_result = {
    "Female_Jobs": {"count": 468, "size": "12.8 KiB"},
}
len_print.data_len(
    "jobs_womens.py",
    {
        "Female_Jobs": Female_Jobs,
    },
)

__all__ = [
    "Female_Jobs",
    "short_womens_jobs",
    "FEMALE_JOBS_TO",
]
