"""
Build comprehensive gendered job label dictionaries.
"""

from __future__ import annotations

from typing import Dict, Mapping

from ...helps import len_print
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from .jobs_singers import FILMS_TYPE
from .jobs_data_basic import RELIGIOUS_KEYS_PP
from .jobs_defs import GenderedLabelMap, combine_gender_labels, GenderedLabel

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


RELIGIOUS_ROLE_LABELS_FEMALES: GenderedLabelMap = {
    "nuns": "راهبات",
}


def _build_female_jobs() -> Dict[str, str]:
    """Create the combined female job mapping with derived categories."""

    female_jobs = dict(FEMALE_JOBS_BASE)
    female_jobs2: Dict[str, str] = {}

    for film_category, film_labels in FILMS_TYPE.items():
        female_jobs2[f"{film_category} actresses"] = f"ممثلات {film_labels['females']}"

    female_jobs2["sportswomen"] = "رياضيات"

    for key, label in FEMALE_JOBS_TO.items():
        female_jobs2[key] = label

    female_jobs.update(female_jobs2)
    return female_jobs


def _build_religious_job_labels(
    religions: Mapping[str, GenderedLabel],
    roles: dict[str, str],
) -> GenderedLabelMap:
    """
    Generate gendered labels for religious roles.
    """

    combined_roles: GenderedLabelMap = {}
    for role_key, role_female_labels in roles.items():
        if not role_key or not role_female_labels:
            continue
        combined_roles[role_key] = role_female_labels

        for religion_key, religion_labels in religions.items():
            if not religion_key or not religion_labels:
                continue
            females_label = combine_gender_labels(role_female_labels, religion_labels["females"])

            if females_label:
                combined_roles[f"{religion_key} {role_key}"] = females_label

    return combined_roles


FEMALE_JOBS_BASE_EXTENDED = _build_religious_job_labels(RELIGIOUS_KEYS_PP, RELIGIOUS_ROLE_LABELS_FEMALES)
Female_Jobs = _build_female_jobs()
short_womens_jobs = Female_Jobs

__all__ = [
    "Female_Jobs",
    "FEMALE_JOBS_BASE",
    "FEMALE_JOBS_BASE_EXTENDED",
    "short_womens_jobs",
    "FEMALE_JOBS_TO",
]

len_print.data_len(
    "jobs_womens.py",
    {
        "Female_Jobs": Female_Jobs,
        "FEMALE_JOBS_BASE_EXTENDED": FEMALE_JOBS_BASE_EXTENDED,
        "short_womens_jobs": short_womens_jobs,
        "FEMALE_JOBS_TO": FEMALE_JOBS_TO,
    },
)
