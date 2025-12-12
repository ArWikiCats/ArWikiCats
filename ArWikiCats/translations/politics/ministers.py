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
    "peace and reconciliation": {"singular": "سلام ومصالحة", "al": "السلام والمصالحة"},
    "veterans and military families": {"singular": "شؤون محاربين قدامى", "al": "شؤون المحاربين القدامى"},
    "veterans affairs": {"singular": "شؤون محاربين قدامى", "al": "شؤون المحاربين القدامى"},
    "military affairs": {"singular": "شؤون عسكرية", "al": "الشؤون العسكرية"},
    "constitutional affairs": {"singular": "شؤون دستورية", "al": "الشؤون الدستورية"},
    "regional development and local governments": {
        "singular": "تنمية محلية",
        "al": "التنمية المحلية",
    },
    "health and human services": {
        "singular": "صحة وخدمات إنسانية",
        "al": "الصحة والخدمات الإنسانية",
    },
    "treasury": {"singular": "خزانة", "al": "الخزانة"},
    "homeland security": {"singular": "أمن داخلي", "al": "الأمن الداخلي"},
    "transportation": {"singular": "نقل", "al": "النقل"},
    "defense": {"singular": "دفاع", "al": "الدفاع"},
    "agriculture": {"singular": "زراعة", "al": "الزراعة"},
    "climate change": {"singular": "تغير المناخ", "al": "تغير المناخ"},
    "communication": {"singular": "اتصالات", "al": "الاتصالات"},
    "communications": {"singular": "اتصالات", "al": "الاتصالات"},
    "construction": {"singular": "بناء", "al": "البناء"},
    "culture": {"singular": "ثقافة", "al": "الثقافة"},
    "national defence": {"singular": "دفاع وطني", "al": "الدفاع الوطني"},
    "defence": {"singular": "دفاع", "al": "الدفاع"},
    "economy": {"singular": "اقتصاد", "al": "الاقتصاد"},
    "education": {"singular": "تعليم", "al": "التعليم"},
    "energy": {"singular": "طاقة", "al": "الطاقة"},
    "environment": {"singular": "بيئة", "al": "البيئة"},
    "family": {"singular": "أسرة", "al": "الأسرة"},
    "finance": {"singular": "مالية", "al": "المالية"},
    "fisheries": {"singular": "ثروة سمكية", "al": "الثروة السمكية"},
    "health": {"singular": "صحة", "al": "الصحة"},
    "human rights": {"singular": "حقوق الإنسان", "al": "الحقوق الإنسان"},
    "immigration": {"singular": "هجرة", "al": "الهجرة"},
    "industry": {"singular": "صناعة", "al": "الصناعة"},
    "information": {"singular": "إعلام", "al": "الإعلام"},
    "infrastructure": {"singular": "بنية تحتية", "al": "البنية التحتية"},
    "interior": {"singular": "داخلية", "al": "الداخلية"},
    "internal affairs": {"singular": "شؤون داخلية", "al": "الشؤون الداخلية"},
    "indigenous affairs": {"singular": "شؤون سكان أصليين", "al": "شؤون السكان الأصليين"},
    "maritime affairs": {"singular": "شؤون بحرية", "al": "الشؤون البحرية"},
    "intelligence": {"singular": "مخابرات", "al": "المخابرات"},
    "labour-and-social security": {
        "singular": "عمل وضمان اجتماعي",
        "al": "العمل والضمان الاجتماعي",
    },
    "labour and social security": {
        "singular": "عمل وضمان اجتماعي",
        "al": "العمل والضمان الاجتماعي",
    },
    "social security": {"singular": "ضمان اجتماعي", "al": "الضمان الاجتماعي"},
    "labor and social affairs": {
        "singular": "عمل وشؤون اجتماعية",
        "al": "العمل والشؤون الاجتماعية",
    },
    "social affairs": {"singular": "شؤون اجتماعية", "al": "الشؤون الاجتماعية"},
    "labor": {"singular": "عمل", "al": "العمل"},
    "labour": {"singular": "عمل", "al": "العمل"},
    "gender equality": {"singular": "المساواة بين الجنسين", "al": "المساواة بين الجنسين"},
    "colonial": {"singular": "إستعمار", "al": "الإستعمار"},
    "broadcasting": {"singular": "إذاعة", "al": "الإذاعة"},
    "land management": {"singular": "إدارة أراضي", "al": "إدارة الأراضي"},
    "housing": {"singular": "إسكان", "al": "الإسكان"},
    "public safety": {"singular": "سلامة عامة", "al": "السلامة العامة"},
    "planning": {"singular": "تخطيط", "al": "التخطيط"},
    "diaspora": {"singular": "شتات", "al": "الشتات"},
    "urban development": {"singular": "تخطيط عمراني", "al": "التخطيط العمراني"},
    "law": {"singular": "قانون", "al": "القانون"},
    "mining": {"singular": "تعدين", "al": "التعدين"},
    "oil": {"singular": "بترول", "al": "البترول"},
    "security": {"singular": "أمن", "al": "الأمن"},
    "nuclear security": {"singular": "أمن نووي", "al": "الأمن النووي"},
    "prisons": {"singular": "سجون", "al": "السجون"},
    "public works": {"singular": "أشغال عامة", "al": "الأشغال العامة"},
    "research": {"singular": "أبحاث", "al": "الأبحاث"},
    "science": {"singular": "العلم", "al": "العلم"},
    "sports": {"singular": "رياضة", "al": "الرياضة"},
    "civil service": {"singular": "خدمة مدنية", "al": "الخدمة المدنية"},
    "technology": {"singular": "تقانة", "al": "التقانة"},
    "irrigation": {"singular": "ري", "al": "الري"},
    "tourism": {"singular": "سياحة", "al": "السياحة"},
    "natural resources": {"singular": "موارد طبيعية", "al": "الموارد الطبيعية"},
    "religious affairs": {"singular": "شؤون دينية", "al": "الشؤون الدينية"},
    "foreign trade": {"singular": "تجارة خارجية", "al": "التجارة الخارجية"},
    "commerce": {"singular": "تجارة", "al": "التجارة"},
    "trade": {"singular": "تجارة", "al": "التجارة"},
    "transport": {"singular": "نقل", "al": "النقل"},
    "water": {"singular": "مياه", "al": "المياه"},
    "women's": {"singular": "شؤون المرأة", "al": "شؤون المرأة"},
    "public service": {"singular": "خدمة عامة", "al": "الخدمة العامة"},
    "justice": {"singular": "عدل", "al": "العدل"},
    "army": {"singular": "جيش", "al": "الجيش"},
    "war": {"singular": "حرب", "al": "الحرب"},
    "navy": {"singular": "بحرية", "al": "البحرية"},
    # "state": {"singular": "خارجية", "al": "الخارجية"},
    "foreign": {"singular": "خارجية", "al": "الخارجية"},
    "foreign affairs": {"singular": "شؤون خارجية", "al": "الشؤون الخارجية"},
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
ministrs_tab_for_Jobs_2020 = {}  # used in Jobs.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    singular_label = ministry_labels["singular"]
    ministrs_tab_for_Jobs_2020[f"secretaries-of {ministry_key}"] = {
        "males": f"وزراء {singular_label}",
        "females": f"وزيرات {singular_label}",
    }
    ministrs_tab_for_Jobs_2020[f"secretaries of {ministry_key}"] = {
        "males": f"وزراء {singular_label}",
        "females": f"وزيرات {singular_label}",
    }
# ---
ministrs_tab_for_pop_format = {}  # used in pop_format.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower().strip()
    short_label = ministry_labels["singular"]
    ministrs_tab_for_pop_format[f"secretaries of {normalized_ministry} of"] = f"وزراء {short_label} {{}}"
    ministrs_tab_for_pop_format[f"secretaries-of {normalized_ministry} of"] = f"وزراء {short_label} {{}}"
# ---
ministrs_for_military_format_men = {}  # used in bot_te_4.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower()
    al_label = ministry_labels["al"]

    ministrs_for_military_format_men[f"assistant secretaries of {normalized_ministry}"] = (
        f"مساعدو وزير {al_label} {{nat}}"
    )
    ministrs_for_military_format_men[f"deputy secretaries of {normalized_ministry}"] = (
        f"نواب وزير {al_label} {{nat}}"
    )
    ministrs_for_military_format_men[f"assistant secretaries-of {normalized_ministry}"] = (
        f"مساعدو وزير {al_label} {{nat}}"
    )
    ministrs_for_military_format_men[f"deputy secretaries-of {normalized_ministry}"] = (
        f"نواب وزير {al_label} {{nat}}"
    )
    ministrs_for_military_format_men[f"deputy secretary of {normalized_ministry}"] = (
        f"نواب وزير {al_label} {{nat}}"
    )
# ---
ministrs_for_military_format_women = {}  # used in bot_te_4.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower()
    al_label = ministry_labels["al"]

    ministrs_for_military_format_women[f"department of {normalized_ministry} agencies"] = (
        f"وكالات وزارة {al_label} {{nat}}"
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry} facilities"] = (
        f"مرافق وزارة {al_label} {{nat}}"
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry} national laboratories"] = (
        f"مختبرات وزارة {al_label} {{nat}}"
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry} national laboratories personnel"] = (
        f"موظفو مختبرات وزارة {al_label} {{nat}}"
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry} officials"] = (
        f"مسؤولو وزارة {al_label} {{nat}}"
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry}"] = (
        f"وزارة {al_label} {{nat}}"
    )

len_print.data_len("ministers.py", {
    "ministrs_for_military_format_women": ministrs_for_military_format_women,
    "ministrs_for_military_format_men": ministrs_for_military_format_men,
    "ministrs_tab_for_pop_format": ministrs_tab_for_pop_format,
    "ministrs_tab_for_Jobs_2020": ministrs_tab_for_Jobs_2020,
    "minister_keyse": minister_keyse,
})
