"""Build comprehensive gendered job label dictionaries.

This module historically assembled several large dictionaries describing job
labels in Arabic.  The original implementation relied on implicit global state
and mutating logic that made the data construction difficult to follow.

The refactor below keeps the exported data identical while restructuring the
pipeline into typed helper functions with clear documentation.  Each helper
focuses on a single transformation—loading JSON data, combining gendered labels,
adding derived sport or film variants, or flattening the output for historic
exports.  The end result is a deterministic data set that is easier to maintain
and safe to import in other modules.
"""

from __future__ import annotations

import logging
import sys
from dataclasses import dataclass
from typing import Dict, List, Mapping, MutableMapping

from ...helps import len_print
from ..companies import companies_to_jobs
from ..utils.json_dir import open_json
from ..mixed.all_keys2 import Books_table
from ..mixed.male_keys import religious_female_keys
from ..nats.Nationality import Nat_mens
from ..politics.ministers import ministrs_tab_for_Jobs_2020
from ..sports.cycling import new2019_cycling
from ..tv.films_mslslat import Films_key_For_Jobs
from .Jobs2 import JOBS_2
from .jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
    copy_gendered_map,
    gendered_label,
    merge_gendered_maps,
)
from .jobs_data import RELIGIOUS_KEYS_PP, MEN_WOMENS_JOBS_2
from .jobs_players_list import (
    FEMALE_JOBS_TO,
    FOOTBALL_KEYS_PLAYERS,
    PLAYERS_TO_MEN_WOMENS_JOBS,
)
from .jobs_singers import MEN_WOMENS_SINGERS, FILMS_TYPE

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

Jobs_new = {}

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

NAT_BEFORE_OCC_BASE: List[str] = [
    "convicted-of-murder",
    "murdered abroad",
    "contemporary",
    "tour de france stage winners",
    "deafblind",
    "deaf",
    "blind",
    "jews",
    "women's rights activists",
    "human rights activists",
    "imprisoned",
    "imprisoned abroad",
    "conservationists",
    "expatriate",
    "defectors",
    "scholars of islam",
    "scholars-of-islam",
    "amputees",
    "expatriates",
    "scholars of",
    "executed abroad",
    "emigrants",
]

MEN_WOMENS_WITH_NATO: GenderedLabelMap = {
    "eugenicists": {
        "mens": "علماء {nato} متخصصون في تحسين النسل",
        "womens": "عالمات {nato} متخصصات في تحسين النسل",
    },
    "politicians who committed suicide": {
        "mens": "سياسيون {nato} أقدموا على الانتحار",
        "womens": "سياسيات {nato} أقدمن على الانتحار",
    },
    "contemporary artists": {
        "mens": "فنانون {nato} معاصرون",
        "womens": "فنانات {nato} معاصرات",
    },
}

TYPI_LABELS: Mapping[str, GenderedLabel] = {
    "classical": {"mens": "كلاسيكيون", "womens": "كلاسيكيات"},
    "historical": {"mens": "تاريخيون", "womens": "تاريخيات"},
}

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

JOBS_2020_BASE.update({
    x: v
    for x, v in jobs_data["JOBS_2020"].items()
    if v.get("mens") and v.get("womens")
})

JOBS_PEOPLE_ROLES.update({
    x: v
    for x, v in jobs_data["JOBS_PEOPLE"].items()
    if v.get("mens") and v.get("womens")
})

JOBS_TYPE_TRANSLATIONS.update({
    x: v
    for x, v in jobs_data["JOBS_TYPE"].items()
    if v
})  # v is string


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

    jobs_key_mens: Dict[str, str]
    jobs_key_womens: Dict[str, str]
    womens_jobs_2017: Dict[str, str]
    female_jobs: Dict[str, str]
    men_womens_jobs: GenderedLabelMap
    nat_before_occ: List[str]
    men_womens_with_nato: GenderedLabelMap
    jobs_new: Dict[str, str]
    jobs_key: Dict[str, str]


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
        jobs[activist_key] = gendered_label(
            f"ناشطون {labels['mens']}",
            f"ناشطات {labels['womens']}",
        )
    return jobs


def _extend_with_disability_jobs(base_jobs: GenderedLabelMap) -> GenderedLabelMap:
    """Insert disability-focused job labels and executive variants."""

    jobs = copy_gendered_map(base_jobs)
    merge_gendered_maps(jobs, DISABILITY_LABELS)
    for domain_key, domain_label in EXECUTIVE_DOMAINS.items():
        if not domain_label:
            continue
        jobs[f"{domain_key} executives"] = gendered_label(
            f"مدراء {domain_label}",
            f"مديرات {domain_label}",
        )
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
        if category not in jobs_pp:
            jobs_pp[category] = {"mens": labels["mens"], "womens": labels["womens"]}

    jobs_pp["fashion journalists"] = {"mens": "صحفيو موضة", "womens": "صحفيات موضة"}
    jobs_pp["zionists"] = {"mens": "صهاينة", "womens": "صهيونيات"}

    merge_gendered_maps(jobs_pp, companies_to_jobs)

    for religion_key, feminine_label in religious_female_keys.items():
        founder_key = f"{religion_key} founders"
        jobs_pp[founder_key] = gendered_label(
            f"مؤسسو {feminine_label}",
            f"مؤسسات {feminine_label}",
        )

    jobs_pp["imprisoned abroad"] = {"mens": "مسجونون في الخارج", "womens": "مسجونات في الخارج"}
    jobs_pp["imprisoned"] = {"mens": "مسجونون", "womens": "مسجونات"}
    jobs_pp["escapees"] = {"mens": "هاربون", "womens": "هاربات"}
    jobs_pp["prison escapees"] = gendered_label(
        "هاربون من السجن",
        "هاربات من السجن",
    )
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


def _load_activist_jobs(men_womens_jobs: MutableMapping[str, GenderedLabel], nat_before_occ: List[str]) -> None:
    """Extend ``men_womens_jobs`` with activist categories from JSON."""

    activists = open_json("jobs/activists_keys.json")
    for category, labels in activists.items():
        lowered = category.lower()
        _append_list_unique(nat_before_occ, lowered)
        men_womens_jobs[lowered] = {"mens": labels["mens"], "womens": labels["womens"]}


def _add_sport_variants(
    men_womens_jobs: MutableMapping[str, GenderedLabel],
    base_jobs: Mapping[str, GenderedLabel],
) -> None:
    """Derive sport, professional, and wheelchair variants for job labels."""

    for base_key, base_labels in base_jobs.items():
        lowered = base_key.lower()
        men_womens_jobs[f"sports {lowered}"] = gendered_label(
            f"{base_labels['mens']} رياضيون",
            f"{base_labels['womens']} رياضيات",
        )
        men_womens_jobs[f"professional {lowered}"] = gendered_label(
            f"{base_labels['mens']} محترفون",
            f"{base_labels['womens']} محترفات",
        )
        men_womens_jobs[f"wheelchair {lowered}"] = gendered_label(
            f"{base_labels['mens']} على الكراسي المتحركة",
            f"{base_labels['womens']} على الكراسي المتحركة",
        )


def _add_cycling_variants(
    men_womens_jobs: MutableMapping[str, GenderedLabel],
    nat_before_occ: List[str],
) -> None:
    """Insert variants derived from cycling events."""

    for event_key, event_label in new2019_cycling.items():
        lowered = event_key.lower()
        men_womens_jobs[f"{lowered} cyclists"] = gendered_label(
            f"دراجو {event_label}",
            f"دراجات {event_label}",
        )
        winners_key = f"{lowered} winners"
        stage_winners_key = f"{lowered} stage winners"
        men_womens_jobs[winners_key] = gendered_label(
            f"فائزون في {event_label}",
            f"فائزات في {event_label}",
        )
        men_womens_jobs[stage_winners_key] = gendered_label(
            f"فائزون في مراحل {event_label}",
            f"فائزات في مراحل {event_label}",
        )
        _append_list_unique(nat_before_occ, winners_key)
        _append_list_unique(nat_before_occ, stage_winners_key)


def _add_jobs_people_variants(men_womens_jobs: MutableMapping[str, GenderedLabel]) -> None:
    """Create combinations of people-centric roles with book genres and types."""

    for role_key, role_labels in JOBS_PEOPLE_ROLES.items():
        if not (role_labels["mens"] and role_labels["womens"]):
            continue
        for book_key, book_label in Books_table.items():
            men_womens_jobs[f"{book_key} {role_key}"] = gendered_label(
                f"{role_labels['mens']} {book_label}",
                f"{role_labels['womens']} {book_label}",
            )
        for genre_key, genre_label in JOBS_TYPE_TRANSLATIONS.items():
            men_womens_jobs[f"{genre_key} {role_key}"] = gendered_label(
                f"{role_labels['mens']} {genre_label}",
                f"{role_labels['womens']} {genre_label}",
            )


def _add_film_variants(men_womens_jobs: MutableMapping[str, GenderedLabel]) -> int:
    """Create film-related job variants and return the number of generated entries."""

    count = 0
    for film_key, film_label in Films_key_For_Jobs.items():
        lowered_film_key = film_key.lower()
        for role_key, role_labels in FILM_ROLE_LABELS.items():
            men_womens_jobs[role_key] = {"mens": role_labels["mens"], "womens": role_labels["womens"]}
            combo_key = f"{lowered_film_key} {role_key}"
            men_womens_jobs[combo_key] = gendered_label(
                f"{role_labels['mens']} {film_label}",
                f"{role_labels['womens']} {film_label}",
            )
            count += 1
    return count


def _add_singer_variants(men_womens_jobs: MutableMapping[str, GenderedLabel]) -> None:
    """Add singer categories and stylistic combinations."""

    for category, labels in MEN_WOMENS_SINGERS.items():
        men_womens_jobs[category] = {"mens": labels["mens"], "womens": labels["womens"]}
        for style_key, style_labels in TYPI_LABELS.items():
            combo_key = f"{style_key} {category}"
            men_womens_jobs[combo_key] = gendered_label(
                f"{labels['mens']} {style_labels['mens']}",
                f"{labels['womens']} {style_labels['womens']}",
            )


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


def _build_jobs_new(
    jobs_key: Mapping[str, str],
    female_jobs: Mapping[str, str],
) -> Dict[str, str]:
    """Build the flattened ``Jobs_new`` mapping used by legacy bots."""

    jobs_new: Dict[str, str] = {}
    for female_key, female_label in female_jobs.items():
        if female_label:
            lowered = female_key.lower()
            jobs_new[lowered] = female_label
    for nationality_key, nationality_label in Nat_mens.items():
        if nationality_label:
            jobs_new[f"{nationality_key.lower()} people"] = nationality_label
    jobs_new["people of the ottoman empire"] = "عثمانيون"
    for job_key, job_label in jobs_key.items():
        lowered = job_key.lower()
        if job_label:
            jobs_new[lowered] = job_label
    return jobs_new


def _finalise_jobs_dataset() -> JobsDataset:
    """Construct the full jobs dataset from individual builders."""

    nat_before_occ = list(NAT_BEFORE_OCC_BASE)
    nat_before_occ.extend(key for key in RELIGIOUS_KEYS_PP.keys())

    jobs_pp = _merge_jobs_sources()
    jobs_pp = _add_jobs_from_jobs2(jobs_pp)

    men_womens_jobs: GenderedLabelMap = {}
    merge_gendered_maps(men_womens_jobs, MEN_WOMENS_JOBS_2)

    _load_activist_jobs(men_womens_jobs, nat_before_occ)

    for job_key, labels in jobs_pp.items():
        men_womens_jobs[job_key.lower()] = {"mens": labels["mens"], "womens": labels["womens"]}

    _add_sport_variants(men_womens_jobs, jobs_pp)
    merge_gendered_maps(men_womens_jobs, PLAYERS_TO_MEN_WOMENS_JOBS)
    _add_cycling_variants(men_womens_jobs, nat_before_occ)
    _add_jobs_people_variants(men_womens_jobs)
    film_variant_count = _add_film_variants(men_womens_jobs)
    _add_singer_variants(men_womens_jobs)

    jobs_key_mens: Dict[str, str] = {}
    womens_jobs_2017: Dict[str, str] = {}
    for job_key, labels in men_womens_jobs.items():
        jobs_key_mens[job_key] = labels["mens"]
        if labels["womens"]:
            womens_jobs_2017[job_key] = labels["womens"]

    jobs_key_mens["men's footballers"] = "لاعبو كرة قدم رجالية"

    female_jobs = _build_female_jobs()
    jobs_key_womens: Dict[str, str] = {}
    for female_key, female_label in female_jobs.items():
        if female_label:
            jobs_key_womens[female_key.lower()] = female_label

    jobs_key: Dict[str, str] = {key: label for key, label in jobs_key_mens.items() if label}

    jobs_new = _build_jobs_new(jobs_key, female_jobs)

    return JobsDataset(
        jobs_key_mens=jobs_key_mens,
        jobs_key_womens=jobs_key_womens,
        womens_jobs_2017=womens_jobs_2017,
        female_jobs=female_jobs,
        men_womens_jobs=men_womens_jobs,
        nat_before_occ=nat_before_occ,
        men_womens_with_nato=copy_gendered_map(MEN_WOMENS_WITH_NATO),
        jobs_new=jobs_new,
        jobs_key=jobs_key,
    )


_DATASET = _finalise_jobs_dataset()

Jobs_key_mens = _DATASET.jobs_key_mens
Jobs_key_womens = _DATASET.jobs_key_womens
womens_Jobs_2017 = _DATASET.womens_jobs_2017
Female_Jobs = _DATASET.female_jobs
Men_Womens_Jobs = _DATASET.men_womens_jobs
Nat_Before_Occ = _DATASET.nat_before_occ
Men_Womens_with_nato = _DATASET.men_womens_with_nato
Jobs_new = _DATASET.jobs_new
Jobs_key = _DATASET.jobs_key

len_print.data_len("jobs.py", {
    "Jobs_key_mens": Jobs_key_mens,
    "Jobs_key_womens": Jobs_key_womens,
    "womens_Jobs_2017": womens_Jobs_2017,
    "Female_Jobs": Female_Jobs,
    "Men_Womens_Jobs": Men_Womens_Jobs,
    "Nat_Before_Occ": Nat_Before_Occ,
    "Men_Womens_with_nato": Men_Womens_with_nato,
    "Jobs_new": Jobs_new,
    "Jobs_key": Jobs_key,
})

__all__ = [
    "Jobs_key_mens",
    "Jobs_key_womens",
    "womens_Jobs_2017",
    "Female_Jobs",
    "Men_Womens_Jobs",
    "Nat_Before_Occ",
    "Men_Womens_with_nato",
    "Jobs_new",
    "Jobs_key"
]
