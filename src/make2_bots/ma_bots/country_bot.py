#!/usr/bin/python3
"""

# from ..ma_bots.country_bot import get_country, Get_c_t_lab


from ..ma_bots import country_bot


lab = country_bot.get_country()

"""
import re
from typing import Dict
from . import ye_ts_bot

from ..date_bots import with_years_bot
from ..p17_bots import nats
from ..sports_bots import team_work

from ..media_bots.films_bot import te_films

from . import country2_bot
from . import country2_lab
from ...translations import SPORTS_KEYS_FOR_LABEL
from ...translations import Nat_mens
from ...translations import New_female_keys

from ...helps.print_bot import print_put, output_test

from ..fromnet.wd_bot import find_wikidata
from ..matables_bots.centries_bot import centries_years_dec
from ...translations import pop_of_without_in
from ...translations import jobs_mens_data
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..reg_lines import RE1_compile, RE2_compile, RE3_compile
from ... import app_settings
get_country_done: Dict[str, str] = {}


def get_country(country: str, start_get_country2: bool = True) -> str:
    """Retrieve the label for a given country name."""

    country = country.lower()

    if country in get_country_done:
        output_test(f'>>>> get_country: "{country}" in get_country_done, lab:"{get_country_done[country]}"')
        return get_country_done[country]

    output_test(">> ----------------- get_country start ----------------- ")
    print_put(f'>>>> Get country for "{country}"')
    resolved_label = country if country.strip().isdigit() else ""
    if not resolved_label:
        resolved_label = New_female_keys.get(country, "")
    if not resolved_label:
        resolved_label = te_films(country)
    if not resolved_label:
        resolved_label = nats.find_nat_others(country)
    if not resolved_label:
        resolved_label = team_work.Get_team_work_Club(country)

    if resolved_label == "" and start_get_country2:
        resolved_label = country2_bot.Get_country2(country)

    if not resolved_label:
        prefix_labels = {
            "women's ": "نسائية",
            "men's ": "رجالية",
            "fasa ": "فاسااا",
            "non-combat ": "غير قتالية",
        }

        for prefix, prefix_label in prefix_labels.items():
            if not country.startswith(prefix):
                continue
            print(f">>> country.startswith({prefix})")
            remainder = country[len(prefix) :]
            remainder_label = country2_bot.Get_country2(remainder)

            if remainder_label == "":
                remainder_label = country2_lab.get_lab_for_country2(remainder)

            if remainder_label == "":
                remainder_label = ye_ts_bot.translate_general_category(remainder)

            if remainder_label:
                resolved_label = f"{remainder_label} {prefix_label}"
                print_put(f'>>>>>> xxx new cnt_la  "{resolved_label}" ')
                break

    OKay = True

    if resolved_label == "" and OKay:
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
        title_separators = [f" {sep} " if sep != "-of " else sep for sep in title_separators]
        for ttt in title_separators:
            if ttt in country:
                OKay = False
                break

    if resolved_label == "" and OKay:
        historical_prefixes = {
            "defunct national ": "{} وطنية سابقة",
        }

        for prefix, prefix_template in historical_prefixes.items():
            if not country.startswith(prefix):
                continue
            print(f">>> country.startswith({prefix})")
            remainder = country[len(prefix) :]
            remainder_label = country2_bot.Get_country2(remainder)

            if remainder_label == "":
                remainder_label = country2_lab.get_lab_for_country2(remainder)

            if remainder_label == "":
                remainder_label = ye_ts_bot.translate_general_category(remainder)

            if remainder_label:
                resolved_label = prefix_template.format(remainder_label)
                if (
                    remainder_label.strip().endswith(" في")
                    and prefix.startswith("defunct ")
                ):
                    resolved_label = f'{remainder_label.strip()[:-len(" في")]} سابقة في'
                print_put(f'>>>>>> cdcdc new cnt_la  "{resolved_label}" ')
                break

    if resolved_label:
        if "سنوات في القرن" in resolved_label:
            resolved_label = re.sub(
                r"سنوات في القرن", "سنوات القرن", resolved_label
            )

    if not resolved_label:
        RE1 = RE1_compile.match(country)
        RE2 = RE2_compile.match(country)
        RE3 = RE3_compile.match(country)

        if RE1 or RE2 or RE3:
            resolved_label = with_years_bot.Try_With_Years(country)

    if resolved_label == "" and country.endswith(" members of"):
        country2 = country.replace(" members of", "")
        resolved_label = Nat_mens.get(country2, "")
        if resolved_label:
            resolved_label = f"{resolved_label} أعضاء في  "
            print_put(f"a<<lightblue>>>2021 get_country lab = {resolved_label}")

    if not resolved_label:
        resolved_label = SPORTS_KEYS_FOR_LABEL.get(country, "")

    get_country_done[country] = resolved_label
    output_test(f'>>>> Get country "{resolved_label}"')
    output_test(">> ----------------- end get_country ----------------- ")
    return resolved_label


def Get_c_t_lab(c_t_lower: str, tito: str, Type: str = "", start_get_country2: bool = True) -> str:
    """Retrieve the corresponding label for a given country or term."""

    print_put(f'Get_c_t_lab Type:"{Type}", tito:"{tito}", c_ct_lower:"{c_t_lower}" ')
    if app_settings.makeerr:
        start_get_country2 = True

    test_3 = re.sub(r"\d+", "", c_t_lower.strip())
    test3_results = ["", "-", "–", "−"]
    c_t_lab = c_t_lower if test_3 in test3_results else ""
    if not c_t_lab:
        c_t_lab = New_female_keys.get(c_t_lower, "")
    if not c_t_lab:
        c_t_lab = centries_years_dec.get(c_t_lower, "")

    if c_t_lab == "" and Type != "Type_lab":
        if c_t_lower.startswith("the "):
            print_put(f'>>>> c_t_lower:"{c_t_lower}" startswith("the ")')
            LLL = c_t_lower[len("the ") :]

            c_t_lab = get_pop_All_18(LLL, "")

            if not c_t_lab:
                c_t_lab = get_country(LLL, start_get_country2=start_get_country2)

    if not c_t_lab:
        if re.sub(r"\d+", "", c_t_lower) == "":
            c_t_lab = c_t_lower
        else:
            c_t_lab = centries_years_dec.get(c_t_lower, "")

    if c_t_lab == "":
        c_t_lab = get_country(c_t_lower, start_get_country2=start_get_country2)

    if c_t_lab == "" and Type == "Type_lab":
        tatos = [" of", " in", " at"]

        for tat in tatos:
            if c_t_lab:
                break

            if not c_t_lower.endswith(tat):
                continue

            tti = c_t_lower[: -len(tat)]

            tto = jobs_mens_data.get(tti, "")

            print_put(f'tti:"{tti}", tto:"{tto}", c_t_lower:"{c_t_lower}" ')

            if c_t_lab == "" and tto:
                c_t_lab = f"{tto} من "
                print_put(f"jobs_mens_data:: add من to c_t_lab:{c_t_lab}, line:1583.")

            if not tto:
                tto = get_pop_All_18(tti, "")

            if not tto:
                tto = get_country(tti, start_get_country2=start_get_country2)

            if c_t_lab == "" and tto:
                if c_t_lower in pop_of_without_in:
                    c_t_lab = tto
                    print_put("skip add في to pop_of_without_in")
                else:
                    c_t_lab = f"{tto} في "
                    print_put(f"XX add في to c_t_lab:{c_t_lab}, line:1596.")
                break
        if c_t_lab == "" and tito.strip() == "in":
            c_t_lab = get_pop_All_18(f"{c_t_lower} in", "")

        if not c_t_lab:
            c_t_lab = get_country(c_t_lower, start_get_country2=start_get_country2)

    if not c_t_lab:
        c_t_lab = find_wikidata(c_t_lower)

    if c_t_lab:
        print_put(f'Get_c_t_lab c_t_lab:"{c_t_lab}" ')

    elif tito.strip() == "for" and c_t_lower.startswith("for "):
        return Get_c_t_lab(c_t_lower[len("for ") :], "", Type=Type)

    return c_t_lab
