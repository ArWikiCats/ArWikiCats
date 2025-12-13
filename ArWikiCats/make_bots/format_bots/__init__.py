#!/usr/bin/python3
"""
!
"""

import re

from ...helps import len_print
from ...helps.log import logger
from .pf_keys import CHANGE_KEY_MAPPINGS, CHANGE_KEY_SECONDARY
from .pf_keys import change_key_secondary_replacements, change_key_mappings_replacements
from .relation_mapping import category_relation_mapping

# Precompiled Regex Patterns
REGEX_SUB_WHITESPACE = re.compile(r"[\s\t]+", re.IGNORECASE)
REGEX_SUB_CENTURY = re.compile(r"[−–\-]century", re.IGNORECASE)
REGEX_SUB_MILLENNIUM = re.compile(r"[−–\-]millennium", re.IGNORECASE)
REGEX_SUB_MILLENNIUM_CENTURY = re.compile(r"[−–\-](millennium|century)", re.I)
REGEX_SUB_ROYAL_DEFENCE_FORCE = re.compile(r"royal (.*?) defence force", re.IGNORECASE)
REGEX_SUB_ROYAL_NAVAL_FORCE = re.compile(r"royal (.*?) naval force", re.IGNORECASE)
REGEX_SUB_ROYAL_NAVY = re.compile(r"royal (.*?) navy", re.IGNORECASE)
REGEX_SUB_ROYAL_AIR_FORCE = re.compile(r"royal (.*?) air force", re.IGNORECASE)
REGEX_SUB_EXPATRIATE_PEOPLE = re.compile(r"(\w+) expatriate (\w+) people in ", re.IGNORECASE)
REGEX_SUB_ORGANISATIONS = re.compile(r"organisations", re.IGNORECASE)
REGEX_SUB_RUS = re.compile(r"rus'", re.IGNORECASE)
REGEX_SUB_THE_KINGDOM_OF = re.compile(r"the kingdom of", re.IGNORECASE)
REGEX_SUB_AUSTRIA_HUNGARY = re.compile(r"austria-hungary", re.IGNORECASE)
REGEX_SUB_AUSTRIA_HUNGARY_2 = re.compile(r"austria hungary", re.IGNORECASE)
REGEX_SUB_UNMANNED_MILITARY_AIRCRAFT = re.compile(r"unmanned military aircraft of", re.IGNORECASE)
REGEX_SUB_UNMANNED_AERIAL_VEHICLES = re.compile(r"unmanned aerial vehicles of", re.IGNORECASE)
REGEX_SUB_DEMOCRATIC_REPUBLIC_CONGO = re.compile(r"democratic republic of congo", re.IGNORECASE)
REGEX_SUB_REPUBLIC_CONGO = re.compile(r"republic of congo", re.IGNORECASE)
REGEX_SUB_ATHLETICS = re.compile(r"athletics \(track and field\)", re.IGNORECASE)
REGEX_SUB_TWIN_PEOPLE = re.compile(r"twin people", re.IGNORECASE)
REGEX_SUB_PERCENT27 = re.compile(r"\%27", re.IGNORECASE)
REGEX_SUB_CATEGORY_MINISTERS = re.compile(r"category\:ministers of ", re.IGNORECASE)
REGEX_SUB_ASSOCIATION_FOOTBALL_AFC = re.compile(r"association football afc", re.IGNORECASE)
REGEX_SUB_ASSOCIATION_FOOTBALL = re.compile(r"association football", re.IGNORECASE)

# Precompiled regex patterns for CHANGE_KEY_MAPPINGS and CHANGE_KEY_SECONDARY will be created in change_cat function
# since they depend on imported dictionaries that may not be fully populated at module level

# ---
for_table = {
    "for national teams": "للمنتخبات الوطنية",
    "for member-of-parliament": "لعضوية البرلمان",
}
# ---
# ---
Dont_Add_min = [
    "women of",
    "founders of",
]
# ---
ar_lab_before_year_to_add_in = [
    # لإضافة "في" بين البداية والسنة في تصنيفات مثل :
    # tab[Category:1900 rugby union tournaments for national teams] = "تصنيف:بطولات اتحاد رغبي للمنتخبات الوطنية 1900"
    "كتاب بأسماء مستعارة",
    "بطولات اتحاد رغبي للمنتخبات الوطنية",
]
# ---
country_before_year = [
    "men's road cycling",
    "women's road cycling",
    "track cycling",
    "motorsport",
    "pseudonymous writers",
    "space",
    "disasters",
    "spaceflight",
    "inventions",
    "sports",
    "introductions",
    "discoveries",
    "comics",
    "nuclear history",
    "military history",
    "military alliances",
]
# ---
# ---Tour de
# category = re.sub(r" {}".format(chk) , " {}".format(chk_lab) , category )
# category = re.sub(r"{} ".format(chk) , "{} ".format(chk_lab) , category )
# ---
Tabl_with_in = {
    "sport in": "الرياضة في",
    # "conversion to" : "التحول إلى",
}
# --- Tour de
pp_start_with = {
    "wikipedia categories named after": "تصنيفات سميت بأسماء {}",
    "candidates for president of": "مرشحو رئاسة {}",
    # "candidates in president of" : "مرشحو رئاسة {}",
    "candidates-for": "مرشحو {}",
    # "candidates for" : "مرشحو {}",
    "categories named afters": "تصنيفات سميت بأسماء {}",
    "scheduled": "{} مقررة",
    # "defunct" : "{} سابقة",
}
# ---
pp_ends_with = {}
pp_ends_with_pase = {
    "-related professional associations": "جمعيات تخصصية متعلقة ب{}",
    "-related media": "إعلام متعلق ب{}",
    "-related lists": "قوائم متعلقة ب{}",
    "with disabilities": "{} بإعاقات",
    " mens tournament": "{} - مسابقة الرجال",
    " - telugu": "{} - تيلوغوي",
    "first division": "{} الدرجة الأولى",
    "second division": "{} الدرجة الثانية",
    "third division": "{} الدرجة الثالثة",
    "forth division": "{} الدرجة الرابعة",
    "candidates": "مرشحو {}",
    "candidates for": "مرشحو {} في",
    "squad": "تشكيلة {}",
    "squads": "تشكيلات {}",
    "final tournaments": "نهائيات مسابقات {}",
    "finals": "نهائيات {}",
    " - kannada": "{} - كنادي",
    " - tamil": "{} - تاميلي",
    " - qualifying": "{} - التصفيات",  # – Mixed Doubles
    " - mixed doubles": "{} - زوجي مختلط",  # – Mixed Doubles
    " - men's tournament": "{} - مسابقة الرجال",
    " - women's tournament": "{} - مسابقة السيدات",
    " - men's qualification": "{} - تصفيات الرجال",
    " - women's qualification": "{} - تصفيات السيدات",
    " – kannada": "{} – كنادي",
    " – tamil": "{} – تاميلي",
    " – qualifying": "{} – التصفيات",  # – Mixed Doubles
    " – mixed doubles": "{} – زوجي مختلط",  # – Mixed Doubles
    " – men's tournament": "{} – مسابقة الرجال",
    " – women's tournament": "{} – مسابقة السيدات",
    " womens tournament": "{} – مسابقة السيدات",
    " – men's qualification": "{} – تصفيات الرجال",
    " – women's qualification": "{} – تصفيات السيدات",
}
# ---
# "mixed doubles" : " زوجي مختلط",
# "mixed team" : " فريق مختلط",
#  "womens team" : " فريق سيدات",
#  "mens team" : " فريق رجال",
#   "womens tournament" : " منافسة السيدات",
#   "mens tournament" : " منافسة الرجال",
# ---
key_5_suff = {
    "tournament": "مسابقة",
    "singles": "فردي",
    "qualification": "تصفيات",
    "team": "فريق",
    "doubles": "زوجي",
}
# ---
key_2_3 = {
    "girls": "فتيات",
    "mixed": "مختلط",
    "boys": "فتيان",
    "singles": "فردي",
    "womens": "سيدات",
    "ladies": "سيدات",
    "males": "رجال",
    "men's": "رجال",
}
fix_o = {
    # "squad navigational boxes": "صناديق تصفح تشكيلات",
    "squads navigational boxes": "صناديق تصفح تشكيلات",
    "navigational boxes": "صناديق تصفح",
    "bids": "ترشيحات",
    "episodes": "حلقات",
    "treaties": "معاهدات",
    "leagues seasons": "مواسم دوريات",
    "leagues": "دوريات",
    "seasons": "مواسم",
    "local elections": "انتخابات محلية",
    "presidential elections": "انتخابات رئاسية",
    "presidential primaries": "انتخابات رئاسية تمهيدية",
    "elections": "انتخابات",
    "champions": "أبطال",
    "organizations": "منظمات",
    "nonprofits": "منظمات غير ربحية",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "applications": "تطبيقات",
    "employees": "موظفو",
    "resolutions": "قرارات",
    # "ministries" : "وزارات",
    "campaigns": "حملات",
    "referees": "حكام",
    # "films" : "أفلام",
    "squad templates": "قوالب تشكيلات",
    "templates": "قوالب",
    "venues": "ملاعب",
    "stadiums": "استادات",
    "managers": "مدربو",
    "trainers": "مدربو",
    "scouts": "كشافة",
    "coaches": "مدربو",
    "teams": "فرق",
    "owners": "ملاك",
    "owners and executives": "رؤساء تنفيذيون وملاك {}",
    "uniforms": "بدلات",
    "announcers": "مذيعو",
    "playoffs": "تصفيات",
    "genres": "أنواع",
    "leaks": "تسريبات",
    "categories": "تصانيف",
    "qualification": "تصفيات",
    "counties": "مقاطعات",
    # "religious occupations": "مهن دينية",
    # "occupations": "مهن",
    "equipment": "معدات",
    "trophies and awards": "جوائز وإنجازات",
    "logos": "شعارات",
    "tactics and skills": "مهارات",
    "terminology": "مصطلحات",
    "variants": "أشكال",
}

pop_format33 = {
    "qualification for the": "تصفيات {} مؤهلة إلى {} ",
    "qualification for": "تصفيات {} مؤهلة إلى {} ",
}
# ---
pop_format = {
    "prehistory of": "{} ما قبل التاريخ",
    "naval units and formations of": "وحدات وتشكيلات {} البحرية",
    "military units and formations of": "وحدات وتشكيلات {} العسكرية",
    "the university of": "جامعة {}",
    "university of arts": "جامعة {} للفنون",
    "the university of arts": "جامعة {} للفنون",
    "university of": "جامعة {}",
    # "university of technology" : "جامعة {} للتكنولوجيا" ,
    "university of art": "جامعة {} للفنون",
    "military installations of": "منشآت {} العسكرية",
    "politics of": "سياسة {}",
    "acting presidents of": "رؤساء {} بالإنابة",
    "diplomatic missions of": "بعثات {} الدبلوماسية",
    "umayyad governors of": "ولاة {} الأمويون",
    "sports-events": "أحداث {} الرياضة",
    "fictional presidents of": "رؤساء {} الخياليون",
    "political history of": "تاريخ {} السياسي",
    "early-modern history of": "تاريخ {} الحديث المبكر",
    "early modern history of": "تاريخ {} الحديث المبكر",
    "modern history of": "تاريخ {} الحديث",
    "contemporary history of": "تاريخ {} المعاصر",
    "economic history of": "تاريخ {} الاقتصادي",
    "cultural history of": "تاريخ {} الثقافي",
    "geographic history of": "تاريخ {} الجغرافي",
    "military history of": "تاريخ {} العسكري",
    "ancient history of": "تاريخ {} القديم",
    "legal history of": "تاريخ {} القانوني",
    "islamic history of": "تاريخ {} الإسلامي",
    "demographic history of": "تاريخ {} الديموغرافي",
    "naval history of": "تاريخ {} العسكري البحري",
    "maritime history of": "تاريخ {} البحري",
    "natural history of": "تاريخ {} الطبيعي",
    "bilateral relations of": "علاقات {} الثنائية",
    "bilateral military relations of": "علاقات {} الثنائية العسكرية",
    "social history of": "تاريخ {} الاجتماعي",
    "foreign relations of": "علاقات {} الخارجية",
    "sports in": "الرياضة في {}",
    "national symbols of": "رموز {} الوطنية",
    "political history": "تاريخ {} السياسي",
    "nuclear history": "تاريخ {} النووي",
    "military history": "تاريخ {} العسكري",
    "natural history": "تاريخ {} الطبيعي",
    "social history": "تاريخ {} الاجتماعي",
    "military-equipment of": "عتاد {} العسكري",
    "permanent delegates of": "مندوبو {} الدائمون",
    "permanent representatives of": "مندوبو {} الدائمون",
    "military equipment of": "عتاد {} العسكري",
    "foreign relations": "علاقات {} الخارجية",
    "grand prix": "جائزة {} الكبرى",
    "motorcycle grand prix": "جائزة {} الكبرى للدراجات النارية",
    # "law" : "قانون {}" ,
}
# ---
pop_format2 = {
    "politics of {}": "سياسة {}",
    "military installations of": "منشآت {} العسكرية",
}
# ---
fof = "{}"
# ---
for start, start_lab in key_2_3.items():
    for suff, suff_lab in key_5_suff.items():
        ke = f" - {start} {suff}"
        lab_ke = f"{fof} - {suff_lab} {start_lab}"
        pp_ends_with[ke] = lab_ke
# ---
for i, i_lab in fix_o.items():
    pp_ends_with[f" {i}"] = i_lab + " {}"

replaces = {
    "election, " : "election ",
    "national women's youth": "national youth women's",
    "national youth women's": "national youth women's",
    "women's youth national": "national youth women's",
    "women's national youth": "national youth women's",
    "youth national women's": "national youth women's",
    "youth women's national": "national youth women's",
    "national women's junior": "national junior women's",
    "national junior women's": "national junior women's",
    "women's junior national": "national junior women's",
    "women's national junior": "national junior women's",
    "junior women's national": "national junior women's",
    "national men's junior": "national junior men's",
    "national junior men's": "national junior men's",
    "men's junior national": "national junior men's",
    "men's national junior": "national junior men's",
    "junior men's national": "national junior men's",
    " men's national": " national men's",
    "women's national": "national women's",
    "junior national": "national junior",
    "youth national": "national youth",
    "amateur national": "national amateur",
    "heads of mission ": "heads-of-mission ",
    "house of commons of canada": "house-of-commons-of-canada",
}


def change_cat(cat_orginal: str) -> str:
    """
    Transform and normalize category names by applying various regex patterns and replacements.

    Args:
        cat_orginal: Original category string to transform

    Returns:
        Transformed category string
    """
    cat_orginal = cat_orginal.lower().strip()
    category = cat_orginal

    category = re.sub(r"\bthe\b", "", category, flags=re.IGNORECASE).strip()

    # Normalize whitespace
    category = REGEX_SUB_WHITESPACE.sub(" ", category)

    # Normalize century and millennium formatting
    category = REGEX_SUB_CENTURY.sub(" century", category)
    category = REGEX_SUB_MILLENNIUM.sub(" millennium", category)
    category = REGEX_SUB_MILLENNIUM_CENTURY.sub(r" \g<1>", category)

    # Reorder royal military force names
    category = REGEX_SUB_ROYAL_DEFENCE_FORCE.sub(r"\g<1> royal defence force", category)
    category = REGEX_SUB_ROYAL_NAVAL_FORCE.sub(r"\g<1> royal naval force", category)
    category = REGEX_SUB_ROYAL_NAVY.sub(r"\g<1> royal navy", category)
    category = REGEX_SUB_ROYAL_AIR_FORCE.sub(r"\g<1> royal air force", category)

    # Apply various normalization patterns
    category = REGEX_SUB_EXPATRIATE_PEOPLE.sub(r"\g<1> expatriate \g<2> peoplee in ", category)
    category = REGEX_SUB_ORGANISATIONS.sub("organizations", category)
    category = REGEX_SUB_RUS.sub("rus", category)
    category = REGEX_SUB_THE_KINGDOM_OF.sub(" kingdom of", category)
    category = REGEX_SUB_AUSTRIA_HUNGARY.sub("austria hungary", category)
    category = REGEX_SUB_AUSTRIA_HUNGARY_2.sub("austria hungary", category)
    category = REGEX_SUB_UNMANNED_MILITARY_AIRCRAFT.sub("unmanned military aircraft-of", category)
    category = REGEX_SUB_UNMANNED_AERIAL_VEHICLES.sub("unmanned aerial vehicles-of", category)
    category = REGEX_SUB_DEMOCRATIC_REPUBLIC_CONGO.sub("democratic-republic-of-congo", category)
    category = REGEX_SUB_REPUBLIC_CONGO.sub("republic-of-congo", category)
    category = REGEX_SUB_ATHLETICS.sub("track-and-field athletics", category)
    category = REGEX_SUB_TWIN_PEOPLE.sub("twinpeople", category)
    category = REGEX_SUB_PERCENT27.sub("'", category)

    # Apply simple string replacements
    simple_replacements = {
        "secretaries of ": "secretaries-of ",
        "sportspeople": "sports-people",
        "roller hockey (quad)": "roller hockey",
        "victoria (australia)": "victoria-australia",
        "party of ": "party-of ",
        " uu-16 ": " u-16 ",
    }
    for old, new in simple_replacements.items():
        category = category.replace(old, new)

    # Apply replaces dictionary
    for x, d in replaces.items():
        category = category.replace(x, d)

    category = change_key_secondary_replacements(category)
    category = change_key_mappings_replacements(category)

    # Final transformations
    category = REGEX_SUB_CATEGORY_MINISTERS.sub("category:ministers-of ", category)
    category = REGEX_SUB_ASSOCIATION_FOOTBALL_AFC.sub("association-football afc", category)
    category = REGEX_SUB_ASSOCIATION_FOOTBALL.sub("football", category)

    # Log changes if any
    if category != cat_orginal:
        logger.info(f'change_cat to :"{category}", orginal: {cat_orginal}.')

    return category


len_print.data_len("pop_format.py", {
    "CHANGE_KEY_MAPPINGS": CHANGE_KEY_MAPPINGS,
    "CHANGE_KEY_SECONDARY": CHANGE_KEY_SECONDARY
})

__all__ = [
    "Dont_Add_min",
    "Tabl_with_in",
    "category_relation_mapping",
    "ar_lab_before_year_to_add_in",
    "change_cat",
    "country_before_year",
    "for_table",
    "pop_format",
    "pop_format2",
    "pop_format33",
    "pp_ends_with",
    "pp_ends_with_pase",
    "pp_start_with",
]
