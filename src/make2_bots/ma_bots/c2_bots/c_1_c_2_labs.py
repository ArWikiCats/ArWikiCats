#!/usr/bin/python3
"""

from .c_1_c_2_labs import c_1_1_lab, c_2_1_lab

"""

import re
from typing import Callable, List
from ...o_bots import fax
from ...media_bots.films_bot import test_films
from .. import contry2_lab

from .. import contry_bot
from ...sports_bots import team_work
from ...o_bots import bys
from ...p17_bots import nats
from ...format_bots import Tabl_with_in, pp_start_with2, pop_format

from ...matables_bots.centries_bot import centries_years_dec

from ...matables_bots.bot_2018 import pop_All_2018
from ...matables_bots.table1_bot import get_KAKO

from ....helps.print_bot import print_put, output_test

from ...date_bots import with_years_bot


def check_sources(text: str) -> str:
    """Check multiple sources for a result based on the provided input."""

    sources: List[Callable[[str], str]] = [
        test_films,
        nats.find_nat_others,
        fax.Get_Teams_new,
    ]
    for source in sources:
        result = source(text)
        if result:
            return result
    return ""


def c_1_1_lab(tat_o: str, With_Years: bool, text: str) -> str:
    """Retrieve a label based on the given parameters."""

    text_no_lower = text.strip()
    text = text.strip().lower()

    label = pop_All_2018.get(text, "")

    if not label:
        label = test_films(text)
    if not label:
        label = nats.find_nat_others(text)
    if not label:
        label = fax.Get_Teams_new(text)
    if not label:
        label = team_work.Get_team_work_Club(text_no_lower)

    if text == "women" and tat_o.strip() == "from":
        label = "نساء"
        print_put(f'>> >> >> Make text "{text}".')

    con_1_in = f"{text.strip()} {tat_o.strip()}"
    if not label:
        label = Tabl_with_in.get(con_1_in, "")
        if label:
            print_put(f'<<<< con_1_in "{con_1_in}", label : "{label}"')

    if not label:
        label = centries_years_dec.get(text, "")

    if not label:
        tst3 = re.sub(r"\d+", "", text.strip())
        test3_results = ["", "-", "–", "−"]
        if tst3 in test3_results:
            label = text

    for prefix, template in pp_start_with2.items():
        if not label:
            if text.startswith(prefix):
                substring = text[len(prefix) :]
                print_put(f' pp_start_with2 <<lightblue>> text :"{text}", substring :"{substring}", tat_o:"{tat_o}" ')
                substring_label = contry2_lab.get_lab_for_contry2(substring)

                if substring_label == "" and With_Years:
                    substring_label = with_years_bot.get_label_with_years(substring)

                if substring_label:
                    print_put(f'>>>><<lightblue>> dddd.startswith prefix("{prefix}"),substring:"{substring}", substring_label:"{substring_label}"')
                    label = template.format(substring_label)
                    print_put(f'>>>> label:"{label}"')

    if text in pop_format:
        label = pop_format[text]

    if not label:
        label = contry_bot.get_country_or_term_label(text, "", Type="Type_lab")
    if not label:
        label = get_KAKO(text)

    if not label:
        output_test(f'>>>> XX--== label =  "{label}" text:"{text}" not in pop_new')
    return label


def c_2_1_lab(With_Years: bool, text: str) -> str:
    """Retrieve a label based on the provided cone identifier."""

    text_no_lower = text.strip()
    text = text.strip().lower()

    label = pop_All_2018.get(text, "")
    if label == "" and text.find(" by ") != -1:
        label = bys.Get_by_label(text)

    if not label:
        label = test_films(text)
    if not label:
        label = nats.find_nat_others(text)
    if not label:
        label = fax.Get_Teams_new(text)
    if label == "" and text.find(" and ") != -1:
        label = bys.Get_and_label(text)
    if not label:
        label = team_work.Get_team_work_Club(text_no_lower)

    if not label:
        label = get_KAKO(text)

    if not label:
        tst3 = re.sub(r"\d+", "", text.strip())
        test3_results = ["", "-", "–", "−"]
        if tst3 in test3_results:
            label = text

    if not label:
        label = test_films(text)
    if not label:
        label = nats.find_nat_others(text)
    if not label:
        label = centries_years_dec.get(text, "")
    if label == "" and With_Years:
        label = with_years_bot.get_label_with_years(text)
    if not label:
        label = contry_bot.get_country_or_term_label(text, "")

    return label
