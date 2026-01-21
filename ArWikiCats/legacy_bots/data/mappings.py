"""
Centralized data mappings for legacy bots.

This module contains all major dictionaries and mapping tables extracted from
various modules to provide a single source of truth for data lookups.

IMPORTANT: This is a pure data file with NO imports from other legacy_bots modules.
"""

from __future__ import annotations

# ============================================================================
# NUMBER TRANSLATIONS (from legacy_utils/numbers1.py)
# ============================================================================

change_numb_to_word = {
    "100": "المئة",
    "200": "المائتين",
    "300": "الثلاثمائة",
}

change_numb = {
    "1": "الأول",
    "2": "الثاني",
    "3": "الثالث",
    "4": "الرابع",
    "5": "الخامس",
    "6": "السادس",
    "7": "السابع",
    "8": "الثامن",
    "9": "التاسع",
    "10": "العاشر",
    "11": "الحادي عشر",
    "12": "الثاني عشر",
    "13": "الثالث عشر",
    "14": "الرابع عشر",
    "15": "الخامس عشر",
    "16": "السادس عشر",
    "17": "السابع عشر",
    "18": "الثامن عشر",
    "19": "التاسع عشر",
    "20": "العشرون",
    "21": "الحادي والعشرون",
    "22": "الثاني والعشرون",
    "23": "الثالث والعشرون",
    "24": "الرابع والعشرون",
    "25": "الخامس والعشرون",
    "26": "السادس والعشرون",
    "27": "السابع والعشرون",
    "28": "الثامن والعشرون",
    "29": "التاسع والعشرون",
    "30": "الثلاثون",
    "31": "الحادي والثلاثون",
    "32": "الثاني والثلاثون",
    "33": "الثالث والثلاثون",
    "34": "الرابع والثلاثون",
    "35": "الخامس والثلاثون",
    "36": "السادس والثلاثون",
    "37": "السابع والثلاثون",
    "38": "الثامن والثلاثون",
    "39": "التاسع والثلاثون",
    "40": "الأربعون",
    "41": "الحادي والأربعون",
    "42": "الثاني والأربعون",
    "43": "الثالث والأربعون",
    "44": "الرابع والأربعون",
    "45": "الخامس والأربعون",
    "46": "السادس والأربعون",
    "47": "السابع والأربعون",
    "48": "الثامن والأربعون",
    "49": "التاسع والأربعون",
    "50": "الخمسون",
    "51": "الحادي والخمسون",
    "52": "الثاني والخمسون",
    "53": "الثالث والخمسون",
    "54": "الرابع والخمسون",
    "55": "الخامس والخمسون",
    "56": "السادس والخمسون",
    "57": "السابع والخمسون",
    "58": "الثامن والخمسون",
    "59": "التاسع والخمسون",
    "60": "الستون",
    "61": "الحادي والستون",
    "62": "الثاني والستون",
    "63": "الثالث والستون",
    "64": "الرابع والستون",
    "65": "الخامس والستون",
    "66": "السادس والستون",
    "67": "السابع والستون",
    "68": "الثامن والستون",
    "69": "التاسع والستون",
    "70": "السبعون",
    "71": "الحادي والسبعون",
    "72": "الثاني والسبعون",
    "73": "الثالث والسبعون",
    "74": "الرابع والسبعون",
    "75": "الخامس والسبعون",
    "76": "السادس والسبعون",
    "77": "السابع والسبعون",
    "78": "الثامن والسبعون",
    "79": "التاسع والسبعون",
    "80": "الثمانون",
    "81": "الحادي والثمانون",
    "82": "الثاني والثمانون",
    "83": "الثالث والثمانون",
    "84": "الرابع والثمانون",
    "85": "الخامس والثمانون",
    "86": "السادس والثمانون",
    "87": "السابع والثمانون",
    "88": "الثامن والثمانون",
    "89": "التاسع والثمانون",
    "90": "التسعون",
    "91": "الحادي والتسعون",
    "92": "الثاني والتسعون",
    "93": "الثالث والتسعون",
    "94": "الرابع والتسعون",
    "95": "الخامس والتسعون",
    "96": "السادس والتسعون",
    "97": "السابع والتسعون",
    "98": "الثامن والتسعون",
    "99": "التاسع والتسعون",
}

# Build extended number mappings (hundreds variations)
for number_key, arabic_label in change_numb.items():
    change_numb_to_word[number_key] = arabic_label
    extended_hundreds_key = number_key
    if len(number_key) == 1:
        extended_hundreds_key = f"10{number_key}"
    if len(number_key) == 2:
        extended_hundreds_key = f"1{number_key}"
    change_numb_to_word[extended_hundreds_key] = f"{arabic_label} بعد المئة"

    extended_two_hundred_key = number_key
    if len(number_key) == 1:
        extended_two_hundred_key = f"20{number_key}"
    if len(number_key) == 2:
        extended_two_hundred_key = f"2{number_key}"
    change_numb_to_word[extended_two_hundred_key] = f"{arabic_label} بعد المائتين"

    extended_three_hundred_key = number_key
    if len(number_key) == 1:
        extended_three_hundred_key = f"30{number_key}"
    if len(number_key) == 2:
        extended_three_hundred_key = f"3{number_key}"
    change_numb_to_word[extended_three_hundred_key] = f"{arabic_label} بعد الثلاثمائة"


# ============================================================================
# SUFFIX MAPPINGS (from legacy_utils/ends_keys.py)
# ============================================================================

pp_ends_with_pase = {
    " - telugu": "{} - تيلوغوي",
    " - boys doubles": "{} - زوجي فتيان",
    " - boys qualification": "{} - تصفيات فتيان",
    " - boys singles": "{} - فردي فتيان",
    " - boys team": "{} - فريق فتيان",
    " - boys tournament": "{} - مسابقة فتيان",
    " - girls doubles": "{} - زوجي فتيات",
    " - girls qualification": "{} - تصفيات فتيات",
    " - girls singles": "{} - فردي فتيات",
    " - girls team": "{} - فريق فتيات",
    " - girls tournament": "{} - مسابقة فتيات",
    " - kannada": "{} - كنادي",
    " - ladies doubles": "{} - زوجي سيدات",
    " - ladies qualification": "{} - تصفيات سيدات",
    " - ladies singles": "{} - فردي سيدات",
    " - ladies team": "{} - فريق سيدات",
    " - ladies tournament": "{} - مسابقة سيدات",
    " - males doubles": "{} - زوجي رجال",
    " - males qualification": "{} - تصفيات رجال",
    " - males singles": "{} - فردي رجال",
    " - males team": "{} - فريق رجال",
    " - males tournament": "{} - مسابقة رجال",
    " - men's doubles": "{} - زوجي رجال",
    " - men's qualification": "{} - تصفيات الرجال",
    " - men's singles": "{} - فردي رجال",
    " - men's team": "{} - فريق رجال",
    " - men's tournament": "{} - مسابقة الرجال",
    " - mixed doubles": "{} - زوجي مختلط",
    " - mixed qualification": "{} - تصفيات مختلط",
    " - mixed singles": "{} - فردي مختلط",
    " - mixed team": "{} - فريق مختلط",
    " - mixed tournament": "{} - مسابقة مختلط",
    " - qualifying": "{} - التصفيات",
    " - singles doubles": "{} - زوجي فردي",
    " - singles qualification": "{} - تصفيات فردي",
    " - singles singles": "{} - فردي فردي",
    " - singles team": "{} - فريق فردي",
    " - singles tournament": "{} - مسابقة فردي",
    " - tamil": "{} - تاميلي",
    " - women's qualification": "{} - تصفيات السيدات",
    " - women's tournament": "{} - مسابقة السيدات",
    " - womens doubles": "{} - زوجي سيدات",
    " - womens qualification": "{} - تصفيات سيدات",
    " - womens singles": "{} - فردي سيدات",
    " - womens team": "{} - فريق سيدات",
    " - womens tournament": "{} - مسابقة سيدات",
    " – kannada": "{} – كنادي",
    " – men's qualification": "{} – تصفيات الرجال",
    " – men's tournament": "{} – مسابقة الرجال",
    " – mixed doubles": "{} – زوجي مختلط",
    " – qualifying": "{} – التصفيات",
    " – tamil": "{} – تاميلي",
    " – women's qualification": "{} – تصفيات السيدات",
    " – women's tournament": "{} – مسابقة السيدات",
}

pp_ends_with = {
    " womens tournament": "{} – مسابقة السيدات",
    " mens tournament": "{} - مسابقة الرجال",
    "-related lists": "قوائم متعلقة ب{}",
    "-related media": "إعلام متعلق ب{}",
    "-related professional associations": "جمعيات تخصصية متعلقة ب{}",
    "candidates": "مرشحو {}",
    "final tournaments": "نهائيات مسابقات {}",
    "finals": "نهائيات {}",
    "first division": "{} الدرجة الأولى",
    "forth division": "{} الدرجة الرابعة",
    "second division": "{} الدرجة الثانية",
    "squad": "تشكيلة {}",
    "squads": "تشكيلات {}",
    "third division": "{} الدرجة الثالثة",
    "with disabilities": "{} بإعاقات",
    " announcers": "مذيعو {}",
    " applications": "تطبيقات {}",
    " bids": "ترشيحات {}",
    " campaigns": "حملات {}",
    " categories": "تصانيف {}",
    " champions": "أبطال {}",
    " coaches": "مدربو {}",
    " counties": "مقاطعات {}",
    " elections": "انتخابات {}",
    " employees": "موظفو {}",
    " episodes": "حلقات {}",
    " equipment": "معدات {}",
    " genres": "أنواع {}",
    " leagues": "دوريات {}",
    " leagues seasons": "مواسم دوريات {}",
    " local elections": "انتخابات محلية {}",
    " logos": "شعارات {}",
    " managers": "مدربو {}",
    " navigational boxes": "صناديق تصفح {}",
    " non-profit organizations": "منظمات غير ربحية {}",
    " non-profit publishers": "ناشرون غير ربحيون {}",
    " nonprofits": "منظمات غير ربحية {}",
    " organizations": "منظمات {}",
    " owners": "ملاك {}",
    " owners and executives": "رؤساء تنفيذيون وملاك {}",
    " playoffs": "تصفيات {}",
    " presidential elections": "انتخابات رئاسية {}",
    " presidential primaries": "انتخابات رئاسية تمهيدية {}",
    " qualification": "تصفيات {}",
    " referees": "حكام {}",
    " resolutions": "قرارات {}",
    " scouts": "كشافة {}",
    " seasons": "مواسم {}",
    " squad templates": "قوالب تشكيلات {}",
    " squads navigational boxes": "صناديق تصفح تشكيلات {}",
    " stadiums": "استادات {}",
    " tactics and skills": "مهارات {}",
    " teams": "فرق {}",
    " templates": "قوالب {}",
    " terminology": "مصطلحات {}",
    " trainers": "مدربو {}",
    " treaties": "معاهدات {}",
    " trophies and awards": "جوائز وإنجازات {}",
    " uniforms": "بدلات {}",
    " variants": "أشكال {}",
    " venues": "ملاعب {}",
}

combined_suffix_mappings = {**pp_ends_with_pase, **pp_ends_with}


# ============================================================================
# PREFIX MAPPINGS (from tmp_bot.py)
# ============================================================================

pp_start_with = {
    "wikipedia categories named after": "تصنيفات سميت بأسماء {}",
    "candidates for president of": "مرشحو رئاسة {}",
    "candidates-for": "مرشحو {}",
    "categories named afters": "تصنيفات سميت بأسماء {}",
    "scheduled": "{} مقررة",
}


# ============================================================================
# TYPE TABLE (from make_bots/bot.py)
# ============================================================================

typeTable_7: dict[str, str] = {
    "air force": "قوات جوية",
    "airlines accidents": "حوادث طيران",
    "aviation accident": "حوادث طيران",
    "aviation accidents": "حوادث طيران",
    "design institutions": "مؤسسات تصميم",
    "distance education institutions": "مؤسسات تعليم عن بعد",
    "executed-burning": "أعدموا شنقاً",
    "executed-decapitation": "أعدموا بقطع الرأس",
    "executed-firearm": "أعدموا بسلاح ناري",
    "executed-hanging": "أعدموا حرقاً",
    "executions": "إعدامات",
    "people executed by": "أشخاص أعدموا من قبل",
    "people executed-by-burning": "أشخاص أعدموا شنقاً",
    "people executed-by-decapitation": "أشخاص أعدموا بقطع الرأس",
    "people executed-by-firearm": "أشخاص أعدموا بسلاح ناري",
    "people executed-by-hanging": "أشخاص أعدموا حرقاً",
    "railway accident": "حوادث سكك حديد",
    "railway accidents": "حوادث سكك حديد",
    "road accidents": "حوادث طرق",
    "transport accident": "حوادث نقل",
    "transport accidents": "حوادث نقل",
    "transport disasters": "كوارث نقل",
}


__all__ = [
    "change_numb",
    "change_numb_to_word",
    "pp_ends_with_pase",
    "pp_ends_with",
    "combined_suffix_mappings",
    "pp_start_with",
    "typeTable_7",
]
