"""

SPORT_FORMTS_EN_AR_IS_P17: English country-name → Arabic country-name.

"""
import functools
from ...translations_formats import FormatData
from ...translations import countries_from_nat
from ..p17_sport_to_move_data import main_data
# from .p17_sport_to_move_under import main_data_under
# SPORT_FORMTS_EN_AR_IS_P17 = main_data | main_data_under


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatData:
    return FormatData(
        main_data,
        countries_from_nat,
        key_placeholder="{en}",
        value_placeholder="{ar}",
    )


# @dump_data(1)
@functools.lru_cache(maxsize=1000)
def get_en_ar_is_p17_label(category: str) -> str:
    nat_bot = _load_bot()
    return nat_bot.search(category)


__all__ = [
    "get_en_ar_is_p17_label",
]
