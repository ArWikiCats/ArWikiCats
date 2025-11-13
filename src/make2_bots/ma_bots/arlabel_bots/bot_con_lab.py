#!/usr/bin/python3
"""
from .arlabel_bots.bot_con_lab import get_con_lab

"""

from ....helps.print_bot import print_put
from ....ma_lists import New_female_keys, New_P17_Finall, pf_keys2
from ...bots import tmp_bot
from ...date_bots import year_lab
from ...format_bots import for_table
from ...fromnet import kooora
from ...fromnet.wd_bot import find_wikidata
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...media_bots.films_bot import test_films
from ...o_bots import bys
from ...p17_bots import nats
from ...sports_bots import team_work
from ..country_bot import Get_c_t_lab, get_country
from .. import country2_lab


def get_con_lab(tito: str, start_get_country2: bool, tito2: str, country: str, country_lower: str) -> str:
    """Retrieve the corresponding label for a given country."""

    con_lab = ""

    if not con_lab:
        con_lab = New_P17_Finall.get(country_lower, "")
    if not con_lab:
        con_lab = pf_keys2.get(country_lower, "")
    if not con_lab:
        con_lab = get_pop_All_18(country_lower, "")
    if not con_lab:
        con_lab = get_pop_All_18(country_lower.replace("-", " "), "")
    if not con_lab:
        con_lab = New_female_keys.get(country_lower.replace("-", " "), "")

    if con_lab == "" and "kingdom-of" in country_lower:
        con_lab = get_pop_All_18(country_lower.replace("kingdom-of", "kingdom of"), "")

    if con_lab == "" and country_lower.startswith("by "):
        con_lab = bys.make_by_label(country_lower)

    if con_lab == "" and " by " in country_lower:
        con_lab = bys.get_by_label(country_lower)

    if tito2 == "for":
        con_lab = for_table.get(country_lower, "")

    if con_lab == "" and country_lower.strip().startswith("in "):
        cco2 = country_lower.strip()[len("in ") :].strip()

        cco2_ = get_country(cco2)

        if not cco2_:
            cco2_ = country2_lab.get_lab_for_country2(cco2)

        if cco2_:
            con_lab = f"في {cco2_}"

    if not con_lab:
        con_lab = year_lab.make_month_lab(country_lower)
    if not con_lab:
        con_lab = test_films(country)
    if not con_lab:
        con_lab = nats.find_nat_others(country)
    if not con_lab:
        con_lab = team_work.Get_team_work_Club(country.strip())

    if not con_lab:
        con_lab = Get_c_t_lab(country_lower, tito, start_get_country2=start_get_country2)

    if not con_lab:
        con_lab = tmp_bot.Work_Templates(country_lower)

    if not con_lab:
        con_lab = country2_lab.get_lab_for_country2(country_lower)

    if not con_lab:
        con_lab = find_wikidata(country_lower)

    if not con_lab:
        con_lab = kooora.kooora_team(country_lower)

    print_put(f"?????? get_con_lab: {country_lower=}, {con_lab=}")

    return con_lab
