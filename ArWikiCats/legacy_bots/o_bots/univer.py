"""University labelling helpers."""

from __future__ import annotations

import functools
from typing import Dict

from ...helps import logger
from ...translations import CITY_TRANSLATIONS_LOWER

MAJORS: Dict[str, str] = {
    "medical sciences": "للعلوم الطبية",
    "international university": "الدولية",
    "art": "للفنون",
    "arts": "للفنون",
    "biology": "للبيولوجيا",
    "chemistry": "للشيمية",
    "computer science": "للكمبيوتر",
    "economics": "للاقتصاد",
    "education": "للتعليم",
    "engineering": "للهندسة",
    "geography": "للجغرافيا",
    "geology": "للجيولوجيا",
    "history": "للتاريخ",
    "law": "للقانون",
    "mathematics": "للرياضيات",
    "technology": "للتكنولوجيا",
    "physics": "للفيزياء",
    "psychology": "للصحة",
    "sociology": "للأمن والسلوك",
    "political science": "للسياسة",
    "social science": "للأمن والسلوك",
    "social sciences": "للأمن والسلوك",
    "science and technology": "للعلوم والتكنولوجيا",
    "science": "للعلوم",
    "reading": "للقراءة",
    "applied sciences": "للعلوم التطبيقية",
}

UNIVERSITIES_TABLES: Dict[str, str] = {
    "national maritime university": "جامعة {} الوطنية البحرية",
    "national university": "جامعة {} الوطنية",
}
# ---
"""
"university of nebraska medical center":"جامعة نبراسكا كلية الطب",
"university of new mexico school of law":"كلية الحقوق في جامعة نيو مكسيكو",
"university of applied sciences, mainz":"جامعة ماينز للعلوم التطبيقية",

"china university of petroleum":"جامعة الصين للبترول",
"odesa national maritime university":"جامعة أوديسا الوطنية البحرية",
"""
for major, arabic_label in MAJORS.items():
    normalized_major = major.lower()
    template = f"جامعة {{}} {arabic_label}"
    UNIVERSITIES_TABLES[f"university of {normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university-of-{normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university of the {normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university-of-the-{normalized_major}"] = template


def _normalise_category(category: str) -> str:
    """Lowercase and strip ``category`` while removing ``Category:`` prefix."""

    normalized = category.lower().strip()
    if normalized.startswith("category:"):
        normalized = normalized[len("category:") :].strip()
    return normalized


def _resolve(normalized_category: str) -> str:
    """Resolve a university-related category to its Arabic label."""
    logger.info(f"<<lightblue>>>> vvvvvvvvvvvv te_universities start, (category:{normalized_category}) vvvvvvvvvvvv ")

    city_key = ""
    university_template = ""

    # Attempt to match based on the suffix first.
    for key, template in UNIVERSITIES_TABLES.items():
        prefixed_key = f"the {key}"
        if normalized_category.endswith(key):
            university_template = template
            city_key = normalized_category[: -len(key)].strip()
            break
        if normalized_category.endswith(prefixed_key):
            university_template = template
            city_key = normalized_category[: -len(prefixed_key)].strip()
            break

    # Fallback to prefix matching when suffixes fail.
    if not city_key:
        for key, template in UNIVERSITIES_TABLES.items():
            prefixed_key = f"the {key}"
            key_with_comma = f"{key}, "
            if normalized_category.startswith(key_with_comma):
                university_template = template
                city_key = normalized_category[len(key_with_comma) :].strip()
                break
            if normalized_category.startswith(key):
                university_template = template
                city_key = normalized_category[len(key) :].strip()
                break
            if normalized_category.startswith(prefixed_key):
                university_template = template
                city_key = normalized_category[len(prefixed_key) :].strip()
                break

    city_label = CITY_TRANSLATIONS_LOWER.get(city_key, "") if city_key else ""
    if city_label and university_template:
        university_label = university_template.format(city_label)
        logger.info(f"<<lightblue>>>>>> te_universities: new {university_label=} ")
        logger.info("<<lightblue>>>> ^^^^^^^^^ te_universities end ^^^^^^^^^ ")
        return university_label

    logger.info("<<lightblue>>>> ^^^^^^^^^ te_universities end ^^^^^^^^^ ")
    return ""


@functools.lru_cache(maxsize=None)
def te_universities(category: str) -> str:
    """Return the Arabic label for university-related categories.

    Args:
        category: Category representing a university or faculty.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """

    normalized_category = _normalise_category(category)

    return _resolve(normalized_category)


__all__ = ["te_universities"]
