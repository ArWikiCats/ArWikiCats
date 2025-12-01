#!/usr/bin/python3
"""
!
"""

from ...helps import len_print

r"""
Category:Housing ministers of Abkhazia
Category:Ministers of Housing of Abkhazia
Category:Ministers for Housing of Abkhazia

Category:Public works ministers of Catalonia
Category:Ministers for Public Works of Luxembourg

Category:Ministers of Economics of Latvia
Category:Economy ministers of Latvia

Category:Religious affairs ministers of Yemen
Category:Ministers of Religious Affairs of the Netherlands

Category:Women government ministers of Latvia
Category:Women's ministers of Fiji

Category:British Secretaries of State for the Environment
Category:British Secretaries of State for Education
Category:British Secretaries of State for Employment
Category:Ministers for Foreign Affairs of Abkhazia
Category:Ministers for Foreign Affairs of Singapore
Category:Ministers for Foreign Affairs of Luxembourg
Category:Ministers for Internal Affairs of Abkhazia
Category:Ministers of Labour and Social Security of Turkey

"""
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
        "s": "إسكان وتنمية حضرية",
        "al": "الإسكان والتنمية الحضرية",
    },
    "peace and reconciliation": {"s": "سلام ومصالحة", "al": "السلام والمصالحة"},
    "veterans affairs": {"s": "شؤون محاربين قدامى", "al": "شؤون المحاربين القدامى"},
    "military affairs": {"s": "شؤون عسكرية", "al": "الشؤون العسكرية"},
    "constitutional affairs": {"s": "شؤون دستورية", "al": "الشؤون الدستورية"},
    "regional development and local governments": {
        "s": "تنمية محلية",
        "al": "التنمية المحلية",
    },
    "health and human services": {
        "s": "صحة وخدمات إنسانية",
        "al": "الصحة والخدمات الإنسانية",
    },
    "treasury": {"s": "خزانة", "al": "الخزانة"},
    "homeland security": {"s": "أمن داخلي", "al": "الأمن الداخلي"},
    "transportation": {"s": "نقل", "al": "النقل"},
    "defense": {"s": "دفاع", "al": "الدفاع"},
    "agriculture": {"s": "زراعة", "al": "الزراعة"},
    "climate change": {"s": "تغير المناخ", "al": "تغير المناخ"},
    "communication": {"s": "اتصالات", "al": "الاتصالات"},
    "communications": {"s": "اتصالات", "al": "الاتصالات"},
    "construction": {"s": "بناء", "al": "البناء"},
    "culture": {"s": "ثقافة", "al": "الثقافة"},
    "national defence": {"s": "دفاع وطني", "al": "الدفاع الوطني"},
    "defence": {"s": "دفاع", "al": "الدفاع"},
    "economy": {"s": "اقتصاد", "al": "الاقتصاد"},
    "education": {"s": "تعليم", "al": "التعليم"},
    "energy": {"s": "طاقة", "al": "الطاقة"},
    "environment": {"s": "بيئة", "al": "البيئة"},
    "family": {"s": "أسرة", "al": "الأسرة"},
    "finance": {"s": "مالية", "al": "المالية"},
    "fisheries": {"s": "ثروة سمكية", "al": "الثروة السمكية"},
    "health": {"s": "صحة", "al": "الصحة"},
    "human rights": {"s": "حقوق الإنسان", "al": "الحقوق الإنسان"},
    "immigration": {"s": "هجرة", "al": "الهجرة"},
    "industry": {"s": "صناعة", "al": "الصناعة"},
    "information": {"s": "إعلام", "al": "الإعلام"},
    "infrastructure": {"s": "بنية تحتية", "al": "البنية التحتية"},
    "interior": {"s": "داخلية", "al": "الداخلية"},
    "internal affairs": {"s": "شؤون داخلية", "al": "الشؤون الداخلية"},
    "indigenous affairs": {"s": "شؤون سكان أصليين", "al": "شؤون السكان الأصليين"},
    "maritime affairs": {"s": "شؤون بحرية", "al": "الشؤون البحرية"},
    "intelligence": {"s": "مخابرات", "al": "المخابرات"},
    "labour-and-social security": {
        "s": "عمل وضمان اجتماعي",
        "al": "العمل والضمان الاجتماعي",
    },
    "labour and social security": {
        "s": "عمل وضمان اجتماعي",
        "al": "العمل والضمان الاجتماعي",
    },
    "social security": {"s": "ضمان اجتماعي", "al": "الضمان الاجتماعي"},
    "labor and social affairs": {
        "s": "عمل وشؤون اجتماعية",
        "al": "العمل والشؤون الاجتماعية",
    },
    "social affairs": {"s": "شؤون اجتماعية", "al": "الشؤون الاجتماعية"},
    "labor": {"s": "عمل", "al": "العمل"},
    "labour": {"s": "عمل", "al": "العمل"},
    "gender equality": {"s": "المساواة بين الجنسين", "al": "المساواة بين الجنسين"},
    "colonial": {"s": "إستعمار", "al": "الإستعمار"},
    "broadcasting": {"s": "إذاعة", "al": "الإذاعة"},
    "land management": {"s": "إدارة أراضي", "al": "إدارة الأراضي"},
    "housing": {"s": "إسكان", "al": "الإسكان"},
    "public safety": {"s": "سلامة عامة", "al": "السلامة العامة"},
    "planning": {"s": "تخطيط", "al": "التخطيط"},
    "diaspora": {"s": "شتات", "al": "الشتات"},
    "urban development": {"s": "تخطيط عمراني", "al": "التخطيط العمراني"},
    "law": {"s": "قانون", "al": "القانون"},
    "mining": {"s": "تعدين", "al": "التعدين"},
    "oil": {"s": "بترول", "al": "البترول"},
    "security": {"s": "أمن", "al": "الأمن"},
    "nuclear security": {"s": "أمن نووي", "al": "الأمن النووي"},
    "prisons": {"s": "سجون", "al": "السجون"},
    "public works": {"s": "أشغال عامة", "al": "الأشغال العامة"},
    "research": {"s": "أبحاث", "al": "الأبحاث"},
    "science": {"s": "العلم", "al": "العلم"},
    "sports": {"s": "رياضة", "al": "الرياضة"},
    "civil service": {"s": "خدمة مدنية", "al": "الخدمة المدنية"},
    "technology": {"s": "تقانة", "al": "التقانة"},
    "irrigation": {"s": "ري", "al": "الري"},
    "tourism": {"s": "سياحة", "al": "السياحة"},
    "natural resources": {"s": "موارد طبيعية", "al": "الموارد الطبيعية"},
    "religious affairs": {"s": "شؤون دينية", "al": "الشؤون الدينية"},
    "foreign trade": {"s": "تجارة خارجية", "al": "التجارة الخارجية"},
    "commerce": {"s": "تجارة", "al": "التجارة"},
    "trade": {"s": "تجارة", "al": "التجارة"},
    "transport": {"s": "نقل", "al": "النقل"},
    "water": {"s": "مياه", "al": "المياه"},
    "women's": {"s": "شؤون المرأة", "al": "شؤون المرأة"},
    "public service": {"s": "خدمة عامة", "al": "الخدمة العامة"},
    "justice": {"s": "عدل", "al": "العدل"},
    "army": {"s": "جيش", "al": "الجيش"},
    "war": {"s": "حرب", "al": "الحرب"},
    "state": {"s": "خارجية", "al": "الخارجية"},
    "foreign": {"s": "خارجية", "al": "الخارجية"},
    "foreign affairs": {"s": "شؤون خارجية", "al": "الشؤون الخارجية"},
}
# ---
# for io in ministrs_keys:
# ss = ministrs_keys[io].replace(' ' , ' ال')
# print('"%s"\t:\t{ "s" : "%s" , "o" : "ال%s" }, ' %  (io , ministrs_keys[io] , ss  ) )
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower().strip()
    short_label = ministry_labels["s"]
    arabic_ministers_label = f"وزراء {short_label}"
    minister_keyse[f"{normalized_ministry} ministries"] = f"وزارات {short_label}"

    minister_keyse[f"{normalized_ministry} ministers"] = arabic_ministers_label

    minister_keyse[f"ministers-of {normalized_ministry}"] = arabic_ministers_label
    minister_keyse[f"ministers of {normalized_ministry}"] = arabic_ministers_label

    minister_keyse[f"secretaries-of {normalized_ministry}"] = arabic_ministers_label
    minister_keyse[f"secretaries of {normalized_ministry}"] = arabic_ministers_label
    # minister_keyse["ministers for {}".format(normalized_ministry) ] = arabic_ministers_label
    minister_keyse[f"ministers-for {normalized_ministry}"] = arabic_ministers_label
    if short_label in keyses_without_in:
        ministrees_keysse[f"ministers of {normalized_ministry} of"] = arabic_ministers_label
        ministrees_keysse[f"ministers-of {normalized_ministry} of"] = arabic_ministers_label
        ministrees_keysse[f"{normalized_ministry} ministers"] = arabic_ministers_label
        ministrees_keysse[f"{normalized_ministry} ministers of"] = arabic_ministers_label
        minister_keyse[f"ministers-of {normalized_ministry} of"] = arabic_ministers_label
        minister_keyse[f"ministers of {normalized_ministry} of"] = arabic_ministers_label
        # minister_keyse["ministers for {} of".format(normalized_ministry) ] = arabic_ministers_label
        minister_keyse[f"ministers-for {normalized_ministry} of"] = arabic_ministers_label
# ---
ministrs_tab_for_Jobs_2020 = {}  # used in Jobs.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    ministrs_tab_for_Jobs_2020[f"secretaries-of {ministry_key}"] = {
        "mens": f"وزراء {ministry_labels['s']}",
        "womens": f"وزيرات {ministry_labels['s']}",
    }
    ministrs_tab_for_Jobs_2020[f"secretaries of {ministry_key}"] = {
        "mens": f"وزراء {ministry_labels['s']}",
        "womens": f"وزيرات {ministry_labels['s']}",
    }
# ---
ministrs_tab_for_pop_format = {}  # used in pop_format.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower().strip()
    short_label = ministry_labels["s"]
    ministrs_tab_for_pop_format[f"secretaries of {normalized_ministry} of"] = "وزراء %s {}" % short_label
    ministrs_tab_for_pop_format[f"secretaries-of {normalized_ministry} of"] = "وزراء %s {}" % short_label
# ---
ministrs_for_military_format_men = {}  # used in bot_te_4.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower()
    # ministrs_for_military_format_men["secretary of the {}".format(mi2)] = 'وزير %s {nat}' % da['al']
    ministrs_for_military_format_men[f"assistant secretaries of {normalized_ministry}"] = (
        "مساعدو وزير %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_men[f"deputy secretaries of {normalized_ministry}"] = (
        "نواب وزير %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_men[f"deputy secretaries of the {normalized_ministry}"] = (
        "نواب وزير %s {nat}" % ministry_labels["al"]
    )

    ministrs_for_military_format_men[f"assistant secretaries-of {normalized_ministry}"] = (
        "مساعدو وزير %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_men[f"deputy secretaries-of {normalized_ministry}"] = (
        "نواب وزير %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_men[f"deputy secretaries-of the {normalized_ministry}"] = (
        "نواب وزير %s {nat}" % ministry_labels["al"]
    )

    ministrs_for_military_format_men[f"deputy secretary of {normalized_ministry}"] = (
        "نواب وزير %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_men[f"deputy secretary of the {normalized_ministry}"] = (
        "نواب وزير %s {nat}" % ministry_labels["al"]
    )
# ---
ministrs_for_military_format_women = {}  # used in bot_te_4.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower()
    ministrs_for_military_format_women[f"department of {normalized_ministry} agencies"] = (
        "وكالات وزارة %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry} facilities"] = (
        "مرافق وزارة %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry} national laboratories"] = (
        "مختبرات وزارة %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry} national laboratories personnel"] = (
        "موظفو مختبرات وزارة %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry} officials"] = (
        "مسؤولو وزارة %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_women[f"department of {normalized_ministry}"] = (
        "وزارة %s {nat}" % ministry_labels["al"]
    )
    ministrs_for_military_format_women[f"department of the {normalized_ministry}"] = (
        "وزارة %s {nat}" % ministry_labels["al"]
    )
# ---
ministrs_for_en_is_P17_ar_is_mens = {}  # used in bot_te_4.py
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower()
    ministrs_for_en_is_P17_ar_is_mens[f"secretaries-of the {normalized_ministry}"] = (
        "وزراء %s {}" % ministry_labels["s"]
    )
    ministrs_for_en_is_P17_ar_is_mens[f"secretaries of the {normalized_ministry}"] = (
        "وزراء %s {}" % ministry_labels["s"]
    )
    ministrs_for_en_is_P17_ar_is_mens[f"secretaries-of {normalized_ministry}"] = "وزراء %s {}" % ministry_labels["s"]
    ministrs_for_en_is_P17_ar_is_mens[f"secretaries of {normalized_ministry}"] = "وزراء %s {}" % ministry_labels["s"]
# ---

len_print.data_len("ministers.py", {
    "ministrs_for_en_is_P17_ar_is_mens": ministrs_for_en_is_P17_ar_is_mens,
    "ministrs_for_military_format_women": ministrs_for_military_format_women,
    "ministrs_for_military_format_men": ministrs_for_military_format_men,
    "ministrs_tab_for_pop_format": ministrs_tab_for_pop_format,
    "ministrs_tab_for_Jobs_2020": ministrs_tab_for_Jobs_2020,
    "minister_keyse": minister_keyse,
})
