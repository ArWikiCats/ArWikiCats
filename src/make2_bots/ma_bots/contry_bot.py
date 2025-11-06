#!/usr/bin/python3
"""

# from ..ma_bots.contry_bot import get_country_label, get_country_or_term_label


from ..ma_bots import contry_bot


lab = contry_bot.get_country_label()

"""
import sys
import re
from typing import Dict
from . import ye_ts_bot

from ..date_bots import with_years_bot
from ..p17_bots import nats
from ..sports_bots import team_work

from ..media_bots.films_bot import test_films

from . import contry2_bot
from . import contry2_lab
from ...ma_lists import Sports_Keys_For_Label
from ...ma_lists import Nat_mens
from ...ma_lists import New_female_keys

from ..matables_bots.bot import Add_to_main2_tab
from ...helps.print_bot import print_put, output_test

from ..fromnet.wd_bot import find_wikidata
from ..matables_bots.centries_bot import centries_years_dec
from ...ma_lists import pop_of_without_in
from ...ma_lists import Jobs_key
from ..matables_bots.bot_2018 import pop_All_2018
from ..reg_lines import RE1_compile, RE2_compile, RE3_compile

get_country_label_done: Dict[str, str] = {}


def get_country_label(country: str, do_Get_contry2: bool = True) -> str:
    """Retrieve the label for a given country name."""

    country_no_lower = country
    country = country.lower()

    if country in get_country_label_done:
        output_test(f'>>>> get_country_label: "{country}" in get_country_label_done, lab:"{get_country_label_done[country]}"')
        return get_country_label_done[country]

    output_test(">> ----------------- get_country_label start ----------------- ")
    print_put(f'>>>> Get country for "{country}"')
    country_label = country if country.strip().isdigit() else ""
    if not country_label:
        country_label = New_female_keys.get(country, "")
    if not country_label:
        country_label = test_films(country_no_lower)
    if not country_label:
        country_label = nats.find_nat_others(country_no_lower)
    if not country_label:
        country_label = team_work.Get_team_work_Club(country_no_lower)

    if country_label == "" and do_Get_contry2:
        country_label = contry2_bot.Get_contry2(country)

    if not country_label:
        Prefix = {
            "women's ": "نسائية",
            "men's ": "رجالية",
            "fasa ": "فاسااا",
            "non-combat ": "غير قتالية",
        }

        for prefix, prefix_label in Prefix.items():
            if not country.startswith(prefix):
                continue
            print(f">>> country.startswith({prefix})")
            substring = country[len(prefix) :]
            Add_to_main2_tab(prefix, prefix_label)
            substring_label = contry2_bot.Get_contry2(substring)

            if substring_label == "":
                substring_label = contry2_lab.get_lab_for_contry2(substring)

            if substring_label == "":
                substring_label = ye_ts_bot.translate_general_category(substring)

            if substring_label:
                Add_to_main2_tab(substring, substring_label)
                country_label = f"{substring_label} {prefix_label}"
                print_put(f'>>>>>> xxx new country_label  "{country_label}" ')
                break

    OKay = True

    if country_label == "" and OKay:
        separators = [
            " by ",
            " based in ",
            " in ",
            " about ",
            "-of ",
            " of ",
            " from ",
            " to ",
            " at ",
            " on ",
        ]

        for separator in separators:
            if separator in country:
                OKay = False
                break

    if country_label == "" and OKay:
        Prefix2 = {
            "defunct national ": "{} وطنية سابقة",
        }

        for prefix, prefix_label in Prefix2.items():
            if not country.startswith(prefix):
                continue
            print(f">>> country.startswith({prefix})")
            substring = country[len(prefix) :]
            substring_label = contry2_bot.Get_contry2(substring)

            if substring_label == "":
                substring_label = contry2_lab.get_lab_for_contry2(substring)

            if substring_label == "":
                substring_label = ye_ts_bot.translate_general_category(substring)

            if substring_label:
                Add_to_main2_tab(substring, substring_label)
                country_label = prefix_label.format(substring_label)
                if substring_label.strip().endswith(" في") and prefix == "defunct ":
                    country_label = f'{substring_label.strip()[:-len(" في")]} سابقة في'
                print_put(f'>>>>>> cdcdc new country_label  "{country_label}" ')
                break

    if country_label:
        if "سنوات في القرن" in country_label:
            country_label = re.sub(r"سنوات في القرن", "سنوات القرن", country_label)

    if not country_label:
        RE1 = RE1_compile.match(country)
        RE2 = RE2_compile.match(country)
        RE3 = RE3_compile.match(country)

        if RE1 or RE2 or RE3:
            country_label = with_years_bot.get_label_with_years(country)

    if country_label == "" and country.endswith(" members of"):
        country2 = country.replace(" members of", "")
        country_label = Nat_mens.get(country2, "")
        if country_label:
            country_label = f"{country_label} أعضاء في  "
            print_put(f"a<<lightblue>>>2021 get_country_label lab = {country_label}")

    if not country_label:
        country_label = Sports_Keys_For_Label.get(country, "")

    get_country_label_done[country] = country_label
    output_test(f'>>>> Get country "{country_label}"')
    output_test(">> ----------------- end get_country_label ----------------- ")
    return country_label


def get_country_or_term_label(text: str, tito: str, Type: str = "", do_Get_contry2: bool = True) -> str:
    """Retrieve the corresponding label for a given country or term."""

    print_put(f'get_country_or_term_label Type:"{Type}", tito:"{tito}", c_ct_lower:"{text}" ')
    if "makeerr" in sys.argv:
        do_Get_contry2 = True

    test_3 = re.sub(r"\d+", "", text.strip())
    test3_results = ["", "-", "–", "−"]
    label = text if test_3 in test3_results else ""
    if not label:
        label = New_female_keys.get(text, "")
    if not label:
        label = centries_years_dec.get(text, "")

    if label == "" and Type != "Type_lab":
        if text.startswith("the "):
            print_put(f'>>>> text:"{text}" startswith("the ")')
            substring = text[len("the ") :]

            label = pop_All_2018.get(substring, "")

            if not label:
                label = get_country_label(substring, do_Get_contry2=do_Get_contry2)

    if not label:
        if re.sub(r"\d+", "", text) == "":
            label = text
        else:
            label = centries_years_dec.get(text, "")

    if label == "":
        label = get_country_label(text, do_Get_contry2=do_Get_contry2)

    if label == "" and Type == "Type_lab":
        suffixes = [" of", " in", " at"]

        for suffix in suffixes:
            if label:
                break

            if not text.endswith(suffix):
                continue

            substring = text[: -len(suffix)]

            substring_label = Jobs_key.get(substring, "")

            print_put(f'substring:"{substring}", substring_label:"{substring_label}", text:"{text}" ')

            if label == "" and substring_label:
                label = f"{substring_label} من "
                print_put(f"Jobs_key:: add من to label:{label}, line:1583.")

            if not substring_label:
                substring_label = pop_All_2018.get(substring, "")

            if not substring_label:
                substring_label = get_country_label(substring, do_Get_contry2=do_Get_contry2)

            if label == "" and substring_label:
                if text in pop_of_without_in:
                    label = substring_label
                    print_put("skip add في to pop_of_without_in")
                else:
                    label = f"{substring_label} في "
                    print_put(f"XX add في to label:{label}, line:1596.")
                break
        if label == "" and tito.strip() == "in":
            label = pop_All_2018.get(f"{text} in", "")

        if not label:
            label = get_country_label(text, do_Get_contry2=do_Get_contry2)

    if not label:
        label = find_wikidata(text)

    if label:
        print_put(f'get_country_or_term_label label:"{label}" ')

    elif tito.strip() == "for" and text.startswith("for "):
        return get_country_or_term_label(text[len("for ") :], "", Type=Type)

    return label
