#!/usr/bin/python3
""" """
from ..translations_formats import FormatData
from ..translations import contries_from_nat

en_is_P17_ar_is_P17: dict[str, str] = {
    "{en} board members": "أعضاء مجلس {ar}",
    "{en} conflict": "نزاع {ar}",
    "{en} cup": "كأس {ar}",
    "{en} elections": "انتخابات {ar}",
    "{en} executive cabinet": "مجلس وزراء {ar} التنفيذي",
    "{en} government personnel": "موظفي حكومة {ar}",
    "{en} government": "حكومة {ar}",
    "{en} governorate": "حكومة {ar}",
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
    contries_from_nat,
    key_placeholder="{en}",
    value_placeholder="{ar}",
)


def resolve_by_contries_names(category: str) -> str:
    return nat_bot.search(category)


__all__ = [
    "resolve_by_contries_names",
]
