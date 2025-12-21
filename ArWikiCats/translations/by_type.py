#!/usr/bin/python3
""" """
import functools
from ..helps import len_print, dump_data
from .utils.json_dir import open_json_file


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

    _by_table_year = {}

    for category_key, category_label in COMPETITION_CATEGORY_LABELS.items():
        for stage_key, stage_label in TOURNAMENT_STAGE_LABELS.items():
            by_entry_key = f"by year - {category_key} {stage_key}"
            translation_label = f"حسب السنة - {stage_label} {category_label}"
            _by_table_year[by_entry_key] = translation_label
    # ---
    return _by_table_year


PRIMARY_BY_COMPONENTS = {
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
    "non-profit organizations": "المنظمات غير الربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "nonprofit organization": "المنظمات غير الربحية",
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
    "by nationality and instrument ": "حسب الجنسية والآلة",
    "by century and instrument": "حسب القرن والآلة",
    "by medium": "حسب الوسط",
    "by name": "حسب الإسم",
    "by voice type": "حسب نوع الصوت",
    "by language": "حسب اللغة",
    "by nationality": "حسب الجنسية",
}

BY_TABLE_BASED = open_json_file("keys/By_table.json") or {}

by_table_main = dict(BY_TABLE_BASED)

_by_of_fields = {}
_by_map_table = {}
_by_and_fields = {}
_by_or_fields = {}
_by_by_fields = {}
_by_music_labels = {}

_by_under_keys = {
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

TOURNAMENT_STAGE_LABELS = {
    "tournament": "مسابقة",
    "singles": "فردي",
    "qualification": "تصفيات",
    "team": "فريق",
    "doubles": "زوجي",
}

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


for context_key, context_label in CONTEXT_FIELD_LABELS.items():
    _by_of_fields.update({
        f"by {context_key} of shooting location": f"حسب {context_label} موقع التصوير",
        f"by {context_key} of developer": f"حسب {context_label} التطوير",
        f"by {context_key} of location": f"حسب {context_label} الموقع",
        f"by {context_key} of setting": f"حسب {context_label} الأحداث",
        f"by {context_key} of disestablishment": f"حسب {context_label} الانحلال",
        f"by {context_key} of reestablishment": f"حسب {context_label} إعادة التأسيس",
        f"by {context_key} of establishment": f"حسب {context_label} التأسيس",
        f"by {context_key} of setting location": f"حسب {context_label} موقع الأحداث",
        f"by {context_key} of invention": f"حسب {context_label} الاختراع",
        f"by {context_key} of introduction": f"حسب {context_label} الاستحداث",
        f"by {context_key} of formal description": f"حسب {context_label} الوصف",
        f"by {context_key} of photographing": f"حسب {context_label} التصوير",
        # f"by photographing {context_key} ": f"حسب {context_label} التصوير",
        f"by {context_key} of completion": f"حسب {context_label} الانتهاء",
    })

for component_key, component_label in PRIMARY_BY_COMPONENTS.items():
    _by_map_table[f"by {component_key}"] = f"حسب {component_label}"

    for secondary_key, secondary_label in PRIMARY_BY_COMPONENTS.items():
        if component_key != secondary_key:

            combined_key = f"by {component_key} and {secondary_key}"
            combined_label = f"حسب {component_label} و{secondary_label}"
            _by_and_fields[combined_key] = combined_label

            either_key = f"by {component_key} or {secondary_key}"
            either_label = f"حسب {component_label} أو {secondary_label}"
            _by_or_fields[either_key] = either_label

            chained_key = f"by {component_key} by {secondary_key}"
            chained_label = f"حسب {component_label} حسب {secondary_label}"
            _by_by_fields[chained_key] = chained_label

ADDITIONAL_BY_COMPONENTS = {
    "composer": "الملحن",
    "composer nationality": "جنسية الملحن",
    "artist": "الفنان",
    "artist nationality": "جنسية الفنان",
    "manufacturer": "الصانع",
    "manufacturer nationality": "جنسية الصانع",
}

for component_key, component_label in ADDITIONAL_BY_COMPONENTS.items():
    _by_music_labels[f"by {component_key}"] = f"حسب {component_label}"
    _by_music_labels[f"by genre and {component_key}"] = f"حسب النوع الفني و{component_label}"

_by_table_year = build_yearly_category_translation()

by_table_main.update(_by_under_keys)
by_table_main.update(_by_table_year)
by_table_main.update(_by_of_fields)
by_table_main.update(_by_map_table)
by_table_main.update(_by_and_fields)
by_table_main.update(_by_or_fields)
by_table_main.update(_by_by_fields)
by_table_main.update(_by_music_labels)
by_table_main.update(_by_music_table_base)

by_orginal2 = {
    entry.replace("by ", "", 1).lower(): by_table_main[entry].replace("حسب ", "", 1) for entry in by_table_main
}


def by_table_main_get(by_section):
    return (
        by_table_main.get(by_section, "") or
        ""
    )


def by_table_get(by_section):
    return (
        by_table_main.get(by_section, "") or
        by_orginal2.get(by_section, "") or
        ""
    )


len_print.data_len("by_table.py", {
    "by_table_main": by_table_main,
    "by_orginal2": by_orginal2,
    "_by_table_year": _by_table_year,
    "_by_of_fields": _by_of_fields,
    "_by_and_fields": _by_and_fields,
    "_by_or_fields": _by_or_fields,
    "_by_by_fields": _by_by_fields,
    "_by_music_labels": _by_music_labels,
    "_by_music_table_base": _by_music_table_base,
    "_by_under_keys": _by_under_keys,
})

__all__ = [
    "by_table_main_get",
    "by_table_get",
]
