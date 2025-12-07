#!/usr/bin/python3
""" """
from ..translations_formats import FormatData
from ..translations import countries_from_nat

en_is_P17_ar_is_P17: dict[str, str] = {
    "Olympic gold medalists for {en} in alpine skiing": "فائزون بميداليات ذهبية أولمبية من {ar} في التزلج على المنحدرات الثلجية",
    "{en} board members": "أعضاء مجلس {ar}",
    # "accidental deaths from falls in {en}": "وفيات عرضية نتيجة السقوط في {ar}",
    "{en} conflict": "نزاع {ar}",
    "{en} cup": "كأس {ar}",
    "{en} elections": "انتخابات {ar}",
    "{en} executive cabinet": "مجلس وزراء {ar} التنفيذي",
    "{en} government personnel": "موظفي حكومة {ar}",
    "{en} government": "حكومة {ar}",
    "{en} governorate": "محافظة {ar}",
    "{en} political leader": "قادة {ar} السياسيون",
    "{en} presidents": "رؤساء {ar}",
    "{en} responses": "استجابات {ar}",
    "{en} territorial judges": "قضاة أقاليم {ar}",
    "{en} territorial officials": "مسؤولو أقاليم {ar}",
    "{en} war and conflict": "حروب ونزاعات {ar}",
    "{en} war": "حرب {ar}",
    "{en} afc women's asian cup squad": "تشكيلات {ar} في كأس آسيا للسيدات",
    "{en} afc asian cup squad": "تشكيلات {ar} في كأس آسيا",
    "{en} fifa world cup squad": "تشكيلات {ar} في كأس العالم",
    "{en} fifa futsal world cup squad": "تشكيلات {ar} في كأس العالم لكرة الصالات",
    "{en} summer olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الصيفية",
    "{en} winter olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الشتوية",
    "{en} olympics squad": "تشكيلات {ar} في الألعاب الأولمبية",
    "{en} summer olympics": " {ar} في الألعاب الأولمبية الصيفية",
    "{en} winter olympics": " {ar} في الألعاب الأولمبية الشتوية",
}

nat_bot = FormatData(
    en_is_P17_ar_is_P17,
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
