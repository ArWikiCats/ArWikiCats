#!/usr/bin/python3
""" """
from ..helps import len_print
from .utils.json_dir import open_json_file

By_table = {}
# ---
By_table = open_json_file("By_table") or {}
# ---
Music_By_table = {
    "by city": "حسب المدينة",
    "by seniority": "حسب الأقدمية",
    "by producer": "حسب المنتج",
    "by software": "حسب البرمجيات",
    "by band": "حسب الفرقة",
    "by medium by nationality": "حسب الوسط حسب الجنسية",
    "by instrument": "حسب الآلة",
    "by instrument, genre and nationality": "حسب الآلة والنوع والجنسية",
    "by genre, nationality and instrument": "حسب النوع والجنسية والآلة",
    "by nationality, genre and instrument": "حسب الجنسية والنوع والآلة",
    "by instrument and nationality": "حسب الآلة والجنسية",
    "by instrument and genre": "حسب الآلة والنوع",
    "by genre and instrument": "حسب النوع والآلة",
    "by nationality and instrument ": "حسب الجنسية والآلة الموسيقية",
    "by century and instrument": "حسب القرن والآلة",
    "by medium": "حسب الوسط",
    "by name": "حسب الإسم",
    "by voice type": "حسب نوع الصوت",
    "by language": "حسب اللغة",
    "by nationality": "حسب الجنسية",
}
# ---

for year in [16, 17, 18, 19, 20, 21, 23]:
    # By_table["by under-%d national team" % year] = "المنتخب الوطني تحت %d سنة"  % year
    By_table[f"by under-{year} national team"] = f"حسب المنتخب الوطني تحت {year} سنة"
    By_table[f"by men's under-{year} national team"] = f"حسب المنتخب الوطني للرجال تحت {year} سنة"
    By_table[f"by women's under-{year} national team"] = f"حسب المنتخب الوطني للسيدات تحت {year} سنة"
# ---
by_table_entries = {by_key: By_table[by_key] for by_key in By_table}
by_Only = by_table_entries
# ---
TOURNAMENT_STAGE_LABELS = {
    "tournament": "مسابقة",
    "singles": "فردي",
    "qualification": "تصفيات",
    "team": "فريق",
    "doubles": "زوجي",
}
# ---
COMPETITION_CATEGORY_LABELS = {
    "girls": "فتيات",
    "mixed": "مختلط",
    "boys": "فتيان",
    "singles": "فردي",
    "womens": "سيدات",
    "ladies": "سيدات",
    "mens": "رجال",
    "men's": "رجال",
}
# ---
for category_key, category_label in COMPETITION_CATEGORY_LABELS.items():
    for stage_key, stage_label in TOURNAMENT_STAGE_LABELS.items():
        by_entry_key = f"by year - {category_key} {stage_key}"
        translation_label = f"حسب السنة - {stage_label} {category_label}"
        By_table[by_entry_key] = translation_label
        # By_table[ "by year – %s %s" % (start , suff ) ] = "حسب السنة – %s %s" % (TOURNAMENT_STAGE_LABELS[suff] , COMPETITION_CATEGORY_LABELS[start])
        # printe.output('%s=[%s]' % (ke , lab_ke) )
# ---
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
    By_table[f"by {context_key} of shooting location"] = f"حسب {context_label} التصوير"
    By_table[f"by {context_key} of developer"] = f"حسب {context_label} التطوير"
    By_table[f"by {context_key} of location"] = f"حسب {context_label} الموقع"
    By_table[f"by {context_key} of setting"] = f"حسب {context_label} الأحداث"
    By_table[f"by {context_key} of disestablishment"] = f"حسب {context_label} الانحلال"
    By_table[f"by {context_key} of reestablishment"] = f"حسب {context_label} إعادة التأسيس"
    By_table[f"by {context_key} of establishment"] = f"حسب {context_label} التأسيس"
    By_table[f"by {context_key} of setting location"] = f"حسب {context_label} موقع الأحداث"
    By_table[f"by {context_key} of invention"] = f"حسب {context_label} الاختراع"
    By_table[f"by {context_key} of introduction"] = f"حسب {context_label} الاستحداث"
    By_table[f"by {context_key} of formal description"] = f"حسب {context_label} الوصف"
    By_table[f"by {context_key} of photographing"] = f"حسب {context_label} التصوير"
    By_table[f"by photographing {context_key} "] = f"حسب {context_label} التصوير"

    By_table[f"by {context_key} of completion"] = f"حسب {context_label} الانتهاء"

    By_table[f"by {context_key} of opening"] = f"حسب {context_label} الافتتاح"
    By_table[f"by opening {context_key} "] = f"حسب {context_label} الافتتاح"
PRIMARY_BY_COMPONENTS = {
    "city": "المدينة",
    "rank": "الرتبة",
    "non-profit organizations": "المؤسسات غير الربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "nonprofit organization": "المؤسسات غير الربحية",
    "series": "السلسلة",
    "sport": "الرياضة",
    "importance": "الأهمية",
    "league": "الدوري",
    "quality": "الجودة",
    "industry": "الصناعة",
    "sector": "القطاع",
    "conflict": "النزاع",
    "role": "الدور",
    "issue": "القضية",
    "organizer": "المنظم",
    "history of colleges and universities": "تاريخ الكليات والجامعات",
    "subdivision": "التقسيم",
    "country subdivision": "تقسيم البلد",
    "country subdivisions": "تقسيمات البلد",
    "county": "المقاطعة",
    "region": "المنطقة",
    "territory": "الإقليم",
    "behavior": "السلوك",
    "event": "الحدث",
    "competition": "المنافسة",
    "political orientation": "التوجه السياسي",
    "orientation": "التوجه",
    "branch": "الطائفة",
    "class": "الصنف",
    "prison": "السجن",
    "former religion": "الدين السابق",
    "religion": "الدين",
    "ethnicity": "المجموعة العرقية",
    "country": "البلد",
    "writer": "الكاتب",
    "record label": "شركة التسجيلات",
    "publication": "المؤسسة",
    "team": "الفريق",
    "club": "النادي",
    "government agency": "الوكالة الحكومية",
    "status": "الحالة",
    "condition": "الحالة",
    "bank": "البنك",
    "occupation": "المهنة",
    "magazine": "المجلة",
    "newspaper": "الصحيفة",
    "station": "المحطة",
    "shipbuilding company": "شركة بناء السفن",
    "company": "الشركة",
    "organization": "المنظمة",
    "continent": "القارة",
    "specialty": "التخصص",
    "medium": "الوسط",
    "educational institution": "الهيئة التعليمية",
    "educational establishment": "المؤسسات التعليمية",
    "research organization": "منظمة البحوث",
    "trade union": "النقابات العمالية",
    "professional association": "الجمعيات المهنية",
    "instrument": "الآلة",
    "type": "الفئة",
    "genre": "النوع الفني",
    "nationality": "الجنسية",
    "country-of-residence": "بلد الإقامة",
    "country of residence": "بلد الإقامة",
    "nation": "الموطن",
    "century": "القرن",
    "decade": "العقد",
    "year": "السنة",
    "millennium": "الألفية",
    "state": "الولاية",
    "party": "الحزب",
}
for component_key, component_label in PRIMARY_BY_COMPONENTS.items():
    by_table_entries[f"by {component_key}"] = f"حسب {component_label}"
    By_table[f"by {component_key}"] = f"حسب {component_label}"
    # print("{} : {}".format("by {}".format(component_key), "حسب {}".format(component_label)))
    for secondary_key, secondary_label in PRIMARY_BY_COMPONENTS.items():
        if component_key != secondary_key:
            combined_key = f"by {component_key} and {secondary_key}"
            combined_label = f"حسب {component_label} و{secondary_label}"
            By_table[combined_key] = combined_label
            # print("{} : {}".format(by_by , ar_ar))
            either_key = f"by {component_key} or {secondary_key}"
            either_label = f"حسب {component_label} أو {secondary_label}"
            By_table[either_key] = either_label
            # print("{} : {}".format(by_by , ar_ar))
            chained_key = f"by {component_key} by {secondary_key}"
            chained_label = f"حسب {component_label} حسب {secondary_label}"
            By_table[chained_key] = chained_label
# ---
ADDITIONAL_BY_COMPONENTS = {
    "composer": "الملحن",
    "composer nationality": "جنسية الملحن",
    "artist": "الفنان",
    "artist nationality": "جنسية الفنان",
    "manufacturer": "الصانع",
    "manufacturer nationality": "جنسية الصانع",
}
# ---
for component_key, component_label in ADDITIONAL_BY_COMPONENTS.items():
    By_table[f"by {component_key}"] = f"حسب {component_label}"
    By_table[f"by genre and {component_key}"] = f"حسب النوع الفني و{component_label}"
# ---
for by, value in Music_By_table.items():  #
    if value:  # and not by.lower() in By_table :
        By_table[by.lower()] = value
# ---
By_table_orginal = By_table

By_orginal2 = {entry.replace("by ", "", 1).lower(): By_table_orginal[entry].replace("حسب ", "", 1) for entry in By_table_orginal}

len_print.data_len("by_table.py", {"by_table": By_table})
