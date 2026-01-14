"""
Rich lookup tables for gendered and national prefix/suffix mappings.
"""

from ...helps import len_print
from ..jobs.jobs_singers import SINGERS_TAB
from ..sports.skeys import (
    SPORT_FORMATS_MALE_NAT,
)
from .all_keys2 import BOOK_CATEGORIES, BOOK_TYPES
from .all_keys3 import BUSINESSPEOPLE_INDUSTRIES
from .Newkey import pop_final6

# الإنجليزية والعربية اسم البلد
# tab[Category:United States board members] = "تصنيف:أعضاء مجلس الولايات المتحدة"

# الانجليزية جنسية
# رجالية بألف ولام التعريف
# tab[Category:Yemeni president cup] = "تصنيف:كأس الرئيس اليمني"


en_is_nat_ar_is_al_mens: dict[str, str] = {
}

# العربي جنسية مثل : Yemeni > اليمني
# tab[Category:syrian invasion] = "تصنيف:الغزو السوري"

baston_men: dict[str, str] = {
    "solidarity movement": "حركة التضامن",
    "invasion": "الغزو",
    "league": "الدوري",
    "professional league": "دوري المحترفين",
    "professional league managers": "مدربو دوري المحترفين",
    "military": "الجيش",
    "army": "الجيش",
}

# نسائية بألف ولام التعريف
# الانجليزية والعربية جنسية
# tab[Category:Yemeni navy] = "تصنيف:البحرية اليمنية"
# tab[Category:syrian air force] = "تصنيف:القوات الجوية السورية"
en_is_nat_ar_is_al_women: dict[str, str] = {
    "royal air force": "القوات الجوية الملكية {}",
    "air force": "القوات الجوية {}",
    "royal defence force": "قوات الدفاع الملكية {}",
    "royal navy": "البحرية {}",
    "naval force": "البحرية {}",
    "naval forces": "البحرية {}",
    "navy": "البحرية {}",
    "airways accidents and incidents": "حوادث الخطوط الجوية {}",
    "airways accidents-and-incidents": "حوادث الخطوط الجوية {}",
    "airways": "الخطوط الجوية {}",
    "youth games": "الألعاب {} الشبابية",
    "financial crisis": "الأزمة المالية {}",
    "presidential crisis": "الأزمة الرئاسية {}",
    # "society" : "الجمعية {}",
    "military academy": "الأكاديمية العسكرية {}",
    "military college": "الكلية العسكرية {}",
    "crisis": "الأزمة {}",
    "energy crisis": "أزمة الطاقة {}",
    "constitutional crisis": "الأزمة الدستورية {}",
    "games competitors": "منافسون في الألعاب {}",
    "games medalists": "فائزون بميداليات الألعاب {}",
    "games gold medalists": "فائزون بميداليات ذهبية في الألعاب {}",
    "games silver medalists": "فائزون بميداليات فضية في الألعاب {}",
    "games bronze medalists": "فائزون بميداليات برونزية في الألعاب {}",
    "television people": "شخصيات التلفزة {}",
    "presidential primaries": "الانتخابات الرئاسية التمهيدية {}",
    "legislative election": "الانتخابات التشريعية {}",
    "parliamentary election": "الانتخابات البرلمانية {}",
    "general election": "الانتخابات العامة {}",
    "regional election": "انتخابات الإقليمية {}",
    "vice-presidential election": "انتخابات نائب الرئاسة {}",
    "presidential primarie": "الانتخابات الرئاسية التمهيدية {nat}",
    "presidential election": "انتخابات الرئاسة {}",
}


# [Category:myanmarian movement] = "تصنيف:الحركة الميانمارية"
baston_women: dict[str, str] = {
    "movement": "الحركة",
    "unity cup": "كأس الوحدة",
    "rail": "السكك الحديدية",
    # "grand prix" : "الجائزة الكبرى",
    "television": "التلفزة",
    "revolution": "الثورة",
    "war": "الحرب",
    "border war": "حرب الحدود",
    "civil war": "الحرب الأهلية",
    "detention": "المعتقلات",
    "para games": "الألعاب البارالمبية",
    "games": "الألعاب",
    "medical association": "الجمعية الطبية",
    "football": "كرة القدم",
    "soccer": "كرة القدم",
    "cinema": "السينما",
    "politics": "السياسة",
    # "sports" : "الرياضة",
}

# جنسية عربي وإنجليزي
# نسائية بدون ألف ولام التعريف
# tab[Category:myanmarian crimes] = "تصنيف:جرائم ميانمارية"
en_is_nat_ar_is_women: dict[str, str] = {
    "phonologies": "تصريفات صوتية {}",
    "crimes": "جرائم {}",
    "crimes against humanity": "جرائم ضد الإنسانية {}",
    "war crimes": "جرائم حرب {}",
    "airstrikes": "ضربات جوية {}",
    "archipelagoes": "أرخبيلات {}",
    "architecture": "عمارة {}",
    "autobiographies": "ترجمة ذاتية {}",
    "automotive": "سيارات {}",
    "awards and decorations": "جوائز وأوسمة {}",
    "awards": "جوائز {}",
    "ballot measures": "إجراءات اقتراع {}",
    "ballot propositions": "اقتراحات اقتراع {}",
    "border crossings": "معابر حدودية {}",
    "border": "حدود {}",
    "brands": "ماركات {}",
    "budgets": "موازنات {}",
    "buildings": "مباني {}",
    "business culture": "ثقافة مالية {}",
    "businesspeople": "شخصيات أعمال {}",
    "cantons": "كانتونات {}",
    "casualties": "خسائر {}",
    "cathedrals": "كاتدرائيات {}",
    "championships": "بطولات {}",
    "civil awards and decorations": "جوائز وأوسمة مدنية {}",
    "classical albums": "ألبومات كلاسيكية {}",
    "classical music": "موسيقى كلاسيكية {}",
    "clothing": "ملابس {}",
    "clubs": "أندية {}",
    "coats of arms": "شعارات نبالة {}",
    "colonial": "مستعمرات {}",
    "comedy albums": "ألبومات كوميدية {}",
    "comedy music": "موسيقى كوميدية {}",
    "comedy": "كوميديا {}",
    "companies": "شركات {}",
    "competitions": "منافسات {}",
    "compilation albums": "ألبومات تجميعية {}",
    "countries": "بلدان {}",
    "culture": "ثقافة {}",
    "decorations": "أوسمة {}",
    "diplomatic missions": "بعثات دبلوماسية {}",
    "discoveries": "اكتشافات {}",
    "drink": "مشروبات {}",
    "elections": "انتخابات {}",
    "encyclopedias": "موسوعات {}",
    "executions": "إعدامات {}",
    "explosions": "انفجارات {}",
    "families": "عائلات {}",
    "fauna": "حيوانات {}",
    "festivals": "مهرجانات {}",
    "folk albums": "ألبومات فلكلورية {}",
    "folk music": "موسيقى فلكلورية {}",
    "folklore characters": "شخصيات فلكلورية {}",
    "football club matches": "مباريات أندية كرة قدم {}",
    "football club seasons": "مواسم أندية كرة قدم {}",
    "forests": "غابات {}",
    "gangs": "عصابات {}",
    "given names": "أسماء شخصية {}",
    "heraldry": "نبالة {}",
    "heritage sites": "موقع تراث عالمي {}",
    "inscriptions": "نقوش {}",
    "introductions": "استحداثات {}",
    "inventions": "اختراعات {}",
    "islands": "جزر {}",
    "issues": "قضايا {}",
    "jewellery": "مجوهرات {}",
    "journalism": "صحافة {}",
    "lakes": "بحيرات {}",
    "learned and professional societies": "جمعيات علمية ومهنية {}",
    "learned societies": "جمعيات علمية {}",
    "literary awards": "جوائز أدبية {}",
    "magazines": "مجلات {}",
    # "magazines": "مجلة {}",
    "mascots": "تمائم {}",
    "masculine given names": "أسماء ذكور {}",
    "media personalities": "شخصيات إعلامية {}",
    "media": "وسائل إعلام {}",
    "memoirs": "مذكرات {}",
    "memorials and cemeteries": "نصب تذكارية ومقابر {}",
    "military equipment": "معدات عسكرية {}",
    "military terminology": "مصطلحات عسكرية {}",
    "military-equipment": "معدات عسكرية {}",
    "military-terminology": "مصطلحات عسكرية {}",
    "mixtape albums": "ألبومات ميكستايب {}",
    "mixtape music": "موسيقى ميكستايب {}",
    "monarchy": "ملكية {}",
    "motorsport": "رياضة محركات {}",
    "mountains": "جبال {}",
    "movies": "أفلام {}",
    "music people": "شخصيات موسيقية {}",
    "music personalities": "شخصيات موسيقية {}",
    "music": "موسيقى {}",
    "musical duos": "فرق موسيقية ثنائية {}",
    "musical groups": "فرق موسيقية {}",
    "musical instruments": "آلات موسيقية {}",
    "mythology": "أساطير {}",
    "phonology": "نطقيات {}",
    "names": "أسماء {}",
    "nationalism": "قومية {}",
    "newspapers": "صحف {}",
    "non-profit organizations": "منظمات غير ربحية {}",
    "non profit organizations": "منظمات غير ربحية {}",
    "novels": "روايات {}",
    "online journalism": "صحافة إنترنت {}",
    "operas": "أوبيرات {}",
    "organisations": "منظمات {}",
    "organizations": "منظمات {}",
    "parishes": "أبرشيات {}",
    "parks": "متنزهات {}",
    "peoples": "شعوب {}",
    "philosophy": "فلسفة {}",
    "plays": "مسرحيات {}",
    "poems": "قصائد {}",
    "political philosophy": "فلسفة سياسية {}",
    "popular culture": "ثقافة شعبية {}",
    "professional societies": "جمعيات مهنية {}",
    "provinces": "مقاطعات {}",
    "publications": "منشورات {}",
    "radio networks": "شبكات مذياع {}",
    "radio stations": "محطات إذاعية {}",
    "radio": "راديو {}",
    "rebellions": "تمردات {}",
    "occupations": "مهن {}",
    "religious occupations": "مهن دينية {}",
    "rectors": "عمدات {}",
    "referendums": "استفتاءات {}",
    "religions": "ديانات {}",
    "resorts": "منتجعات {}",
    "restaurants": "مطاعم {}",
    "revolutions": "ثورات {}",
    "riots": "أعمال شغب {}",
    "road cycling": "سباقات دراجات على الطريق {}",
    "roads": "طرقات {}",
    "royal families": "عائلات ملكية {}",
    "schools and colleges": "مدارس وكليات {}",
    "sculptures": "منحوتات {}",
    "sea temples": "معابد بحرية {}",
    "short stories": "قصص قصيرة {}",
    "societies": "جمعيات {}",
    "songs": "أغاني {}",
    "sorts events": "أحداث رياضية {}",
    "sports-events": "أحداث رياضية {}",
    "soundtracks": "موسيقى تصويرية {}",
    "sport": "رياضة {}",
    "sports competitions": "منافسات رياضية {}",
    "sports events": "أحداث رياضية {}",
    "sports": "رياضة {}",
    "surnames": "ألقاب {}",
    "swamps": "مستنقعات {}",
    "telenovelas": "تيلينوفيلا {}",
    "television commercials": "إعلانات تجارية تلفزيونية {}",
    "television films": "أفلام تلفزيونية {}",
    "miniseries": "مسلسلات قصيرة {}",
    "television networks": "شبكات تلفزيونية {}",
    "television news": "أخبار تلفزيونية {}",
    "television personalities": "شخصيات تلفزيونية {}",
    "television programmes": "برامج تلفزيونية {}",
    "television programs": "برامج تلفزيونية {}",
    "television series": "مسلسلات تلفزيونية {}",
    "film series": "سلاسل أفلام {}",
    "television series-debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series-endings": "مسلسلات تلفزيونية {} انتهت في",
    "television stations": "محطات تلفزيونية {}",
    "television-seasons": "مواسم تلفزيونية {}",
    "temples": "معابد {}",
    "tennis": "كرة مضرب {}",
    "terminology": "مصطلحات {}",
    "titles": "ألقاب {}",
    "tour": "بطولات {}",
    "towns": "بلدات {}",
    "trains": "قطارات {}",
    "trials": "محاكمات {}",
    "tribes": "قبائل {}",
    "underground culture": "ثقافة باطنية {}",
    "universities": "جامعات {}",
    "verbs": "أفعال {}",
    # "video game businesspeople": "شخصيات أعمال {} في ألعاب الفيديو",
    "video games": "ألعاب فيديو {}",
    "volcanoes": "براكين {}",
    "wars": "حروب {}",
    "waterfalls": "شلالات {}",
    "webcomic": "ويب كومكس {}",
    "webcomics": "ويب كومكس {}",
    "websites": "مواقع ويب {}",
    "women's sport": "رياضة {} نسائية",
    "works": "أعمال {}",
    "youth competitions": "منافسات شبابية {}",
    "youth music competitions": "منافسات موسيقية شبابية {}",
    "youth sports competitions": "منافسات رياضية شبابية {}",
    # "athletic conference schools" : "كرة مضرب {}",
    # "ballot measures":"استفتاءات عامة {}",
    # "books" : "كتب {}",
    # "cinema" : "سينما {}",
    # "dukes" : "دوقات {}",
}


def _extend_sport_mappings() -> None:
    """Populate sport related mappings for both genders."""

    for key, value in SPORT_FORMATS_MALE_NAT.items():
        en_is_nat_ar_is_al_mens[key] = value

    for category, label in baston_men.items():
        en_is_nat_ar_is_al_mens[category.lower()] = f"{label} {{}}"


def _extend_singer_and_business_entries() -> None:
    """Populate singer and businessperson derived mappings."""

    for key, label in SINGERS_TAB.items():
        en_is_nat_ar_is_women[f"{key} groups"] = f"فرق {label} {{}}"
        en_is_nat_ar_is_women[f"{key} musical groups"] = f"فرق موسيقى {label} {{}}"

    for key, label in BUSINESSPEOPLE_INDUSTRIES.items():
        en_is_nat_ar_is_women[f"{key} businesspeople"] = f"شخصيات أعمال {{}} في {label}"

        en_is_nat_ar_is_women[f"{key} industry businesspeople"] = f"شخصيات أعمال {{}} في صناعة {label}"


def _extend_book_entries() -> dict:
    """Populate mappings derived from book categories."""
    data = {}
    for key, label in BOOK_CATEGORIES.items():
        lowered = key.lower()
        data[lowered] = f"{label} {{}}"
        for book_type, book_label in BOOK_TYPES.items():
            composite = f"{book_type.lower()} {lowered}"
            data[composite] = f"{label} {book_label} {{}}"

        data[f"non fiction {lowered}"] = f"{label} {{}} غير خيالية"
        data[f"non-fiction {lowered}"] = f"{label} {{}} غير خيالية"
        data[f"online {lowered}"] = f"{label} إنترنت {{}}"

    for key, label in pop_final6.items():
        data[key.lower()] = f"{label} {{}}"
    return data


change_male_to_female: dict[str, str] = {
    "{} مغتربون": "{} مغتربات",
    "{} مختطفون": "{} مختطفات",
    "{} معاقون": "{} معاقات",
    "{} مثليون": "{} مثليات",
    "{} أصليون": "{} أصليات",
    "{} أسطوريون": "{} أسطوريات",
    "{} خياليون": "{} خياليات",
    "{} بحريون": "{} بحريات",
    "{} سياسيون": "{} سياسيات",
    "{} معاصرون": "{} معاصرات",
    "{} عسكريون": "{} عسكريات",
    "{} لاتينيون": "{} لاتينيات",
    "{} رومانسيون": "{} رومانسيات",
    "{} دينيون": "{} دينيات",
}

ttk: dict[str, str] = {
    "cultural depictions of": "التصوير الثقافي ل{}",
    "fictional depictions of": "التصوير الخيالي ل{}",
    "depictions of": "تصوير عن {}",
}

ttk2: dict[str, str] = {
    "cultural depictions of": "تصوير ثقافي عن {}",
    "fictional depictions of": "تصوير خيالي عن {}",
    "depictions of": "تصوير عن {}",
}
_extend_sport_mappings()

_extend_singer_and_business_entries()
books_keys = _extend_book_entries()
en_is_nat_ar_is_women.update(books_keys)

__all__ = [
    "change_male_to_female",
    "en_is_nat_ar_is_al_mens",
    "en_is_nat_ar_is_al_women",
    "en_is_nat_ar_is_women",
]


len_print.data_len(
    "bot_te_4_list.py",
    {
        "en_is_nat_ar_is_al_mens": en_is_nat_ar_is_al_mens,
        "en_is_nat_ar_is_al_women": en_is_nat_ar_is_al_women,
        "en_is_nat_ar_is_women": en_is_nat_ar_is_women,
        "change_male_to_female": change_male_to_female,
    },
)
