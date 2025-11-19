#!/usr/bin/python3
"""
!
"""
from .ministers import (
    ministrs_for_military_format_men,
    ministrs_for_en_is_P17_ar_is_mens,
    ministrs_for_military_format_women,
)
# الإنجليزية اسم البلد والعربية جنسية مؤنث بدون ألف ولام التعريف
military_format_women_without_al_from_end = {
    # Category:Unmanned_aerial_vehicles_of_Jordan > طائرات بدون طيار أردنية
    "unmanned military aircraft-of": "طائرات عسكرية بدون طيار {nat}",
    "unmanned aerial vehicles-of": "طائرات بدون طيار {nat}",
    "unmanned military aircraft-oof": "طائرات عسكرية بدون طيار {nat}",
    "unmanned aerial vehicles-oof": "طائرات بدون طيار {nat}",
}
military_format_women_without_al = {
    "unmanned military aircraft of": "طائرات عسكرية بدون طيار {nat}",
    "unmanned aerial vehicles of": "طائرات بدون طيار {nat}",
    "federal legislation": "تشريعات فيدرالية {nat}",
    "courts": "محاكم {nat}",
    "sports templates": "قوالب رياضة {nat}",
    "political party": "أحزاب سياسية {nat}",
    # "diplomacy" : "دبلوماسية {nat}",
    # "communications" : "اتصالات {nat}",
    # "sports navigational boxes" : "صناديق تصفح رياضة {nat}",
}
# ---
# الإنجليزية اسم البلد والعربية جنسية مؤنث بألف ولام التعريف
military_format_women = {
    "air force": "القوات الجوية {nat}",
    "airlines": "الخطوط الجوية {nat}",
    "armed forces": "القوات المسلحة {nat}",
    "army aviation": "طيران القوات المسلحة {nat}",
    "army": "القوات المسلحة {nat}",
    "case law": "السوابق القضائية {nat}",
    "communications": "الاتصالات {nat}",
    "diplomacy": "الدبلوماسية {nat}",
    "federal election candidates": "مرشحو الانتخابات الفيدرالية {nat}",
    "federal election": "الانتخابات الفيدرالية {nat}",
    "federal elections": "الانتخابات الفيدرالية {nat}",
    "football club": "أندية كرة القدم {nat}",
    "football manager history": "تاريخ مدربي كرة القدم {nat}",
    "football manager": "مدربي كرة القدم {nat}",
    "football": "كرة القدم {nat}",
    "general election candidates": "مرشحو الانتخابات العامة {nat}",
    "general election": "الانتخابات العامة {nat}",
    "general elections": "الانتخابات العامة {nat}",
    "legislature election": "الانتخابات التشريعية {nat}",
    "legislature elections": "الانتخابات التشريعية {nat}",
    "local election": "الانتخابات المحلية {nat}",
    "local elections": "الانتخابات المحلية {nat}",
    "national navy": "القوات البحرية الوطنية {nat}",
    "naval forces": "القوات البحرية {nat}",
    "navy": "القوات البحرية {nat}",
    "presidential candidates": "مرشحو الرئاسة {nat}",
    "presidential election": "انتخابات الرئاسة {nat}",
    "presidential elections": "انتخابات الرئاسة {nat}",
    "presidential electors": "ناخبو الرئاسة {nat}",
    "presidential primaries": "الانتخابات الرئاسية التمهيدية {nat}",
    # "presidential primaries": "انتخابات رئاسية تمهيدية {nat}",
    "presidential-elections": "انتخابات الرئاسة {nat}",
    "presidential-primaries": "الانتخابات الرئاسية التمهيدية {nat}",
    "state legislative": "المجالس التشريعية للولايات {nat}",
    "state lower house": "المجالس الدنيا للولايات {nat}",
    "state upper house": "المجالس العليا للولايات {nat}",
    "supreme court": "المحكمة العليا {nat}",
}  # Category:United_States_Coast_Guard_Aviation
# ---
for yu in ministrs_for_en_is_P17_ar_is_mens:
    military_format_women[yu] = ministrs_for_en_is_P17_ar_is_mens[yu]
# ---
for yu in ministrs_for_military_format_women:
    military_format_women[yu] = ministrs_for_military_format_women[yu]
# ---#president of france
# الإنجليزية اسم البلد والعربية جنسية مذكر
military_format_men = {
    "congressional delegation": "وفود الكونغرس {nat}",
    "congressional delegations": "وفود الكونغرس {nat}",
    "parliament": "البرلمان {nat}",
    "congress": "الكونغرس {nat}",
    # "house-of-representatives" : "مجلس النواب {nat}",
    # "house of representatives" : "مجلس النواب {nat}",
    "house of commons": "مجلس العموم {nat}",
    "house-of-commons": "مجلس العموم {nat}",
    "senate election": "انتخابات مجلس الشيوخ {nat}",
    "senate elections": "انتخابات مجلس الشيوخ {nat}",
    "premier division": "الدوري {nat} الممتاز",
    "coast guard": "خفر السواحل {nat}",
    "fa cup": "كأس الاتحاد {nat}",  # Category:Iraq FA Cup
    "federation cup": "كأس الاتحاد {nat}",  # Category:Bangladesh Federation Cup
    "marine corps personnel": "أفراد سلاح مشاة البحرية {nat}",
    "army personnel": "أفراد الجيش {nat}",
    "coast guard aviation": "طيران خفر السواحل {nat}",
    "abortion law": "قانون الإجهاض {nat}",
    "labour law": "قانون العمل {nat}",  # Category:French_labour_law
    "professional league": "دوري المحترفين {nat}",
    "first division league": "الدوري {nat} الدرجة الأولى",
    "second division": "الدوري {nat} الدرجة الثانية",
    "second division league": "الدوري {nat} الدرجة الثانية",
    "third division league": "الدوري {nat} الدرجة الثالثة",
    "forth division league": "الدوري {nat} الدرجة الرابعة",
}
# ---
for yu in ministrs_for_military_format_men:
    military_format_men[yu] = ministrs_for_military_format_men[yu]
# ---
