#!/usr/bin/python3
"""
pop_All_2018
"""
from typing import Dict
from ..sports.olympics_data import olympics
from ..utils.json_dir import open_json_file


def load_pop_All_2018() -> Dict[str, str]:
    """Load and merge population-related label sources into a single mapping."""
    # result: 524266 item with TEAMS_NEW
    # result: 226,093 item
    data = open_json_file("population/pop_All_2018.json") or {}  # 161

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
