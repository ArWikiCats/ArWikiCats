"""Resolve Arabic labels for army-related categories."""

from __future__ import annotations

import functools
from ..translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ..translations.nats.Nationality import all_country_with_nat_ar

_all_country_with_nat = {
    "eastern asian": {
        "male": "آسيوي شرقي",
        "males": "آسيويين شرقيون",
        "female": "آسيوية شرقية",
        "females": "آسيويات شرقيات",
        "en": "eastern asia",
        "ar": "شرق آسيا",
        "the_female": "الآسيوية الشرقية",
        "the_male": "الآسيوي الشرقي"
    },
    "eastern european": {
        "male": "أوروبي شرقي",
        "males": "أوروبيون شرقيون",
        "female": "أوروبية شرقية",
        "females": "أوروبيات شرقيات",
        "en": "eastern european",
        "ar": "شرق أوروبا",
        "the_female": "الأوروبية الشرقية",
        "the_male": "الأوروبي الشرقي"
    },
    "ecuadorian": {
        "male": "إكوادوري",
        "males": "إكوادوريون",
        "female": "إكوادورية",
        "females": "إكوادوريات",
        "en": "ecuador",
        "ar": "الإكوادور",
        "the_female": "الإكوادورية",
        "the_male": "الإكوادوري"
    },
    "egyptian": {
        "male": "مصري",
        "males": "مصريون",
        "female": "مصرية",
        "females": "مصريات",
        "en": "egypt",
        "ar": "مصر",
        "the_female": "المصرية",
        "the_male": "المصري"
    },
    "emirati": {
        "male": "إماراتي",
        "males": "إماراتيون",
        "female": "إماراتية",
        "females": "إماراتيات",
        "en": "united arab emirates",
        "ar": "الإمارات العربية المتحدة",
        "the_female": "الإماراتية",
        "the_male": "الإماراتي"
    },
    "emiri": {
        "male": "إماراتي",
        "males": "إماراتيون",
        "female": "إماراتية",
        "females": "إماراتيات",
        "en": "united arab emirates",
        "ar": "الإمارات العربية المتحدة",
        "the_female": "الإماراتية",
        "the_male": "الإماراتي"
    },
    "emirian": {
        "male": "إماراتي",
        "males": "إماراتيون",
        "female": "إماراتية",
        "females": "إماراتيات",
        "en": "united arab emirates",
        "ar": "الإمارات العربية المتحدة",
        "the_female": "الإماراتية",
        "the_male": "الإماراتي"
    },
    "english": {
        "male": "إنجليزي",
        "males": "إنجليز",
        "female": "إنجليزية",
        "females": "إنجليزيات",
        "en": "england",
        "ar": "إنجلترا",
        "the_female": "الإنجليزية",
        "the_male": "الإنجليزي"
    },
    "equatoguinean": {
        "male": "غيني استوائي",
        "males": "غينيون استوائيون",
        "female": "غينية استوائية",
        "females": "غينيات استوائيات",
        "en": "equatorial guinea",
        "ar": "غينيا الاستوائية",
        "the_female": "الغينية الاستوائية",
        "the_male": "الغيني الاستوائي"
    },
    "equatorial guinean": {
        "male": "غيني استوائي",
        "males": "غينيون استوائيون",
        "female": "غينية استوائية",
        "females": "غينيات استوائيات",
        "en": "equatorial guinea",
        "ar": "غينيا الاستوائية",
        "the_female": "الغينية الاستوائية",
        "the_male": "الغيني الاستوائي"
    }
}
# ---
ministrs_keys = {
    "veterans and military families": {"singular": "شؤون محاربين قدامى", "al": "شؤون المحاربين القدامى"},
    "navy": {"singular": "بحرية", "al": "البحرية"},
    "housing and urban development": {
        "singular": "إسكان وتنمية حضرية",
        "al": "الإسكان والتنمية الحضرية",
    },
    "peace and reconciliation": {"singular": "سلام ومصالحة", "al": "السلام والمصالحة"},
    "veterans affairs": {"singular": "شؤون محاربين قدامى", "al": "شؤون المحاربين القدامى"},
    "military affairs": {"singular": "شؤون عسكرية", "al": "الشؤون العسكرية"},
    "constitutional affairs": {"singular": "شؤون دستورية", "al": "الشؤون الدستورية"},
    "regional development and local governments": {
        "singular": "تنمية محلية",
        "al": "التنمية المحلية",
    },
    "human services": {"singular": "خدمات إنسانية", "al": "الخدمات الإنسانية"},
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
    # "state": {"singular": "خارجية", "al": "الخارجية"},
    "foreign": {"singular": "خارجية", "al": "الخارجية"},
    "foreign affairs": {"singular": "شؤون خارجية", "al": "الشؤون الخارجية"},
}
# ---
add_keys = [
    ("health", "human services"),
    ("communications", "transportation"),
    ("environment", "natural resources"),
    ("labor", "employment"),
    ("war", "navy"),
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
state_secretaries_mapping = {
    "united states secretaries of state": "وزراء خارجية أمريكيون",
    "secretaries of state of {en}": "وزراء خارجية {males}",
    "secretaries of state for {en}": "وزراء خارجية {males}",

    "{en} assistant secretaries of {ministry}": "مساعدو وزير {al} {the_male}",
    "{en} deputy secretaries of {ministry}": "نواب وزير {al} {the_male}",
    "{en} under secretaries of {ministry}": "نواب وزير {al} {the_male}",

    "assistant secretaries of {ministry} of {en}": "مساعدو وزير {al} {the_male}",
    "deputy secretaries of {ministry} of {en}": "نواب وزير {al} {the_male}",
    "under secretaries of {ministry} of {en}": "نواب وزير {al} {the_male}",

    "{en} secretaries of {ministry}" : "وزراء {singular} {males}",
    "secretaries of {ministry} of {en}" : "وزراء {singular} {males}",
    "secretaries of {ministry}" : "وزراء {singular}",

    "state lieutenant governors of {en}": "نواب حكام الولايات في {ar}",
    "state secretaries of state of {en}": "وزراء خارجية الولايات في {ar}",
    "state cabinet secretaries of {en}" : "أعضاء مجلس وزراء {ar}",
}

state_secretaries_mapping.update({
    x.replace("secretaries of", "secretaries-of"): y
    for x, y in state_secretaries_mapping.items()
    if "secretaries of" in x
})


def remove_the(text: str) -> str:
    if text.lower().startswith("the "):
        return text[4:]
    return text


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = {
        remove_the(v["en"]): v
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar") and v.get("en")
    }

    nats_data.update({
        "ireland": {
            "male": "أيرلندي",
            "males": "أيرلنديون",
            "female": "أيرلندية",
            "females": "أيرلنديات",
            "en": "ireland",
            "ar": "أيرلندا",
            "the_female": "الأيرلندية",
            "the_male": "الأيرلندي"
        }
    })

    both_bot = format_multi_data_v2(
        formatted_data=state_secretaries_mapping,
        data_list=nats_data,
        key_placeholder="{en}",
        data_list2=ministrs_keys,
        key2_placeholder="{ministry}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


def resolve_secretaries_labels(category: str) -> str:
    both_bot = _load_bot()
    result = both_bot.search_all_category(category)
    return result


__all__ = [
    "resolve_secretaries_labels"
]
