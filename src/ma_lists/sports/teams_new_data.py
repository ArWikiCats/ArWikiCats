#!/usr/bin/python3
"""

"""
from typing import Dict
from .sports_lists import AFTER_KEYS
from .Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Jobs, Sports_Keys_For_olympic
from ..jobs.jobs_players_list import FOOTBALL_KEYS_PLAYERS
from ...helps import len_print

New_With_Women = {}


def load_teams_new() -> Dict[str, str]:
    """
    lazy load Teams_new

    # result length: "count": 325907, "size": "7.3 MiB" ( Sports_Keys_New*1425  (223*1425))
    """
    # ---
    Teams_new = {
        "current seasons": "مواسم حالية",
        "international races": "سباقات دولية",
        "national championships": "بطولات وطنية",
        "national champions": "أبطال بطولات وطنية",
        "world competitions": "منافسات عالمية",
        "military competitions": "منافسات عسكرية",
        "men's teams": "فرق رجالية",
        "world championships competitors": "منافسون في بطولات العالم",
        "world championships medalists": "فائزون بميداليات بطولات العالم",
        "women's teams": "فرق نسائية",
        "world championships": "بطولة العالم",
        "international women's competitions": "منافسات نسائية دولية",
        "international men's competitions": "منافسات رجالية دولية",
        "international competitions": "منافسات دولية",
        "national team results": "نتائج منتخبات وطنية",
        "national teams": "منتخبات وطنية",
        "national youth teams": "منتخبات وطنية شبابية",
        "national men's teams": "منتخبات وطنية رجالية",
        "national women's teams": "منتخبات وطنية نسائية",
        "men's footballers" : "لاعبو كرة قدم رجالية",
    }
    # ---
    Years_List = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
    # ---
    for year in Years_List:
        Teams_new[f"under-{year} sport"] = "رياضة تحت %d سنة" % year
    # ---
    for hg, hga in Sports_Keys_For_Jobs.items():
        Teams_new[f"{hg} managers"] = f"مدربو {hga}"
        Teams_new[f"{hg} coaches"] = f"مدربو {hga}"
        Teams_new[f"{hg} people"] = f"أعلام {hga}"
        Teams_new[f"{hg} playerss"] = f"لاعبو {hga}"
        Teams_new[f"{hg} players"] = f"لاعبو {hga}"
        Teams_new[f"{hg} referees"] = f"حكام {hga}"
    # ---
    Teams_new["national youth sports teams of"] = "منتخبات رياضية وطنية شبابية في"
    Teams_new["national sports teams of"] = "منتخبات رياضية وطنية في"
    Teams_new["national sports teams"] = "منتخبات رياضية وطنية"
    Teams_new["national men's sports teams"] = "منتخبات رياضية وطنية رجالية"
    Teams_new["national men's sports teams of"] = "منتخبات رياضية وطنية رجالية في"
    Teams_new["national women's sports teams"] = "منتخبات رياضية وطنية نسائية"
    Teams_new["national women's sports teams of"] = "منتخبات رياضية وطنية نسائية في"
    # ---
    menstts = {
        "": "",
        "men's a' ": " للرجال للمحليين",
        "men's b ": " الرديف للرجال",
        "men's ": " للرجال",
        "women's ": " للسيدات",
        "men's youth ": " للشباب",
        "women's youth ": " للشابات",
        # "professional " : " للمحترفين",
        "amateur ": " للهواة",
        "youth ": " للشباب",
    }
    # ---
    for mem, labe in Sports_Keys_For_Label.items():
        Teams_new[f"youth {mem}"] = f"{labe} للشباب"
        Teams_new[f"{mem} mass media"] = f"إعلام {labe}"
        Teams_new[f"{mem} non-playing staff"] = f"طاقم {labe} غير اللاعبين"
        for jjj in menstts:
            Teams_new[f"{jjj.strip()} {mem}"] = f"{labe} {menstts[jjj].strip()}"
        # ---
        labes = f"{Sports_Keys_For_Label[mem]} أولمبية"
        # ---
        if mem in Sports_Keys_For_olympic:
            labes = Sports_Keys_For_olympic[mem]
        # ---
        Teams_new[f"{mem} olympic champions"] = f"أبطال {labes}"
        Teams_new[f"{mem} olympics"] = labes
        Teams_new[f"{mem} olympic"] = labes
        Teams_new[f"olympic {mem}"] = labes
        Teams_new[f"olympics mens {mem}"] = labes
        Teams_new[f"international {mem}"] = labes.replace("أولمبي", "دولي")
        # ---
        Teams_new[f"olympics men's {mem}"] = labes + " للرجال"
        Teams_new[f"olympics women's {mem}"] = labes + " للسيدات"
    # ---
    PPP_Keys = {
        "men's": "رجالية",  # للرجال
        "women's": "نسائية",  # للسيدات
        "youth": "شبابية",  # للشباب
        "men's youth": "للشباب",  # للشابات
        "women's youth": "للشابات",  # للشابات
        "amateur": "للهواة",  # للهواة
    }
    # ---
    New_With_Women = dict(Sports_Keys_For_Jobs)
    # New_With_Women = {}
    # ---
    for team, job_label in Sports_Keys_For_Jobs.items():
        # ---
        for PP in PPP_Keys:
            New_With_Women[f"{PP} {team}"] = f"{job_label} {PPP_Keys[PP]}"
    # ---
    for sport, LAAP in New_With_Women.items():
        # ---
        for after in AFTER_KEYS:
            llab = AFTER_KEYS[after]
            Teams_new[f"{sport} {after}"] = f"{llab} {LAAP}"
        # ---
        for after in FOOTBALL_KEYS_PLAYERS:
            PP_o = f"{sport} {after}"
            # ---
            llab = FOOTBALL_KEYS_PLAYERS[after]["mens"]
            if PP_o.find("women's") != -1:
                llab = FOOTBALL_KEYS_PLAYERS[after]["womens"]
            # ---
            Teams_new[PP_o] = f"{llab} {LAAP}"
    # ---
    return Teams_new


Teams_new = {}
# Teams_new = load_teams_new()

len_print.data_len("sports.py", {
    "Teams_new": Teams_new,             # "count": 325907, "size": "7.3 MiB" ( Sports_Keys_New*1425  (223*1425))
    "New_With_Women": New_With_Women,   # "count": 4116, "size": "101.4 KiB"
})

__all__ = [
    "Teams_new",
    "load_teams_new",
]
