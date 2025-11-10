#!/usr/bin/python3
"""
pop_All_2018
"""
# ---
from typing import Dict
from ..utils.json_dir import open_json_file
from ..sports.olympics_data import olympics
from ..mixed.all_keys2 import pf_keys2
from ..geo.Labels_Contry import New_P17_Finall
from ..tv.films_mslslat import films_mslslat_tab
from ..jobs.Jobs import Jobs_new, Jobs_key
from ..sports.Sport_key import Sports_Keys_For_Label
from ..by_type import By_table
from ..sports.teams_new_data import Teams_new


def load_pop_All_2018() -> Dict[str, str]:
    # result: 524266 item
    data = open_json_file("pop_All_2018") or {}     # 161

    sources = [
        pf_keys2,               # 26,557
        Jobs_new,               # 134,421
        Jobs_key,               # 132,864
        films_mslslat_tab,      # 2,480
        By_table,               # 15,899
        Teams_new,              # 373,927
        New_P17_Finall,         # 62,671
        Sports_Keys_For_Label,  # 687
    ]
    for source in sources:
        for pla, value in source.items():
            if value:
                data.setdefault(pla.lower(), value)

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
