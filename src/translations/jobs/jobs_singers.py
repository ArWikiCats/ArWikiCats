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
            combined[composite_key] = {"mens": f"{role_labels['mens']} {category_label}", "womens": f"{role_labels['womens']} {category_label}"}
        # combined[ f"{category_key} singers" ] = { "mens": f"مغنو {category_label}" ,"womens": f"مغنيات {category_label}" }
        # combined[ f"{category_key} writers" ] = { "mens": f"كتاب {category_label}" ,"womens": f"كاتبات {category_label}" }
        # combined[ f"{category_key} authors" ] = { "mens": f"مؤلفو {category_label}" ,"womens": f"مؤلفات {category_label}" }
        # combined[ f"{category_key} journalists" ] = { "mens": f"صحفيو {category_label}" ,"womens": f"صحفيات {category_label}" }
        # combined[ f"{category_key} bandleaders" ] = { "mens": f"قادة فرق {category_label}" ,"womens": f"قائدات فرق {category_label}" }
        # combined[ f"{category_key} cheerleaders" ] = { "mens": f"قادة تشجيع {category_label}" ,"womens": f"قائدات تشجيع {category_label}" }

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
        "historian": {"mens": "مؤرخو", "womens": "مؤرخات"},
        "authors": {"mens": "مؤلفو", "womens": "مؤلفات"},
        "bloggers": {"mens": "مدونو", "womens": "مدونات"},
        "writers": {"mens": "كتاب", "womens": "كاتبات"},
        "journalists": {"mens": "صحفيو", "womens": "صحفيات"},
    }

    for topic_key, topic_labels in topics.items():
        mens_topic = topic_labels["mens"]
        womens_topic = topic_labels["womens"]

        for role_key, role_labels in roles.items():
            variants[f"{topic_key} {role_key}"] = {
                "mens": f"{role_labels['mens']} {mens_topic}",
                "womens": f"{role_labels['womens']} {womens_topic}",
            }

        variants[f"non-fiction {topic_key} writers"] = {
            "mens": f"كتاب {mens_topic} غير روائيون",
            "womens": f"كاتبات {womens_topic} غير روائيات",
        }
        variants[f"non fiction {topic_key} writers"] = {
            "mens": f"كتاب {mens_topic} غير روائيون",
            "womens": f"كاتبات {womens_topic} غير روائيات",
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
        actors[f"{film_key} actors"] = {"mens": f"ممثلو {film_labels['mens']}", "womens": ""}

    return actors


# ---------------------------------------------------------------------------
# Static configuration


FILMS_TYPE: Mapping[str, GenderedLabel] = {
    "film": {"mens": "أفلام", "womens": "أفلام"},
    "silent film": {"mens": "أفلام صامتة", "womens": "أفلام صامتة"},
    "pornographic film": {"mens": "أفلام إباحية", "womens": "أفلام إباحية"},
    "television": {"mens": "تلفزيون", "womens": "تلفزيون"},
    "musical theatre": {"mens": "مسرحيات موسيقية", "womens": "مسرحيات موسيقية"},
    "stage": {"mens": "مسرح", "womens": "مسرح"},
    "radio": {"mens": "راديو", "womens": "راديو"},
    "voice": {"mens": "أداء صوتي", "womens": "أداء صوتي"},
    "video game": {"mens": "ألعاب فيديو", "womens": "ألعاب فيديو"},
}
"""Media categories used when constructing actor related job labels."""


SINGERS_MAIN_CATEGORIES: Dict[str, str] = {
    "song": "أغاني",
    "albums": "ألبومات",
    "comedy": "كوميديا",
    "music": "موسيقى",
    "country": "كانتري",
    "light": "خفيفة",
    "house": "الهاوس",
    "chamber": "الحجرة",
    "children's songs": "أغاني أطفال",
    "children's": "أطفال",
    "classical": "كلاسيكية",
    "electronic": "إلكترونية",
    "electronica": "إلكترونيكا",
    "abidat rma": "عبيدات الرما",
    "algerian chaabi": "الشعبي",
    "algerian hip hop": "هيب هوب جزائري",
    "andalusian classical music": "طرب أندلسي",
    "bakersfield sound": "موسيقى بيكرسفيلد",
    "bluegrass music": "بلوغراس",
    "canzone napoletana": "أغنية نابولية",
    "chaoui music": "شاوي",
    "country music": "كانتري",
    "electro": "موسيقى كهربائية",
    "electroacoustic music": "إليكتروكوستيك",
    "french hip hop": "هيب هوب فرنسي",
    "gharnati music": "طرب غرناطي",
    "glitch": "موسيقى الخلل",
    "gospel music": "غوسبل",
    "gregorian chant": "الغناء الجريجوري",
    "heavy metal": "موسيقى الميتال",
    "hip hop music": "هيب هوب",
    "house music": "هاوس",
    "khaliji": "موسيقى خليجية",
    "musique concrète": "موسيقى ملموسة",
    "música popular brasileira": "موسيقى شعبية برازيلية",
    "new wave of british heavy metal": "الموجة الجديدة لموسيقى الهيفي ميتال البريطانية",
    "parody music": "موسيقي كوميدية",
    "patriotic song": "أغنية وطنية",
    "peruvian waltz": "الفالس البيروفي",
    "progressive house": "موسيقى هاوس تقدمية",
    "romance": "موسيقى رومانسية",
    "sawt": "فن الصوت",
    "swing music": "سوينغ",
    "technical death metal": "ديث ميتال الفني",
    "trap music": "تراب",
}

"""Seed mapping of singer categories to their Arabic descriptions."""


SINGERS_AFTER_ROLES: Mapping[str, GenderedLabel] = {
    "record producers": {"mens": "منتجو تسجيلات", "womens": "منتجات تسجيلات"},
    "musicians": {"mens": "موسيقيو", "womens": "موسيقيات"},
    "singers": {"mens": "مغنو", "womens": "مغنيات"},
    "singer-songwriters": {"mens": "مغنون وكتاب أغاني", "womens": "مغنيات وكاتبات أغاني"},
    "songwriters": {"mens": "كتاب أغان", "womens": "كاتبات أغان"},
    "critics": {"mens": "نقاد", "womens": "ناقدات"},
    "educators": {"mens": "معلمو", "womens": "معلمات"},
    "historians": {"mens": "مؤرخو", "womens": "مؤرخات"},
    "bloggers": {"mens": "مدونو", "womens": "مدونات"},
    "drummers": {"mens": "طبالو", "womens": "طبالات"},
    "violinists": {"mens": "عازفو كمان", "womens": "عازفات كمان"},
    "trumpeters": {"mens": "عازفو بوق", "womens": "عازفات بوق"},
    "bassoonists": {"mens": "عازفو باسون", "womens": "عازفات باسون"},
    "trombonists": {"mens": "عازفو ترومبون", "womens": "عازفات ترومبون"},
    "composers": {"mens": "ملحنو", "womens": "ملحنات"},
    "flautists": {"mens": "عازفو فولت", "womens": "عازفات فولت"},
    "writers": {"mens": "كتاب", "womens": "كاتبات"},
    "guitarists": {"mens": "عازفو قيثارة", "womens": "عازفات قيثارة"},
    "pianists": {"mens": "عازفو بيانو", "womens": "عازفات بيانو"},
    "saxophonists": {"mens": "عازفو سكسفون", "womens": "عازفات سكسفون"},
    "authors": {"mens": "مؤلفو", "womens": "مؤلفات"},
    "journalists": {"mens": "صحفيو", "womens": "صحفيات"},
    "bandleaders": {"mens": "قادة فرق", "womens": "قائدات فرق"},
    "cheerleaders": {"mens": "قادة تشجيع", "womens": "قائدات تشجيع"},
}

"""Roles that can be combined with the singer categories above."""

NON_FICTION_BASE_TOPICS: Mapping[str, GenderedLabel] = {
    "non-fiction": {"mens": "غير روائيون", "womens": "غير روائيات"},
    "non-fiction environmental": {
        "mens": "بيئة غير روائيون",
        "womens": "بيئة غير روائيات",
    },
    "detective": {"mens": "بوليسيون", "womens": "بوليسيات"},
    "military": {"mens": "عسكريون", "womens": "عسكريات"},
    "nautical": {"mens": "بحريون", "womens": "بحريات"},
    "maritime": {"mens": "بحريون", "womens": "بحريات"},
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

SINGER_CATEGORY_LABELS: Dict[str, str] = dict(SINGERS_MAIN_CATEGORIES)
SINGER_CATEGORY_LABELS.update(SINGERS_TAB)
"""Complete mapping of singer categories combining static and JSON sources."""

NON_FICTION_TOPICS: Dict[str, GenderedLabel] = dict(NON_FICTION_BASE_TOPICS)

for topic_key, topic_label in NON_FICTION_ADDITIONAL_TOPICS.items():
    NON_FICTION_TOPICS[topic_key] = {"mens": topic_label, "womens": topic_label}

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
        "SINGERS_MAIN_CATEGORIES": SINGERS_MAIN_CATEGORIES,
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
    "SINGERS_MAIN_CATEGORIES",
    "MEN_WOMENS_SINGERS",
    "SINGERS_TAB",
]
