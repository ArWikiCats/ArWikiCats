""" """

import re

from ...helps.log import logger
from ...helps.jsonl_dump import dump_data
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
from ..jobs_bots.get_helps import get_suffix
from ..matables_bots.bot import All_P17


@dump_data(enable=True)
def add_definite_article(label: str) -> str:
    """Prefix each word in ``label`` with the Arabic definite article."""
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label


def _resolve_p17_2_label(category: str, templates: dict, nat_key: str, add_article: bool = False) -> str:
    """Resolve gendered nationality templates for P17-style categories."""
    for suffix1, template in templates.items():
        suffix_key = f" {suffix1.strip().lower()}"
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


@dump_data(enable=True)
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


@dump_data(enable=True)
def Get_P17(category: str) -> str:  # الإنجليزي جنسية والعربي اسم البلد
    """
    Resolve categories that start with nationality adjectives into country labels.

    TODO: use FormatData method
    """
    resolved_label = ""
    con_3_lab = ""
    country_start_lab = ""
    category = category.lower()

    suffix, country_start = get_suffix(category, "All_P17")
    country_start_lab = All_P17.get(country_start, "")

    if not suffix and not country_start:
        suffix, country_start = get_suffix(category, "contries_from_nat")
        country_start_lab = contries_from_nat.get(country_start, "")

    if suffix and country_start:
        logger.debug(f'<<lightpurple>>>>>> country_start_lab:"{country_start_lab}"')
        logger.debug(f'<<lightblue>> country_start:"{country_start}", suffix:"{suffix}"')

        FOF = ""
        if suffix in category_relation_mapping:
            codd = category_relation_mapping[suffix]
            if codd.startswith("لل"):
                con_3_lab = "{} " + codd
                logger.debug(f'get lab from category_relation_mapping con_3_lab:"{con_3_lab}"')

        if not con_3_lab:
            con_3_lab = SPORT_FORMTS_EN_AR_IS_P17.get(suffix.strip(), "")
            if con_3_lab:
                FOF = "<<lightgreen>>SPORT_FORMTS_EN_AR_IS_P17<<lightblue>>"

        if not con_3_lab:
            con_3_lab = en_is_P17_ar_is_P17.get(suffix.strip(), "")

        if not con_3_lab:
            con_3_lab = Get_Sport_Format_xo_en_ar_is_P17(suffix.strip())

        if not con_3_lab:
            con_3_lab = pop_format.get(suffix, "")
            if con_3_lab:
                FOF = "<<lightgreen>>pop_format<<lightblue>>"

        if con_3_lab:
            if FOF:
                logger.debug(f'<<lightblue>>>>>> {FOF} .startswith({country_start}), suffix:"{suffix}"')
            if "{nat}" in con_3_lab:
                resolved_label = con_3_lab.format(nat=country_start_lab)
            else:
                resolved_label = con_3_lab.format(country_start_lab)

            logger.debug(f'<<lightblue>>>>>> Get_P17: test_60: new cnt_la "{resolved_label}" ')

        logger.debug(f'<<lightred>>>>>> con_3_lab: "{con_3_lab}", cnt_la :"{resolved_label}" == ""')

    else:
        logger.info(f'<<lightred>>>>>> suffix: "{suffix}" or country_start :"{country_start}" == ""')

    if resolved_label:
        logger.info(f'<<lightblue>>>>>> Get_P17 cnt_la "{resolved_label}" ')

    return resolved_label
