#!/usr/bin/python3
"""

"""
from typing import Dict
from ..sports.sports_lists import AFTER_KEYS
from ..sports.Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Jobs, Sports_Keys_For_olympic
from ..jobs.jobs_players_list import FOOTBALL_KEYS_PLAYERS
# from ...helps import len_print

New_With_Women = {}


def load_teams_new() -> Dict[str, str]:
    """
    lazy load Teams_new

    # result length: "count": 325907, "size": "7.3 MiB" ( Sports_Keys_New*1425  (223*1425))
    """
    # ---
    data = {
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
        data[f"under-{year} sport"] = "رياضة تحت %d سنة" % year
    # ---
    for hg, hga in Sports_Keys_For_Jobs.items():
        data[f"{hg} managers"] = f"مدربو {hga}"
        data[f"{hg} coaches"] = f"مدربو {hga}"
        data[f"{hg} people"] = f"أعلام {hga}"
        data[f"{hg} playerss"] = f"لاعبو {hga}"
        data[f"{hg} players"] = f"لاعبو {hga}"
        data[f"{hg} referees"] = f"حكام {hga}"
    # ---
    data["national youth sports teams of"] = "منتخبات رياضية وطنية شبابية في"
    data["national sports teams of"] = "منتخبات رياضية وطنية في"
    data["national sports teams"] = "منتخبات رياضية وطنية"
    data["national men's sports teams"] = "منتخبات رياضية وطنية رجالية"
    data["national men's sports teams of"] = "منتخبات رياضية وطنية رجالية في"
    data["national women's sports teams"] = "منتخبات رياضية وطنية نسائية"
    data["national women's sports teams of"] = "منتخبات رياضية وطنية نسائية في"
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
        data[f"youth {mem}"] = f"{labe} للشباب"
        data[f"{mem} mass media"] = f"إعلام {labe}"
        data[f"{mem} non-playing staff"] = f"طاقم {labe} غير اللاعبين"
        for jjj in menstts:
            data[f"{jjj.strip()} {mem}"] = f"{labe} {menstts[jjj].strip()}"
        # ---
        labes = f"{Sports_Keys_For_Label[mem]} أولمبية"
        # ---
        if mem in Sports_Keys_For_olympic:
            labes = Sports_Keys_For_olympic[mem]
        # ---
        data[f"{mem} olympic champions"] = f"أبطال {labes}"
        data[f"{mem} olympics"] = labes
        data[f"{mem} olympic"] = labes
        data[f"olympic {mem}"] = labes
        data[f"olympics mens {mem}"] = labes
        data[f"international {mem}"] = labes.replace("أولمبي", "دولي")
        # ---
        data[f"olympics men's {mem}"] = labes + " للرجال"
        data[f"olympics women's {mem}"] = labes + " للسيدات"
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
            data[f"{sport} {after}"] = f"{llab} {LAAP}"
        # ---
        for after in FOOTBALL_KEYS_PLAYERS:
            PP_o = f"{sport} {after}"
            # ---
            llab = FOOTBALL_KEYS_PLAYERS[after]["mens"]
            if PP_o.find("women's") != -1:
                llab = FOOTBALL_KEYS_PLAYERS[after]["womens"]
            # ---
            data[PP_o] = f"{llab} {LAAP}"
    # ---
    return data


__all__ = [
    "load_teams_new",
]
