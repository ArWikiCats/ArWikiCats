#!/usr/bin/python3
"""
pop_All_2018
"""

# ---
from typing import Dict

from ..by_type import By_table
from ..geo.labels_country import New_P17_Finall
from ..jobs.Jobs import Jobs_new, jobs_mens_data
from ..mixed.all_keys2 import pf_keys2
from ..sports.olympics_data import olympics
from ..sports.Sport_key import SPORTS_KEYS_FOR_LABEL
from ..sports.sub_teams_keys import sub_teams_new
from ..tv.films_mslslat import films_mslslat_tab
from ..utils.json_dir import open_json_file

# from ..sports.teams_new_data import TEAMS_NEW


def load_pop_All_2018() -> Dict[str, str]:
    """Load and merge population-related label sources into a single mapping."""
    # result: 524266 item with TEAMS_NEW
    # result: 226,093 item
    data = open_json_file("population/pop_All_2018.json") or {}  # 161

    sources = [
        pf_keys2,  # 26,557
        Jobs_new,  # 132,174
        jobs_mens_data,  # 130,632
        films_mslslat_tab,  # 2,480
        By_table,  # 15,899
        sub_teams_new,  # 12,134
        # TEAMS_NEW,            # 352,946
        New_P17_Finall,  # 62,671
        SPORTS_KEYS_FOR_LABEL,  # 672
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
