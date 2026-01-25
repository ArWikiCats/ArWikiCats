"""
Build comprehensive gendered job label dictionaries.
"""

from __future__ import annotations

from typing import Mapping

from ..data_builders.build_jobs import (
    _build_jobs_new,
    _finalise_jobs_dataset,
)
from ..data_builders.jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
)
from ..helps import len_print
from ..mixed import BOOK_CATEGORIES, RELIGIOUS_FEMALE_KEYS
from ..nats import Nat_mens
from ..sports import BASE_CYCLING_EVENTS
from ..utils import open_json_file
from .Jobs2 import JOBS_2, JOBS_3333
from .jobs_data_basic import MEN_WOMENS_JOBS_2, NAT_BEFORE_OCC, RELIGIOUS_KEYS_PP
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


jobs_pp = open_json_file("jobs/jobs_Men_Womens_PP.json")
# sport_variants = _add_sport_variants(jobs_pp)                 # 4,107
sport_variants = open_json_file("sport_variants_found.json")  # 35

# people_variants = _add_jobs_people_variants(JOBS_PEOPLE_ROLES, BOOK_CATEGORIES, JOBS_TYPE_TRANSLATIONS)                 # 2,096
people_variants = open_json_file("people_variants_found.json")  # 94

activists = open_json_file("jobs/activists_keys.json")
_DATASET = _finalise_jobs_dataset(
    jobs_pp,
    sport_variants,
    people_variants,
    MEN_WOMENS_JOBS_2,
    NAT_BEFORE_OCC,
    MEN_WOMENS_SINGERS_BASED,
    MEN_WOMENS_SINGERS,
    PLAYERS_TO_MEN_WOMENS_JOBS,
    SPORT_JOB_VARIANTS,
    RELIGIOUS_FEMALE_KEYS,
    BASE_CYCLING_EVENTS,
    JOBS_2,
    JOBS_3333,
    RELIGIOUS_KEYS_PP,
    FOOTBALL_KEYS_PLAYERS,
    EXECUTIVE_DOMAINS,
    DISABILITY_LABELS,
    JOBS_2020_BASE,
    companies_to_jobs,
    activists,
)

jobs_mens_data = _DATASET.males_jobs
jobs_womens_data = _DATASET.females_jobs
Jobs_new = _build_jobs_new(short_womens_jobs, Nat_mens)

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
