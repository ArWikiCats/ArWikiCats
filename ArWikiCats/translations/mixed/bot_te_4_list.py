"""
Rich lookup tables for gendered and national prefix/suffix mappings.
"""

from ...helps import len_print
from ..jobs.jobs_singers import SINGERS_TAB
from ..sports import (
    SPORT_FORMTS_FEMALE_NAT,
    SPORT_FORMTS_MALE_NAT,
    SPORTS_KEYS_FOR_TEAM,
)
from ..sports.games_labs import SUMMER_WINTER_GAMES
from .all_keys2 import BOOK_CATEGORIES, BOOK_TYPES
from .all_keys3 import BUSINESSPEOPLE_INDUSTRIES
from .keys_23 import AFC_KEYS
from .Newkey import pop_final6

# الإنجليزية والعربية اسم البلد
# tab[Category:United States board members] = "تصنيف:أعضاء مجلس الولايات المتحدة"

# الإنجليزي جنسية والعربي اسم البلد
# tab[Category:Bahraini King's Cup] = "تصنيف:كأس ملك البحرين"
en_is_nat_ar_is_P17: dict[str, str] = {
    "grand prix": "جائزة {} الكبرى",
    "king's cup": "كأس ملك {}",  # Bahraini King's Cup
    "cup": "كأس {}",
    "independence": "استقلال {}",
    "open": "{} المفتوحة",
    "ladies open": "{} المفتوحة للسيدات",
    "national university": "جامعة {} الوطنية",
    "national university alumni": "خريجو جامعة {} الوطنية",
    # "open (tennis)" : "{} المفتوحة للتنس",
}


# الانجليزية جنسية
# رجالية بألف ولام التعريف
# tab[Category:Yemeni president cup] = "تصنيف:كأس الرئيس اليمني"


en_is_nat_ar_is_al_mens: dict[str, str] = {
    "president cup": "كأس الرئيس {}",
    "federation cup": "كأس الاتحاد {}",
    "fa cup": "كأس الاتحاد {}",
    "occupation": "الاحتلال {}",
    "super cup": "كأس السوبر {}",
    "elite cup": "كأس النخبة {}",
    "referendum": "الاستفتاء {}",
    "involvement": "التدخل {}",
    "census": "التعداد {}",
    # "professional football league": "الدوري {} لكرة القدم للمحترفين",
    "professional football league": "دوري كرة القدم {} للمحترفين",
    "premier football league": "الدوري {} الممتاز لكرة القدم",
    "national super league": "دوري السوبر {}",
    "super league": "دوري السوبر {}",
    "premier league": "الدوري {} الممتاز",
    "premier division": "الدوري {} الممتاز",
    "amateur football league": "الدوري {} لكرة القدم للهواة",
    "football league": "الدوري {} لكرة القدم",
    "population census": "التعداد السكاني {}",
    "population and housing census": "التعداد {} للسكان والمساكن",
    "national party": "الحزب الوطني {}",
    "criminal law": "القانون الجنائي {}",
    "family law": "قانون الأسرة {}",
    "labour law": "قانون العمل {}",
    "abortion law": "قانون الإجهاض {}",
    "rugby union leagues": "اتحاد دوري الرجبي {}",
    "women's rugby union": "اتحاد الرجبي {} للنساء",
    "rugby union": "اتحاد الرجبي {}",
    "presidential pardons": "العفو الرئاسي {}",
    "pardons": "العفو {}",
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

# رجالية بدون ألف ولام التعريف
# tab[Category:syrian descent] = "تصنيف:أصل سوري"

en_is_nat_ar_is_man: dict[str, str] = {
    "descent": "أصل {}",
    "military occupations": "احتلال عسكري {}",
    "integration": "تكامل {}",
    "innovation": "ابتكار {}",
    "design": "تصميم {}",
    "contemporary art": "فن معاصر {}",
    "art": "فن {}",
    "cuisine": "مطبخ {}",
    "calendar": "تقويم {}",
    "non fiction literature": "أدب غير خيالي {}",
    "non-fiction literature": "أدب غير خيالي {}",
    "literature": "أدب {}",
    "caste system": "نظام طبقي {}",
    "law": "قانون {}",
    "military equipment": "عتاد عسكري {}",
    "wine": "نبيذ {}",
    "history": "تاريخ {}",
    "nuclear history": "تاريخ نووي {}",
    "military history": "تاريخ عسكري {}",
    "diaspora": "شتات {}",
    "traditions": "تراث {}",
    "folklore": "فلكور {}",
    # "literary critics" : "نقد أدبي {}",
    "television": "تلفاز {}",
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
    "games medalists": "فائزون بميداليات في الألعاب {}",
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


def _extend_female_sport_mappings() -> None:
    """
    Populate sport related mappings for female categories.

    # Russian Professional Football League
    # دوري كرة القدم الروسي للمحترفين

    """
    data = {}
    for key, value in SPORT_FORMTS_FEMALE_NAT.items():
        data[key] = value
    for category, label in baston_women.items():
        data[category.lower()] = f"{label} {{}}"
    return data


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
    "television miniseries": "مسلسلات قصيرة {}",
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


def _build_new_kkk() -> dict[str, str]:
    """
    English nationality → Arabic country-name
    Example: “men's hockey cup” → “كأس {} الهوكي للرجال”
    """
    label_index: dict[str, str] = {}

    for team2, team2_lab in SPORTS_KEYS_FOR_TEAM.items():
        # Category:National junior women's goalball teams
        label_index[f"men's {team2} cup"] = f"كأس {{}} {team2_lab} للرجال"
        label_index[f"women's {team2} cup"] = f"كأس {{}} {team2_lab} للسيدات"
        label_index[f"{team2} cup"] = f"كأس {{}} {team2_lab}"
        label_index[f"national junior men's {team2} team"] = f"منتخب {{}} {team2_lab} للناشئين"
        label_index[f"national junior {team2} team"] = f"منتخب {{}} {team2_lab} للناشئين"
        label_index[f"national {team2} team"] = f"منتخب {{}} {team2_lab}"
        label_index[f"national women's {team2} team"] = f"منتخب {{}} {team2_lab} للسيدات"
        label_index[f"national men's {team2} team"] = f"منتخب {{}} {team2_lab} للرجال"

    return label_index


def _extend_sport_mappings() -> None:
    """Populate sport related mappings for both genders."""

    for key, value in SPORT_FORMTS_MALE_NAT.items():
        en_is_nat_ar_is_al_mens[key] = value

    for category, label in baston_men.items():
        en_is_nat_ar_is_al_mens[category.lower()] = f"{label} {{}}"


def _extend_singer_and_business_entries() -> None:
    """Populate singer and businessperson derived mappings."""

    for key, label in SINGERS_TAB.items():
        en_is_nat_ar_is_man[key] = f"{label} {{}}"
        en_is_nat_ar_is_women[f"{key} groups"] = f"فرق {label} {{}}"
        en_is_nat_ar_is_women[f"{key} musical groups"] = f"فرق موسيقى {label} {{}}"

    for key, label in BUSINESSPEOPLE_INDUSTRIES.items():
        en_is_nat_ar_is_women[f"{key} businesspeople"] = f"شخصيات أعمال {{}} في {label}"

        en_is_nat_ar_is_women[f"{key} industry businesspeople"] = f"شخصيات أعمال {{}} في صناعة {label}"


en_is_nat_ar_is_women_2: dict[str, str] = dict(en_is_nat_ar_is_women)


def _extend_book_entries() -> None:
    """Populate mappings derived from book categories."""

    for key, label in BOOK_CATEGORIES.items():
        lowered = key.lower()
        en_is_nat_ar_is_women[lowered] = f"{label} {{}}"
        for book_type, book_label in BOOK_TYPES.items():
            composite = f"{book_type.lower()} {lowered}"
            en_is_nat_ar_is_women[composite] = f"{label} {book_label} {{}}"

        en_is_nat_ar_is_women[f"non fiction {lowered}"] = f"{label} {{}} غير خيالية"
        en_is_nat_ar_is_women[f"non-fiction {lowered}"] = f"{label} {{}} غير خيالية"
        en_is_nat_ar_is_women[f"online {lowered}"] = f"{label} إنترنت {{}}"

    for key, label in pop_final6.items():
        en_is_nat_ar_is_women[key.lower()] = f"{label} {{}}"


change_male_to_female: dict[str, str] = {
    "{} مغتربون": "{} مغتربات",
    "{} مختطفون": "{} مختطفات",
    "{} معدمون": "{} معدمات",
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

Multi_sport_for_Jobs: dict[str, str] = {
    "afc asian cup": "كأس آسيا",
    "afc cup": "كأس الاتحاد الآسيوي",
    "fifa futsal world cup": "كأس العالم لكرة الصالات",
}

Multi_sport_for_Jobs.update(SUMMER_WINTER_GAMES)
Multi_sport_for_Jobs.update(AFC_KEYS)

SPORT_FORMTS_NEW_KKK = _build_new_kkk()  # الإنجليزي جنسية والعربي اسم البلد

en_is_nat_ar_is_P17.update(SPORT_FORMTS_NEW_KKK)

_extend_sport_mappings()

en_is_nat_ar_is_al_women.update(_extend_female_sport_mappings())

_extend_singer_and_business_entries()
_extend_book_entries()


__all__ = [
    "change_male_to_female",
    "Multi_sport_for_Jobs",
    "en_is_nat_ar_is_P17",
    "en_is_nat_ar_is_al_mens",
    "en_is_nat_ar_is_man",
    "en_is_nat_ar_is_al_women",
    "en_is_nat_ar_is_women",
    "en_is_nat_ar_is_women_2",
]


len_print.data_len(
    "bot_te_4_list.py",
    {
        "en_is_nat_ar_is_P17": en_is_nat_ar_is_P17,
        "en_is_nat_ar_is_al_mens": en_is_nat_ar_is_al_mens,
        "en_is_nat_ar_is_man": en_is_nat_ar_is_man,
        "en_is_nat_ar_is_al_women": en_is_nat_ar_is_al_women,
        "en_is_nat_ar_is_women": en_is_nat_ar_is_women,
        "change_male_to_female": change_male_to_female,
        "Multi_sport_for_Jobs": Multi_sport_for_Jobs,
        "en_is_nat_ar_is_women_2": en_is_nat_ar_is_women_2,
    },
)
