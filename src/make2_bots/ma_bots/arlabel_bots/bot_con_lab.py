#!/usr/bin/python3
"""
!

"""

from .. import country2_lab
from ....helps.print_bot import print_put
from ....translations import New_female_keys, New_P17_Finall, pf_keys2
from ...bots import tmp_bot
from ...date_bots import year_lab
from ...format_bots import for_table
from ...fromnet import kooora
from ...fromnet.wd_bot import find_wikidata
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...media_bots.films_bot import te_films
from ...o_bots import bys
from ...p17_bots import nats
from ...sports_bots import team_work
from ..country_bot import Get_c_t_lab, get_country


def get_con_lab(preposition: str, tito2: str, country: str, country_lower: str, start_get_country2: bool) -> str:
    """Retrieve the corresponding label for a given country."""

    label = ""

    if not label:
        label = New_P17_Finall.get(country_lower, "")
    if not label:
        label = pf_keys2.get(country_lower, "")
    if not label:
        label = get_pop_All_18(country_lower, "")
    if not label:
        label = get_pop_All_18(country_lower.replace("-", " "), "")
    if not label:
        label = New_female_keys.get(country_lower.replace("-", " "), "")

    if label == "" and "kingdom-of" in country_lower:
        label = get_pop_All_18(country_lower.replace("kingdom-of", "kingdom of"), "")

    if label == "" and country_lower.startswith("by "):
        label = bys.make_by_label(country_lower)

    if label == "" and " by " in country_lower:
        label = bys.get_by_label(country_lower)

    if tito2 == "for":
        label = for_table.get(country_lower, "")

    if label == "" and country_lower.strip().startswith("in "):
        cco2 = country_lower.strip()[len("in ") :].strip()

        cco2_ = get_country(cco2)

        if not cco2_:
            cco2_ = country2_lab.get_lab_for_country2(cco2)

        if cco2_:
            label = f"في {cco2_}"

    if not label:
        label = year_lab.make_month_lab(country_lower)
    if not label:
        label = te_films(country)
    if not label:
        label = nats.find_nat_others(country)
    if not label:
        label = team_work.Get_team_work_Club(country.strip())

    if not label:
        label = Get_c_t_lab(country_lower, preposition, start_get_country2=start_get_country2)

    if not label:
        label = tmp_bot.Work_Templates(country_lower)

    if not label:
        label = country2_lab.get_lab_for_country2(country_lower)

    if not label:
        label = find_wikidata(country_lower)

    if not label:
        label = kooora.kooora_team(country_lower)

    print_put(f"?????? get_con_lab: {country_lower=}, {label=}")

    return label
