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

BY_TABLE_BASED = {
    # all keys with " and "
    "by state and year": "حسب الولاية والسنة",
    "by populated place and occupation": "حسب المكان المأهول والمهنة",
    "by occupation and continent": "حسب المهنة والقارة",
    "by nation and year": "حسب الموطن والسنة",
    "by ethnic or national origin and occupation": "حسب الأصل العرقي أو الوطني والمهنة",
    "by continent and occupation": "حسب القارة والمهنة",
    "by country and city": "حسب البلد والمدينة",
    "by country and occupation": "حسب البلد والمهنة",
    "by country and war": "حسب البلد والحرب",

    # all keys with " or "
    "by university or college": "حسب الجامعة أو الكلية",
    "by territory or dependency": "حسب الإقليم أو التبعية",
    "by state or union territory": "حسب الولاية أو الإقليم الاتحادي",
    "by province or territory": "حسب المقاطعة أو الإقليم",
    "by ethnic or national origin": "حسب الأصل العرقي أو الوطني",
    "by faith or belief": "حسب الإيمان أو العقيدة",
    "by country or language": "حسب البلد أو اللغة",
    "by club or team": "حسب النادي أو الفريق",
    "by city or town": "حسب المدينة أو البلدة",
    "by division or state": "حسب المقاطعة أو الولاية",
    "by state or division": "حسب الولاية أو المقاطعة",

    # all keys with " of "
    "by year of completion": "حسب سنة الانتهاء",
    "by year of conclusion": "حسب سنة الإبرام",
    "by year of entry into force": "حسب سنة دخولها حيز التنفيذ",
    "by year of introduction": "حسب سنة الاستحداث",
    "by year of photographing": "حسب سنة التصوير",
    "by type of words": "حسب نوع الكلمات",
    "by region of area studies": "حسب منطقة الدراسات",
    "by period of setting": "حسب حقبة الأحداث",
    "by period of time": "حسب الفترة الزمنية",
    "by legislative term of office": "حسب الفترة التشريعية للمنصب",
    "by field of research": "حسب مجال البحث",
    "by decade of introduction": "حسب عقد الاستحداث",
    "by continent of production": "حسب قارة الإنتاج",
    "by country of arrest": "حسب بلد الاعتقال",
    "by country of origin": "حسب البلد الأصل",
    "by country of production": "حسب بلد الإنتاج",
    "by country of residence": "حسب بلد الإقامة",
    "by year of closing": "حسب سنة الاغلاق",
    "by decade of closing": "حسب عقد الاغلاق",
    "by century of closing": "حسب قرن الاغلاق",
    "by body of water": "حسب المسطح المائي",
    "by cause of death": "حسب سبب الوفاة",
    "by city of setting": "حسب مدينة الأحداث",
    "by country of setting": "حسب بلد الأحداث",
    "by continent of setting": "حسب قارة الأحداث",
    "by country of location": "حسب بلد الموقع",
    "by city of shooting location": "حسب مدينة موقع التصوير",
    "by city of location": "حسب مدينة الموقع",
    "by period of setting location": "حسب حقبة موقع الأحداث",
    "by continent of shooting location": "حسب قارة موقع التصوير",
    "by country of setting location": "حسب بلد موقع الأحداث",
    "by country of shooting location": "حسب بلد موقع التصوير",

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

    "by home video label": "حسب علامة الفيديو المنزلي",
    "by color process": "حسب عملية التلوين",

    "by shooting location": "حسب موقع التصوير",
    "by production location": "حسب موقع الإنتاج",
    "by commune": "حسب البلدية",
    "by academic discipline": "حسب التخصص الأكاديمي",
    "by administrative subdivisions": "حسب التقسيم الإداري",
    "by administrative unit": "حسب الوحدة الإدارية",
    "by age category": "حسب تصنيف العمر",
    "by airline": "حسب شركة الطيران",
    "by architectural style": "حسب الطراز المعماري",
    "by artist nationality": "حسب جنسية الفنان",
    "by artist": "حسب الفنان",
    "by association": "حسب الجمعية",
    "by athletic event": "حسب حدث ألعاب القوى",
    "by audience": "حسب الجمهور",
    "by autonomous community": "حسب الحكم الذاتي",
    "by award": "حسب الجائزة",
    "by basin": "حسب الحوض",
    "by belief": "حسب العقيدة",
    "by belligerent party": "حسب الطرف المحارب",
    "by borough": "حسب البلدة",
    "by branch": "حسب الفرع",
    "by brand": "حسب العلامة التجارية",
    "by builder": "حسب الباني",
    "by cemetery": "حسب المقبرة",
    "by census-designated place": "حسب المكان المخصص للتعداد",
    "by century": "حسب القرن",
    "by channel": "حسب القناة",
    "by city": "حسب المدينة",
    "by class": "حسب الصنف",
    "by closing year": "حسب سنة الاغلاق",
    "by club": "حسب النادي",
    "by color": "حسب اللون",
    "by community": "حسب المجتمع",
    "by competition won": "حسب المنافسة التي فازوا بها",
    "by competition": "حسب المنافسة",
    "by composer nationality": "حسب جنسية الملحن",
    "by composer": "حسب الملحن",
    "by congress": "حسب الكونغرس",
    "by constituency": "حسب الدائرة",
    "by continent": "حسب القارة",
    "by country invaded": "حسب البلد المغزو",
    "by country subdivision": "حسب تقسيم البلد",
    "by country subdivisions": "حسب تقسيمات البلد",
    "by country": "حسب البلد",
    "by country-of-residence": "حسب بلد الإقامة",
    "by county": "حسب المقاطعة",
    "by criminal charge": "حسب التهمة الجنائية",
    "by criminal conviction": "حسب الإدانة الجنائية",
    "by culture": "حسب الثقافة",
    "by date": "حسب التاريخ",
    "by day": "حسب اليوم",
    "by decade": "حسب العقد",
    "by defunct club": "حسب النادي السابق",
    "by defunct competition": "حسب المنافسة السابقة",
    "by department": "حسب القسم",
    "by dependent territory": "حسب الأقاليم التابعة",
    "by descent": "حسب الأصل",
    "by designer": "حسب المصمم",
    "by destination country": "حسب بلد الوجهة",
    "by destination language": "حسب اللغة المترجم إليها",
    "by destination": "حسب الوجهة",
    "by detaining country": "حسب بلد الأسر",
    "by diocese": "حسب الأبرشية",
    "by director": "حسب المخرج",
    "by document": "حسب الوثيقة",
    "by educational affiliation": "حسب الانتماء التعليمي",
    "by educational institution": "حسب الهيئة التعليمية",
    "by election": "حسب الانتخابات",
    "by era": "حسب العصر",
    "by ethnicity": "حسب المجموعة العرقية",
    "by event": "حسب الحدث",
    "by faith": "حسب الإيمان",
    "by field": "حسب المجال",
    "by first-level administrative country subdivision": "حسب تقسيمات البلدان من المستوى الأول",
    "by format": "حسب التنسيق",
    "by former country": "حسب البلد السابق",
    "by french title": "حسب العنوان الفرنسي",
    "by gender": "حسب الجنس",
    "by genre": "حسب النوع الفني",
    "by geographic setting": "حسب الموقع الجغرافي للأحداث",
    "by geographical categorization": "حسب التصنيف الجغرافي",
    "by governorate": "حسب المحافظة",
    "by hamlet": "حسب القرية",
    "by height": "حسب الارتفاع",
    "by heritage register": "حسب سجل التراث",
    "by high school": "حسب المدرسة الثانوية",
    "by host country": "حسب البلد المضيف",
    "by host": "حسب المضيف",
    "by ideology": "حسب الأيديولوجية",
    "by industry": "حسب الصناعة",
    "by instrument": "حسب الآلة",
    "by interest": "حسب الاهتمام",
    "by invading country": "حسب البلد الغازي",
    "by invention": "حسب الاختراع",
    "by island": "حسب الجزيرة",
    "by issue": "حسب القضية",
    "by jurisdiction": "حسب الاختصاص القضائي",
    "by lake": "حسب البحيرة",
    "by language family": "حسب العائلة اللغوية",
    "by language": "حسب اللغة",
    "by league representative team": "حسب فريق ممثل الدوري",
    "by lenght": "حسب الطول",
    "by length": "حسب الطول",
    "by line": "حسب الخط",
    "by livery": "حسب الكسوة",
    "by location": "حسب الموقع",
    "by manufacturer nationality": "حسب جنسية الصانع",
    "by manufacturer": "حسب الصانع",
    "by material": "حسب المادة",
    "by medium by nationality": "حسب الوسط حسب الجنسية",
    "by medium": "حسب الوسط",
    "by millennium": "حسب الألفية",
    "by mission country": "حسب بلد البعثة",
    "by month": "حسب الشهر",
    "by movement": "حسب الحركة",
    "by municipality": "حسب البلدية",
    "by museum": "حسب المتحف",
    "by music genre": "حسب نوع الموسيقى",
    "by musician": "حسب الموسيقي",
    "by name": "حسب الإسم",
    "by nation": "حسب الموطن",
    "by nationality": "حسب الجنسية",
    "by network": "حسب شبكة البث",
    "by occupation": "حسب المهنة",
    "by occupied country": "حسب البلد المحتل",
    "by occupying country": "حسب بلد الاحتلال",
    "by operator": "حسب المشغل",
    "by organizer": "حسب المنظم",
    "by parish": "حسب الأبرشية",
    "by party": "حسب الحزب",
    "by patron saint": "حسب الراعي المقدس",
    "by period": "حسب الحقبة",
    "by perpetrator": "حسب مرتكب الجريمة",
    "by person": "حسب الشخص",
    "by place": "حسب المكان",
    "by political orientation": "حسب التوجه السياسي",
    "by political party": "حسب الحزب السياسي",
    "by populated place": "حسب المكان المأهول",
    "by portfolio": "حسب الحقيبة الوزارية",
    "by position": "حسب المركز",
    "by prefecture": "حسب الولاية",
    "by presidential administration": "حسب الإدارة الرئاسية",
    "by professional league": "حسب دوري المحترفين",
    "by propellant": "حسب المادة الدافعة",
    "by province": "حسب المقاطعة",
    "by range": "حسب النطاق",
    "by receiving country": "حسب البلد المستضيف",
    "by region": "حسب المنطقة",
    "by religion": "حسب الدين",
    "by reserve team": "حسب الفريق الاحتياطي",
    "by route": "حسب الطريق",
    "by school": "حسب المدرسة",
    "by script": "حسب النص",
    "by sea": "حسب البحر",
    "by season": "حسب الموسم",
    "by sending country": "حسب البلد المرسل",
    "by series": "حسب السلسلة",
    "by shape": "حسب الشكل",
    "by source": "حسب المصدر",
    "by south korean band": "حسب الفرقة الكورية الجنوبية",
    "by specialism": "حسب النشاط",
    "by specialty": "حسب التخصص",
    "by sport": "حسب الرياضة",
    "by sports event": "حسب الحدث الرياضي",
    "by state": "حسب الولاية",
    "by strength": "حسب القوة",
    "by studio": "حسب استوديو الإنتاج",
    "by subdivision": "حسب التقسيم",
    "by subfield": "حسب الحقل الفرعي",
    "by subgenre": "حسب النوع الفرعي",
    "by subject area": "حسب مجال الموضوع",
    "by subject": "حسب الموضوع",
    "by taxon": "حسب الأصنوفة",
    "by team": "حسب الفريق",
    "by technique": "حسب التقنية",
    "by technology": "حسب التكنولوجيا",
    "by term": "حسب الفترة",
    "by theatre": "حسب المسرح",
    "by time": "حسب الوقت",
    "by topic": "حسب الموضوع",
    "by tour": "حسب البطولة",
    "by tournament": "حسب البطولة",
    "by town": "حسب البلدة",
    "by township": "حسب ضواحي المدن",
    "by track": "حسب المسار",
    "by type": "حسب الفئة",
    "by u.s. state": "حسب الولاية الأمريكية",
    "by unincorporated community": "حسب المجتمع غير المدمج",
    "by union territory": "حسب الإقليم الاتحادي",
    "by university": "حسب الجامعة",
    "by user": "حسب المستخدم",
    "by village": "حسب القرية",
    "by voice type": "حسب نوع الصوت",
    "by voivodeship": "حسب الفويفود",
    "by war": "حسب الحرب",
    "by weight class": "حسب فئة الوزن",
    "by writer nationality": "حسب جنسية الكاتب",
    "by writer": "حسب الكاتب",
    "by year": "حسب السنة",
    "by zoo name": "حسب اسم الحديقة",
    "by opening decade": "حسب عقد الافتتاح",
    "by opening year": "حسب سنة الافتتاح"
}

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
    "by blade weapons": "بالأسلحة البيضاء"
}


by_table_main = BY_TABLE_BASED | by_table_not_hasab

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
