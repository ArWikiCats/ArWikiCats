#!/usr/bin/python3
"""
!
"""

from ...helps import len_print

# ---
ministrees_keysse = {  # to add it to pop_of_without_in in all_keys2.py
    "deputy prime ministers": "نواب رؤساء وزراء",
}
# ---
minister_keyse = {
    "ministers of": "وزراء",
    "government ministers of": "وزراء",
    "women's ministers of": "وزيرات",
    "women government ministers of": "وزيرات",
    "deputy prime ministers of": "نواب رؤساء وزراء",
    "finance ministers of": "وزراء مالية",
    "foreign ministers of": "وزراء خارجية",
    "prime ministers of": "رؤساء وزراء",
    "sport-ministers": "وزراء رياضة",
    "sports-ministers": "وزراء رياضة",
    "ministers of power": "وزراء طاقة",
    "ministers-of power": "وزراء طاقة",
}
# ---#
keyses_without_in = [
    "زراعة",
    "اتصالات",
    "ثقافة",
    "دفاع",
    "اقتصاد",
    "تعليم",
    "طاقة",
    "بيئة",
    "أسرة",
    "مالية",
    "صحة",
    "صناعة",
    "إعلام",
    "داخلية",
    "مخابرات",
    "إسكان",
    "عدل",
    "تخطيط",
    "عمل",
    "قانون",
    "بترول",
    "أمن",
    "رياضة",
    "سياحة",
    "نقل",
    "مياه",
    "زراعة",
    "خارجية",
    "عدل",
]
# ---
ministrs_keys = {
    "housing and urban development": {
        "singular": "إسكان وتنمية حضرية",
        "al": "الإسكان والتنمية الحضرية",
    },
    "regional development and local governments": {
        "singular": "تنمية محلية",
        "al": "التنمية المحلية",
    },
    "agriculture": {"singular": "زراعة", "al": "الزراعة"},
    "army": {"singular": "جيش", "al": "الجيش"},
    "broadcasting": {"singular": "إذاعة", "al": "الإذاعة"},
    "civil service": {"singular": "خدمة مدنية", "al": "الخدمة المدنية"},
    "climate change": {"singular": "تغير المناخ", "al": "تغير المناخ"},
    "colonial": {"singular": "إستعمار", "al": "الإستعمار"},
    "commerce": {"singular": "تجارة", "al": "التجارة"},
    "communication": {"singular": "اتصالات", "al": "الاتصالات"},
    "communications": {"singular": "اتصالات", "al": "الاتصالات"},
    "constitutional affairs": {"singular": "شؤون دستورية", "al": "الشؤون الدستورية"},
    "construction": {"singular": "بناء", "al": "البناء"},
    "cooperatives": {"singular": "تعاونيات", "al": "التعاونيات"},
    "culture": {"singular": "ثقافة", "al": "الثقافة"},
    "defence": {"singular": "دفاع", "al": "الدفاع"},
    "defense": {"singular": "دفاع", "al": "الدفاع"},
    "diaspora": {"singular": "شتات", "al": "الشتات"},
    "economy": {"singular": "اقتصاد", "al": "الاقتصاد"},
    "education": {"singular": "تعليم", "al": "التعليم"},
    "employment": {"singular": "توظيف", "al": "التوظيف"},
    "energy": {"singular": "طاقة", "al": "الطاقة"},
    "environment": {"singular": "بيئة", "al": "البيئة"},
    "family": {"singular": "أسرة", "al": "الأسرة"},
    "finance": {"singular": "مالية", "al": "المالية"},
    "fisheries": {"singular": "ثروة سمكية", "al": "الثروة السمكية"},
    "foreign affairs": {"singular": "شؤون خارجية", "al": "الشؤون الخارجية"},
    "foreign trade": {"singular": "تجارة خارجية", "al": "التجارة الخارجية"},
    "foreign": {"singular": "خارجية", "al": "الخارجية"},
    "gender equality": {"singular": "المساواة بين الجنسين", "al": "المساواة بين الجنسين"},
    "health": {"singular": "صحة", "al": "الصحة"},
    "homeland security": {"singular": "أمن داخلي", "al": "الأمن الداخلي"},
    "housing": {"singular": "إسكان", "al": "الإسكان"},
    "human rights": {"singular": "حقوق الإنسان", "al": "الحقوق الإنسان"},
    "human services": {"singular": "خدمات إنسانية", "al": "الخدمات الإنسانية"},
    "immigration": {"singular": "هجرة", "al": "الهجرة"},
    "indigenous affairs": {"singular": "شؤون سكان أصليين", "al": "شؤون السكان الأصليين"},
    "industry": {"singular": "صناعة", "al": "الصناعة"},
    "information": {"singular": "إعلام", "al": "الإعلام"},
    "infrastructure": {"singular": "بنية تحتية", "al": "البنية التحتية"},
    "intelligence": {"singular": "مخابرات", "al": "المخابرات"},
    "interior": {"singular": "داخلية", "al": "الداخلية"},
    "internal affairs": {"singular": "شؤون داخلية", "al": "الشؤون الداخلية"},
    "irrigation": {"singular": "ري", "al": "الري"},
    "justice": {"singular": "عدل", "al": "العدل"},
    "labor": {"singular": "عمل", "al": "العمل"},
    "labour": {"singular": "عمل", "al": "العمل"},
    "labour-and-social security": {"singular": "عمل وضمان اجتماعي", "al": "العمل والضمان الاجتماعي"},
    "land management": {"singular": "إدارة أراضي", "al": "إدارة الأراضي"},
    "law": {"singular": "قانون", "al": "القانون"},
    "maritime affairs": {"singular": "شؤون بحرية", "al": "الشؤون البحرية"},
    "military affairs": {"singular": "شؤون عسكرية", "al": "الشؤون العسكرية"},
    "mining": {"singular": "تعدين", "al": "التعدين"},
    "national defence": {"singular": "دفاع وطني", "al": "الدفاع الوطني"},
    "natural resources": {"singular": "موارد طبيعية", "al": "الموارد الطبيعية"},
    "navy": {"singular": "بحرية", "al": "البحرية"},
    "nuclear security": {"singular": "أمن نووي", "al": "الأمن النووي"},
    "oil": {"singular": "بترول", "al": "البترول"},
    "peace": {"singular": "سلام", "al": "السلام"},
    "planning": {"singular": "تخطيط", "al": "التخطيط"},
    "prisons": {"singular": "سجون", "al": "السجون"},
    "public safety": {"singular": "سلامة عامة", "al": "السلامة العامة"},
    "public service": {"singular": "خدمة عامة", "al": "الخدمة العامة"},
    "public works": {"singular": "أشغال عامة", "al": "الأشغال العامة"},
    "reconciliation": {"singular": "مصالحة", "al": "المصالحة"},
    "religious affairs": {"singular": "شؤون دينية", "al": "الشؤون الدينية"},
    "research": {"singular": "أبحاث", "al": "الأبحاث"},
    "science": {"singular": "العلم", "al": "العلم"},
    "security": {"singular": "أمن", "al": "الأمن"},
    "social affairs": {"singular": "شؤون اجتماعية", "al": "الشؤون الاجتماعية"},
    "social security": {"singular": "ضمان اجتماعي", "al": "الضمان الاجتماعي"},
    "sports": {"singular": "رياضة", "al": "الرياضة"},
    "technology": {"singular": "تقانة", "al": "التقانة"},
    "tourism": {"singular": "سياحة", "al": "السياحة"},
    "trade": {"singular": "تجارة", "al": "التجارة"},
    "transport": {"singular": "نقل", "al": "النقل"},
    "transportation": {"singular": "نقل", "al": "النقل"},
    "treasury": {"singular": "خزانة", "al": "الخزانة"},
    "urban development": {"singular": "تخطيط عمراني", "al": "التخطيط العمراني"},
    "veterans affairs": {"singular": "شؤون محاربين قدامى", "al": "شؤون المحاربين القدامى"},
    "veterans and military families": {"singular": "شؤون محاربين قدامى", "al": "شؤون المحاربين القدامى"},
    "war": {"singular": "حرب", "al": "الحرب"},
    "water": {"singular": "مياه", "al": "المياه"},
    "women's": {"singular": "شؤون المرأة", "al": "شؤون المرأة"},
    # "state": {"singular": "خارجية", "al": "الخارجية"},
}

add_keys = [
    ("health", "human services"),
    ("communications", "transportation"),
    ("environment", "natural resources"),
    ("labor", "employment"),
    ("labor", "social affairs"),
    ("war", "navy"),
    ("culture", "tourism"),
    ("labour", "social security"),
    ("agriculture", "cooperatives"),
    ("peace", "reconciliation"),
]
# ---
for key1, key2 in add_keys:
    combined_key = f"{key1} and {key2}"
    key_1_data = ministrs_keys.get(key1, {})
    key_2_data = ministrs_keys.get(key2, {})
    # ---
    if not key_1_data or not key_2_data:
        continue
    # ---
    key_1_singular = key_1_data.get("singular", "")
    key_2_singular = key_2_data.get("singular", "")
    # ---
    key_1_al = key_1_data.get("al", "")
    key_2_al = key_2_data.get("al", "")
    # ---
    if not any([key_1_singular, key_2_singular, key_1_al, key_2_al]):
        continue
    # ---
    ministrs_keys[combined_key] = {
        "singular": f"{key_1_singular} و{key_2_singular}",
        "al": f"{key_1_al} و{key_2_al}",
    }
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower().strip()
    short_label = ministry_labels["singular"]
    arabic_ministers_label = f"وزراء {short_label}"
    minister_keyse[f"{normalized_ministry} ministries"] = f"وزارات {short_label}"

    minister_keyse[f"{normalized_ministry} ministers"] = arabic_ministers_label

    minister_keyse[f"ministers-of {normalized_ministry}"] = arabic_ministers_label
    minister_keyse[f"ministers of {normalized_ministry}"] = arabic_ministers_label

    minister_keyse[f"secretaries-of {normalized_ministry}"] = arabic_ministers_label
    minister_keyse[f"secretaries of {normalized_ministry}"] = arabic_ministers_label
    minister_keyse[f"ministers-for {normalized_ministry}"] = arabic_ministers_label

    if short_label in keyses_without_in:
        ministrees_keysse[f"ministers of {normalized_ministry} of"] = arabic_ministers_label
        ministrees_keysse[f"ministers-of {normalized_ministry} of"] = arabic_ministers_label
        ministrees_keysse[f"{normalized_ministry} ministers"] = arabic_ministers_label
        ministrees_keysse[f"{normalized_ministry} ministers of"] = arabic_ministers_label
        minister_keyse[f"ministers-of {normalized_ministry} of"] = arabic_ministers_label
        minister_keyse[f"ministers of {normalized_ministry} of"] = arabic_ministers_label
        minister_keyse[f"ministers-for {normalized_ministry} of"] = arabic_ministers_label
# ---
ministrees_keysse = {}
# ---
len_print.data_len("ministers.py", {
    "minister_keyse": minister_keyse,
})
