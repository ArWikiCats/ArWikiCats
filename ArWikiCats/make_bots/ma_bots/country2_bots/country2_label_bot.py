#!/usr/bin/python3
"""
This module provides functions for processing and generating labels for country names based on separators.
"""

import re
from typing import Tuple

from ....helps.jsonl_dump import dump_data
from ....helps.log import logger
from ....utils import fix_minor, check_key_in_tables_return_tuple
from ...format_bots import category_relation_mapping, pop_format, pop_format2
from .. import country_bot
from ....translations import By_table, typeTable
from ...matables_bots.bot import Films_O_TT, add_to_Films_O_TT
from ...matables_bots.check_bot import check_key_new_players
from .c_1_c_2_labs import c_1_1_lab, c_2_1_lab


def _resolve_war(resolved_label: str, part_2_normalized: str, part_1_normalized: str) -> str:

    maren = re.match(r"\d\d\d\d", part_2_normalized)
    if maren:
        if part_1_normalized == "war of" and resolved_label == f"الحرب في {part_2_normalized}":
            resolved_label = f"حرب {part_2_normalized}"
            logger.info(f'<<lightpurple>> >>>> change cnt_la to "{resolved_label}".')

    return resolved_label


def make_cnt_lab(
    separator: str,
    country: str,
    part_2_label: str,
    part_1_label: str,
    part_1_normalized: str,
    part_2_normalized: str,
    ar_separator: str
) -> str:
    """
    Construct a formatted string based on various input parameters.
    """
    country2 = country.lower().strip()

    resolved_label = part_1_label + ar_separator + part_2_label
    in_players = check_key_new_players(part_1_normalized.lower())

    to_check_them_tuble = {
        "typeTable": typeTable,
        "Films_O_TT": Films_O_TT,
    }
    co_in_tables, tab_name = check_key_in_tables_return_tuple(part_1_normalized, to_check_them_tuble)

    if co_in_tables or in_players:
        if in_players:
            if part_2_label.startswith("أصل "):
                logger.info(f'>>>>>> Add من to part_1_normalized:"{part_1_normalized}" part_1_normalized in New_players:')
                resolved_label = f"{part_1_label}{ar_separator}من {part_2_label}"
            else:
                logger.info(f'>>>>>> Add في to part_1_normalized:"{part_1_normalized}" part_1_normalized in New_players:')
                resolved_label += " في "
        if part_2_normalized not in By_table:
            # Films_O_TT[country2] = resolved_label
            add_to_Films_O_TT(country2, resolved_label)
            # print(f": {country2=}, {resolved_label=}\n"*10)
        else:
            logger.info("<<lightblue>>>>>> part_2_normalized in By_table")

    if part_2_label:
        if not part_2_normalized.startswith("by "):
            tashr = f"{part_1_normalized} {separator.strip()}"
            faxos = pop_format.get(part_1_normalized) or pop_format.get(tashr)
            if faxos:
                logger.info(f'<<lightblue>>>>>> part_1_normalized in pop_format "{faxos}":')
                resolved_label = faxos.format(part_2_label)

        if part_1_normalized in pop_format2:
            logger.info(f'<<lightblue>>>>>> part_1_normalized in pop_format2 "{pop_format2[part_1_normalized]}":')
            resolved_label = pop_format2[part_1_normalized].format(part_2_label)

    logger.info(f'<<lightpurple>> >>>> country 2_tit "{country2}": label: {resolved_label}')

    resolved_label = " ".join(resolved_label.strip().split())
    resolved_label = _resolve_war(resolved_label, part_2_normalized, part_1_normalized)

    if resolved_label.endswith(" في "):
        resolved_label = resolved_label[: -len(" في ")]

    return resolved_label


@dump_data()
def split_text_by_separator(separator: str, country: str) -> Tuple[str, str]:
    """
    Process a country name based on a specified separator.
    TODO: separators need refactoring
    """

    country = country.strip()
    country2 = country.lower()
    if separator.lower() not in country2:
        return "", ""

    part_1 = country2.split(separator)[0]
    part_2 = country2.split(separator)[1]

    Mash = f"^(.*?)(?:{separator}?)(.*?)$"

    Type_t = re.sub(Mash, r"\g<1>", country, flags=re.IGNORECASE)
    country_t = re.sub(Mash, r"\g<2>", country, flags=re.IGNORECASE)

    test_N = country2.lower().replace(part_1.strip().lower(), "")

    test_N = re.sub(re.escape(part_2.strip()), "", test_N, flags=re.I)
    test_N = test_N.replace(part_2.strip().lower(), "")

    # specific case
    if separator.strip() == "by":
        part_2 = f"by {part_2}"
        country_t = f"by {country_t}"

    # specific case
    if separator.strip() in ["of", "-of"]:
        Type_t = f"{Type_t} of"
        part_1 = f"{part_1} of"

    logger.info(f'>>>> {part_1=}, {test_N.strip()}, {part_2.strip()=}')

    if test_N and test_N.strip() != separator.strip():
        logger.info(f'>>>> <<lightblue>> test_N != "", {Type_t=}, {separator=}, {country_t=}')
        part_1 = Type_t
        part_2 = country_t

    return part_1, part_2


@dump_data()
def separator_arabic_resolve(separator: str, part_1_normalized: str) -> str:
    """
    Generate a specific string based on input parameters.
    TODO: need refactoring
    """
    ar_separator = " "

    if separator.strip() == "to" and part_1_normalized.strip() == "ambassadors of":
        ar_separator = " لدى "
    elif separator.strip() == "to":
        ar_separator = " إلى "
    elif separator.strip() == "on":
        ar_separator = " على "
    elif separator.strip() == "about":
        ar_separator = " عن "
    elif separator.strip() in category_relation_mapping:
        if separator.strip() != "by":
            ar_separator = f" {category_relation_mapping[separator.strip()]} "
    elif separator.strip() == "based in":
        ar_separator = " مقرها في "

    return ar_separator


@dump_data()
def make_parts_labels(part_1, part_2, separator, With_Years) -> Tuple[str, str]:

    part_2_label = c_2_1_lab(part_2, With_Years=With_Years)
    part_1_label = c_1_1_lab(separator, part_1, With_Years=With_Years)

    if not part_2_label:
        part_2_label = country_bot.Get_c_t_lab(part_2, "")

    if not part_1_label:
        part_1_label = country_bot.Get_c_t_lab(part_1, "", lab_type="type_label")

    if part_2_label == "" or part_1_label == "":
        logger.info(f">>>> XX--== <<lightgreen>> {part_1=}, {part_1_label=}, {part_2=}, {part_2_label=}")
        return "", ""

    part_1_normalized = part_1.strip().lower()
    part_2_normalized = part_2.strip().lower()

    if (separator.strip() == "in" or part_1_normalized.endswith(" in")) and (not part_1_normalized.endswith(" في")):
        logger.debug(f'>>>> Add في to {part_1_label=}')
        part_1_label = f"{part_1_label} في"

    elif (separator.strip() == "from" or part_2_normalized.endswith(" from")) and (not part_2_label.endswith(" من")):
        logger.debug(f'>>>> Add من to {part_2_label=}')
        part_2_label = f"من {part_2_label}"

    return part_1_label, part_2_label


def get_separator(country: str) -> str:
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

    normalized_country = country.lower().strip()

    for sep in title_separators:
        separator = f" {sep} " if sep != "-of " else sep
        if separator in normalized_country:
            return separator

    return ""


@dump_data()
def country_2_title_work(country: str, With_Years: bool = True) -> str:

    separator = get_separator(country)

    if not separator:
        logger.info(f">>>> country_2_title_work <<red>> {separator=}")
        return ""

    part_1, part_2 = split_text_by_separator(separator, country)

    logger.info(f'2060 {part_1=}, {part_2=}, {separator=}')

    part_1_label, part_2_label = make_parts_labels(part_1, part_2, separator, With_Years)

    if part_2_label == "" or part_1_label == "":
        logger.info(f">>>> XX--== <<lightgreen>> {part_1=}, {part_1_label=}, {part_2=}, {part_2_label=}")
        return ""

    part_1_normalized = part_1.strip().lower()
    part_2_normalized = part_2.strip().lower()

    logger.info(f">>>> XX--== <<lightgreen>> {part_1_normalized=}, {part_1_label=}, {part_2_normalized=}, {part_2_label=}")

    if separator.strip() == "to" and (part_1_label.startswith("سفراء ") or part_1_normalized.strip() == "ambassadors of"):
        ar_separator = " لدى "
    else:
        ar_separator = separator_arabic_resolve(separator, part_1_normalized)

    resolved_label = make_cnt_lab(
        separator=separator,
        country=country,
        part_2_label=part_2_label,
        part_1_label=part_1_label,
        part_1_normalized=part_1_normalized,
        part_2_normalized=part_2_normalized,
        ar_separator=ar_separator,
    )

    resolved_label = fix_minor(resolved_label, separator)

    return resolved_label


__all__ = [
    "make_cnt_lab",
    "country_2_title_work",
    "separator_arabic_resolve",
    "split_text_by_separator",
]
