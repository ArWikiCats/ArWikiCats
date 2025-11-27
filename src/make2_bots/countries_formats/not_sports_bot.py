#!/usr/bin/python3
""" """
from ...translations_formats.format_data import FormatData
from ...translations import contries_from_nat

en_is_P17_ar_is_P17: dict[str, str] = {
    "{en} cup": "كأس {ar}",
    "{en} presidents": "رؤساء {ar}",
    "{en} territorial officials": "مسؤولو أقاليم {ar}",
    "{en} territorial judges": "قضاة أقاليم {ar}",
    "{en} war": "حرب {ar}",
    "{en} war and conflict": "حروب ونزاعات {ar}",
    "{en} governorate": "حكومة {ar}",
}

nat_bot = FormatData(
    en_is_P17_ar_is_P17,
    contries_from_nat,
    key_placeholder="{en}",
    value_placeholder="{ar}",
)


def resolve_en_is_P17_ar_is_P17(category: str):
    return nat_bot.search(category)


__all__ = [
    "resolve_en_is_P17_ar_is_P17",
]
