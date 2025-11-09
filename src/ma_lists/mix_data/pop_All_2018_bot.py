#!/usr/bin/python3
"""
pop_All_2018
"""
# ---
from ..utils.json_dir import open_json_file
from ..sports.olympics_data import olympics
from ..mixed.all_keys2 import pf_keys2
from ..geo.Labels_Contry import New_P17_Finall
from ..tv.films_mslslat import films_mslslat_tab
from ..jobs.Jobs import Jobs_new, Jobs_key
from ..sports.Sport_key import Sports_Keys_For_Label
from ..by_type import By_table
from ..sports.teams_new_data import Teams_new


def load_pop_All_2018() -> None:

    data = open_json_file("data") or {}

    for gg, gg_lab in pf_keys2.items():
        gg2 = gg.lower()
        if not data.get(gg2):
            data[gg2] = gg_lab

    for pla in Jobs_new:
        pla2 = pla.lower()
        if Jobs_new[pla]:
            if not data.get(pla2):
                data[pla2] = Jobs_new[pla]
    for pla in Jobs_key:
        pla2 = pla.lower()
        if Jobs_key[pla]:
            if not data.get(pla2):
                data[pla2] = Jobs_key[pla]

    for cyi in films_mslslat_tab:
        cyi2 = cyi.lower()
        if not data.get(cyi2):
            data[cyi2] = films_mslslat_tab[cyi]

    for by in By_table:
        by2 = by.lower()
        if By_table[by]:
            if not data.get(by2):
                data[by2] = By_table[by]

    for paa, taba in Teams_new.items():
        paa2 = paa.lower()
        if taba:
            if not data.get(paa2):
                data[paa2] = taba

    for xo in list(New_P17_Finall):
        xo2 = xo.lower()
        if not data.get(xo2):
            data[xo2] = New_P17_Finall[xo]

    for paa in Sports_Keys_For_Label:
        paa2 = paa.lower()
        if Sports_Keys_For_Label[paa]:
            if not data.get(paa2):
                data[paa2] = Sports_Keys_For_Label[paa]

    # data["conflicts"] = "نزاعات"
    data["by country"] = "حسب البلد"
    data["in"] = "في"
    data["films"] = "أفلام"
    data["decades"] = "عقود"
    data["women"] = "المرأة"
    data["women in"] = "المرأة في"

    data["medalists"] = "فائزون بميداليات"
    data["gold medalists"] = "فائزون بميداليات ذهبية"
    data["silver medalists"] = "فائزون بميداليات فضية"
    data["bronze medalists"] = "فائزون بميداليات برونزية"

    data["kingdom of"] = "مملكة"
    data["kingdom-of"] = "مملكة"

    data["country"] = "البلد"

    for olmp, olmp_lab in olympics.items():
        data[olmp] = olmp_lab

    return data
