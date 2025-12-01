#!/usr/bin/python3
"""
This module provides functions for processing and generating labels for country names based on separators.
"""

import re
from typing import Tuple

from ....helps.log import logger
from ....utils import fix_minor
from ...format_bots import category_relation_mapping
from .. import country_bot
from .c_1_c_2_labs import c_1_1_lab, c_2_1_lab
from .cn_lab import make_cnt_lab


def make_conas(separator: str, country: str) -> Tuple[str, str]:
    """
    Process a country name based on a specified separator.
    TODO: separators need refactoring
    """

    country2_no_lower = country.strip()
    country2 = country.lower().strip()

    part_1 = country2.split(separator)[0]
    part_2 = country2.split(separator)[1]

    Mash = f"^(.*?)(?:{separator}?)(.*?)$"

    Type_t = re.sub(Mash, r"\g<1>", country2_no_lower, flags=re.IGNORECASE)
    country_t = re.sub(Mash, r"\g<2>", country2_no_lower, flags=re.IGNORECASE)

    test_N = country2.lower().replace(part_1.strip().lower(), "")

    test_N = re.sub(re.escape(part_2.strip()), "", test_N, flags=re.I)
    test_N = test_N.replace(part_2.strip().lower(), "")

    if separator.strip() == "by":
        part_2 = f"by {part_2}"
        country_t = f"by {country_t}"

    if separator.strip() in ["of", "-of"]:
        Type_t = f"{Type_t} of"
        part_1 = f"{part_1} of"

    logger.info(f'>>>> part_1:"{part_1.strip()}",test_N:"{test_N.strip()}",con 2:"{part_2.strip()}"')

    if test_N and test_N.strip() != separator.strip():
        logger.info(f'>>>> <<lightblue>> test_N != "",Type_t:"{Type_t}",separator:"{separator}",country_t:"{country_t}"')
        part_1 = Type_t
        part_2 = country_t

    return part_1, part_2


def separator_arabic_resolve(separator: str, part_1_label: str, part_1_normalized: str) -> str:
    """
    Generate a specific string based on input parameters.
    TODO: need refactoring
    """
    sps = " "

    if separator.strip() == "to" and part_1_normalized.strip() == "ambassadors of":
        sps = " لدى "
    elif separator.strip() == "to":
        sps = " إلى "
    elif separator.strip() == "on":
        sps = " على "
    elif separator.strip() == "about":
        sps = " عن "
    elif separator.strip() in category_relation_mapping:
        if separator.strip() != "by":
            sps = f" {category_relation_mapping[separator.strip()]} "
    elif separator.strip() == "based in":
        sps = " مقرها في "

    if separator.strip() == "to" and part_1_label.startswith("سفراء "):
        sps = " لدى "

    return sps


def country_2_tit(separator: str, country: str, With_Years: bool = True) -> str:
    """
    Convert country name and generate labels based on input parameters.
    """

    logger.info(f'>>>> <<lightblue>> country_2_tit: <<lightyellow>> {country=}.')

    part_1, part_2 = make_conas(separator, country)

    logger.info(f'2060 part_1:"{part_1}",part_2:"{part_2}",separator:"{separator}"')

    part_2_label = c_2_1_lab(part_2, With_Years=With_Years)
    part_1_label = c_1_1_lab(separator, part_1, With_Years=With_Years)

    if not part_2_label:
        part_2_label = country_bot.Get_c_t_lab(part_2, "")

    if not part_1_label:
        part_1_label = country_bot.Get_c_t_lab(part_1, "", lab_type="type_label")

    part_1_normalized = part_1.strip().lower()
    part_2_normalized = part_2.strip().lower()

    fAAA = '>>>> XX--== <<lightgreen>> Ccon_1:"%s", lab"%s", part_2_normalized:"%s", lab"%s", cnt_test: "%s"'

    country2 = country.lower().strip()
    remaining_text = country2

    if part_2_label == "" or part_1_label == "":
        logger.info(fAAA % (part_1_normalized, part_1_label, part_2_normalized, part_2_label, remaining_text))
        return ""

    remaining_text = remaining_text.replace(part_1_normalized, "").replace(part_2_normalized, "").replace(separator.strip(), "").strip()

    if (separator.strip() == "in" or part_1_normalized.endswith(" in")) and (not part_1_normalized.endswith(" في")):
        logger.debug(f'>>>> Add في to part_1_label : "{part_1_label}"')
        part_1_label = f"{part_1_label} في"

    elif (separator.strip() == "from" or part_2_normalized.endswith(" from")) and (not part_2_label.endswith(" من")):
        logger.debug(f'>>>> Add من to part_2_label : "{part_2_label}"')
        part_2_label = f"من {part_2_label}"

    logger.info(fAAA % (part_1_normalized, part_1_label, part_2_normalized, part_2_label, remaining_text))

    sps = separator_arabic_resolve(separator, part_1_label, part_1_normalized)

    if remaining_text:
        logger.info(f'>>>> cnt_test:"{remaining_text}" != "" ')

    resolved_label = make_cnt_lab(separator, country2, part_2_label, part_1_label, part_1_normalized, part_2_normalized, sps)

    return resolved_label


def country_2_title_work(country: str, With_Years: bool = True) -> str:
    title_separators = [
        "based in",
        "in",
        "by",
        "about",
        "to",
        "of",
        "-of ",  # special case
        "from",
        "at",
        "on",
    ]
    resolved_label = ""

    normalized_country = country.lower().strip()

    for sep in title_separators:
        separator = f" {sep} " if sep != "-of " else sep
        if separator in normalized_country:
            resolved_label = country_2_tit(separator, country, With_Years=With_Years)
            resolved_label = fix_minor(resolved_label, separator)
            break

    return resolved_label


__all__ = [
    "country_2_title_work",
    "country_2_tit",
    "separator_arabic_resolve",
    "make_conas",
]
