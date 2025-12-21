#!/usr/bin/python3
"""
TODO: use it to replace get_and_label, get_by_label functions in bys.py

"""
import re
import functools
from ...helps import logger
from ...translations import open_json_file
from ...translations_formats import format_multi_data, MultiDataFormatterBase

CONTEXT_FIELD_LABELS = {
    "city": "مدينة",
    "date": "تاريخ",
    "country": "بلد",
    "continent": "قارة",
    "location": "موقع",
    "period": "حقبة",
    "time": "وقت",
    "year": "سنة",
    "decade": "عقد",
    "era": "عصر",
    "millennium": "ألفية",
    "century": "قرن",
}
BY_TABLE_BASED = open_json_file("keys/By_table.json") or {}

PRIMARY_COMPONENTS = {
    "setting location": "موقع الأحداث",
    "city": "المدينة",
    "continent": "القارة",
    "country": "البلد",
    "century": "القرن",
    "decade": "العقد",
    "year": "السنة",
    "millennium": "الألفية",

    "date": "التاريخ",
    "location": "الموقع",
    "period": "الحقبة",
    "time": "الوقت",
    "era": "العصر",

    "bank": "البنك",
    "behavior": "السلوك",
    "branch": "الفرع",
    "class": "الصنف",
    "club": "النادي",
    "company": "الشركة",
    "competition": "المنافسة",
    "condition": "الحالة",
    "conflict": "النزاع",
    "country of residence": "بلد الإقامة",
    "country subdivision": "تقسيم البلد",
    "country subdivisions": "تقسيمات البلد",
    "country-of-residence": "بلد الإقامة",
    "county": "المقاطعة",
    "educational establishment": "المؤسسة التعليمية",
    "educational institution": "الهيئة التعليمية",
    "ethnicity": "المجموعة العرقية",
    "event": "الحدث",
    "former religion": "الدين السابق",
    "genre": "النوع الفني",
    "government agency": "الوكالة الحكومية",
    "history of colleges and universities": "تاريخ الكليات والجامعات",
    "importance": "الأهمية",
    "industry": "الصناعة",
    "instrument": "الآلة",
    "issue": "القضية",
    "league": "الدوري",
    "magazine": "المجلة",
    "medium": "الوسط",
    "nation": "الموطن",
    "nationality": "الجنسية",
    "newspaper": "الصحيفة",
    "non-profit organizations": "المؤسسات غير الربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "nonprofit organization": "المؤسسات غير الربحية",
    "occupation": "المهنة",
    "organization": "المنظمة",
    "organizer": "المنظم",
    "orientation": "التوجه",
    "party": "الحزب",
    "political orientation": "التوجه السياسي",
    "prison": "السجن",
    "professional association": "الجمعيات المهنية",
    "publication": "المؤسسة",
    "quality": "الجودة",
    "rank": "الرتبة",
    "record label": "شركة التسجيلات",
    "region": "المنطقة",
    "religion": "الدين",
    "research organization": "منظمة البحوث",
    "role": "الدور",
    "sector": "القطاع",
    "series": "السلسلة",
    "shipbuilding company": "شركة بناء السفن",
    "specialty": "التخصص",
    "sport": "الرياضة",
    "state": "الولاية",
    "station": "المحطة",
    "status": "الحالة",
    "subdivision": "التقسيم",
    "team": "الفريق",
    "territory": "الإقليم",
    "trade union": "النقابات العمالية",
    "type": "الفئة",
    "writer": "الكاتب",
}


def build_yearly_category_translation():
    COMPETITION_CATEGORY_LABELS = {
        "girls": "فتيات",
        "mixed": "مختلط",
        "boys": "فتيان",
        "singles": "فردي",
        "womens": "سيدات",
        "ladies": "سيدات",
        "males": "رجال",
        "men's": "رجال",
    }
    # ---
    TOURNAMENT_STAGE_LABELS = {
        "tournament": "مسابقة",
        "singles": "فردي",
        "qualification": "تصفيات",
        "team": "فريق",
        "doubles": "زوجي",
    }

    data = {}

    for category_key, category_label in COMPETITION_CATEGORY_LABELS.items():
        for stage_key, stage_label in TOURNAMENT_STAGE_LABELS.items():
            by_entry_key = f"by year - {category_key} {stage_key}"
            translation_label = f"حسب السنة - {stage_label} {category_label}"
            data[by_entry_key] = translation_label
    # ---
    return data


by_keys_under = {
    "by men's under-16 national team": "حسب المنتخب الوطني للرجال تحت 16 سنة",
    "by men's under-17 national team": "حسب المنتخب الوطني للرجال تحت 17 سنة",
    "by men's under-18 national team": "حسب المنتخب الوطني للرجال تحت 18 سنة",
    "by men's under-19 national team": "حسب المنتخب الوطني للرجال تحت 19 سنة",
    "by men's under-20 national team": "حسب المنتخب الوطني للرجال تحت 20 سنة",
    "by men's under-21 national team": "حسب المنتخب الوطني للرجال تحت 21 سنة",
    "by men's under-23 national team": "حسب المنتخب الوطني للرجال تحت 23 سنة",
    "by under-16 national team": "حسب المنتخب الوطني تحت 16 سنة",
    "by under-17 national team": "حسب المنتخب الوطني تحت 17 سنة",
    "by under-18 national team": "حسب المنتخب الوطني تحت 18 سنة",
    "by under-19 national team": "حسب المنتخب الوطني تحت 19 سنة",
    "by under-20 national team": "حسب المنتخب الوطني تحت 20 سنة",
    "by under-21 national team": "حسب المنتخب الوطني تحت 21 سنة",
    "by under-23 national team": "حسب المنتخب الوطني تحت 23 سنة",
    "by women's under-16 national team": "حسب المنتخب الوطني للسيدات تحت 16 سنة",
    "by women's under-17 national team": "حسب المنتخب الوطني للسيدات تحت 17 سنة",
    "by women's under-18 national team": "حسب المنتخب الوطني للسيدات تحت 18 سنة",
    "by women's under-19 national team": "حسب المنتخب الوطني للسيدات تحت 19 سنة",
    "by women's under-20 national team": "حسب المنتخب الوطني للسيدات تحت 20 سنة",
    "by women's under-21 national team": "حسب المنتخب الوطني للسيدات تحت 21 سنة",
    "by women's under-23 national team": "حسب المنتخب الوطني للسيدات تحت 23 سنة"
}
_by_music_table_base = {
    "by city": "حسب المدينة",
    "by seniority": "حسب الأقدمية",
    "by producer": "حسب المنتج",
    "by software": "حسب البرمجيات",
    "by band": "حسب الفرقة",
    "by medium by nationality": "حسب الوسط حسب الجنسية",
    "by instrument": "حسب الآلة",
    "by instrument, genre and nationality": "حسب الآلة والنوع الفني والجنسية",
    "by genre, nationality and instrument": "حسب النوع الفني والجنسية والآلة",
    "by nationality, genre and instrument": "حسب الجنسية والنوع والآلة",
    "by instrument and nationality": "حسب الآلة والجنسية",
    "by instrument and genre": "حسب الآلة والنوع الفني",
    "by genre and instrument": "حسب النوع الفني والآلة",
    "by nationality and instrument ": "حسب الجنسية والآلة الموسيقية",
    "by century and instrument": "حسب القرن والآلة",
    "by medium": "حسب الوسط",
    "by name": "حسب الإسم",
    "by voice type": "حسب نوع الصوت",
    "by language": "حسب اللغة",
    "by nationality": "حسب الجنسية",
}


def fix_keys(label: str) -> str:
    """Fix common issues in keys before processing."""

    context_keys = "|".join(CONTEXT_FIELD_LABELS.keys())
    label = re.sub(f"({context_keys}) of", r"\g<1>-of", label, flags=re.I)

    return label


formatted_data = {
    "by {en} and city of setting": "حسب {ar} ومدينة الأحداث",
    "by {en} by city-of {en2}": "حسب {ar} حسب مدينة {ar2}",
    "by {en} or city-of {en2}": "حسب {ar} أو مدينة {ar2}",
    "by {en} and city-of {en2}": "حسب {ar} ومدينة {ar2}",
    "by year - {en}": "حسب {ar}",
    "by {en}": "حسب {ar}",
    "by {en2}": "حسب {ar2}",
    "by {en} or {en2}": "حسب {ar} أو {ar2}",

    "by {en} and {en2}": "حسب {ar} و{ar2}",
    "by {en} and {en}": "حسب {ar} و{ar}",

    "by {en2} and {en}": "حسب {ar2} و{ar}",
    "by {en} by {en2}": "حسب {ar} حسب {ar2}",
}

by_of_keys_2 = {
    "by city of {en}": "حسب مدينة {ar}",
    "by date of {en}": "حسب تاريخ {ar}",
    "by country of {en}": "حسب بلد {ar}",
    "by continent of {en}": "حسب قارة {ar}",
    "by location of {en}": "حسب موقع {ar}",
    "by period of {en}": "حسب حقبة {ar}",
    "by time of {en}": "حسب وقت {ar}",
    "by year of {en}": "حسب سنة {ar}",
    "by decade of {en}": "حسب عقد {ar}",
    "by era of {en}": "حسب عصر {ar}",
    "by millennium of {en}": "حسب ألفية {ar}",
    "by century of {en}": "حسب قرن {ar}",
}

for context_key, context_label in CONTEXT_FIELD_LABELS.items():
    formatted_data[f"by {context_key} of {{en}}"] = f"حسب {context_label} {{ar}}"
    # # formatted_data[f"by {{en2}} and {context_key} of {{en}}"] = f"حسب {{ar2}} و{context_label} {{ar}}"
    # # formatted_data[f"by {{en}} and {context_key} of {{en2}}"] = f"حسب {{ar}} و{context_label} {{ar2}}"
    # ---
    formatted_data[f"by {context_key}-of {{en}}"] = f"حسب {context_label} {{ar}}"
    formatted_data[f"by {{en2}} and {context_key}-of {{en}}"] = f"حسب {{ar2}} و{context_label} {{ar}}"
    formatted_data[f"by {{en}} and {context_key}-of {{en2}}"] = f"حسب {{ar}} و{context_label} {{ar2}}"

# formatted_data.update(by_of_keys_2)

data_to_find = dict(BY_TABLE_BASED)
data_to_find.update(build_yearly_category_translation())
data_to_find.update(_by_music_table_base)
data_to_find.update(by_keys_under)

ADDITIONAL_COMPONENTS_BY = {
    "composer": "الملحن",
    "composer nationality": "جنسية الملحن",
    "artist": "الفنان",
    "artist nationality": "جنسية الفنان",
    "manufacturer": "الصانع",
    "manufacturer nationality": "جنسية الصانع",
}
by_data_new = dict(PRIMARY_COMPONENTS)
by_data_new.update(ADDITIONAL_COMPONENTS_BY)
# by_data_new.update({x: v for x, v in CONTEXT_FIELD_LABELS.items() if x not in PRIMARY_COMPONENTS})

by_data_new.update({
    "nonprofit organization": "المؤسسات غير الربحية",
    "shooting location": "موقع التصوير",
    "developer": "التطوير",
    "location": "الموقع",
    "setting": "الأحداث",
    "country of residence": "بلد الإقامة",
    "country-of residence": "بلد الإقامة",
    "disestablishment": "الانحلال",
    "reestablishment": "إعادة التأسيس",
    "establishment": "التأسيس",
    "setting location": "موقع الأحداث",
    "invention": "الاختراع",
    "introduction": "الاستحداث",
    "formal description": "الوصف",
    "photographing": "التصوير",
    "completion": "الانتهاء",
    "opening": "الافتتاح",
})

by_data_new = {fix_keys(k): v for k, v in by_data_new.items()}


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:

    both_bot = format_multi_data(
        formatted_data=formatted_data,
        data_list=by_data_new,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        data_list2=dict(by_data_new),
        key2_placeholder="{en2}",
        value2_placeholder="{ar2}",
        text_after="",
        text_before="",
        search_first_part=False,
        use_other_formatted_data=False,
        data_to_find=data_to_find,
        regex_filter=r"[\w-]",
    )
    return both_bot


@functools.lru_cache(maxsize=10000)
def resolve_by_labels(category: str) -> str:
    # if formatted_data.get(category): return formatted_data[category]
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start resolve_by_labels: {category=}")
    both_bot = _load_bot()
    result = both_bot.search_all_category(category)
    logger.debug(f"<<yellow>> end resolve_by_labels: {category=}, {result=}")
    return result


__all__ = [
    "resolve_by_labels",
]
