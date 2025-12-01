"""
Build comprehensive gendered job label dictionaries.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Dict, List, Mapping, MutableMapping

from ...helps import len_print
from ..companies import companies_to_jobs
from ..mixed.all_keys2 import BOOK_CATEGORIES
from ..mixed.male_keys import RELIGIOUS_FEMALE_KEYS
from ..nats.Nationality import Nat_mens
from ..politics.ministers import ministrs_tab_for_Jobs_2020
from ..sports.cycling import BASE_CYCLING_EVENTS
from ..tv.films_mslslat import film_Keys_for_female
from ..utils.json_dir import open_json
from .Jobs2 import JOBS_2
from .jobs_data_basic import MEN_WOMENS_JOBS_2, NAT_BEFORE_OCC, RELIGIOUS_KEYS_PP
from .jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
    copy_gendered_map,
    merge_gendered_maps,
)
from .jobs_players_list import FOOTBALL_KEYS_PLAYERS, PLAYERS_TO_MEN_WOMENS_JOBS
from .jobs_singers import MEN_WOMENS_SINGERS
from .jobs_womens import Female_Jobs

LOGGER = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------


def _append_list_unique(sequence: List[str], value: str) -> None:
    """Append ``value`` to ``sequence`` if it is not already present."""

    if value not in sequence:
        sequence.append(value)


# ---------------------------------------------------------------------------
# Static configuration
# ---------------------------------------------------------------------------

JOBS_2020_BASE: GenderedLabelMap = {
    "ecosocialists": {"mens": "إيكولوجيون", "womens": "إيكولوجيات"},
    "wheelchair tennis players": {
        "mens": "لاعبو كرة مضرب على الكراسي المتحركة",
        "womens": "لاعبات كرة مضرب على الكراسي المتحركة",
    },
}

DISABILITY_LABELS: GenderedLabelMap = {
    "deaf": {"mens": "صم", "womens": "صم"},
    "blind": {"mens": "مكفوفون", "womens": "مكفوفات"},
    "deafblind": {"mens": "صم ومكفوفون", "womens": "صم ومكفوفات"},
}

EXECUTIVE_DOMAINS: Mapping[str, str] = {
    "railroad": "سكك حديدية",
    "media": "وسائل إعلام",
    "public transportation": "نقل عام",
    "film studio": "استوديوهات أفلام",
    "advertising": "إعلانات",
    "music industry": "صناعة الموسيقى",
    "newspaper": "جرائد",
    "radio": "مذياع",
    "television": "تلفاز",
}

TYPI_LABELS: Mapping[str, GenderedLabel] = {
    "classical": {"mens": "كلاسيكيون", "womens": "كلاسيكيات"},
    "historical": {"mens": "تاريخيون", "womens": "تاريخيات"},
}

JOBS_TYPE_TRANSLATIONS: Mapping[str, str] = {
    "adventure": "مغامرة",
    "alternate history": "تاريخ بديل",
    "animated": "رسوم متحركة",
    "science fiction action": "خيال علمي وحركة",
}

JOBS_PEOPLE_ROLES: Mapping[str, GenderedLabel] = {
    "bloggers": {"mens": "مدونو", "womens": "مدونات"},
    "writers": {"mens": "كتاب", "womens": "كاتبات"},
}

jobs_data = open_json("jobs/jobs.json")

JOBS_2020_BASE.update({x: v for x, v in jobs_data["JOBS_2020"].items() if v.get("mens") and v.get("womens")})

JOBS_PEOPLE_ROLES.update({x: v for x, v in jobs_data["JOBS_PEOPLE"].items() if v.get("mens") and v.get("womens")})

JOBS_TYPE_TRANSLATIONS.update({x: v for x, v in jobs_data["JOBS_TYPE"].items() if v})  # v is string


FILM_ROLE_LABELS: Mapping[str, GenderedLabel] = {
    "filmmakers": {"mens": "صانعو أفلام", "womens": "صانعات أفلام"},
    "film editors": {"mens": "محررو أفلام", "womens": "محررات أفلام"},
    "film directors": {"mens": "مخرجو أفلام", "womens": "مخرجات أفلام"},
    "film producers": {"mens": "منتجو أفلام", "womens": "منتجات أفلام"},
    "film critics": {"mens": "نقاد أفلام", "womens": "ناقدات أفلام"},
    "film historians": {"mens": "مؤرخو أفلام", "womens": "مؤرخات أفلام"},
    "cinema editors": {"mens": "محررون سينمائون", "womens": "محررات سينمائيات"},
    "cinema directors": {"mens": "مخرجون سينمائون", "womens": "مخرجات سينمائيات"},
    "cinema producers": {"mens": "منتجون سينمائون", "womens": "منتجات سينمائيات"},
}


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------


@dataclass
class JobsDataset:
    """Aggregate all exported job dictionaries."""

    jobs_keys_mens: Dict[str, str]
    w_jobs_2017: Dict[str, str]


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------


def _build_jobs_2020() -> GenderedLabelMap:
    """Return the 2020 job dictionary merged with ministerial categories."""

    jobs_2020 = copy_gendered_map(JOBS_2020_BASE)
    for category, labels in ministrs_tab_for_Jobs_2020.items():
        jobs_2020[category] = {"mens": labels["mens"], "womens": labels["womens"]}
    return jobs_2020


def _extend_with_religious_jobs(base_jobs: GenderedLabelMap) -> GenderedLabelMap:
    """Add religious role combinations and their activist variants."""

    jobs = copy_gendered_map(base_jobs)
    for religion_key, labels in RELIGIOUS_KEYS_PP.items():
        jobs[religion_key] = {"mens": labels["mens"], "womens": labels["womens"]}
        activist_key = f"{religion_key} activists"
        jobs[activist_key] = {"mens": f"ناشطون {labels['mens']}", "womens": f"ناشطات {labels['womens']}"}
    return jobs


def _extend_with_disability_jobs(base_jobs: GenderedLabelMap) -> GenderedLabelMap:
    """Insert disability-focused job labels and executive variants."""

    jobs = copy_gendered_map(base_jobs)
    merge_gendered_maps(jobs, DISABILITY_LABELS)
    for domain_key, domain_label in EXECUTIVE_DOMAINS.items():
        if not domain_label:
            continue
        jobs[f"{domain_key} executives"] = {"mens": f"مدراء {domain_label}", "womens": f"مديرات {domain_label}"}
    return jobs


def _merge_jobs_sources() -> GenderedLabelMap:
    """Combine JSON sources and static configuration into a single map."""

    jobs_pp = open_json("jobs/jobs_Men_Womens_PP.json")
    jobs_pp = _extend_with_religious_jobs(jobs_pp)
    jobs_pp = _extend_with_disability_jobs(jobs_pp)

    jobs_2020 = _build_jobs_2020()
    for job_name, labels in jobs_2020.items():
        if labels["mens"] and labels["womens"]:
            lowered = job_name.lower()
            if lowered not in jobs_pp:
                jobs_pp[lowered] = {"mens": labels["mens"], "womens": labels["womens"]}

    for category, labels in FOOTBALL_KEYS_PLAYERS.items():
        lowered = category.lower()
        if lowered not in jobs_pp:
            jobs_pp[lowered] = {"mens": labels["mens"], "womens": labels["womens"]}

    jobs_pp["fashion journalists"] = {"mens": "صحفيو موضة", "womens": "صحفيات موضة"}
    jobs_pp["zionists"] = {"mens": "صهاينة", "womens": "صهيونيات"}

    merge_gendered_maps(jobs_pp, companies_to_jobs)

    for religion_key, feminine_label in RELIGIOUS_FEMALE_KEYS.items():
        founder_key = f"{religion_key} founders"
        jobs_pp[founder_key] = {"mens": f"مؤسسو {feminine_label}", "womens": f"مؤسسات {feminine_label}"}

    jobs_pp["imprisoned abroad"] = {"mens": "مسجونون في الخارج", "womens": "مسجونات في الخارج"}
    jobs_pp["imprisoned"] = {"mens": "مسجونون", "womens": "مسجونات"}
    jobs_pp["escapees"] = {"mens": "هاربون", "womens": "هاربات"}
    jobs_pp["prison escapees"] = {"mens": "هاربون من السجن", "womens": "هاربات من السجن"}
    jobs_pp["missionaries"] = {"mens": "مبشرون", "womens": "مبشرات"}
    jobs_pp["venerated"] = {"mens": "مبجلون", "womens": "مبجلات"}

    return jobs_pp


def _add_jobs_from_jobs2(jobs_pp: GenderedLabelMap) -> GenderedLabelMap:
    """Merge entries from :mod:`Jobs2` that are missing from ``jobs_pp``."""

    merged = copy_gendered_map(jobs_pp)
    for job_key, labels in JOBS_2.items():
        lowered = job_key.lower()
        if lowered not in merged and (labels["mens"] or labels["womens"]):
            merged[lowered] = {"mens": labels["mens"], "womens": labels["womens"]}
    return merged


def _load_activist_jobs(m_w_jobs: MutableMapping[str, GenderedLabel], nat_before_occ: List[str]) -> None:
    """Extend ``m_w_jobs`` with activist categories from JSON."""

    activists = open_json("jobs/activists_keys.json")
    for category, labels in activists.items():
        lowered = category.lower()
        _append_list_unique(nat_before_occ, lowered)
        m_w_jobs[lowered] = {"mens": labels["mens"], "womens": labels["womens"]}


def _add_sport_variants(
    m_w_jobs: MutableMapping[str, GenderedLabel],
    base_jobs: Mapping[str, GenderedLabel],
) -> None:
    """Derive sport, professional, and wheelchair variants for job labels."""

    for base_key, base_labels in base_jobs.items():
        lowered = base_key.lower()
        m_w_jobs[f"sports {lowered}"] = {
            "mens": f"{base_labels['mens']} رياضيون",
            "womens": f"{base_labels['womens']} رياضيات",
        }
        m_w_jobs[f"professional {lowered}"] = {
            "mens": f"{base_labels['mens']} محترفون",
            "womens": f"{base_labels['womens']} محترفات",
        }
        m_w_jobs[f"wheelchair {lowered}"] = {
            "mens": f"{base_labels['mens']} على الكراسي المتحركة",
            "womens": f"{base_labels['womens']} على الكراسي المتحركة",
        }


def _add_cycling_variants(
    m_w_jobs: MutableMapping[str, GenderedLabel],
    nat_before_occ: List[str],
) -> None:
    """Insert variants derived from cycling events."""

    for event_key, event_label in BASE_CYCLING_EVENTS.items():
        lowered = event_key.lower()
        m_w_jobs[f"{lowered} cyclists"] = {"mens": f"دراجو {event_label}", "womens": f"دراجات {event_label}"}
        winners_key = f"{lowered} winners"
        stage_winners_key = f"{lowered} stage winners"
        m_w_jobs[winners_key] = {"mens": f"فائزون في {event_label}", "womens": f"فائزات في {event_label}"}
        m_w_jobs[stage_winners_key] = {
            "mens": f"فائزون في مراحل {event_label}",
            "womens": f"فائزات في مراحل {event_label}",
        }
        _append_list_unique(nat_before_occ, winners_key)
        _append_list_unique(nat_before_occ, stage_winners_key)


def _add_jobs_people_variants(m_w_jobs: MutableMapping[str, GenderedLabel]) -> None:
    """Create combinations of people-centric roles with book genres and types."""

    for role_key, role_labels in JOBS_PEOPLE_ROLES.items():
        if not (role_labels["mens"] and role_labels["womens"]):
            continue
        for book_key, book_label in BOOK_CATEGORIES.items():
            m_w_jobs[f"{book_key} {role_key}"] = {
                "mens": f"{role_labels['mens']} {book_label}",
                "womens": f"{role_labels['womens']} {book_label}",
            }
        for genre_key, genre_label in JOBS_TYPE_TRANSLATIONS.items():
            m_w_jobs[f"{genre_key} {role_key}"] = {
                "mens": f"{role_labels['mens']} {genre_label}",
                "womens": f"{role_labels['womens']} {genre_label}",
            }


def _add_film_variants(m_w_jobs: MutableMapping[str, GenderedLabel]) -> None:
    """Create film-related job variants and return the number of generated entries."""

    for film_key, film_label in film_Keys_for_female.items():
        lowered_film_key = film_key.lower()
        for role_key, role_labels in FILM_ROLE_LABELS.items():
            m_w_jobs[role_key] = {"mens": role_labels["mens"], "womens": role_labels["womens"]}
            combo_key = f"{lowered_film_key} {role_key}"
            m_w_jobs[combo_key] = {
                "mens": f"{role_labels['mens']} {film_label}",
                "womens": f"{role_labels['womens']} {film_label}",
            }


def _add_singer_variants(m_w_jobs: MutableMapping[str, GenderedLabel]) -> None:
    """Add singer categories and stylistic combinations."""

    for category, labels in MEN_WOMENS_SINGERS.items():
        m_w_jobs[category] = {"mens": labels["mens"], "womens": labels["womens"]}
        for style_key, style_labels in TYPI_LABELS.items():
            combo_key = f"{style_key} {category}"
            m_w_jobs[combo_key] = {
                "mens": f"{labels['mens']} {style_labels['mens']}",
                "womens": f"{labels['womens']} {style_labels['womens']}",
            }


def _build_jobs_new(
    female_jobs: Mapping[str, str],
) -> Dict[str, str]:
    """Build the flattened ``Jobs_new`` mapping used by legacy bots."""

    data: Dict[str, str] = {}

    for female_key, female_label in female_jobs.items():
        if female_label:
            lowered = female_key.lower()
            data[lowered] = female_label

    for nationality_key, nationality_label in Nat_mens.items():
        if nationality_label:
            data[f"{nationality_key.lower()} people"] = nationality_label

    data["people of the ottoman empire"] = "عثمانيون"

    return data


def _finalise_jobs_dataset() -> JobsDataset:
    """Construct the full jobs dataset from individual builders."""

    jobs_pp = _merge_jobs_sources()
    jobs_pp = _add_jobs_from_jobs2(jobs_pp)

    m_w_jobs: GenderedLabelMap = {}
    merge_gendered_maps(m_w_jobs, MEN_WOMENS_JOBS_2)

    _load_activist_jobs(m_w_jobs, NAT_BEFORE_OCC)

    for job_key, labels in jobs_pp.items():
        m_w_jobs[job_key.lower()] = {"mens": labels["mens"], "womens": labels["womens"]}

    _add_sport_variants(m_w_jobs, jobs_pp)
    merge_gendered_maps(m_w_jobs, PLAYERS_TO_MEN_WOMENS_JOBS)
    _add_cycling_variants(m_w_jobs, NAT_BEFORE_OCC)
    _add_jobs_people_variants(m_w_jobs)
    _add_film_variants(m_w_jobs)
    _add_singer_variants(m_w_jobs)

    jobs_keys_mens: Dict[str, str] = {}
    w_jobs_2017: Dict[str, str] = {}

    for job_key, labels in m_w_jobs.items():
        jobs_keys_mens[job_key] = labels["mens"]
        if labels["womens"]:
            w_jobs_2017[job_key] = labels["womens"]

    jobs_keys_mens["men's footballers"] = "لاعبو كرة قدم رجالية"

    jobs_keys_mens = {key: label for key, label in jobs_keys_mens.items() if label}

    return JobsDataset(
        jobs_keys_mens=jobs_keys_mens,
        w_jobs_2017=w_jobs_2017,
    )


_DATASET = _finalise_jobs_dataset()

jobs_mens_data = _DATASET.jobs_keys_mens

jobs_womens_data = _DATASET.w_jobs_2017

Jobs_new = _build_jobs_new(Female_Jobs)

_len_result = {
    "jobs_mens_data": {"count": 97797, "size": "3.7 MiB"},  # "zoologists": "علماء حيوانات"
    "Jobs_key": {"count": 97784, "size": "3.7 MiB"},  # "zoologists": "علماء حيوانات"
    "Men_Womens_Jobs": {
        "count": 97796,
        "size": "3.7 MiB",
    },  # "zoologists": { "mens": "علماء حيوانات", "womens": "عالمات حيوانات" }
    "Jobs_new": {"count": 99104, "size": "3.7 MiB"},  # same as Jobs_key +
    "jobs_womens_data": {"count": 75244, "size": "1.8 MiB"},
}
len_print.data_len(
    "jobs.py",
    {
        "jobs_mens_data": jobs_mens_data,
        "jobs_womens_data": jobs_womens_data,
        "Jobs_new": Jobs_new,
    },
)

__all__ = [
    "jobs_mens_data",
    "jobs_womens_data",
    "Jobs_new",
]
