"""Utilities for assembling singer-related gendered job labels.

The original module produced a large dictionary that combined JSON-backed
translations with numerous string concatenation patterns.  The refactor below
documents each data source, adds typing, and centralises the transformation
logic so the behaviour remains stable while being much easier to reason about
and extend.
"""

from __future__ import annotations

from typing import Any, Dict, Mapping

from ..utils.json_dir import open_json_file
from .jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
    gendered_label,
    join_terms,
    load_gendered_label_map,
)

# ---------------------------------------------------------------------------
# JSON sources


JSON_SINGERS_LABELS_FILE = "jobs_Men_Womens_Singers"
"""Filename of the JSON document that stores legacy singer role translations."""

JSON_SINGERS_TAB_FILE = "singers_tab"
"""Filename for supplemental singer category labels pulled from Wikidata."""


# ---------------------------------------------------------------------------
# Helper functions


def _load_string_map(filename: str) -> Dict[str, str]:
    """Load a JSON mapping whose values are plain strings.

    Args:
        filename: Basename of the JSON document stored under ``jsons/``.

    Returns:
        A dictionary containing string to string mappings.  Non-string entries
        are ignored to keep the result deterministic.
    """

    raw_data: Any = open_json_file(filename)
    result: Dict[str, str] = {}
    if isinstance(raw_data, Mapping):
        for raw_key, raw_value in raw_data.items():
            if isinstance(raw_key, str) and isinstance(raw_value, str):
                result[raw_key] = raw_value
    return result


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
            combined[composite_key] = gendered_label(
                join_terms(role_labels["mens"], category_label),
                join_terms(role_labels["womens"], category_label),
            )
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
    for topic_key, topic_labels in topics.items():
        mens_topic = topic_labels["mens"]
        womens_topic = topic_labels["womens"]
        variants[f"{topic_key} historian"] = gendered_label(
            join_terms("مؤرخو", mens_topic),
            join_terms("مؤرخات", womens_topic),
        )
        variants[f"{topic_key} authors"] = gendered_label(
            join_terms("مؤلفو", mens_topic),
            join_terms("مؤلفات", womens_topic),
        )
        variants[f"{topic_key} bloggers"] = gendered_label(
            join_terms("مدونو", mens_topic),
            join_terms("مدونات", womens_topic),
        )
        variants[f"{topic_key} writers"] = gendered_label(
            join_terms("كتاب", mens_topic),
            join_terms("كاتبات", womens_topic),
        )
        variants[f"non-fiction {topic_key} writers"] = gendered_label(
            join_terms("كتاب", mens_topic, "غير روائيون"),
            join_terms("كاتبات", womens_topic, "غير روائيات"),
        )
        variants[f"{topic_key} journalists"] = gendered_label(
            join_terms("صحفيو", mens_topic),
            join_terms("صحفيات", womens_topic),
        )
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
        actors[f"{film_key} actors"] = gendered_label(
            join_terms("ممثلو", film_labels["mens"]),
            "",
        )
    return actors


# ---------------------------------------------------------------------------
# Static configuration


FILMS_TYPE: Mapping[str, GenderedLabel] = {
    "film": gendered_label("أفلام", "أفلام"),
    "silent film": gendered_label("أفلام صامتة", "أفلام صامتة"),
    "pornographic film": gendered_label("أفلام إباحية", "أفلام إباحية"),
    "television": gendered_label("تلفزيون", "تلفزيون"),
    "musical theatre": gendered_label("مسرحيات موسيقية", "مسرحيات موسيقية"),
    "stage": gendered_label("مسرح", "مسرح"),
    "radio": gendered_label("راديو", "راديو"),
    "voice": gendered_label("أداء صوتي", "أداء صوتي"),
    "video game": gendered_label("ألعاب فيديو", "ألعاب فيديو"),
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
}
"""Seed mapping of singer categories to their Arabic descriptions."""


SINGERS_AFTER_ROLES: Mapping[str, GenderedLabel] = {
    "record producers": gendered_label("منتجو تسجيلات", "منتجات تسجيلات"),
    "musicians": gendered_label("موسيقيو", "موسيقيات"),
    "singers": gendered_label("مغنو", "مغنيات"),
    "singer-songwriters": gendered_label("مغنون وكتاب أغاني", "مغنيات وكاتبات أغاني"),
    "songwriters": gendered_label("كتاب أغان", "كاتبات أغان"),
    "critics": gendered_label("نقاد", "ناقدات"),
    "educators": gendered_label("معلمو", "معلمات"),
    "historians": gendered_label("مؤرخو", "مؤرخات"),
    "bloggers": gendered_label("مدونو", "مدونات"),
    "drummers": gendered_label("طبالو", "طبالات"),
    "violinists": gendered_label("عازفو كمان", "عازفات كمان"),
    "trumpeters": gendered_label("عازفو بوق", "عازفات بوق"),
    "bassoonists": gendered_label("عازفو باسون", "عازفات باسون"),
    "trombonists": gendered_label("عازفو ترومبون", "عازفات ترومبون"),
    "composers": gendered_label("ملحنو", "ملحنات"),
    "flautists": gendered_label("عازفو فولت", "عازفات فولت"),
    "writers": gendered_label("كتاب", "كاتبات"),
    "guitarists": gendered_label("عازفو قيثارة", "عازفات قيثارة"),
    "pianists": gendered_label("عازفو بيانو", "عازفات بيانو"),
    "saxophonists": gendered_label("عازفو سكسفون", "عازفات سكسفون"),
    "authors": gendered_label("مؤلفو", "مؤلفات"),
    "journalists": gendered_label("صحفيو", "صحفيات"),
    "bandleaders": gendered_label("قادة فرق", "قائدات فرق"),
    "cheerleaders": gendered_label("قادة تشجيع", "قائدات تشجيع"),
}
"""Roles that can be combined with the singer categories above."""


NON_FICTION_BASE_TOPICS: Mapping[str, GenderedLabel] = {
    "non-fiction": gendered_label("غير روائيون", "غير روائيات"),
    "non-fiction environmental": gendered_label("بيئة غير روائيون", "بيئة غير روائيات"),
    "detective": gendered_label("بوليسيون", "بوليسيات"),
    "military": gendered_label("عسكريون", "عسكريات"),
    "nautical": gendered_label("بحريون", "بحريات"),
    "maritime": gendered_label("بحريون", "بحريات"),
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


SINGERS_TAB: Dict[str, str] = _load_string_map(JSON_SINGERS_TAB_FILE)
"""Supplemental singer categories sourced from JSON configuration."""


SINGER_CATEGORY_LABELS: Dict[str, str] = dict(SINGERS_MAIN_CATEGORIES)
SINGER_CATEGORY_LABELS.update(SINGERS_TAB)
"""Complete mapping of singer categories combining static and JSON sources."""


NON_FICTION_TOPICS: Dict[str, GenderedLabel] = dict(NON_FICTION_BASE_TOPICS)
for topic_key, topic_label in NON_FICTION_ADDITIONAL_TOPICS.items():
    NON_FICTION_TOPICS[topic_key] = gendered_label(topic_label, topic_label)
"""Expanded non-fiction topics covering both static and dynamically generated entries."""


MEN_WOMENS_SINGERS: GenderedLabelMap = {}
MEN_WOMENS_SINGERS.update(load_gendered_label_map(JSON_SINGERS_LABELS_FILE))
MEN_WOMENS_SINGERS.update(_build_category_role_labels(SINGER_CATEGORY_LABELS, SINGERS_AFTER_ROLES))
MEN_WOMENS_SINGERS.update(_build_non_fiction_variants(NON_FICTION_TOPICS))
MEN_WOMENS_SINGERS.update(_build_actor_labels(FILMS_TYPE))
"""All singer-related job labels keyed by their English identifiers."""


# ---------------------------------------------------------------------------
# Backwards compatibility exports


films_type: Mapping[str, GenderedLabel] = FILMS_TYPE
"""Compatibility alias for legacy imports."""


Men_Womens_Singers: GenderedLabelMap = MEN_WOMENS_SINGERS
"""Compatibility alias retaining the mixed-case variable name used previously."""


singers_tab: Dict[str, str] = SINGERS_TAB
"""Compatibility alias for the legacy lowercase singer category mapping."""


__all__ = [
    "FILMS_TYPE",
    "JSON_SINGERS_LABELS_FILE",
    "JSON_SINGERS_TAB_FILE",
    "MEN_WOMENS_SINGERS",
    "NON_FICTION_ADDITIONAL_TOPICS",
    "NON_FICTION_BASE_TOPICS",
    "NON_FICTION_TOPICS",
    "SINGER_CATEGORY_LABELS",
    "SINGERS_AFTER_ROLES",
    "SINGERS_MAIN_CATEGORIES",
    "SINGERS_TAB",
    "films_type",
    "Men_Womens_Singers",
    "singers_tab",
]
