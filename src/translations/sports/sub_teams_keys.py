#!/usr/bin/python3
""" """

from ...helps import len_print
from ..sports.Sport_key import SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_OLYMPIC

sub_teams_new = {
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
    "men's footballers": "لاعبو كرة قدم رجالية",
    "national youth sports teams of": "منتخبات رياضية وطنية شبابية في",
    "national sports teams of": "منتخبات رياضية وطنية في",
    "national sports teams": "منتخبات رياضية وطنية",
    "national men's sports teams": "منتخبات رياضية وطنية رجالية",
    "national men's sports teams of": "منتخبات رياضية وطنية رجالية في",
    "national women's sports teams": "منتخبات رياضية وطنية نسائية",
    "national women's sports teams of": "منتخبات رياضية وطنية نسائية في",
}
# ---
YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# ---
for year in YEARS_LIST:
    sub_teams_new[f"under-{year} sport"] = f"رياضة تحت {year} سنة"

sport_starts = {
    "men's a'": "للرجال للمحليين",
    "men's b": "الرديف للرجال",
    "men's": "للرجال",
    "women's": "للسيدات",
    "men's youth": "للشباب",
    "women's youth": "للشابات",
    # "professional": "للمحترفين",
    "amateur": "للهواة",
    "youth": "للشباب",
}
# ---
for sport, sport_label in SPORTS_KEYS_FOR_LABEL.items():
    sub_teams_new[f"youth {sport}"] = f"{sport_label} للشباب"
    sub_teams_new[f"{sport} mass media"] = f"إعلام {sport_label}"
    sub_teams_new[f"{sport} non-playing staff"] = f"طاقم {sport_label} غير اللاعبين"
    for modifier, modifier_label in sport_starts.items():
        sub_teams_new[f"{modifier} {sport}"] = f"{sport_label} {modifier_label}"
    olympic_label = SPORTS_KEYS_FOR_OLYMPIC.get(sport, f"{sport_label} أولمبية")
    sub_teams_new[f"{sport} olympic champions"] = f"أبطال {olympic_label}"
    sub_teams_new[f"{sport} olympics"] = olympic_label
    sub_teams_new[f"{sport} olympic"] = olympic_label
    sub_teams_new[f"olympic {sport}"] = olympic_label
    sub_teams_new[f"olympics mens {sport}"] = olympic_label
    sub_teams_new[f"international {sport}"] = olympic_label.replace("أولمبي", "دولي")
    sub_teams_new[f"olympics men's {sport}"] = f"{olympic_label} للرجال"
    sub_teams_new[f"olympics women's {sport}"] = f"{olympic_label} للسيدات"


len_print.data_len("sports/sub_teams_keys.py", {"sub_teams_new": sub_teams_new})  # 12,806
