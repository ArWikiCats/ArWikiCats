"""Translation helpers for United States counties, states, and parties."""

from __future__ import annotations

from ..translations_formats.format_data import FormatData

US_STATES = {
    "alabama": "ألاباما",
    "alaska": "ألاسكا",
    "arizona": "أريزونا",
    "arkansas": "أركنساس",
    "california": "كاليفورنيا",
    "colorado": "كولورادو",
    "connecticut": "كونيتيكت",
    "delaware": "ديلاوير",
    "florida": "فلوريدا",
    "georgia (u.s. state)": "ولاية جورجيا",
    "georgia": "جورجيا",
    "hawaii": "هاواي",
    "idaho": "أيداهو",
    "illinois": "إلينوي",
    "indiana": "إنديانا",
    "iowa": "آيوا",
    "kansas": "كانساس",
    "kentucky": "كنتاكي",
    "louisiana": "لويزيانا",
    "maine": "مين",
    "maryland": "ماريلند",
    "massachusetts": "ماساتشوستس",
    "michigan": "ميشيغان",
    "minnesota": "منيسوتا",
    "mississippi": "مسيسيبي",
    "missouri": "ميزوري",
    "montana": "مونتانا",
    "nebraska": "نبراسكا",
    "nevada": "نيفادا",
    "new hampshire": "نيوهامشير",
    "new jersey": "نيوجيرسي",
    "new mexico": "نيومكسيكو",
    "new york (state)": "ولاية نيويورك",
    "new york": "نيويورك",
    "north carolina": "كارولاينا الشمالية",
    "north dakota": "داكوتا الشمالية",
    "ohio": "أوهايو",
    "oklahoma": "أوكلاهوما",
    "oregon": "أوريغون",
    "pennsylvania": "بنسلفانيا",
    "rhode island": "رود آيلاند",
    "south carolina": "كارولاينا الجنوبية",
    "south dakota": "داكوتا الجنوبية",
    "tennessee": "تينيسي",
    "texas": "تكساس",
    "utah": "يوتا",
    "vermont": "فيرمونت",
    "virginia": "فرجينيا",
    "washington (state)": "ولاية واشنطن",
    "washington": "واشنطن",
    "washington, d.c.": "واشنطن العاصمة",
    "west virginia": "فيرجينيا الغربية",
    "wisconsin": "ويسكونسن",
    "wyoming": "وايومنغ",
}

_STATE_SUFFIX_TEMPLATES_BASE = {
    "{en} in the War of 1812": "{ar} في حرب 1812",
    "{en} senate": "مجلس شيوخ ولاية {ar}",
    "{en} house-of-representatives elections": "انتخابات مجلس نواب ولاية {ar}",
    "{en} house-of-representatives": "مجلس نواب ولاية {ar}",
    "{en} house of representatives": "مجلس نواب ولاية {ar}",
    "{en} state politics": "سياسة ولاية {ar}",
    "{en} state attorneys general": "مدعي ولاية {ar} العام",
    "{en} attorneys general": "مدعي {ar} العام",
    "{en} gubernatorial elections": "انتخابات حاكم {ar}",
    "{en} politics": "سياسة {ar}",
    "{en} state senators": "أعضاء مجلس شيوخ ولاية {ar}",
    "{en} senators": "أعضاء مجلس شيوخ ولاية {ar}",
    # " ballot measures":"استفتاءات عامة {ar}",
    "{en} ballot measures": "إجراءات اقتراع {ar}",
    "{en} ballot propositions": "اقتراحات اقتراع {ar}",
    "{en} referendums": "استفتاءات {ar}",
    "{en} territory": "إقليم {ar}",
    "{en} territory officials": "مسؤولو إقليم {ar}",
    "{en} territory judges": "قضاة إقليم {ar}",
    "{en} law": "قانون {ar}",
    "{en} city councils": "مجالس مدن {ar}",
    # " councils" : "مجالس {ar}",
    "{en} state courts": "محكمة ولاية {ar}",
    "{en} state court judges": "قضاة محكمة ولاية {ar}",
    "{en} court judges": "قضاة محكمة {ar}",
    "{en} court of appeals": "محكمة استئناف {ar}",
    "{en} court of appeals judges‎": "قضاة محكمة استئناف {ar}",
    "{en} appellate court judges": "قضاة محكمة استئناف {ar}",
    "{en} state superior court judges": "قضاة محكمة ولاية {ar} العليا",
    "{en} superior court judges": "قضاة محكمة {ar} العليا",
    "{en} supreme court justices": "قضاة محكمة {ar} العليا",
    "{en} supreme court": "محكمة {ar} العليا",
    "{en} state legislature": "هيئة ولاية {ar} التشريعية",
    "{en} territorial legislature": "هيئة {ar} التشريعية الإقليمية",
    "{en} legislature": "هيئة {ar} التشريعية",
    "{en} legislative assembly": "هيئة {ar} التشريعية",
    "{en} general assembly": "جمعية {ar} العامة",
    "{en} state assembly": "جمعية ولاية {ar}",
    "{en} board of health": "مجلس الصحة في ولاية {ar}",
    "{en} board of education": "مجلس التعليم في ولاية {ar}",
    "{en} local politicians": "سياسيون محليون في {ar}",
    "{en} politicians": "سياسيو {ar}",
    "{en} sheriffs": "مأمورو {ar}",
    "{en} lawyers": "محامون من ولاية {ar}",
    "{en} republicans": "جمهوريون من ولاية {ar}",
    "{en} democrats": "ديمقراطيون من ولاية {ar}",
    "{en} independents": "مستقلون من ولاية {ar}",
}

_USA_PARTY_LABELS = {
    "democratic republican": "الحزب الديمقراطي الجمهوري",
    "democratic-republican": "الحزب الديمقراطي الجمهوري",
    "democratic-republican party": "الحزب الديمقراطي الجمهوري",
    "anti-Administration party": "حزب معاداة الإدارة",
    "anti Administration party": "حزب معاداة الإدارة",
    "Pro Administration Party": "حزب دعم الإدارة",
    "Pro-Administration Party": "حزب دعم الإدارة",
    "Anti-Monopoly Party": "حزب مكافحة الاحتكار",
    "Free Soil Party": "حزب التربة الحرة",
    "Liberty Party (1840)": "حزب الحرية 1840",
    "Opposition Party": "أوبوسيشن بارتي",
    "Readjuster Party": "ريدجوستر بارتي",
    "Silver Republican Party": "الحزب الجمهوري الفضي",
    "conditional Union Party": "حزب الاتحاد المشروط",
    "Unconditional Union Party": "حزب الاتحاد غير المشروط",
    "Asian-American": "",
    "Censured or reprimanded": "",
    # 'Expelled' : 'مطرودون' ,
    "Independent": "",
    "Jewish": "",
    "Nonpartisan League": "",
    "democratic party": "الحزب الديمقراطي",
    "republican party": "الحزب الجمهوري",
    "whig party": "حزب اليمين",
    "National Republican Party": "الحزب الجمهوري الوطني",
    "National Republican": "الحزب الجمهوري الوطني",
    "Unionist Party": "الحزب الوحدوي",
    "Unionist": "الحزب الوحدوي",
    "Know-Nothing": "حزب لا أدري",
    "Know Nothing": "حزب لا أدري",
    "alaskan independence Party": "حزب استقلال ألاسكا",
    "anti-masonic Party": "حزب مناهضة الماسونية",
    "anti masonic Party": "حزب مناهضة الماسونية",
    "constitutional union Party": "حزب الاتحاد الدستوري",
    # 'Country Party (Rhode Island)' : 'حزب الدولة (رود آيلاند)',
    "Greenback Party": "حزب الدولار الأمريكي",
    "Farmer–Labor Party": "حزب العمال المزارعين",
    "Farmer Labor Party": "حزب العمال المزارعين",
    "Federalist Party": "الحزب الفيدرالي الأمريكي",
    # 'Independent' : 'مستقلون',
    "Independent Voters Association": "رابطة الناخبين المستقلين",
    "Law and Order Party of Rhode Island": "حزب القانون والنظام في رود آيلاند",
    "Liberal Republican Party": "الحزب الجمهوري الليبرالي",
    "Nonpartisan League state": "الرابطة غير الحزبية",
    "Nullifier Party": "حزب الرفض",
    "People's Party": "حزب الشعب",
    "Peoples Party": "حزب الشعب",
    "Silver Party": "الحزب الفضي",
    "Green Party": "حزب الخضر",
    "Green": "حزب الخضر",
    "Citizens Party": "حزب المواطنين",
    "Solidarity": "حزب التضامن",
    "Socialist Party USA": "الحزب الاشتراكي",
    "Socialist Party": "الحزب الاشتراكي",
    "Liberty Union Party": "حزب الحرية المتحد",
}

USA_PARTY_LABELS = {x.strip(): y.strip() for x, y in _USA_PARTY_LABELS.items() if y.strip()}

us_states_new_keys = dict(_STATE_SUFFIX_TEMPLATES_BASE)

for party_name, party_label in USA_PARTY_LABELS.items():
    normalized_party_name = party_name.lower()
    us_states_new_keys[f"{{en}} {normalized_party_name}s"] = f"أعضاء {party_label} في {{ar}}"

    simplified_party_name = normalized_party_name.replace(" party", "")
    us_states_new_keys[f"{{en}} {simplified_party_name}s"] = f"أعضاء {party_label} في {{ar}}"


nat_bot = FormatData(
    us_states_new_keys,
    US_STATES,
    key_placeholder="{en}",
    value_placeholder="{ar}",
)


def normalize_state(ar_name: str) -> str:
    if "ولاية ولاية" in ar_name:
        ar_name = ar_name.replace("ولاية ولاية", "ولاية")

    if "ولاية واشنطن العاصمة" in ar_name:
        ar_name = ar_name.replace("ولاية واشنطن العاصمة", "واشنطن العاصمة")

    return ar_name


def resolve_us_states(category: str):
    result = nat_bot.search(category)

    result = normalize_state(result)

    return result


__all__ = [
    "resolve_us_states",
]
