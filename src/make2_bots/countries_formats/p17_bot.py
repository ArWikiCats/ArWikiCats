""" """

import re

from ...helps.log import logger
from ...translations import (
    SPORT_FORMTS_EN_AR_IS_P17,
    Get_Sport_Format_xo_en_ar_is_P17,
    all_country_with_nat_keys_is_en,
    contries_from_nat,
    en_is_P17_ar_is_al_women,
    en_is_P17_ar_is_mens,
    en_is_P17_ar_is_P17,
)
from ..format_bots import category_relation_mapping, pop_format
from ..jobs_bots.get_helps import get_con_3
from ..matables_bots.bot import All_P17


def add_definite_article(label: str) -> str:
    """Prefix each word in ``label`` with the Arabic definite article."""
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label


def _resolve_p17_2_label(category: str, templates: dict, nat_key: str, add_article: bool = False) -> str:
    """Resolve gendered nationality templates for P17-style categories."""
    for suffix, template in templates.items():
        suffix_key = f" {suffix.strip().lower()}"
        if category.lower().endswith(suffix_key):
            country_prefix = category[: -len(suffix_key)].strip()

            nat_label = all_country_with_nat_keys_is_en.get(country_prefix, {}).get(nat_key, "")

            if nat_label:
                if add_article:
                    nat_label = add_definite_article(nat_label)

                logger.debug(f'<<lightblue>>>>>> {nat_key}: "{nat_label}" ')
                resolved_label = template.format(nat_label)
                logger.debug(f'<<lightblue>>>>>> {nat_key} template match: new cnt_la "{resolved_label}" ')
                return resolved_label
    return ""


def Get_P17_2(category: str) -> str:  # الإنجليزي اسم البلد والعربي جنسية رجال
    """
    Return a nationality-based label for categories ending with country names.

    Example: united states government officials
    """
    logger.info(f'<<lightblue>>>>>> Get_P17_2 "{category}" ')  # ""

    resolved_label = _resolve_p17_2_label(category, en_is_P17_ar_is_mens, "mens")

    if not resolved_label:
        resolved_label = _resolve_p17_2_label(category, en_is_P17_ar_is_al_women, "women", add_article=True)

    return resolved_label


def Get_P17(category: str) -> str:  # الإنجليزي جنسية والعربي اسم البلد
    """
    Resolve categories that start with nationality adjectives into country labels.

    TODO: use FormatData method
    """
    resolved_label = ""
    con_3_lab = ""
    country_start_lab = ""
    category = category.lower()

    con_3, country_start = get_con_3(category, "All_P17")
    country_start_lab = All_P17.get(country_start, "")

    if not con_3 and not country_start:
        con_3, country_start = get_con_3(category, "contries_from_nat")
        country_start_lab = contries_from_nat.get(country_start, "")

    if con_3 and country_start:
        logger.debug(f'<<lightpurple>>>>>> country_start_lab:"{country_start_lab}"')
        logger.debug(f'<<lightblue>> country_start:"{country_start}", con_3:"{con_3}"')

        FOF = ""
        if con_3 in category_relation_mapping:
            codd = category_relation_mapping[con_3]
            if codd.startswith("لل"):
                con_3_lab = "{} " + codd
                logger.debug(f'get lab from category_relation_mapping con_3_lab:"{con_3_lab}"')

        if not con_3_lab:
            con_3_lab = SPORT_FORMTS_EN_AR_IS_P17.get(con_3.strip(), "")
            if con_3_lab:
                FOF = "<<lightgreen>>SPORT_FORMTS_EN_AR_IS_P17<<lightblue>>"

        if not con_3_lab:
            con_3_lab = en_is_P17_ar_is_P17.get(con_3.strip(), "")

        if not con_3_lab:
            con_3_lab = Get_Sport_Format_xo_en_ar_is_P17(con_3.strip())

        if not con_3_lab:
            con_3_lab = pop_format.get(con_3, "")
            if con_3_lab:
                FOF = "<<lightgreen>>pop_format<<lightblue>>"

        if con_3_lab:
            if FOF:
                logger.debug(f'<<lightblue>>>>>> {FOF} .startswith({country_start}), con_3:"{con_3}"')
            if "{nat}" in con_3_lab:
                resolved_label = con_3_lab.format(nat=country_start_lab)
            else:
                resolved_label = con_3_lab.format(country_start_lab)

            logger.debug(f'<<lightblue>>>>>> Get_P17: test_60: new cnt_la "{resolved_label}" ')

        logger.debug(f'<<lightred>>>>>> con_3_lab: "{con_3_lab}", cnt_la :"{resolved_label}" == ""')

    else:
        logger.info(f'<<lightred>>>>>> con_3: "{con_3}" or country_start :"{country_start}" == ""')

    if resolved_label:
        logger.info(f'<<lightblue>>>>>> Get_P17 cnt_la "{resolved_label}" ')

    return resolved_label
