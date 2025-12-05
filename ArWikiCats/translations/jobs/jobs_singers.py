#!/usr/bin/python3
"""
Utilities for assembling singer-related gendered job labels.
"""

from __future__ import annotations

import sys
from typing import Dict, Mapping

from ...helps import len_print
from ..utils.json_dir import open_json
from .jobs_defs import GenderedLabel, GenderedLabelMap

# ---------------------------------------------------------------------------
# Helper functions


def _build_category_role_labels(
    categories: Mapping[str, str],
    roles: Mapping[str, GenderedLabel],
) -> GenderedLabelMap:
    """Combine singer categories with job role templates.

    Args:
        categories: Mapping of English category identifiers to Arabic
            descriptors (e.g. ``"song" -> "أغاني"``).
        roles: Mapping of role names to gendered Arabic labels.

    Returns:
        A dictionary containing entries like ``"song singers"`` with fully
        assembled masculine and feminine Arabic labels.
    """

    combined: GenderedLabelMap = {}

    for category_key, category_label in categories.items():
        for role_key, role_labels in roles.items():
            composite_key = f"{category_key} {role_key}"
            combined[composite_key] = {
                "mens": f"{role_labels['mens']} {category_label}",
                "females": f"{role_labels['females']} {category_label}",
            }
        # combined[ f"{category_key} singers" ] = { "mens": f"مغنو {category_label}" ,"females": f"مغنيات {category_label}" }
        # combined[ f"{category_key} writers" ] = { "mens": f"كتاب {category_label}" ,"females": f"كاتبات {category_label}" }
        # combined[ f"{category_key} authors" ] = { "mens": f"مؤلفو {category_label}" ,"females": f"مؤلفات {category_label}" }
        # combined[ f"{category_key} journalists" ] = { "mens": f"صحفيو {category_label}" ,"females": f"صحفيات {category_label}" }
        # combined[ f"{category_key} bandleaders" ] = { "mens": f"قادة فرق {category_label}" ,"females": f"قائدات فرق {category_label}" }
        # combined[ f"{category_key} cheerleaders" ] = { "mens": f"قادة تشجيع {category_label}" ,"females": f"قائدات تشجيع {category_label}" }

    return combined


def _build_non_fiction_variants(
    topics: Mapping[str, GenderedLabel],
) -> GenderedLabelMap:
    """Create job labels for non-fiction authors and historians.

    Args:
        topics: Mapping whose values describe the subject area.

    Returns:
        Gendered role labels covering historians, authors, bloggers, writers,
        journalists, and specialised "non-fiction" writers for every topic.
    """

    variants: GenderedLabelMap = {}

    roles = {
        "historian": {"mens": "مؤرخو", "females": "مؤرخات"},
        "authors": {"mens": "مؤلفو", "females": "مؤلفات"},
        "bloggers": {"mens": "مدونو", "females": "مدونات"},
        "writers": {"mens": "كتاب", "females": "كاتبات"},
        "journalists": {"mens": "صحفيو", "females": "صحفيات"},
    }

    for topic_key, topic_labels in topics.items():
        mens_topic = topic_labels["mens"]
        womens_topic = topic_labels["females"]

        for role_key, role_labels in roles.items():
            variants[f"{topic_key} {role_key}"] = {
                "mens": f"{role_labels['mens']} {mens_topic}",
                "females": f"{role_labels['females']} {womens_topic}",
            }

        variants[f"non-fiction {topic_key} writers"] = {
            "mens": f"كتاب {mens_topic} غير روائيون",
            "females": f"كاتبات {womens_topic} غير روائيات",
        }
        variants[f"non fiction {topic_key} writers"] = {
            "mens": f"كتاب {mens_topic} غير روائيون",
            "females": f"كاتبات {womens_topic} غير روائيات",
        }
    return variants


def _build_actor_labels(film_types: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Create actor job labels for every film medium.

    Args:
        film_types: Mapping of medium names to their Arabic descriptors.

    Returns:
        A mapping with keys like ``"film actors"``.  The feminine forms remain
        empty to preserve the behaviour from the legacy dataset, which relied on
        downstream fallbacks when feminine labels were missing.
    """

    actors: GenderedLabelMap = {}

    for film_key, film_labels in film_types.items():
        actors[f"{film_key} actors"] = {"mens": f"ممثلو {film_labels['mens']}", "females": ""}

    return actors


# ---------------------------------------------------------------------------
# Static configuration


FILMS_TYPE: Mapping[str, GenderedLabel] = {
    "film": {"mens": "أفلام", "females": "أفلام"},
    "silent film": {"mens": "أفلام صامتة", "females": "أفلام صامتة"},
    "pornographic film": {"mens": "أفلام إباحية", "females": "أفلام إباحية"},
    "television": {"mens": "تلفزيون", "females": "تلفزيون"},
    "musical theatre": {"mens": "مسرحيات موسيقية", "females": "مسرحيات موسيقية"},
    "stage": {"mens": "مسرح", "females": "مسرح"},
    "radio": {"mens": "راديو", "females": "راديو"},
    "voice": {"mens": "أداء صوتي", "females": "أداء صوتي"},
    "video game": {"mens": "ألعاب فيديو", "females": "ألعاب فيديو"},
}

"""Seed mapping of singer categories to their Arabic descriptions."""


SINGERS_AFTER_ROLES: Mapping[str, GenderedLabel] = {
    "record producers": {"mens": "منتجو تسجيلات", "females": "منتجات تسجيلات"},
    "musicians": {"mens": "موسيقيو", "females": "موسيقيات"},
    "singers": {"mens": "مغنو", "females": "مغنيات"},
    "singer-songwriters": {"mens": "مغنون وكتاب أغاني", "females": "مغنيات وكاتبات أغاني"},
    "songwriters": {"mens": "كتاب أغان", "females": "كاتبات أغان"},
    "critics": {"mens": "نقاد", "females": "ناقدات"},
    "educators": {"mens": "معلمو", "females": "معلمات"},
    "historians": {"mens": "مؤرخو", "females": "مؤرخات"},
    "bloggers": {"mens": "مدونو", "females": "مدونات"},
    "drummers": {"mens": "طبالو", "females": "طبالات"},
    "violinists": {"mens": "عازفو كمان", "females": "عازفات كمان"},
    "trumpeters": {"mens": "عازفو بوق", "females": "عازفات بوق"},
    "bassoonists": {"mens": "عازفو باسون", "females": "عازفات باسون"},
    "trombonists": {"mens": "عازفو ترومبون", "females": "عازفات ترومبون"},
    "composers": {"mens": "ملحنو", "females": "ملحنات"},
    "flautists": {"mens": "عازفو فولت", "females": "عازفات فولت"},
    "writers": {"mens": "كتاب", "females": "كاتبات"},
    "guitarists": {"mens": "عازفو قيثارة", "females": "عازفات قيثارة"},
    "pianists": {"mens": "عازفو بيانو", "females": "عازفات بيانو"},
    "saxophonists": {"mens": "عازفو سكسفون", "females": "عازفات سكسفون"},
    "authors": {"mens": "مؤلفو", "females": "مؤلفات"},
    "journalists": {"mens": "صحفيو", "females": "صحفيات"},
    "bandleaders": {"mens": "قادة فرق", "females": "قائدات فرق"},
    "cheerleaders": {"mens": "قادة تشجيع", "females": "قائدات تشجيع"},
}

"""Roles that can be combined with the singer categories above."""

NON_FICTION_BASE_TOPICS: Mapping[str, GenderedLabel] = {
    "non-fiction": {"mens": "غير روائيون", "females": "غير روائيات"},
    "non-fiction environmental": {
        "mens": "بيئة غير روائيون",
        "females": "بيئة غير روائيات",
    },
    "detective": {"mens": "بوليسيون", "females": "بوليسيات"},
    "military": {"mens": "عسكريون", "females": "عسكريات"},
    "nautical": {"mens": "بحريون", "females": "بحريات"},
    "maritime": {"mens": "بحريون", "females": "بحريات"},
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
    "technology": "تقنية",
    "comedy": "كوميدي",
}

"""Topics duplicated for both masculine and feminine forms when generating variants."""


# ---------------------------------------------------------------------------
# Aggregate data assembly

SINGERS_TAB: Dict[str, str] = open_json("jobs/singers_tab.json") or {}

SINGER_CATEGORY_LABELS: Dict[str, str] = SINGERS_TAB
"""Complete mapping of singer categories combining static and JSON sources."""

NON_FICTION_TOPICS: Dict[str, GenderedLabel] = dict(NON_FICTION_BASE_TOPICS)

for topic_key, topic_label in NON_FICTION_ADDITIONAL_TOPICS.items():
    NON_FICTION_TOPICS[topic_key] = {"mens": topic_label, "females": topic_label}

"""Expanded non-fiction topics covering both static and dynamically generated entries."""

MEN_WOMENS_SINGERS: GenderedLabelMap = open_json("jobs/jobs_Men_Womens_Singers.json") or {}

MEN_WOMENS_SINGERS.update(_build_category_role_labels(SINGER_CATEGORY_LABELS, SINGERS_AFTER_ROLES))

MEN_WOMENS_SINGERS.update(_build_non_fiction_variants(NON_FICTION_TOPICS))

MEN_WOMENS_SINGERS.update(_build_actor_labels(FILMS_TYPE))

len_print.data_len(
    "jobs_singers.py",
    {
        "FILMS_TYPE": FILMS_TYPE,
        "NON_FICTION_ADDITIONAL_TOPICS": NON_FICTION_ADDITIONAL_TOPICS,
        "NON_FICTION_BASE_TOPICS": NON_FICTION_BASE_TOPICS,
        "NON_FICTION_TOPICS": NON_FICTION_TOPICS,
        "SINGER_CATEGORY_LABELS": SINGER_CATEGORY_LABELS,
        "SINGERS_AFTER_ROLES": SINGERS_AFTER_ROLES,
        "MEN_WOMENS_SINGERS": MEN_WOMENS_SINGERS,
        "SINGERS_TAB": SINGERS_TAB,
    },
)

__all__ = [
    "FILMS_TYPE",
    "NON_FICTION_ADDITIONAL_TOPICS",
    "NON_FICTION_BASE_TOPICS",
    "NON_FICTION_TOPICS",
    "SINGER_CATEGORY_LABELS",
    "SINGERS_AFTER_ROLES",
    "MEN_WOMENS_SINGERS",
    "SINGERS_TAB",
]
