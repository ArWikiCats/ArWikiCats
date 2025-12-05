""" """

import functools

from ...helps.log import logger
from ...translations import (
    countries_nat_en_key,
    en_is_P17_ar_is_al_women,
    en_is_P17_ar_is_mens,
)
from .utils import resolve_p17_2_label


@functools.lru_cache(maxsize=10000)
def get_p17_2(category: str) -> str:  # الإنجليزي اسم البلد والعربي جنسية رجال
    """
    Category input in english is country name, return arabic as males nationality.

    Return a nationality-based label for categories ending with country names.

    Example:
        males: [Category:United States government officials] = "تصنيف:مسؤولون حكوميون أمريكيون"
        women: [Category:syria air force] = "تصنيف:القوات الجوية السورية
    """
    logger.info(f'<<lightblue>>>>>> get_p17_2 "{category}" ')  # ""

    # resolved males:
    resolved_label = resolve_p17_2_label(category, en_is_P17_ar_is_mens, "males", countries_nat_en_key)

    if not resolved_label:
        resolved_label = resolve_p17_2_label(category, en_is_P17_ar_is_al_women, "female", countries_nat_en_key, add_article=True)

    return resolved_label


__all__ = [
    "get_p17_2",
]
