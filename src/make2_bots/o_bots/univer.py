"""University labelling helpers."""

from __future__ import annotations

from typing import Dict

from ...helps.print_bot import print_put
from ...ma_lists import N_cit_ies_s_lower
from .utils import get_or_set

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

for major, arabic_label in MAJORS.items():
    normalized_major = major.lower()
    template = f"جامعة {{}} {arabic_label}"
    UNIVERSITIES_TABLES[f"university of {normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university-of-{normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university of the {normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university-of-the-{normalized_major}"] = template

UNIVERSITIES_CACHE: Dict[str, str] = {}


def _normalise_category(category: str) -> str:
    """Lowercase and strip ``category`` while removing ``Category:`` prefix."""

    normalized = category.lower().strip()
    if normalized.startswith("category:"):
        normalized = normalized[len("category:") :].strip()
    return normalized


def test_universities(category: str) -> str:
    """Return the Arabic label for university-related categories.

    Args:
        category: Category representing a university or faculty.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """

    normalized_category = _normalise_category(category)

    if normalized_category in UNIVERSITIES_CACHE:
        return UNIVERSITIES_CACHE[normalized_category]

    def _resolve() -> str:
        print_put(f"<<lightblue>>>> vvvvvvvvvvvv test_universities start, (category:{normalized_category}) vvvvvvvvvvvv ")

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

        city_label = N_cit_ies_s_lower.get(city_key, "") if city_key else ""
        if city_label and university_template:
            university_label = university_template.format(city_label)
            print_put(f'<<lightblue>>>>>> test_universities: new univer_lab  "{university_label}" ')
            print_put("<<lightblue>>>> ^^^^^^^^^ test_universities end ^^^^^^^^^ ")
            return university_label

        print_put("<<lightblue>>>> ^^^^^^^^^ test_universities end ^^^^^^^^^ ")
        return ""

    return get_or_set(UNIVERSITIES_CACHE, normalized_category, _resolve)


# Backwards compatibility ----------------------------------------------------------------------
test_Universities = test_universities

__all__ = ["test_universities", "test_Universities"]
