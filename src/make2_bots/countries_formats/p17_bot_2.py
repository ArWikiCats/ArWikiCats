""" """

import re

from ...helps.log import logger
from ...translations import (
    countries_nat_en_key,
    en_is_P17_ar_is_al_women,
    en_is_P17_ar_is_mens,
)
from .utils import add_definite_article


def _resolve_p17_2_label(category: str, templates: dict, nat_key: str, add_article: bool = False) -> str:
    """Resolve gendered nationality templates for P17-style categories."""
    for suffix1, template in templates.items():
        suffix_key = f" {suffix1.strip().lower()}"

        if not category.lower().endswith(suffix_key):
            continue

        country_prefix = category[: -len(suffix_key)].strip()

        nat_data = countries_nat_en_key.get(country_prefix) or countries_nat_en_key.get(country_prefix.lower(), {})
        nat_label = nat_data.get(nat_key, "")

        if not nat_label:
            logger.info(f"<<lightblue>>>>>> No {nat_key} label for {country_prefix}")
            continue

        if add_article:
            nat_label = add_definite_article(nat_label)

        logger.debug(f'<<lightblue>>>>>> {nat_key}: "{nat_label}" ')
        resolved_label = template.format(nat_label)

        logger.debug(f'<<lightblue>>>>>> {nat_key} template match: new cnt_la "{resolved_label}" ')
        return resolved_label

    return ""


def Get_P17_2(category: str) -> str:  # الإنجليزي اسم البلد والعربي جنسية رجال
    """
    Category input in english is country name, return arabic as mens nationality.

    Return a nationality-based label for categories ending with country names.

    Example:
        mens: [Category:United States government officials] = "تصنيف:مسؤولون حكوميون أمريكيون"
        women: [Category:syria air force] = "تصنيف:القوات الجوية السورية
    """
    logger.info(f'<<lightblue>>>>>> Get_P17_2 "{category}" ')  # ""

    # resolved mens:
    resolved_label = _resolve_p17_2_label(category, en_is_P17_ar_is_mens, "mens")

    if not resolved_label:
        resolved_label = _resolve_p17_2_label(category, en_is_P17_ar_is_al_women, "women", add_article=True)

    return resolved_label


__all__ = [
    "Get_P17_2",
    "_resolve_p17_2_label",
]
