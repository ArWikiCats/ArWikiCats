#!/usr/bin/python3
"""
Resolve country names categories translations
"""
from ..translations_formats import FormatData
from ..translations import countries_from_nat
from ..make_bots.p17_sport_to_move_data import main_data

formatted_data_en_ar_only: dict[str, str] = {
    "{en}": "{ar}",
    "olympic gold medalists for {en}": "فائزون بميداليات ذهبية أولمبية من {ar}",
    "{en} women's international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم",
    "olympic gold medalists for {en} in alpine skiing": "فائزون بميداليات ذهبية أولمبية من {ar} في التزلج على المنحدرات الثلجية",

    "police of {en}": "شرطة {ar}",
    "army of {en}": "جيش {ar}",
    "national congress ({en})": "المؤتمر الوطني ({ar})",
    "national council ({en})": "المجلس الوطني ({ar})",
    "national assembly ({en})": "الجمعية الوطنية ({ar})",

    "senate ({en})": "مجلس الشيوخ ({ar})",
    "{en} general assembly": "جمعية {ar} العامة",
    "parliament of {en}": "برلمان {ar}",
    "accidental deaths from falls in {en}": "وفيات عرضية نتيجة السقوط في {ar}",
    "bodies of water of {en}": "مسطحات مائية في {ar}",
    "national university of {en}": "جامعة {ar} الوطنية",
    "national library of {en}": "مكتبة {ar} الوطنية",
    "{en} afc asian cup squad": "تشكيلات {ar} في كأس آسيا",
    "{en} afc women's asian cup squad": "تشكيلات {ar} في كأس آسيا للسيدات",
    "{en} board members": "أعضاء مجلس {ar}",
    "{en} conflict": "نزاع {ar}",
    "{en} cup": "كأس {ar}",
    "{en} elections": "انتخابات {ar}",
    "{en} executive cabinet": "مجلس وزراء {ar} التنفيذي",
    "{en} fifa futsal world cup squad": "تشكيلات {ar} في كأس العالم لكرة الصالات",
    "{en} fifa world cup squad": "تشكيلات {ar} في كأس العالم",
    "{en} government personnel": "موظفي حكومة {ar}",
    "{en} government": "حكومة {ar}",
    "{en} governorate": "محافظة {ar}",
    "{en} olympics squad": "تشكيلات {ar} في الألعاب الأولمبية",
    "{en} political leader": "قادة {ar} السياسيون",
    "{en} presidents": "رؤساء {ar}",
    "{en} responses": "استجابات {ar}",
    "{en} summer olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الصيفية",
    "{en} summer olympics": " {ar} في الألعاب الأولمبية الصيفية",
    "{en} territorial judges": "قضاة أقاليم {ar}",
    "{en} territorial officials": "مسؤولو أقاليم {ar}",
    "{en} war and conflict": "حروب ونزاعات {ar}",
    "{en} war": "حرب {ar}",
    "{en} winter olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الشتوية",
    "{en} winter olympics": " {ar} في الألعاب الأولمبية الشتوية",
}

formatted_data_en_ar_only.update(main_data)

nat_bot = FormatData(
    formatted_data_en_ar_only,
    countries_from_nat,
    key_placeholder="{en}",
    value_placeholder="{ar}",
    text_before="the ",
)


def resolve_by_countries_names(category: str) -> str:
    normalized_category = category.lower().replace("category:", "")

    result = nat_bot.search(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    return result


__all__ = [
    "resolve_by_countries_names",
]
