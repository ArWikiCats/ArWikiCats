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
    # ---
    print_put(f"<<lightblue>>>> vvvvvvvvvvvv test_universities start, (category:{category}) vvvvvvvvvvvv ")
    # ---
    city_key = ""
    university_template = ""
    # ---
    for xi, xi_lab in UNIVERSITIES_TABLES.items():
        xi2 = f"the {xi}"
        if category.endswith(xi):
            university_template = xi_lab
            city_key = category[: -len(xi)].strip()
            break
        elif category.endswith(xi2):
            university_template = xi_lab
            city_key = category[: -len(xi2)].strip()
            break
    # ---
    if not city_key:
        for xi, xi_lab in UNIVERSITIES_TABLES.items():
            xi3 = f"{xi}, "
            the_xi = f"the {xi}"
            if category.startswith(xi3):
                university_template = xi_lab
                city_key = category[len(xi3) :].strip()
                break
            elif category.startswith(xi):
                university_template = xi_lab
                city_key = category[len(xi) :].strip()
                break
            elif category.startswith(the_xi):
                university_template = xi_lab
                city_key = category[len(the_xi) :].strip()
                break
    # ---
    city_label = ""
    if city_key:
        # ---
        city_label = N_cit_ies_s_lower.get(city_key, "")
        # ---
        print_put(
            f"<<lightblue>>>> test_universities cite:{city_key}, majorlab:{university_template}, citelab:{city_label}"
        )
    # ---
    univer_lab = ""
    # ---
    if city_label:
        univer_lab = university_template.format(city_label)
        print_put(f'<<lightblue>>>>>> test_universities: new univer_lab  "{univer_lab}" ')
    # ---
    print_put("<<lightblue>>>> ^^^^^^^^^ test_universities end ^^^^^^^^^ ")
    # ---
    UNIVERSITIES_CACHE[normalized_category] = univer_lab
    # ---
    return univer_lab


__all__ = [
    "test_universities"
]
