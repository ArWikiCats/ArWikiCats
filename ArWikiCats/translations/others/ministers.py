#!/usr/bin/python3
"""
!
"""

from ..helps import len_print

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
ministers_keys = {
    "housing and urban development": {
        "no_al": "إسكان وتنمية حضرية",
        "with_al": "الإسكان والتنمية الحضرية",
    },
    "regional development and local governments": {
        "no_al": "تنمية محلية",
        "with_al": "التنمية المحلية",
    },
    "agriculture": {"no_al": "زراعة", "with_al": "الزراعة"},
    "army": {"no_al": "جيش", "with_al": "الجيش"},
    "broadcasting": {"no_al": "إذاعة", "with_al": "الإذاعة"},
    "civil service": {"no_al": "خدمة مدنية", "with_al": "الخدمة المدنية"},
    "climate change": {"no_al": "تغير المناخ", "with_al": "تغير المناخ"},
    "colonial": {"no_al": "إستعمار", "with_al": "الإستعمار"},
    "commerce": {"no_al": "تجارة", "with_al": "التجارة"},
    "communication": {"no_al": "اتصالات", "with_al": "الاتصالات"},
    "communications": {"no_al": "اتصالات", "with_al": "الاتصالات"},
    "constitutional affairs": {"no_al": "شؤون دستورية", "with_al": "الشؤون الدستورية"},
    "construction": {"no_al": "بناء", "with_al": "البناء"},
    "cooperatives": {"no_al": "تعاونيات", "with_al": "التعاونيات"},
    "culture": {"no_al": "ثقافة", "with_al": "الثقافة"},
    "defence": {"no_al": "دفاع", "with_al": "الدفاع"},
    "defense": {"no_al": "دفاع", "with_al": "الدفاع"},
    "diaspora": {"no_al": "شتات", "with_al": "الشتات"},
    "economy": {"no_al": "اقتصاد", "with_al": "الاقتصاد"},
    "education": {"no_al": "تعليم", "with_al": "التعليم"},
    "employment": {"no_al": "توظيف", "with_al": "التوظيف"},
    "energy": {"no_al": "طاقة", "with_al": "الطاقة"},
    "environment": {"no_al": "بيئة", "with_al": "البيئة"},
    "family": {"no_al": "أسرة", "with_al": "الأسرة"},
    "finance": {"no_al": "مالية", "with_al": "المالية"},
    "fisheries": {"no_al": "ثروة سمكية", "with_al": "الثروة السمكية"},
    "foreign affairs": {"no_al": "شؤون خارجية", "with_al": "الشؤون الخارجية"},
    "foreign trade": {"no_al": "تجارة خارجية", "with_al": "التجارة الخارجية"},
    "foreign": {"no_al": "خارجية", "with_al": "الخارجية"},
    "gender equality": {"no_al": "المساواة بين الجنسين", "with_al": "المساواة بين الجنسين"},
    "health": {"no_al": "صحة", "with_al": "الصحة"},
    "homeland security": {"no_al": "أمن داخلي", "with_al": "الأمن الداخلي"},
    "housing": {"no_al": "إسكان", "with_al": "الإسكان"},
    "human rights": {"no_al": "حقوق الإنسان", "with_al": "الحقوق الإنسان"},
    "human services": {"no_al": "خدمات إنسانية", "with_al": "الخدمات الإنسانية"},
    "immigration": {"no_al": "هجرة", "with_al": "الهجرة"},
    "indigenous affairs": {"no_al": "شؤون سكان أصليين", "with_al": "شؤون السكان الأصليين"},
    "industry": {"no_al": "صناعة", "with_al": "الصناعة"},
    "information": {"no_al": "إعلام", "with_al": "الإعلام"},
    "infrastructure": {"no_al": "بنية تحتية", "with_al": "البنية التحتية"},
    "intelligence": {"no_al": "مخابرات", "with_al": "المخابرات"},
    "interior": {"no_al": "داخلية", "with_al": "الداخلية"},
    "internal affairs": {"no_al": "شؤون داخلية", "with_al": "الشؤون الداخلية"},
    "irrigation": {"no_al": "ري", "with_al": "الري"},
    "justice": {"no_al": "عدل", "with_al": "العدل"},
    "labor": {"no_al": "عمل", "with_al": "العمل"},
    "labour": {"no_al": "عمل", "with_al": "العمل"},
    "labour-and-social security": {"no_al": "عمل وضمان اجتماعي", "with_al": "العمل والضمان الاجتماعي"},
    "land management": {"no_al": "إدارة أراضي", "with_al": "إدارة الأراضي"},
    "law": {"no_al": "قانون", "with_al": "القانون"},
    "maritime affairs": {"no_al": "شؤون بحرية", "with_al": "الشؤون البحرية"},
    "military affairs": {"no_al": "شؤون عسكرية", "with_al": "الشؤون العسكرية"},
    "mining": {"no_al": "تعدين", "with_al": "التعدين"},
    "national defence": {"no_al": "دفاع وطني", "with_al": "الدفاع الوطني"},
    "natural resources": {"no_al": "موارد طبيعية", "with_al": "الموارد الطبيعية"},
    "navy": {"no_al": "بحرية", "with_al": "البحرية"},
    "nuclear security": {"no_al": "أمن نووي", "with_al": "الأمن النووي"},
    "oil": {"no_al": "بترول", "with_al": "البترول"},
    "peace": {"no_al": "سلام", "with_al": "السلام"},
    "planning": {"no_al": "تخطيط", "with_al": "التخطيط"},
    "prisons": {"no_al": "سجون", "with_al": "السجون"},
    "public safety": {"no_al": "سلامة عامة", "with_al": "السلامة العامة"},
    "public service": {"no_al": "خدمة عامة", "with_al": "الخدمة العامة"},
    "public works": {"no_al": "أشغال عامة", "with_al": "الأشغال العامة"},
    "reconciliation": {"no_al": "مصالحة", "with_al": "المصالحة"},
    "religious affairs": {"no_al": "شؤون دينية", "with_al": "الشؤون الدينية"},
    "research": {"no_al": "أبحاث", "with_al": "الأبحاث"},
    "science": {"no_al": "العلم", "with_al": "العلم"},
    "security": {"no_al": "أمن", "with_al": "الأمن"},
    "social affairs": {"no_al": "شؤون اجتماعية", "with_al": "الشؤون الاجتماعية"},
    "social security": {"no_al": "ضمان اجتماعي", "with_al": "الضمان الاجتماعي"},
    "sports": {"no_al": "رياضة", "with_al": "الرياضة"},
    "technology": {"no_al": "تقانة", "with_al": "التقانة"},
    "tourism": {"no_al": "سياحة", "with_al": "السياحة"},
    "trade": {"no_al": "تجارة", "with_al": "التجارة"},
    "transport": {"no_al": "نقل", "with_al": "النقل"},
    "transportation": {"no_al": "نقل", "with_al": "النقل"},
    "treasury": {"no_al": "خزانة", "with_al": "الخزانة"},
    "urban development": {"no_al": "تخطيط عمراني", "with_al": "التخطيط العمراني"},
    "veterans affairs": {"no_al": "شؤون محاربين قدامى", "with_al": "شؤون المحاربين القدامى"},
    "veterans and military families": {"no_al": "شؤون محاربين قدامى", "with_al": "شؤون المحاربين القدامى"},
    "war": {"no_al": "حرب", "with_al": "الحرب"},
    "water": {"no_al": "مياه", "with_al": "المياه"},
    "women's": {"no_al": "شؤون المرأة", "with_al": "شؤون المرأة"},
    "electricity": {"no_al": "كهرباء", "with_al": "الكهرباء"},
    # "state": {"no_al": "خارجية", "with_al": "الخارجية"},
}

add_keys = [
    ("health", "human services"),
    ("communications", "transportation"),
    ("environment", "natural resources"),
    ("labor", "employment"),
    ("labor", "social affairs"),
    ("labour", "employment"),
    ("labour", "social affairs"),
    ("war", "navy"),
    ("culture", "tourism"),
    ("labour", "social security"),
    ("agriculture", "cooperatives"),
    ("peace", "reconciliation"),
    ("electricity", "water"),
    ("environment", "climate change"),
]
# ---
for key1, key2 in add_keys:
    combined_key = f"{key1} and {key2}"
    key_1_data = ministers_keys.get(key1, {})
    key_2_data = ministers_keys.get(key2, {})
    # ---
    if not key_1_data or not key_2_data:
        continue
    # ---
    key_1_singular = key_1_data.get("no_al", "")
    key_2_singular = key_2_data.get("no_al", "")
    # ---
    key_1_al = key_1_data.get("with_al", "")
    key_2_al = key_2_data.get("with_al", "")
    # ---
    if not any([key_1_singular, key_2_singular, key_1_al, key_2_al]):
        continue
    # ---
    ministers_keys[combined_key] = {
        "no_al": f"{key_1_singular} و{key_2_singular}",
        "with_al": f"{key_1_al} و{key_2_al}",
    }


len_print.data_len(
    "ministers.py",
    {
        "ministers_keys": ministers_keys,
    },
)
