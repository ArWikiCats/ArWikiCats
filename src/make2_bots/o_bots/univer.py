#!/usr/bin/python3
"""
python3 core8/pwb.py make/m test Category:People executed by the International Military Tribunal in Nuremberg

from  make.bots import univer # univer.universities_tables | univer.test_Universities(cate)
"""

from ...ma_lists import N_cit_ies_s_lower
from ...helps.print_bot import print_put

# ---
majors = {
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
for major, maj_ar in majors.items():
    major = major.lower()
    universities_tables[f"university of {major}"] = "جامعة {} %s" % maj_ar
    universities_tables[f"university-of-{major}"] = "جامعة {} %s" % maj_ar

    universities_tables[f"university of the {major}"] = "جامعة {} %s" % maj_ar
    universities_tables[f"university-of-the-{major}"] = "جامعة {} %s" % maj_ar

test_Universities_cash = {}


def test_Universities(cate):
    cate = cate.lower()
    # ---
    if cate.startswith("category:"):
        cate = cate[len("category:") :].strip()
    # ---
    if cate.lower().strip() in test_Universities_cash:
        return test_Universities_cash[cate.lower().strip()]
    # ---
    print_put(f"<<lightblue>>>> vvvvvvvvvvvv test_Universities start, (cate:{cate}) vvvvvvvvvvvv ")
    # ---
    cite = ""
    majorlab = ""
    # ---
    for xi, xi_lab in universities_tables.items():
        xi2 = f"the {xi}"
        if cate.endswith(xi):
            majorlab = xi_lab
            cite = cate[: -len(xi)].strip()
            break
        elif cate.endswith(xi2):
            majorlab = xi_lab
            cite = cate[: -len(xi2)].strip()
            break
    # ---
    if not cite:
        for xi, xi_lab in universities_tables.items():
            xi3 = f"{xi}, "
            the_xi = f"the {xi}"
            if cate.startswith(xi3):
                majorlab = xi_lab
                cite = cate[len(xi3) :].strip()
                break
            elif cate.startswith(xi):
                majorlab = xi_lab
                cite = cate[len(xi) :].strip()
                break
            elif cate.startswith(the_xi):
                majorlab = xi_lab
                cite = cate[len(the_xi) :].strip()
                break
    # ---
    citelab = ""
    if cite:
        # ---
        citelab = N_cit_ies_s_lower.get(cite, "")
        # ---
        print_put(f"<<lightblue>>>> test_Universities cite:{cite}, majorlab:{majorlab}, citelab:{citelab}")
    # ---
    univer_lab = ""
    # ---
    if citelab:
        univer_lab = majorlab.format(citelab)
        print_put(f'<<lightblue>>>>>> test_Universities: new univer_lab  "{univer_lab}" ')
    # ---
    print_put("<<lightblue>>>> ^^^^^^^^^ test_Universities end ^^^^^^^^^ ")
    # ---
    test_Universities_cash[cate.lower().strip()] = univer_lab
    # ---
    return univer_lab
