#!/usr/bin/python3
"""
This module provides functions for processing and generating labels for country names based on separators.
"""

import functools
import re
from typing import Tuple

from ...format_bots.relation_mapping import translation_category_relations
from ...helps import logger
from ...new_resolvers.bys_new import resolve_by_labels
from ...new_resolvers.reslove_all import new_resolvers_all
from ...time_resolvers.time_to_arabic import convert_time_to_arabic
from ...translations import get_from_pf_keys2
from ...utils import fix_minor
from .. import sport_lab_suffixes, team_work, with_years_bot
from ..films_and_others_bot import te_films
from ..ma_bots import country_bot
from ..make_bots.bot_2018 import get_pop_All_18
from ..matables_bots.bot import add_to_Films_O_TT
from ..matables_bots.check_bot import check_key_new_players
from ..matables_bots.table1_bot import get_KAKO
from ..o_bots import bys, parties_bot, univer
from ..o_bots.peoples_resolver import work_peoples
from .utils import split_text_by_separator


@functools.lru_cache(maxsize=10000)
def wrap_lab_for_country2(country: str) -> str:
    """
    TODO: should be moved to functions directory.
    Retrieve laboratory information for a specified country.
    """

    country2 = country.lower().strip()

    resolved_label = (
        new_resolvers_all(country2)
        or get_from_pf_keys2(country2)
        or get_pop_All_18(country2)
        or te_films(country2)
        or sport_lab_suffixes.get_teams_new(country2)
        or parties_bot.get_parties_lab(country2)
        or team_work.Get_team_work_Club(country2)
        or univer.te_universities(country2)
        or work_peoples(country2)
        or get_KAKO(country2)
        or convert_time_to_arabic(country2)
        or get_pop_All_18(country2)
        or ""
    )
    logger.info(f'>> wrap_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label


def time_label(text: str) -> str:
    """Generate a time-related label based on the provided text."""
    tst3 = re.sub(r"\d+", "", text.strip())
    test3_results = ["", "-", "–", "−"]
    if tst3 in test3_results:
        return text
    return ""


def get_table_with_in(cone_1: str, separator: str) -> str:
    table_with_in = {
        "sport in": "الرياضة في",
    }
    con_1_in = f"{cone_1.strip()} {separator.strip()}"
    part_1_label = table_with_in.get(con_1_in, "")
    logger.debug(f"<<<< {con_1_in=}, {part_1_label=}")

    return part_1_label


@functools.lru_cache(maxsize=10000)
def c_1_1_lab(separator: str, cone_1: str, with_years: bool = False) -> str:
    """
    Retrieve a label based on the given parameters.
    Example:
        {"separator": " in ", "cone_1": "cultural depictions of competitors", "output": "تصوير ثقافي عن منافسون"},
    """

    cone_1 = cone_1.strip().lower()

    if cone_1 == "women" and separator.strip() == "from":
        part_1_label = "نساء"
        logger.debug(f">> >> >> Make {cone_1=}.")
        return part_1_label

    part_1_label = (
        get_pop_All_18(cone_1)
        or te_films(cone_1)
        or new_resolvers_all(cone_1)
        or sport_lab_suffixes.get_teams_new(cone_1)
        or parties_bot.get_parties_lab(cone_1)
        or team_work.Get_team_work_Club(cone_1)
        or get_table_with_in(cone_1, separator)
        or convert_time_to_arabic(cone_1)
        or time_label(cone_1)
        or get_from_pf_keys2(cone_1)
        or get_KAKO(cone_1)
        or ""
    )

    if not part_1_label:
        logger.debug(f'>>>> XX--== part_1_label =  "{part_1_label}" {cone_1=}')

    return part_1_label


@functools.lru_cache(maxsize=10000)
def c_2_1_lab(cone_2: str, with_years: bool = False) -> str:
    """Retrieve a label based on the provided cone identifier."""

    cone_2 = cone_2.strip().lower()

    part_2_label = (
        get_pop_All_18(cone_2)
        or bys.get_by_label(cone_2)
        or te_films(cone_2)
        or new_resolvers_all(cone_2)
        or sport_lab_suffixes.get_teams_new(cone_2)
        or parties_bot.get_parties_lab(cone_2)
        or bys.get_and_label(cone_2)
        or team_work.Get_team_work_Club(cone_2)
        or get_from_pf_keys2(cone_2.strip().lower())
        or get_KAKO(cone_2)
        or time_label(cone_2)
        or convert_time_to_arabic(cone_2)
        or ""
    )

    logger.debug(f"{cone_2=} -> {part_2_label=}")

    return part_2_label


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
    ar_separator: str,
) -> str:
    """
    Construct a formatted string based on various input parameters.
    """
    country2 = country.lower().strip()

    resolved_label = part_1_label + ar_separator + part_2_label
    in_players = check_key_new_players(part_1_normalized.lower())

    if in_players:
        if in_players:
            if part_2_label.startswith("أصل "):
                logger.info(f">>>>>> Add من to {part_1_normalized=} part_1_normalized in New_players:")
                resolved_label = f"{part_1_label}{ar_separator}من {part_2_label}"
            else:
                logger.info(f">>>>>> Add في to {part_1_normalized=} part_1_normalized in New_players:")
                if not resolved_label.strip().endswith(" في"):
                    resolved_label += " في "

        if not resolve_by_labels(part_2_normalized):
            # Films_O_TT[country2] = resolved_label
            add_to_Films_O_TT(country2, resolved_label)
        else:
            logger.info("<<lightblue>>>>>> part_2_normalized in By table main")

    if part_2_label:
        label_format_mappings = {
            "politics of {}": "سياسة {}",
            "military installations of": "منشآت {} العسكرية",
        }
        if part_1_normalized in label_format_mappings:
            logger.info(
                f'<<lightblue>>>>>> part_1_normalized in label_format_mappings "{label_format_mappings[part_1_normalized]}":'
            )
            resolved_label = label_format_mappings[part_1_normalized].format(part_2_label)

    # NOTE: important to fix bug like: [sport in ottoman] = "الرياضة في في الدولة العثمانية" !

    resolved_label = resolved_label.replace(" في في ", " في ")

    logger.info(f'<<lightpurple>> >>>> country 2_tit "{country2}": label: {resolved_label}')

    resolved_label = " ".join(resolved_label.strip().split())
    resolved_label = _resolve_war(resolved_label, part_2_normalized, part_1_normalized)

    if resolved_label.endswith(" في "):
        resolved_label = resolved_label[: -len(" في ")]

    return resolved_label


def separator_arabic_resolve(separator: str) -> str:
    """
    Generate a specific string based on input parameters.
    TODO: need refactoring
    """
    ar_separator = " "
    separator = separator.strip()

    if separator == "to":
        ar_separator = " إلى "
    elif separator == "on":
        ar_separator = " على "
    elif separator == "about":
        ar_separator = " عن "
    elif separator in translation_category_relations and separator != "by":
        ar_separator = f" {translation_category_relations[separator]} "
    elif separator == "based in":
        ar_separator = " مقرها في "

    return ar_separator


# @dump_data()
def make_parts_labels(part_1, part_2, separator, with_years) -> Tuple[str, str]:
    part_2_label = (
        new_resolvers_all(part_2)
        or c_2_1_lab(part_2)
        or country_bot.Get_c_t_lab(part_2, "")
        or (with_years_bot.Try_With_Years(part_2) if with_years else "")
        or ""
    )

    part_1_label = (
        new_resolvers_all(part_1)
        or c_1_1_lab(separator, part_1, with_years=with_years)
        or country_bot.Get_c_t_lab(part_1, "", lab_type="type_label")
        or ""
    )

    if part_2_label == "" or part_1_label == "":
        logger.info(f">>>> XX--== <<lightgreen>> {part_1=}, {part_1_label=}, {part_2=}, {part_2_label=}")
        return "", ""

    part_1_normalized = part_1.strip().lower()
    part_2_normalized = part_2.strip().lower()

    if (separator.strip() == "in" or part_1_normalized.endswith(" in")) and (not part_1_normalized.endswith(" في")):
        logger.debug(f">>>> Add في to {part_1_label=}")
        part_1_label = f"{part_1_label} في"

    elif (separator.strip() == "from" or part_2_normalized.endswith(" from")) and (not part_2_label.endswith(" من")):
        logger.debug(f">>>> Add من to {part_2_label=}")
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


def country_2_title_work(country: str, with_years: bool = True) -> str:
    separator = get_separator(country)

    if not separator:
        logger.info(f">>>> country_2_title_work <<red>> {separator=}")
        return ""

    part_1, part_2 = split_text_by_separator(separator, country)

    logger.info(f"2060 {part_1=}, {part_2=}, {separator=}")

    part_1_label, part_2_label = make_parts_labels(part_1, part_2, separator, with_years)

    if part_2_label == "" or part_1_label == "":
        logger.info(f">>>> XX--== <<lightgreen>> {part_1=}, {part_1_label=}, {part_2=}, {part_2_label=}")
        return ""

    part_1_normalized = part_1.strip().lower()
    part_2_normalized = part_2.strip().lower()

    logger.info(
        f">>>> XX--== <<lightgreen>> {part_1_normalized=}, {part_1_label=}, {part_2_normalized=}, {part_2_label=}"
    )

    if separator.strip() == "to" and (
        part_1_label.startswith("سفراء ") or part_1_normalized.strip() == "ambassadors of"
    ):
        ar_separator = " لدى "
    else:
        ar_separator = separator_arabic_resolve(separator)

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
