"""
Build comprehensive gendered job label dictionaries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Mapping, MutableMapping

from ...helps import len_print
from ..mixed.all_keys2 import BOOK_CATEGORIES
from ..mixed.female_keys import RELIGIOUS_FEMALE_KEYS
from ..nats.Nationality import Nat_mens
from ..sports.cycling import BASE_CYCLING_EVENTS
from ..utils.json_dir import open_json_file
from .Jobs2 import JOBS_2, JOBS_3333
from .jobs_data_basic import MEN_WOMENS_JOBS_2, NAT_BEFORE_OCC, RELIGIOUS_KEYS_PP
from .jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
    copy_gendered_map,
    merge_gendered_maps,
)
from .jobs_players_list import FOOTBALL_KEYS_PLAYERS, PLAYERS_TO_MEN_WOMENS_JOBS, SPORT_JOB_VARIANTS
from .jobs_singers import MEN_WOMENS_SINGERS, MEN_WOMENS_SINGERS_BASED
from .jobs_womens import short_womens_jobs

# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

companies_to_jobs = {
    "mass media owners": {"males": "ملاك وسائل إعلام", "females": "مالكات وسائل إعلام"},
    "media owners": {"males": "ملاك إعلامية", "females": "مالكات إعلامية"},
    "magazine founders": {"males": "مؤسسو مجلات", "females": "مؤسسات مجلات"},
    "television company founders": {"males": "مؤسسو شركات تلفاز", "females": "مؤسسات شركات تلفاز"},
    "technology company founders": {"males": "مؤسسو شركات تقانة", "females": "مؤسسات شركات تقانة"},
    "mass media company founders": {"males": "مؤسسو شركات وسائل إعلام", "females": "مؤسسات شركات وسائل إعلام"},
    "media company founders": {"males": "مؤسسو شركات إعلامية", "females": "مؤسسات شركات إعلامية"},
    "financial company founders": {"males": "مؤسسو شركات مالية", "females": "مؤسسات شركات مالية"},
    "retail company founders": {"males": "مؤسسو شركات تجارة التجزئة", "females": "مؤسسات شركات تجارة التجزئة"},
    "internet company founders": {"males": "مؤسسو شركات إنترنت", "females": "مؤسسات شركات إنترنت"},
    "drink company founders": {"males": "مؤسسو شركات مشروبات", "females": "مؤسسات شركات مشروبات"},
    "publishing company founders": {"males": "مؤسسو شركات نشر", "females": "مؤسسات شركات نشر"},
    "entertainment company founders": {"males": "مؤسسو شركات ترفيه", "females": "مؤسسات شركات ترفيه"},
    "food company founders": {"males": "مؤسسو شركات أطعمة", "females": "مؤسسات شركات أطعمة"},
    "real estate company founders": {"males": "مؤسسو شركات عقارية", "females": "مؤسسات شركات عقارية"},
    "food and drink company founders": {
        "males": "مؤسسو شركات أطعمة ومشروبات",
        "females": "مؤسسات شركات أطعمة ومشروبات",
    },
    "pharmaceutical company founders": {"males": "مؤسسو شركات أدوية", "females": "مؤسسات شركات أدوية"},
    "shipping company founders": {"males": "مؤسسو شركات نقل بحري", "females": "مؤسسات شركات نقل بحري"},
    "airline founders": {"males": "مؤسسو خطوط جوية", "females": "مؤسسات خطوط جوية"},
    "construction and civil engineering company founders": {
        "males": "مؤسسو شركات بناء وهندسة مدنية",
        "females": "مؤسسات شركات بناء وهندسة مدنية",
    },
    "engineering company founders": {"males": "مؤسسو شركات هندسية", "females": "مؤسسات شركات هندسية"},
    "design company founders": {"males": "مؤسسو شركات تصميم", "females": "مؤسسات شركات تصميم"},
    "energy company founders": {"males": "مؤسسو شركات طاقة", "females": "مؤسسات شركات طاقة"},
    "health care company founders": {"males": "مؤسسو شركات رعاية صحية", "females": "مؤسسات شركات رعاية صحية"},
    "manufacturing company founders": {"males": "مؤسسو شركات تصنيع", "females": "مؤسسات شركات تصنيع"},
    "media founders": {"males": "مؤسسو وسائل إعلامية", "females": "مؤسسات وسائل إعلامية"},
    "mining company founders": {"males": "مؤسسو شركات تعدين", "females": "مؤسسات شركات تعدين"},
    "transport company founders": {"males": "مؤسسو شركات نقل", "females": "مؤسسات شركات نقل"},
}


def _append_list_unique(sequence: List[str], value: str) -> None:
    """Append ``value`` to ``sequence`` if it is not already present."""

    if value not in sequence:
        sequence.append(value)


# ---------------------------------------------------------------------------
# Static configuration
# ---------------------------------------------------------------------------

JOBS_2020_BASE: GenderedLabelMap = {
    "ecosocialists": {"males": "إيكولوجيون", "females": "إيكولوجيات"},
    "wheelchair tennis players": {
        "males": "لاعبو كرة مضرب على الكراسي المتحركة",
        "females": "لاعبات كرة مضرب على الكراسي المتحركة",
    },
}

DISABILITY_LABELS: GenderedLabelMap = {
    "deaf": {"males": "صم", "females": "صم"},
    "blind": {"males": "مكفوفون", "females": "مكفوفات"},
    "deafblind": {"males": "صم ومكفوفون", "females": "صم ومكفوفات"},
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
    "classical": {"males": "كلاسيكيون", "females": "كلاسيكيات"},
    "historical": {"males": "تاريخيون", "females": "تاريخيات"},
}

JOBS_TYPE_TRANSLATIONS: Mapping[str, str] = {
    "adventure": "مغامرة",
    "alternate history": "تاريخ بديل",
    "animated": "رسوم متحركة",
    "science fiction action": "خيال علمي وحركة",
}

JOBS_PEOPLE_ROLES: Mapping[str, GenderedLabel] = {
    "bloggers": {"males": "مدونون", "females": "مدونات"},
    "writers": {"males": "كتاب", "females": "كاتبات"},
    "news anchors": {"males": "مذيعو أخبار", "females": "مذيعات أخبار"},
    "non-fiction writers": {"males": "كتاب غير روائيين", "females": "كاتبات غير روائيات"},
    "critics": {"males": "نقاد", "females": "ناقدات"},
    "personalities": {"males": "شخصيات", "females": "شخصيات"},
    "journalists": {"males": "صحفيو", "females": "صحفيات"},
    "producers": {"males": "منتجو", "females": "منتجات"},
    "authors": {"males": "مؤلفو", "females": "مؤلفات"},
    "editors": {"males": "محررو", "females": "محررات"},
    "artists": {"males": "فنانو", "females": "فنانات"},
    "directors": {"males": "مخرجو", "females": "مخرجات"},
    "publisherspeople": {"males": "ناشرو", "females": "ناشرات"},
    "publishers (people)": {"males": "ناشرو", "females": "ناشرات"},
    "presenters": {"males": "مذيعو", "females": "مذيعات"},
    "creators": {"males": "مبتكرو", "females": "مبتكرات"},
}

jobs_data = open_json_file("jobs/jobs.json")

JOBS_2020_BASE.update({x: v for x, v in jobs_data["JOBS_2020"].items() if v.get("males") and v.get("females")})

JOBS_TYPE_TRANSLATIONS.update({x: v for x, v in jobs_data["JOBS_TYPE"].items() if v})  # v is string


FILM_ROLE_LABELS: Mapping[str, GenderedLabel] = {
    "filmmakers": {"males": "صانعو أفلام", "females": "صانعات أفلام"},
    "film editors": {"males": "محررو أفلام", "females": "محررات أفلام"},
    "film directors": {"males": "مخرجو أفلام", "females": "مخرجات أفلام"},
    "film producers": {"males": "منتجو أفلام", "females": "منتجات أفلام"},
    "film critics": {"males": "نقاد أفلام", "females": "ناقدات أفلام"},
    "film historians": {"males": "مؤرخو أفلام", "females": "مؤرخات أفلام"},
    "cinema editors": {"males": "محررون سينمائون", "females": "محررات سينمائيات"},
    "cinema directors": {"males": "مخرجون سينمائون", "females": "مخرجات سينمائيات"},
    "cinema producers": {"males": "منتجون سينمائون", "females": "منتجات سينمائيات"},
}


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------


@dataclass
class JobsDataset:
    """Aggregate all exported job dictionaries."""

    males_jobs: Dict[str, str]
    females_jobs: Dict[str, str]


# ---------------------------------------------------------------------------
# Builders
# ---------------------------------------------------------------------------


def _build_jobs_2020() -> GenderedLabelMap:
    """Return the 2020 job dictionary merged with ministerial categories."""

    jobs_2020 = copy_gendered_map(JOBS_2020_BASE)
    return jobs_2020


def _extend_with_religious_jobs(base_jobs: GenderedLabelMap) -> GenderedLabelMap:
    """Add religious role combinations and their activist variants."""

    jobs = copy_gendered_map(base_jobs)
    for religion_key, labels in RELIGIOUS_KEYS_PP.items():
        jobs[religion_key] = {"males": labels["males"], "females": labels["females"]}
        activist_key = f"{religion_key} activists"
        jobs[activist_key] = {"males": f"ناشطون {labels['males']}", "females": f"ناشطات {labels['females']}"}
    return jobs


def _extend_with_disability_jobs(base_jobs: GenderedLabelMap) -> GenderedLabelMap:
    """Insert disability-focused job labels and executive variants."""

    jobs = copy_gendered_map(base_jobs)
    merge_gendered_maps(jobs, DISABILITY_LABELS)
    for domain_key, domain_label in EXECUTIVE_DOMAINS.items():
        if not domain_label:
            continue
        jobs[f"{domain_key} executives"] = {"males": f"مدراء {domain_label}", "females": f"مديرات {domain_label}"}
    return jobs


def _merge_jobs_sources() -> GenderedLabelMap:
    """Combine JSON sources and static configuration into a single map."""

    jobs_pp = open_json_file("jobs/jobs_Men_Womens_PP.json")
    jobs_pp.update(
        {
            "candidates": {"males": "مرشحون", "females": "مرشحات"},
            "presidential candidates": {"males": "مرشحون رئاسيون", "females": "مرشحات رئاسيات"},
            "political candidates": {"males": "مرشحون سياسيون", "females": "مرشحات سياسيات"},
        }
    )

    jobs_pp["coaches"] = {"males": "مدربون", "females": "مدربات"}
    # jobs_pp["sports coaches"] = {"males": "مدربون رياضيون", "females": "مدربات رياضيات"}
    jobs_pp.setdefault("men", {"males": "رجال", "females": ""})

    jobs_pp = _extend_with_religious_jobs(jobs_pp)
    jobs_pp = _extend_with_disability_jobs(jobs_pp)

    jobs_2020 = _build_jobs_2020()
    for job_name, labels in jobs_2020.items():
        if labels["males"] and labels["females"]:
            lowered = job_name.lower()
            if lowered not in jobs_pp:
                jobs_pp[lowered] = {"males": labels["males"], "females": labels["females"]}

    for category, labels in FOOTBALL_KEYS_PLAYERS.items():
        lowered = category.lower()
        if lowered not in jobs_pp:
            jobs_pp[lowered] = {"males": labels["males"], "females": labels["females"]}

    jobs_pp["fashion journalists"] = {"males": "صحفيو موضة", "females": "صحفيات موضة"}
    jobs_pp["zionists"] = {"males": "صهاينة", "females": "صهيونيات"}

    merge_gendered_maps(jobs_pp, companies_to_jobs)

    for religion_key, feminine_label in RELIGIOUS_FEMALE_KEYS.items():
        founder_key = f"{religion_key} founders"
        jobs_pp[founder_key] = {"males": f"مؤسسو {feminine_label}", "females": f"مؤسسات {feminine_label}"}

    jobs_pp["imprisoned abroad"] = {"males": "مسجونون في الخارج", "females": "مسجونات في الخارج"}
    jobs_pp["imprisoned"] = {"males": "مسجونون", "females": "مسجونات"}
    jobs_pp["escapees"] = {"males": "هاربون", "females": "هاربات"}
    jobs_pp["prison escapees"] = {"males": "هاربون من السجن", "females": "هاربات من السجن"}
    jobs_pp["missionaries"] = {"males": "مبشرون", "females": "مبشرات"}
    jobs_pp["venerated"] = {"males": "مبجلون", "females": "مبجلات"}

    return jobs_pp


def _add_jobs_from_jobs2(jobs_pp: GenderedLabelMap) -> GenderedLabelMap:
    """Merge entries from :mod:`Jobs2` that are missing from ``jobs_pp``."""

    merged = copy_gendered_map(jobs_pp)
    sources = [JOBS_2, JOBS_3333]
    for source in sources:
        for job_key, labels in source.items():
            lowered = job_key.lower()
            if lowered not in merged and (labels["males"] or labels["females"]):
                merged[lowered] = {"males": labels["males"], "females": labels["females"]}

    return merged


def _load_activist_jobs(m_w_jobs: MutableMapping[str, GenderedLabel], nat_before_occ: List[str]) -> None:
    """Extend ``m_w_jobs`` with activist categories from JSON."""

    activists = open_json_file("jobs/activists_keys.json")
    for category, labels in activists.items():
        lowered = category.lower()
        _append_list_unique(nat_before_occ, lowered)
        m_w_jobs[lowered] = {"males": labels["males"], "females": labels["females"]}


def _add_sport_variants(
    base_jobs: Mapping[str, GenderedLabel],
) -> dict[str, GenderedLabel]:
    """
    Derive sport, professional, and wheelchair variants for job labels.

    added 4605 new items (base_jobs: 1535*3)
    """
    data: dict[str, GenderedLabel] = {}
    for base_key, base_labels in base_jobs.items():
        lowered = base_key.lower()
        data[f"sports {lowered}"] = {
            "males": f"{base_labels['males']} رياضيون",
            "females": f"{base_labels['females']} رياضيات",
        }
        data[f"professional {lowered}"] = {
            "males": f"{base_labels['males']} محترفون",
            "females": f"{base_labels['females']} محترفات",
        }
        data[f"wheelchair {lowered}"] = {
            "males": f"{base_labels['males']} على الكراسي المتحركة",
            "females": f"{base_labels['females']} على الكراسي المتحركة",
        }
    return data


def _add_cycling_variants(nat_before_occ: List[str]) -> dict[str, GenderedLabel]:
    """Insert variants derived from cycling events."""
    data: dict[str, GenderedLabel] = {}
    for event_key, event_label in BASE_CYCLING_EVENTS.items():
        lowered = event_key.lower()
        data[f"{lowered} cyclists"] = {"males": f"دراجو {event_label}", "females": f"دراجات {event_label}"}

        winners_key = f"{lowered} winners"
        stage_winners_key = f"{lowered} stage winners"

        data[winners_key] = {"males": f"فائزون في {event_label}", "females": f"فائزات في {event_label}"}
        data[stage_winners_key] = {
            "males": f"فائزون في مراحل {event_label}",
            "females": f"فائزات في مراحل {event_label}",
        }
        _append_list_unique(nat_before_occ, winners_key)
        _append_list_unique(nat_before_occ, stage_winners_key)

    return data


def _add_jobs_people_variants() -> dict[str, GenderedLabel]:
    """Create combinations of people-centric roles with book genres and types."""
    data: dict[str, GenderedLabel] = {}
    for role_key, role_labels in JOBS_PEOPLE_ROLES.items():
        if not (role_labels["males"] and role_labels["females"]):
            continue
        for book_key, book_label in BOOK_CATEGORIES.items():
            data[f"{book_key} {role_key}"] = {
                "males": f"{role_labels['males']} {book_label}",
                "females": f"{role_labels['females']} {book_label}",
            }
        for genre_key, genre_label in JOBS_TYPE_TRANSLATIONS.items():
            data[f"{genre_key} {role_key}"] = {
                "males": f"{role_labels['males']} {genre_label}",
                "females": f"{role_labels['females']} {genre_label}",
            }

    return data


def _add_film_variants() -> dict[str, GenderedLabel]:
    """Create film-related job variants and return the number of generated entries."""
    """
    data: dict[str, GenderedLabel] = {}
    for film_key, film_label in film_keys_for_female.items():
        lowered_film_key = film_key.lower()
        for role_key, role_labels in FILM_ROLE_LABELS.items():
            data[role_key] = {"males": role_labels["males"], "females": role_labels["females"]}
            combo_key = f"{lowered_film_key} {role_key}"
            data[combo_key] = {
                "males": f"{role_labels['males']} {film_label}",
                "females": f"{role_labels['females']} {film_label}",
            }
    """

    data = {
        "film directors": {"males": "مخرجو أفلام", "females": "مخرجات أفلام"},
        "filmmakers": {"males": "صانعو أفلام", "females": "صانعات أفلام"},
        "film producers": {"males": "منتجو أفلام", "females": "منتجات أفلام"},
        "film critics": {"males": "نقاد أفلام", "females": "ناقدات أفلام"},
        "film editors": {"males": "محررو أفلام", "females": "محررات أفلام"},
        "documentary filmmakers": {"males": "صانعو أفلام وثائقية", "females": "صانعات أفلام وثائقية"},
        "documentary film directors": {"males": "مخرجو أفلام وثائقية", "females": "مخرجات أفلام وثائقية"},
        "animated film directors": {"males": "مخرجو أفلام رسوم متحركة", "females": "مخرجات أفلام رسوم متحركة"},
        "experimental filmmakers": {"males": "صانعو أفلام تجريبية", "females": "صانعات أفلام تجريبية"},
        "animated film producers": {"males": "منتجو أفلام رسوم متحركة", "females": "منتجات أفلام رسوم متحركة"},
        "pornographic film directors": {"males": "مخرجو أفلام إباحية", "females": "مخرجات أفلام إباحية"},
        "lgbtq film directors": {"males": "مخرجو أفلام إل جي بي تي كيو", "females": "مخرجات أفلام إل جي بي تي كيو"},
        "comedy film directors": {"males": "مخرجو أفلام كوميدية", "females": "مخرجات أفلام كوميدية"},
        "science fiction film directors": {"males": "مخرجو أفلام خيال علمي", "females": "مخرجات أفلام خيال علمي"},
        "fiction film directors": {"males": "مخرجو أفلام خيالية", "females": "مخرجات أفلام خيالية"},
        "pornographic film producers": {"males": "منتجو أفلام إباحية", "females": "منتجات أفلام إباحية"},
        "documentary film producers": {"males": "منتجو أفلام وثائقية", "females": "منتجات أفلام وثائقية"},
        "horror film directors": {"males": "مخرجو أفلام رعب", "females": "مخرجات أفلام رعب"},
        "film historians": {"males": "مؤرخو أفلام", "females": "مؤرخات أفلام"},
        "silent film directors": {"males": "مخرجو أفلام صامتة", "females": "مخرجات أفلام صامتة"},
        "action film directors": {"males": "مخرجو أفلام حركة", "females": "مخرجات أفلام حركة"},
        "cinema editors": {"males": "محررون سينمائون", "females": "محررات سينمائيات"},
        "silent film producers": {"males": "منتجو أفلام صامتة", "females": "منتجات أفلام صامتة"},
        "propaganda film directors": {"males": "مخرجو أفلام دعائية", "females": "مخرجات أفلام دعائية"},
        "war filmmakers": {"males": "صانعو أفلام حربية", "females": "صانعات أفلام حربية"},
        "fantasy film directors": {"males": "مخرجو أفلام فانتازيا", "females": "مخرجات أفلام فانتازيا"},
        "feminist filmmakers": {"males": "صانعو أفلام نسوية", "females": "صانعات أفلام نسوية"},
        "horror film producers": {"males": "منتجو أفلام رعب", "females": "منتجات أفلام رعب"},
        "japanese horror film directors": {"males": "مخرجو أفلام رعب يابانية", "females": "مخرجات أفلام رعب يابانية"},
        "lgbtq film producers": {"males": "منتجو أفلام إل جي بي تي كيو", "females": "منتجات أفلام إل جي بي تي كيو"},
        "parody film directors": {"males": "مخرجو أفلام ساخرة", "females": "مخرجات أفلام ساخرة"},
    }

    return data


def _add_singer_variants() -> dict[str, GenderedLabel]:
    """Add singer categories and stylistic combinations."""

    data: dict[str, GenderedLabel] = {
        "classical composers": {"males": "ملحنون كلاسيكيون", "females": "ملحنات كلاسيكيات"},
        "classical musicians": {"males": "موسيقيون كلاسيكيون", "females": "موسيقيات كلاسيكيات"},
        "classical pianists": {"males": "عازفو بيانو كلاسيكيون", "females": "عازفات بيانو كلاسيكيات"},
        "classical violinists": {"males": "عازفو كمان كلاسيكيون", "females": "عازفات كمان كلاسيكيات"},
        "classical cellists": {"males": "عازفو تشيلو كلاسيكيون", "females": "عازفات تشيلو كلاسيكيات"},
        "classical guitarists": {"males": "عازفو قيثارة كلاسيكيون", "females": "عازفات قيثارة كلاسيكيات"},
        "historical novelists": {"males": "روائيون تاريخيون", "females": "روائيات تاريخيات"},
        "classical singers": {"males": "مغنون كلاسيكيون", "females": "مغنيات كلاسيكيات"},
        "classical mandolinists": {"males": "عازفو مندولين كلاسيكيون", "females": "عازفات مندولين كلاسيكيات"},
        "classical saxophonists": {"males": "عازفو سكسفون كلاسيكيون", "females": "عازفات سكسفون كلاسيكيات"},
        "classical percussionists": {"males": "فنانون إيقاعيون كلاسيكيون", "females": "فنانات إيقاعيات كلاسيكيات"},
        "classical music critics": {"males": "نقاد موسيقى كلاسيكيون", "females": "ناقدات موسيقى كلاسيكيات"},
        "classical painters": {"males": "رسامون كلاسيكيون", "females": "رسامات كلاسيكيات"},
        "classical writers": {"males": "كتاب كلاسيكيون", "females": "كاتبات كلاسيكيات"},
        "classical choreographers": {"males": "مصممو رقص كلاسيكيون", "females": "مصممات رقص كلاسيكيات"},
        "classical dancers": {"males": "راقصون كلاسيكيون", "females": "راقصات كلاسيكيات"},
    }

    return data


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

    m_w_jobs: GenderedLabelMap = {}
    males_jobs: Dict[str, str] = {}
    females_jobs: Dict[str, str] = {}

    jobs_sources = _merge_jobs_sources()
    jobs_pp = _add_jobs_from_jobs2(jobs_sources)  # 1,369

    # sport_variants = _add_sport_variants(jobs_pp)                 # 4,107
    sport_variants = open_json_file("sport_variants_found.json")  # 35

    # people_variants = _add_jobs_people_variants()                 # 2,096
    people_variants = open_json_file("people_variants_found.json")  # 94

    merge_gendered_maps(m_w_jobs, MEN_WOMENS_JOBS_2)  # 534
    _load_activist_jobs(m_w_jobs, NAT_BEFORE_OCC)  # 95
    cycling_variants = _add_cycling_variants(NAT_BEFORE_OCC)  # 27
    film_variants = _add_film_variants()  # 1,881
    singer_variants = _add_singer_variants()  # 16

    m_w_jobs.update(MEN_WOMENS_SINGERS_BASED)  # 65
    m_w_jobs.update(MEN_WOMENS_SINGERS)  # 7,181 > to > 433
    m_w_jobs.update(jobs_pp)
    m_w_jobs.update(sport_variants)
    m_w_jobs.update(cycling_variants)
    m_w_jobs.update(people_variants)
    m_w_jobs.update(film_variants)
    m_w_jobs.update(singer_variants)

    merge_gendered_maps(m_w_jobs, PLAYERS_TO_MEN_WOMENS_JOBS)  # 1,345
    merge_gendered_maps(m_w_jobs, SPORT_JOB_VARIANTS)  # 61,486

    m_w_jobs["sports coaches"] = {"males": "مدربو رياضة", "females": "مدربات رياضة"}

    for job_key, labels in m_w_jobs.items():
        males_jobs[job_key] = labels["males"]
        if labels["females"]:
            females_jobs[job_key] = labels["females"]

    males_jobs["men's footballers"] = "لاعبو كرة قدم رجالية"

    # males_jobs["sports coaches"] = "مدربو رياضة"
    # females_jobs["sports coaches"] = "مدربات رياضة"

    males_jobs = {key: label for key, label in males_jobs.items() if label}

    len_print.data_len(
        "jobs.py",
        {
            "NAT_BEFORE_OCC_JOBS": NAT_BEFORE_OCC,
            "jobs_pp": jobs_pp,
            "jobs_sources": jobs_sources,
            "sport_variants": sport_variants,
            "cycling_variants": cycling_variants,
            "people_variants": people_variants,
            "film_variants": film_variants,
            "singer_variants": singer_variants,
        },
    )

    return JobsDataset(
        males_jobs=males_jobs,
        females_jobs=females_jobs,
    )


_DATASET = _finalise_jobs_dataset()

jobs_mens_data = _DATASET.males_jobs
jobs_womens_data = _DATASET.females_jobs
Jobs_new = _build_jobs_new(short_womens_jobs)

_len_result = {
    "jobs_mens_data": {"count": 97797, "size": "3.7 MiB"},  # "zoologists": "علماء حيوانات"
    "Jobs_key": {"count": 97784, "size": "3.7 MiB"},  # "zoologists": "علماء حيوانات"
    "Men_Womens_Jobs": {
        "count": 97796,
        "size": "3.7 MiB",
    },  # "zoologists": { "males": "علماء حيوانات", "females": "عالمات حيوانات" }
    "Jobs_new": {"count": 99104, "size": "3.7 MiB"},  # same as Jobs_key +
    "jobs_womens_data": {"count": 75244, "size": "1.8 MiB"},
}

len_print.data_len(
    "jobs.py",
    {
        "companies_to_jobs": companies_to_jobs,
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
