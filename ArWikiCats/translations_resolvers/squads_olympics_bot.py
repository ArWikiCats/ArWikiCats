#!/usr/bin/python3
""" """
from ..translations_formats.DataModel.format_data import FormatData
from ..translations import contries_from_nat

en_is_P17_ar_is_P17_SPORTS: dict[str, str] = {
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
    en_is_P17_ar_is_P17_SPORTS,
    contries_from_nat,
    key_placeholder="{en}",
    value_placeholder="{ar}",
)


def resolve_en_is_P17_ar_is_P17_SPORTS(category: str):
    return nat_bot.search(category)


__all__ = [
    "resolve_en_is_P17_ar_is_P17_SPORTS",
]
