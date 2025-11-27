#!/usr/bin/python3
""" """
from ...translations_formats.format_data import FormatData
from ...translations import contries_from_nat

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
