#!/usr/bin/python3
"""
TODO: use it to replace get_by_label functions in bys.py

"""

import functools
import logging
import re

from ..helps import len_print
from ..translations_formats import MultiDataFormatterBase, format_multi_data

logger = logging.getLogger(__name__)

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


def build_yearly_category_translation():
    """Builds a dictionary of yearly category translations for competitions.

    Creates mappings between English competition category labels and their Arabic translations,
    combining competition types (e.g., girls, boys, mixed) with tournament stages (e.g., singles, doubles).

    Returns:
        dict: A dictionary mapping English category keys to Arabic translation labels.
              Example: {"by year - girls singles": "حسب السنة - فردي فتيات"}
    """
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


def fix_keys(label: str) -> str:
    """
    Normalize category keys by converting context phrases like "X of" to "X-of".

    Converts occurrences of any context field name followed by " of" into "X-of" (case-insensitive) to standardize keys for matching.

    Parameters:
        label (str): Category label to normalize.

    Returns:
        str: The normalized label.
    """

    context_keys = "|".join(CONTEXT_FIELD_LABELS.keys())
    label = re.sub(f"({context_keys}) of", r"\g<1>-of", label, flags=re.I)

    return label


@functools.lru_cache(maxsize=1)
def _load_formatted_data() -> dict[str, str]:
    """Load and return formatted data for category translations.

    Creates a dictionary of formatted category patterns with placeholders that map
    English category structures to their Arabic equivalents. This includes patterns
    for combinations of different context fields like city, date, country, etc.

    Returns:
        dict: Dictionary mapping English formatted category patterns to Arabic translations
              with placeholders for dynamic content substitution.
    """
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
    return formatted_data


@functools.lru_cache(maxsize=1)
def _load_data_to_find() -> dict[str, str]:
    """
    Builds a mapping of specific English category phrases to their Arabic translations for exact-match lookup.

    Includes age-group national team phrases, yearly competition category entries, and various domain-specific "by ..." phrases (including sensitive/violent terms) that should be matched exactly rather than by pattern.

    Returns:
        dict[str, str]: Mapping from English category phrase to Arabic translation.
    """
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
        "by women's under-23 national team": "حسب المنتخب الوطني للسيدات تحت 23 سنة",
    }

    data_to_find = {
        "by women's national team": "حسب المنتخب الوطني للسيدات",
        "by women's youth national team": "حسب المنتخب الوطني للناشئات",
        "by women's under-23 national team": "حسب المنتخب الوطني للسيدات تحت 23 سنة",
        "by women's under-21 national team": "حسب المنتخب الوطني للسيدات تحت 21 سنة",
        "by women's under-20 national team": "حسب المنتخب الوطني للسيدات تحت 20 سنة",
        "by women's under-17 national team": "حسب المنتخب الوطني للسيدات تحت 17 سنة",
        "by national amateur team": "حسب المنتخب الوطني للهواة",
        "by national men's amateur team": "حسب المنتخب الوطني للهواة للرجال",
        "by national men's team": "حسب منتخب الرجال الوطني",
        "by national team": "حسب المنتخب الوطني",
        "by men's a' national team": "حسب منتخب المحليين",
        "by men's b national team": "حسب المنتخب الرديف",
        "by men's amateur national team": "حسب المنتخب الوطني للهواة للرجال",
        "by amateur national team": "حسب المنتخب الوطني للهواة",
        "by women's amateur national team": "حسب المنتخب الوطني للهواة للسيدات",
        "by youth national team": "حسب المنتخب الوطني للشباب",
        "by national women's amateur team": "حسب المنتخب الوطني للهواة للسيدات",
        "by national women's team": "حسب منتخب السيدات الوطني",
        "by national youth team": "حسب المنتخب الوطني للشباب",
        "by nationality, genre and instrument": "حسب الجنسية والنوع والآلة",
        "by instrument, genre and nationality": "حسب الآلة والنوع الفني والجنسية",
        "by genre, nationality and instrument": "حسب النوع الفني والجنسية والآلة",
    }

    data_to_find.update(build_yearly_category_translation())
    data_to_find.update(by_keys_under)

    by_table_not_hasab = {
        "by airstrike": "بضربات جوية",
        "by airstrikes": "بضربات جوية",
        "by alexander phimister proctor": "بواسطة الكسندر فيميستر بروكتور",
        "by violence": "بسبب العنف",
        "by suicide bomber": "بتفجير انتحاري",
        "by stabbing": "بالطعن",
        "by projectile weapons": "بسلاح القذائف",
        "by organized crime": "بواسطة الجريمة المنظمة",
        "by law enforcement officers": "بواسطة ضباط إنفاذ القانون",
        "by law enforcement": "بواسطة إنفاذ القانون",
        "by improvised explosive device": "بعبوة ناسفة بدائية الصنع",
        "by guillotine": "بالمقصلة",
        "by hanging": "بالشنق",
        "by firearm": "بسلاح ناري",
        "by firing squad": "رميا بالرصاص",
        "by explosive device": "بعبوة ناسفة",
        "by decapitation": "بقطع الرأس",
        "by covid-19 pandemic": "بجائحة فيروس كورونا",
        "by burning": "بالحرق",
        "by blade weapons": "بالأسلحة البيضاء",
    }
    data_to_find.update(by_table_not_hasab)

    return data_to_find


data_to_find = _load_data_to_find()


@functools.lru_cache(maxsize=1)
def _load_by_data_new() -> dict[str, str]:
    """
    Load a comprehensive mapping of English category keys used with "by" to their Arabic translations.

    The returned mapping covers many domains (locations, occupations, institutions, sports, weapons, events, etc.) and has its keys normalized through fix_keys before being returned.

    Returns:
        dict[str, str]: Mapping of normalized English category keys to their Arabic translation strings.
    """
    _to_review = {
        "guillotine": "بالمقصلة",
        "hanging": "بالشنق",
        "burning": "بالحرق",
        "stabbing": "بالطعن",
        "blade weapons": "بالأسلحة البيضاء",
    }
    by_data_new = {
        "country of origin": "البلد الأصل",
        "year of entry into force": "سنة دخولها حيز التنفيذ",
        "home video label": "علامة الفيديو المنزلي",
        "color process": "عملية التلوين",
        "ethnic or national origin": "الأصل العرقي أو الوطني",
        "origin": "الأصل",
        "arrest": "الاعتقال",
        "university": "الجامعة",
        "college": "الكلية",
        "dependency": "التبعية",
        "state": "الولاية",
        "division": "المقاطعة",
        "union territory": "الإقليم الاتحادي",
        "province": "المقاطعة",
        "county": "المقاطعة",
        "territory": "الإقليم",
        "academic discipline": "التخصص الأكاديمي",
        "administrative subdivisions": "التقسيم الإداري",
        "administrative unit": "الوحدة الإدارية",
        "age category": "تصنيف العمر",
        "airline": "شركة الطيران",
        "alexander phimister proctor": "بواسطة الكسندر فيميستر بروكتور",
        "amateur national team": "المنتخب الوطني للهواة",
        "architectural style": "الطراز المعماري",
        "artist nationality": "جنسية الفنان",
        "artist": "الفنان",
        "association": "الجمعية",
        "athletic event": "حدث ألعاب القوى",
        "audience": "الجمهور",
        "autonomous community": "الحكم الذاتي",
        "award": "الجائزة",
        "band": "الفرقة",
        "bank": "البنك",
        "basin": "الحوض",
        "behavior": "السلوك",
        "belief": "العقيدة",
        "belligerent party": "الطرف المحارب",
        "body of water": "المسطح المائي",
        "borough": "البلدة",
        "branch": "الفرع",
        "brand": "العلامة التجارية",
        "builder": "الباني",
        "cause of death": "سبب الوفاة",
        "cemetery": "المقبرة",
        "census-designated place": "المكان المخصص للتعداد",
        "century": "القرن",
        "channel": "القناة",
        "city": "المدينة",
        "class": "الصنف",
        "closing year": "سنة الاغلاق",
        "closing": "الاغلاق",
        "club": "النادي",
        "color": "اللون",
        "commune": "البلدية",
        "community": "المجتمع",
        "conclusion": "الإبرام",
        "company": "الشركة",
        "competition won": "المنافسة التي فازوا بها",
        "competition": "المنافسة",
        "completion": "الانتهاء",
        "composer nationality": "جنسية الملحن",
        "composer": "الملحن",
        "condition": "الحالة",
        "conflict": "النزاع",
        "congress": "الكونغرس",
        "constituency": "الدائرة",
        "continent": "القارة",
        "country invaded": "البلد المغزو",
        "country of residence": "بلد الإقامة",
        "country subdivision": "تقسيم البلد",
        "country subdivisions": "تقسيمات البلد",
        "country": "البلد",
        "country-of residence": "بلد الإقامة",
        "country-of-residence": "بلد الإقامة",
        "covid-19 pandemic": "بجائحة فيروس كورونا",
        "criminal charge": "التهمة الجنائية",
        "criminal conviction": "الإدانة الجنائية",
        "culture": "الثقافة",
        "date": "التاريخ",
        "day": "اليوم",
        "decade": "العقد",
        "decapitation": "بقطع الرأس",
        "defunct club": "النادي السابق",
        "defunct competition": "المنافسة السابقة",
        "department": "القسم",
        "dependent territory": "الأقاليم التابعة",
        "descent": "الأصل",
        "designer": "المصمم",
        "destination country": "بلد الوجهة",
        "destination language": "اللغة المترجم إليها",
        "destination": "الوجهة",
        "detaining country": "بلد الأسر",
        "developer": "التطوير",
        "diocese": "الأبرشية",
        "director": "المخرج",
        "disestablishment": "الانحلال",
        "document": "الوثيقة",
        "educational affiliation": "الانتماء التعليمي",
        "educational establishment": "المؤسسة التعليمية",
        "educational institution": "الهيئة التعليمية",
        "election": "الانتخابات",
        "era": "العصر",
        "establishment": "التأسيس",
        "ethnicity": "المجموعة العرقية",
        "event": "الحدث",
        "explosive device": "بعبوة ناسفة",
        "faith": "الإيمان",
        "field of research": "مجال البحث",
        "field": "المجال",
        "firearm": "بسلاح ناري",
        "firing squad": "رميا بالرصاص",
        "first-level administrative country subdivision": "تقسيمات البلدان من المستوى الأول",
        "formal description": "الوصف",
        "format": "التنسيق",
        "former country": "البلد السابق",
        "former religion": "الدين السابق",
        "french title": "العنوان الفرنسي",
        "gender": "الجنس",
        "genre": "النوع الفني",
        "geographic setting": "الموقع الجغرافي للأحداث",
        "geographical categorization": "التصنيف الجغرافي",
        "government agency": "الوكالة الحكومية",
        "governorate": "المحافظة",
        "hamlet": "القرية",
        "height": "الارتفاع",
        "heritage register": "سجل التراث",
        "high school": "المدرسة الثانوية",
        "history of colleges and universities": "تاريخ الكليات والجامعات",
        "host country": "البلد المضيف",
        "host": "المضيف",
        "ideology": "الأيديولوجية",
        "importance": "الأهمية",
        "improvised explosive device": "بعبوة ناسفة بدائية الصنع",
        "industry": "الصناعة",
        "instrument": "الآلة",
        "interest": "الاهتمام",
        "introduction": "الاستحداث",
        "invading country": "البلد الغازي",
        "invention": "الاختراع",
        "island": "الجزيرة",
        "issue": "القضية",
        "jurisdiction": "الاختصاص القضائي",
        "lake": "البحيرة",
        "language family": "العائلة اللغوية",
        "language": "اللغة",
        "law enforcement officers": "بواسطة ضباط إنفاذ القانون",
        "law enforcement": "بواسطة إنفاذ القانون",
        "league representative team": "فريق ممثل الدوري",
        "league": "الدوري",
        "legislative term of office": "الفترة التشريعية للمنصب",
        "lenght": "الطول",
        "length": "الطول",
        "line": "الخط",
        "livery": "الكسوة",
        "location": "الموقع",
        "magazine": "المجلة",
        "manufacturer nationality": "جنسية الصانع",
        "manufacturer": "الصانع",
        "material": "المادة",
        "medium": "الوسط",
        "millennium": "الألفية",
        "mission country": "بلد البعثة",
        "month": "الشهر",
        "movement": "الحركة",
        "municipality": "البلدية",
        "museum": "المتحف",
        "music genre": "نوع الموسيقى",
        "musician": "الموسيقي",
        "name": "الإسم",
        "nation": "الموطن",
        "nationality": "الجنسية",
        "network": "شبكة البث",
        "newspaper": "الصحيفة",
        "non-profit organizations": "المنظمات غير الربحية",
        "non-profit publishers": "ناشرون غير ربحيون",
        "nonprofit organization": "المنظمات غير الربحية",
        "occupation": "المهنة",
        "occupied country": "البلد المحتل",
        "occupying country": "بلد الاحتلال",
        "opening decade": "عقد الافتتاح",
        "opening year": "سنة الافتتاح",
        "opening": "الافتتاح",
        "operator": "المشغل",
        "organization": "المنظمة",
        "organized crime": "بواسطة الجريمة المنظمة",
        "organizer": "المنظم",
        "orientation": "التوجه",
        "parish": "الأبرشية",
        "party": "الحزب",
        "patron saint": "الراعي المقدس",
        "period of setting location": "حقبة موقع الأحداث",
        "period of setting": "حقبة الأحداث",
        "period of time": "الفترة الزمنية",
        "period": "الحقبة",
        "perpetrator": "مرتكب الجريمة",
        "person": "الشخص",
        "photographing": "التصوير",
        "place": "المكان",
        "political orientation": "التوجه السياسي",
        "political party": "الحزب السياسي",
        "populated place": "المكان المأهول",
        "portfolio": "الحقيبة الوزارية",
        "position": "المركز",
        "prefecture": "الولاية",
        "presidential administration": "الإدارة الرئاسية",
        "prison": "السجن",
        "producer": "المنتج",
        "production": "الإنتاج",
        "production location": "موقع الإنتاج",
        "professional association": "الجمعيات المهنية",
        "professional league": "دوري المحترفين",
        "projectile weapons": "بسلاح القذائف",
        "propellant": "المادة الدافعة",
        "publication": "المؤسسة",
        "quality": "الجودة",
        "range": "النطاق",
        "rank": "الرتبة",
        "receiving country": "البلد المستضيف",
        "record label": "شركة التسجيلات",
        "reestablishment": "إعادة التأسيس",
        "region of area studies": "منطقة الدراسات",
        "region": "المنطقة",
        "religion": "الدين",
        "research organization": "منظمة البحوث",
        "reserve team": "الفريق الاحتياطي",
        "role": "الدور",
        "route": "الطريق",
        "school": "المدرسة",
        "script": "النص",
        "sea": "البحر",
        "season": "الموسم",
        "sector": "القطاع",
        "sending country": "البلد المرسل",
        "seniority": "الأقدمية",
        "series": "السلسلة",
        "setting location": "موقع الأحداث",
        "setting": "الأحداث",
        "shape": "الشكل",
        "shipbuilding company": "شركة بناء السفن",
        "shooting location": "موقع التصوير",
        "software": "البرمجيات",
        "source": "المصدر",
        "south korean band": "الفرقة الكورية الجنوبية",
        "specialism": "النشاط",
        "specialty": "التخصص",
        "sport": "الرياضة",
        "sports event": "الحدث الرياضي",
        "station": "المحطة",
        "status": "الحالة",
        "strength": "القوة",
        "studio": "استوديو الإنتاج",
        "subdivision": "التقسيم",
        "subfield": "الحقل الفرعي",
        "subgenre": "النوع الفرعي",
        "subject area": "مجال الموضوع",
        "subject": "الموضوع",
        "suicide bomber": "بتفجير انتحاري",
        "taxon": "الأصنوفة",
        "team": "الفريق",
        "technique": "التقنية",  # not تقانة
        "technology": "التقانة",  # التكنولوجيا
        "term": "الفترة",
        "theatre": "المسرح",
        "time": "الوقت",
        "topic": "الموضوع",
        "tour": "البطولة",
        "tournament": "البطولة",
        "town": "البلدة",
        "township": "ضواحي المدن",
        "track": "المسار",
        "trade union": "النقابات العمالية",
        "type of words": "نوع الكلمات",
        "type": "الفئة",
        "u.s. state": "الولاية الأمريكية",
        "unincorporated community": "المجتمع غير المدمج",
        "user": "المستخدم",
        "village": "القرية",
        "violence": "بسبب العنف",
        "voice type": "نوع الصوت",
        "voivodeship": "الفويفود",
        "war": "الحرب",
        "weight class": "فئة الوزن",
        "writer nationality": "جنسية الكاتب",
        "writer": "الكاتب",
        "year": "السنة",
        "youth national team": "المنتخب الوطني للشباب",
        "zoo name": "اسم الحديقة",
    }

    # by_data_new.update({x: v for x, v in CONTEXT_FIELD_LABELS.items() if x not in by_data_new})

    by_data_new = {fix_keys(k): v for k, v in by_data_new.items()}

    return by_data_new


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    """Load and configure the category translation bot.

    Creates and configures a MultiDataFormatterBase instance that handles
    the translation of category names using formatted data and lookup tables.

    Returns:
        MultiDataFormatterBase: Configured bot instance for category translation.
    """
    formatted_data = _load_formatted_data()
    by_data_new = _load_by_data_new()

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
    """Resolve a category label to its Arabic translation.

    Attempts to find an Arabic translation for the given English category name.
    First checks for direct matches in the data_to_find dictionary, then uses
    the translation bot to process more complex category patterns.

    Args:
        category (str): The English category name to be translated.

    Returns:
        str: The Arabic translation of the category, or an empty string if not found.
    """
    # if formatted_data.get(category): return formatted_data[category]
    normalized_category = fix_keys(category)
    label = data_to_find.get(category) or data_to_find.get(normalized_category)
    if label:
        return label

    logger.debug(f"<<yellow>> start {normalized_category=}")
    both_bot = _load_bot()
    result = both_bot.search_all_category(normalized_category)
    logger.info(f"<<yellow>> end {normalized_category=}, {result=}")
    return result


len_print.data_len(
    "bys_new.py",
    {
        "bys_new_data_to_find": data_to_find,
        "bys_new_formatted_data": _load_formatted_data(),
        "bys_new_by_data_new": _load_by_data_new(),
    },
)

__all__ = [
    "resolve_by_labels",
]
