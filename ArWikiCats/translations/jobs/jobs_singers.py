#!/usr/bin/python3
"""
Utilities for assembling singer-related gendered job labels.
"""

from __future__ import annotations

import sys
from typing import Dict, Mapping

from ..data_builders.jobs_defs import GenderedLabel, GenderedLabelMap
from ..helps import len_print
from ..utils import open_json_file

# ---------------------------------------------------------------------------
# Helper functions


# ---------------------------------------------------------------------------
# Static configuration


FILMS_TYPE: Mapping[str, GenderedLabel] = {
    "film": {"males": "أفلام", "females": "أفلام"},
    "silent film": {"males": "أفلام صامتة", "females": "أفلام صامتة"},
    "pornographic film": {"males": "أفلام إباحية", "females": "أفلام إباحية"},
    "television": {"males": "تلفزيون", "females": "تلفزيون"},
    "musical theatre": {"males": "مسرحيات موسيقية", "females": "مسرحيات موسيقية"},
    "stage": {"males": "مسرح", "females": "مسرح"},
    "radio": {"males": "راديو", "females": "راديو"},
    "voice": {"males": "أداء صوتي", "females": "أداء صوتي"},
    "video game": {"males": "ألعاب فيديو", "females": "ألعاب فيديو"},
}

"""Seed mapping of singer categories to their Arabic descriptions."""


SINGERS_AFTER_ROLES: Mapping[str, GenderedLabel] = {
    "musicians": {"males": "موسيقيو", "females": "موسيقيات"},
    "singers": {"males": "مغنو", "females": "مغنيات"},
    "educators": {"males": "معلمو", "females": "معلمات"},
    "historians": {"males": "مؤرخو", "females": "مؤرخات"},
    "bloggers": {"males": "مدونو", "females": "مدونات"},
    "drummers": {"males": "طبالو", "females": "طبالات"},
    "authors": {"males": "مؤلفو", "females": "مؤلفات"},
    "journalists": {"males": "صحفيو", "females": "صحفيات"},
    "composers": {"males": "ملحنو", "females": "ملحنات"},
    "record producers": {"males": "منتجو تسجيلات", "females": "منتجات تسجيلات"},
    "singer-songwriters": {"males": "مغنون وكتاب أغاني", "females": "مغنيات وكاتبات أغاني"},
    "songwriters": {"males": "كتاب أغان", "females": "كاتبات أغان"},
    "critics": {"males": "نقاد", "females": "ناقدات"},
    "violinists": {"males": "عازفو كمان", "females": "عازفات كمان"},
    "trumpeters": {"males": "عازفو بوق", "females": "عازفات بوق"},
    "bassoonists": {"males": "عازفو باسون", "females": "عازفات باسون"},
    "trombonists": {"males": "عازفو ترومبون", "females": "عازفات ترومبون"},
    "flautists": {"males": "عازفو فولت", "females": "عازفات فولت"},
    "writers": {"males": "كتاب", "females": "كاتبات"},
    "guitarists": {"males": "عازفو قيثارة", "females": "عازفات قيثارة"},
    "pianists": {"males": "عازفو بيانو", "females": "عازفات بيانو"},
    "saxophonists": {"males": "عازفو سكسفون", "females": "عازفات سكسفون"},
    "bandleaders": {"males": "قادة فرق", "females": "قائدات فرق"},
    "cheerleaders": {"males": "قادة تشجيع", "females": "قائدات تشجيع"},
}

"""Roles that can be combined with the singer categories above."""

NON_FICTION_BASE_TOPICS: Mapping[str, GenderedLabel] = {
    "non-fiction": {"males": "غير روائيين", "females": "غير روائيات"},
    "non-fiction environmental": {
        "males": "بيئة غير روائيين",
        "females": "بيئة غير روائيات",
    },
    "detective": {"males": "بوليسيون", "females": "بوليسيات"},
    "military": {"males": "عسكريون", "females": "عسكريات"},
    "nautical": {"males": "بحريون", "females": "بحريات"},
    "maritime": {"males": "بحريون", "females": "بحريات"},
}

"""Seed topics that receive dedicated non-fiction role variants."""


NON_FICTION_ADDITIONAL_TOPICS: Mapping[str, str] = {
    "environmental": "بيئة",
    "economics": "إقتصاد",
    "hymn": "ترانيم",
    "architecture": "عمارة",
    "magazine": "مجلات",
    "medical": "طب",
    "organized crime": "جريمة منظمة",
    "crime": "جريمة",
    "legal": "قانون",
    "business": "أعمال تجارية",
    "nature": "طبيعة",
    "political": "سياسة",
    "art": "فن",
    "food": "طعام",
    "travel": "سفر",
    "spiritual": "روحانية",
    "arts": "فنون",
    "social sciences": "علوم اجتماعية",
    "music": "موسيقى",
    "science": "علم",
    "technology": "تقانة",
    "comedy": "كوميدي",
}

"""Topics duplicated for both masculine and feminine forms when generating variants."""


# ---------------------------------------------------------------------------
# Aggregate data assembly

SINGERS_TAB: Dict[str, str] = open_json_file("jobs/singers_tab.json") or {}

SINGER_CATEGORY_LABELS: Dict[str, str] = SINGERS_TAB
"""Complete mapping of singer categories combining static and JSON sources."""

NON_FICTION_TOPICS: Dict[str, GenderedLabel] = dict(NON_FICTION_BASE_TOPICS)

for topic_key, topic_label in NON_FICTION_ADDITIONAL_TOPICS.items():
    NON_FICTION_TOPICS[topic_key] = {"males": topic_label, "females": topic_label}

"""Expanded non-fiction topics covering both static and dynamically generated entries."""

MEN_WOMENS_SINGERS_BASED: GenderedLabelMap = open_json_file("jobs/jobs_Men_Womens_Singers.json") or {}

MEN_WOMENS_SINGERS = open_json_file("MEN_WOMENS_SINGERS_found.json")

len_print.data_len(
    "jobs_singers.py",
    {
        "MEN_WOMENS_SINGERS_BASED": MEN_WOMENS_SINGERS_BASED,
        "FILMS_TYPE": FILMS_TYPE,
        "NON_FICTION_BASE_TOPICS": NON_FICTION_BASE_TOPICS,
        "NON_FICTION_TOPICS": NON_FICTION_TOPICS,
        "SINGER_CATEGORY_LABELS": SINGER_CATEGORY_LABELS,
        "SINGERS_AFTER_ROLES": SINGERS_AFTER_ROLES,
        "MEN_WOMENS_SINGERS": MEN_WOMENS_SINGERS,
        "SINGERS_TAB": SINGERS_TAB,
    },
)

__all__ = [
    "MEN_WOMENS_SINGERS_BASED",
    "FILMS_TYPE",
    "MEN_WOMENS_SINGERS",
    "SINGERS_TAB",
]
