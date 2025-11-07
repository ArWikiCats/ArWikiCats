"""Mappings for club-related categories and miscellaneous concepts."""

from __future__ import annotations

import sys
from typing import Final, Tuple

from ...helps import len_print
from .key_registry import KeyRegistry, load_json_mapping
from .male_keys import New_male_keys

BASE_POP_FINAL_5: Final[dict[str, str]] = {
    "trustees of": "أمناء",
    "members of": "أعضاء",
    "independent members": "أعضاء مستقلون",
    "jacksonian members": "أعضاء جاكسونيون",
    "members": "أعضاء",
    "secession": "الانفصالية",
    "separatism": "الانفصالية",
    "military of": "عسكرية",
    "tanks of": "دبابات",
    "relationships": "علاقات",
    "mass media": "وسائل الإعلام",
    "denominations": "طوائف",
    "equipment of": "معدات",
    "radars of": "رادارات",
    "cargo ships of": "سفن بضائع",
    "ships of": "سفن",
    "satellites of": "أقمار صناعية تتبع",
    "military aviation": "طيران عسكري",
    "wind farms": "مزارع الرياح",
    "aviation": "طيران",
    "equipment": "معدات",
    "military-equipment of": "عتاد عسكري",
    "military equipment of": "عتاد عسكري",
    "barracks": "ثكنات",
    "deuterostomes": "ثانويات الفم",
    "order of gold star (ukraine)": "وسام النجمة الذهبية الأوكراني",
    "order of the holy sepulchre": "فرسان القبر المقدس",
    "behistun inscription": "نقش بيستون",
    "macaronic language": "تلميع",
    "binding energy": "طاقة الارتباط",
    "dumping (pricing policy)": "إغراق تجاري",
    "cosmopolitanism": "كوسموبوليتية",
    "lakshmi": "لاكشمي",
    "medical privacy": "خصوصية صحية",
    "kinetic energy": "طاقة حركية",
    "prohibition": "منع الكحول",
    "chemnitz": "كيمنتس",
    "glucose": "غلوكوز",
    "weimar": "فايمار",
    "kempten": "كمبتن",
    "bottrop": "بوتروب",
    "greifswald": "غرايفسفالت",
    "schweinfurt": "شفاينفورت",
    "wilhelmshaven": "فيلهلمسهافن",
    "hof, bavaria": "هوف",
    "wolfsburg": "فولفسبورغ",
    "baden-baden": "بادن بادن",
    "patriotism": "وطنية",
    "memmingen": "ميمينجين",
    "rostock": "روستوك",
    "salzgitter": "زالتسغيتر",
    "zwickau": "تسفيكاو",
    "dortmund": "دورتموند",
    "ingolstadt": "إنغولشتات",
    "rosenheim": "روزنهايم",
    "economic indicators": "مؤشرات اقتصادية",
    "scientific skepticism": "شكوكية علمية",
    "tropes": "مجازات",
    "theism": "الإيمان بالله",
    "chemical energy": "طاقة كيميائية",
    "setting": "مواقع الأحداث",
    "fictional characters": "شخصيات خيالية",
    "economic systems": "أنظمة اقتصادية",
    "platonism": "أفلاطونية",
    "electric power": "طاقة كهربائية",
    "fifa": "فيفا",
    "determinism": "حتمية",
    "european system of central banks": "النظام الأوروبي للبنوك المركزية",
    "homeostasis": "استتباب",
    "irony": "سخرية",
    "rationalism": "عقلانية",
    "plot (narrative)": "حبكة (سرد)",
    "injection (medicine)": "حقن طبي",
    "ointments": "مراهم",
    "cardiac arrhythmia": "اضطراب النظم القلبي",
    "economic bubbles": "فقاعات اقتصادية",
    "euphemisms": "تسميل",
    "onomatopoeia": "محاكاة صوتية",
    "synecdoche": "مجاز مرسل",
    "flora of azerbaijan": "نباتات أذربيجان",
    "oligopoly": "احتكار القلة",
    "aphorisms": "حكمة",
    "dehydration": "تجفاف",
    "traffic management": "إدارة الحركة",
    "walking": "مشي",
    "types of soil": "أنواع التربة",
    "gnosticism": "غنوصية",
    "humanism": "إنسانية",
    "dresden": "درسدن",
    "metonymy": "كناية",
    "monopoly (economics)": "احتكار",
    "monopoly": "الاحتكار",
    "prayer": "صلاة",
    "tübingen": "توبينغن",
    "leipzig": "لايبزيغ",
    "nuclear power": "طاقة نووية",
    "bonn": "بون",
    "wiesbaden": "فيسبادن",
    "kassel": "كاسل",
    "communism": "شيوعية",
    "gera": "غيرا",
    "plauen": "بلاوين",
    "religious fundamentalism": "أصولية دينية",
    "mannheim": "مانهايم",
    "lüneburg": "لونبورغ",
    "eisenach": "أيسناخ",
    "death": "موت",
    "do it yourself": "افعلها بنفسك",
    "duisburg": "دويسبورغ",
    "erfurt": "إرفورت",
    "bamberg": "بامبرغ",
    "bochum": "بوخوم",
    "darmstadt": "دارمشتات",
    "göttingen": "غوتنغن",
    "offenbach am main": "أوفنباخ أم ماين",
    "karlsruhe": "كارلسروه",
    "heilbronn": "هايلبرون",
    "force": "قوى",
    "pforzheim": "بفورتسهايم",
    "atheism": "إلحاد",
    "osnabrück": "أوسنابروك",
    "schwerin": "شفيرين",
    "materialism": "مادية",
    "bremerhaven": "بريمرهافن",
    "würzburg": "فورتسبورغ",
    "erlangen": "إرلنغن",
    "fables": "حكاية رمزية",
    "fürth": "فورت",
    "idealism": "مثالية",
    "jena": "يينا",
    "regensburg": "ريغنسبورغ",
    "global warming": "احترار عالمي",
    "ulm": "أولم",
    "amberg": "آمبرغ",
    "metaphors": "استعارات",
}

RESOURCE_LABELS: Final[dict[str, str]] = {
    "bauxite": "البوكسيت",
    "coal gas-fired power stations": "محطات توليد الطاقة تعمل بغاز الفحم",
    "coal": "الفحم",
    "coal-fired power stations": "محطات توليد الطاقة تعمل بالفحم",
    "computer companies": "شركات حوسبة",
    "copper": "النحاس",
    "dragon boat": "قوارب التنين",
    "electric power generation": "توليد الكهرباء",
    "electric power transmission": "نقل الكهرباء",
    "electric power": "القدرة الكهربائية",
    "electricity sector": "قطاع الكهرباء",
    "former power stations": "محطات طاقة سابقة",
    "fossil fuel": "وقود أحفوري",
    "fossil fuels": "وقود أحفوري",
    "gas-fired power plants": "محطات طاقة وقود أحفوري",
    "gold": "الذهب",
    "hydraulic fracturing": "تصديع مائي",
    "hydroelectric power stations": "محطات طاقة كهرمائية",
    "hydroelectricity": "الطاقة الكهرومائية",
    "hydroelectrics": "كهرمائية",
    "industries": "صناعات",
    "influence (social and political)": "تأثير اجتماعي وسياسي",
    "man-made disasters": "كوارث من صنع الإنسان",
    "mines": "مناجم",
    "mining": "التعدين",
    "natural gas fields": "خطوط غاز طبيعي",
    "natural gas pipelines": "خطوط أنابيب غاز",
    "natural gas": "غاز طبيعي",
    "natural gas-fired power stations": "محطات توليد الطاقة تعمل بالغاز الطبيعي",
    "nuclear power stations": "محطات طاقة نووية",
    "nuclear power": "طاقة نووية",
    "nuclear weapons testing": "اختبار الأسلحة النووية",
    "oil and gas": "النفط والغاز",
    "oil fields": "حقول نفط",
    "oil shale": "صخر زيتي",
    "oil shale-fired power stations": "محطات توليد الطاقة تعمل بالصخر الزيتي",
    "oil": "نفط",
    "oil-fired power stations": "محطات توليد الطاقة تعمل بزيت الوقود",
    "peat-fired power stations": "محطات توليد الطاقة تعمل بالخث",
    "petroleum": "بترول",
    "photovoltaic power stations": "محطات طاقة كهروضوئية",
    "photovoltaics": "خلايا كهروضوئية",
    "pollution": "تلوث",
    "power (social and political)": "نفوذ اجتماعي وسياسي",
    "power companies": "شركات طاقة",
    "power stations": "محطات طاقة",
    "proposed power stations": "محطات طاقة مقترحة",
    "sedimentary rocks": "صخور رسوبية",
    "service industries": "صناعات خدمية",
    "shipping": "النقل البحري",
    "solar eclipses": "كسوفات شمسية",
    "solar power stations": "محطات طاقة شمسية",
    "solar power": "طاقة شمسية",
    "solid fuel": "وقود صلب",
    "solid fuels": "وقود صلب",
    "trucking": "النقل بالشاحنات",
    "water resource management in": "إدارة الموارد المائية في",
    "water transportation": "النقل المائي",
    "wind power": "طاقة الرياح",
}


def _build_club_entries(clubs: dict[str, str], registry: KeyRegistry) -> dict[str, str]:
    """Populate club specific entries and return the lowercase index."""

    lowercase_clubs: dict[str, str] = {}
    for club, label in clubs.items():
        if not club or not label:
            continue
        club_lower = club.lower()
        registry.data[f"{club_lower} players"] = f"لاعبو {label}"
        registry.data[f"{club_lower} seasons"] = f"مواسم {label}"
        registry.data[f"{club_lower} songs"] = f"أغاني {label}"
        registry.data[f"{club_lower} chairmen and investors"] = f"رؤساء ومسيرو {label}"
        registry.data[f"{club_lower} non-playing staff"] = f"طاقم {label} غير اللاعبين"
        registry.data[f"{club_lower} matches"] = f"مباريات {label}"
        registry.data[f"{club_lower} managers"] = f"مدربو {label}"
        registry.data[f"{club_lower} templates"] = f"قوالب {label}"
        registry.data[club_lower] = label
        lowercase_clubs[club_lower] = label
    return lowercase_clubs


def _build_resource_entries(registry: KeyRegistry) -> None:
    """Add energy and resource related labels."""

    for key, label in RESOURCE_LABELS.items():
        registry.data[key.lower()] = label


def build_pop_final_5() -> Tuple[dict[str, str], dict[str, str]]:
    """Build the club and miscellaneous concept mappings."""

    registry = KeyRegistry(BASE_POP_FINAL_5)
    clubs = load_json_mapping("Clubs_key")
    clubs_index = _build_club_entries(clubs, registry)
    _build_resource_entries(registry)
    registry.update(New_male_keys)

    len_print.lenth_pri("all_keys5.py", {"pop_final_5": sys.getsizeof(registry.data)})

    return registry.data, clubs_index


pop_final_5, Clubs_key_2 = build_pop_final_5()

__all__ = ["pop_final_5", "Clubs_key_2"]
