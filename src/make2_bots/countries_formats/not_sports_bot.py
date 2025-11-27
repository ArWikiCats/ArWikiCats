#!/usr/bin/python3
""" """
from ...translations_formats.format_data import FormatData
from ...translations import contries_from_nat

SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT: dict[str, str] = {
    "{en} cup": "كأس {ar}",
    "{en} presidents": "رؤساء {ar}",
    "{en} territorial officials": "مسؤولو أقاليم {ar}",
    "{en} territorial judges": "قضاة أقاليم {ar}",
    "{en} war": "حرب {ar}",
    "{en} war and conflict": "حروب ونزاعات {ar}",
    "{en} governorate": "حكومة {ar}",
}

nat_bot = FormatData(
    SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT,
    contries_from_nat,
    key_placeholder="{en}",
    value_placeholder="{ar}",
)


def resolve_SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT(category: str):
    return nat_bot.search(category)


__all__ = [
    "resolve_SPORT_FORMTS_EN_AR_IS_P17_NOT_SPORT",
]
