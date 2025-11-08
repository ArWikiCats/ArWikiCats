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
# ---
universities_tables = {
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
for major, maj_ar in MAJORS.items():
    major = major.lower()
    universities_tables[f"university of {major}"] = "جامعة {} %s" % maj_ar
    universities_tables[f"university-of-{major}"] = "جامعة {} %s" % maj_ar

    universities_tables[f"university of the {major}"] = "جامعة {} %s" % maj_ar
    universities_tables[f"university-of-the-{major}"] = "جامعة {} %s" % maj_ar

test_universities_cash = {}


def test_universities(cate: str) -> str:
    cate = cate.lower()
    # ---
    if cate.startswith("category:"):
        cate = cate[len("category:") :].strip()
    # ---
    if cate.lower().strip() in test_universities_cash:
        return test_universities_cash[cate.lower().strip()]
    # ---
    print_put(f"<<lightblue>>>> vvvvvvvvvvvv test_universities start, (cate:{cate}) vvvvvvvvvvvv ")
    # ---
    city_key = ""
    university_template = ""
    # ---
    for xi, xi_lab in universities_tables.items():
        xi2 = f"the {xi}"
        if cate.endswith(xi):
            university_template = xi_lab
            city_key = cate[: -len(xi)].strip()
            break
        elif cate.endswith(xi2):
            university_template = xi_lab
            city_key = cate[: -len(xi2)].strip()
            break
    # ---
    if not city_key:
        for xi, xi_lab in universities_tables.items():
            xi3 = f"{xi}, "
            the_xi = f"the {xi}"
            if cate.startswith(xi3):
                university_template = xi_lab
                city_key = cate[len(xi3) :].strip()
                break
            elif cate.startswith(xi):
                university_template = xi_lab
                city_key = cate[len(xi) :].strip()
                break
            elif cate.startswith(the_xi):
                university_template = xi_lab
                city_key = cate[len(the_xi) :].strip()
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
    test_universities_cash[cate.lower().strip()] = univer_lab
    # ---
    return univer_lab
