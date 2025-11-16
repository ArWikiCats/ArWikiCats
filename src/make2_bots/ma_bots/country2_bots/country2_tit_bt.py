#!/usr/bin/python3
"""
This module provides functions for processing and generating labels for country names based on separators.
"""

import re
from typing import Tuple

from ....helps import printe
from ...format_bots import category_relation_mapping
from ....helps.print_bot import print_put, output_test
from .c_1_c_2_labs import c_1_1_lab, c_2_1_lab
from .cn_lab import make_cnt_lab
from .. import country_bot


def make_conas(tat_o: str, country: str) -> Tuple[str, str]:
    """Process a country name based on a specified separator."""

    country2_no_lower = country.strip()
    country2 = country.lower().strip()

    con_1 = country2.split(tat_o)[0]
    con_2 = country2.split(tat_o)[1]

    Mash = f"^(.*?)(?:{tat_o}?)(.*?)$"

    Type_t = re.sub(Mash, r"\g<1>", country2_no_lower, flags=re.IGNORECASE)
    country_t = re.sub(Mash, r"\g<2>", country2_no_lower, flags=re.IGNORECASE)

    test_N = country2.lower().replace(con_1.strip().lower(), "")

    try:
        test_N = test_N.strip().replace(con_2.strip().lower(), "")
    except Exception:
        printe.output(f'<<lightblue>> >>>> <<lightblue>> except, test_N:"{test_N}",con_2:"{con_2}",con_1:"{con_1}"')
        test_N = re.sub(con_2.strip().lower(), "", test_N)
        test_N = test_N.replace(con_2.strip().lower(), "")

    if tat_o.strip() == "by":
        con_2 = f"by {con_2}"
        country_t = f"by {country_t}"

    if tat_o.strip() in ["of", "-of"]:
        Type_t = f"{Type_t} of"
        con_1 = f"{con_1} of"

    print_put(f'>>>> con_1:"{con_1.strip()}",test_N:"{test_N.strip()}",con 2:"{con_2.strip()}"')

    if test_N and test_N.strip() != tat_o.strip():
        print_put(f'>>>> <<lightblue>> test_N != "",Type_t:"{Type_t}",tat_o:"{tat_o}",country_t:"{country_t}"')
        con_1 = Type_t
        con_2 = country_t

    return con_1, con_2


def make_sps(tat_o: str, c_1_l: str, cona_1: str) -> str:
    """Generate a specific string based on input parameters."""

    sps = " "

    if tat_o.strip() == "to" and cona_1.strip() == "ambassadors of":
        sps = " لدى "
    elif tat_o.strip() == "to":
        sps = " إلى "
    elif tat_o.strip() == "on":
        sps = " على "
    elif tat_o.strip() == "about":
        sps = " عن "
    elif tat_o.strip() in category_relation_mapping:
        if tat_o.strip() != "by":
            sps = f" {category_relation_mapping[tat_o.strip()]} "
    elif tat_o.strip() == "based in":
        sps = " مقرها في "

    if tat_o.strip() == "to" and c_1_l.startswith("سفراء "):
        sps = " لدى "

    return sps


def country_2_tit(tat_o: str, country: str, With_Years: bool = True) -> str:
    """Convert country name and generate labels based on input parameters."""

    print_put(f'>>>> <<lightblue>> country_2_tit: <<lightyellow>> New Way to find lab for "{country.lower().strip()}".')

    con_1, con_2 = make_conas(tat_o, country)

    print_put(f'2060 con_1:"{con_1}",con_2:"{con_2}",tat_o:"{tat_o}"')

    c_2_l = c_2_1_lab(With_Years, con_2)
    c_1_l = c_1_1_lab(tat_o, With_Years, con_1)

    if not c_2_l:
        c_2_l = country_bot.Get_c_t_lab(con_2, "")

    if not c_1_l:
        c_1_l = country_bot.Get_c_t_lab(con_1, "", Type="Type_lab")

    cona_1 = con_1.strip().lower()
    cona_2 = con_2.strip().lower()

    fAAA = '>>>> XX--== <<lightgreen>> Ccon_1:"%s", lab"%s", cona_2:"%s", lab"%s", cnt_test: "%s"'

    country2 = country.lower().strip()
    remaining_text = country2

    if c_2_l == "" or c_1_l == "":
        print_put(fAAA % (cona_1, c_1_l, cona_2, c_2_l, remaining_text))
        return ""

    remaining_text = (
        remaining_text.replace(cona_1, "")
        .replace(cona_2, "")
        .replace(tat_o.strip(), "")
        .strip()
    )

    if (tat_o.strip() == "in" or cona_1.endswith(" in")) and (not cona_1.endswith(" في")):
        output_test(f'>>>> Add في to c_1_l : "{c_1_l}"')
        c_1_l = f"{c_1_l} في"

    elif (tat_o.strip() == "from" or cona_2.endswith(" from")) and (not c_2_l.endswith(" من")):
        output_test(f'>>>> Add من to c_2_l : "{c_2_l}"')
        c_2_l = f"من {c_2_l}"

    print_put(fAAA % (cona_1, c_1_l, cona_2, c_2_l, remaining_text))

    sps = make_sps(tat_o, c_1_l, cona_1)

    if remaining_text:
        print_put(f'>>>> cnt_test:"{remaining_text}" != "" ')

    resolved_label = make_cnt_lab(tat_o, country2, c_2_l, c_1_l, cona_1, cona_2, sps)

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
            break

    return resolved_label


__all__ = [
    "country_2_title_work",
    "country_2_tit",
    "make_sps",
    "make_conas",
]
