#!/usr/bin/python3
"""
from .arlabel_bots.bot_con_lab import get_connector_label

"""

import sys
from typing import Dict
from .. import contry2_lab
from ...sports_bots import team_work
from ...date_bots import year_lab

from ...bots import tmp_bot
from ...o_bots import bys
from ...p17_bots import nats

from ...media_bots.films_bot import test_films

from ....ma_lists import pf_keys2
from ....ma_lists import New_P17_Finall
from ....ma_lists import New_female_keys

from ...fromnet.wd_bot import find_wikidata
from ...fromnet import kooora
from ...format_bots import for_table

from ...matables_bots.bot_2018 import pop_All_2018


from ....helps.print_bot import print_put

from ..contry_bot import get_country_label, get_country_or_term_label

Find_f_wikidata: Dict[int, bool] = {1: "nowikidata" not in sys.argv}


def get_connector_label(tito: str, do_get_country2: bool, tito2: str, country: str, country_lower: str) -> str:
    """Retrieve the corresponding label for a given country."""

    connector_label = ""

    if not connector_label:
        connector_label = New_P17_Finall.get(country_lower, "")
    if not connector_label:
        connector_label = pf_keys2.get(country_lower, "")
    if not connector_label:
        connector_label = pop_All_2018.get(country_lower, "")
    if not connector_label:
        connector_label = pop_All_2018.get(country_lower.replace("-", " "), "")
    if not connector_label:
        connector_label = New_female_keys.get(country_lower.replace("-", " "), "")

    if connector_label == "" and "kingdom-of" in country_lower:
        connector_label = pop_All_2018.get(country_lower.replace("kingdom-of", "kingdom of"), "")

    if connector_label == "" and country_lower.startswith("by "):
        connector_label = bys.Make_By_lab(country_lower)

    if connector_label == "" and " by " in country_lower:
        connector_label = bys.Get_by_label(country_lower)

    if tito2 == "for":
        connector_label = for_table.get(country_lower, "")

    if connector_label == "" and country_lower.strip().startswith("in "):
        country_substring = country_lower.strip()[len("in ") :].strip()

        country_substring_label = get_country_label(country_substring)

        if not country_substring_label:
            country_substring_label = contry2_lab.get_lab_for_contry2(country_substring)

        if country_substring_label:
            connector_label = f"في {country_substring_label}"

    if not connector_label:
        connector_label = year_lab.get_month_label(country_lower)
    if not connector_label:
        connector_label = test_films(country)
    if not connector_label:
        connector_label = nats.find_nat_others(country)
    if not connector_label:
        connector_label = team_work.Get_team_work_Club(country.strip())

    if not connector_label:
        connector_label = get_country_or_term_label(country_lower, tito, do_Get_contry2=do_get_country2)

    if not connector_label:
        connector_label = tmp_bot.Work_Templates(country_lower)

    if not connector_label:
        connector_label = contry2_lab.get_lab_for_contry2(country_lower)

    if not connector_label:
        connector_label = find_wikidata(country_lower)
    if not connector_label:
        connector_label = kooora.kooora_team(country_lower, Local=Find_f_wikidata[1])

    print_put(f"?????? get_connector_label: {country_lower=}, {connector_label=}")

    return connector_label
