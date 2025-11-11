#!/usr/bin/python3
"""

"""
from ...helps import len_print
from ..sports.Sport_key import Sports_Keys_For_Label, Sports_Keys_For_olympic

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
    "men's footballers" : "لاعبو كرة قدم رجالية",
}
# ---
Years_List = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# ---
for year in Years_List:
    sub_teams_new[f"under-{year} sport"] = f"رياضة تحت {year} سنة"
# ---
sub_teams_new["national youth sports teams of"] = "منتخبات رياضية وطنية شبابية في"
sub_teams_new["national sports teams of"] = "منتخبات رياضية وطنية في"
sub_teams_new["national sports teams"] = "منتخبات رياضية وطنية"
sub_teams_new["national men's sports teams"] = "منتخبات رياضية وطنية رجالية"
sub_teams_new["national men's sports teams of"] = "منتخبات رياضية وطنية رجالية في"
sub_teams_new["national women's sports teams"] = "منتخبات رياضية وطنية نسائية"
sub_teams_new["national women's sports teams of"] = "منتخبات رياضية وطنية نسائية في"
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
    sub_teams_new[f"youth {mem}"] = f"{labe} للشباب"
    sub_teams_new[f"{mem} mass media"] = f"إعلام {labe}"
    sub_teams_new[f"{mem} non-playing staff"] = f"طاقم {labe} غير اللاعبين"
    for jjj in menstts:
        sub_teams_new[f"{jjj.strip()} {mem}"] = f"{labe} {menstts[jjj].strip()}"
    # ---
    labes = f"{Sports_Keys_For_Label[mem]} أولمبية"
    # ---
    if mem in Sports_Keys_For_olympic:
        labes = Sports_Keys_For_olympic[mem]
    # ---
    sub_teams_new[f"{mem} olympic champions"] = f"أبطال {labes}"
    sub_teams_new[f"{mem} olympics"] = labes
    sub_teams_new[f"{mem} olympic"] = labes
    sub_teams_new[f"olympic {mem}"] = labes
    sub_teams_new[f"olympics mens {mem}"] = labes
    sub_teams_new[f"international {mem}"] = labes.replace("أولمبي", "دولي")
    # ---
    sub_teams_new[f"olympics men's {mem}"] = labes + " للرجال"
    sub_teams_new[f"olympics women's {mem}"] = labes + " للسيدات"
# ---


len_print.data_len("sports/sub_teams_keys.py", {
    "sub_teams_new" : sub_teams_new     # 12,806
})
