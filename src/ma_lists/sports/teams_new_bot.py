#!/usr/bin/python3
"""

"""
import sys

from .sports_lists import AFTER_KEYS, PPP_Keys
from .Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Jobs, Sports_Keys_For_olympic
from ..jobs.jobs_players_list import Football_Keys_players
from ...helps import len_print

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
}
# ---
Years_List = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# السنة الواحدة تساوي 45,560 مدخلة
# ---
# قبل تعديل national
# sports.py: len:"sport_formts_female_nat":  1359170  , len:"sport_formts_en_ar_is_p17":  1359224  , len:"Teams_new":  1496011
# بعد التعديل
# sports.py: len:"sport_formts_female_nat":  559982  , len:"sport_formts_en_ar_is_p17":  564640  , len:"Teams_new":  696189
# ---
# Sports_Keys_For_Jobs["judo"] = "جودو"
# ---
# for typee in PPP_Keys:
# Teams_new["{} sports".format(typee) ] = "رياضات {}".format( PPP_Keys[typee])
# ---
for hg, hga in Sports_Keys_For_Jobs.items():
    # Teams_new[hg] = hga
    Teams_new[f"{hg} managers"] = f"مدربو {hga}"
    Teams_new[f"{hg} coaches"] = f"مدربو {hga}"
    Teams_new[f"{hg} people"] = f"أعلام {hga}"
    Teams_new[f"{hg} playerss"] = f"لاعبو {hga}"
    Teams_new[f"{hg} players"] = f"لاعبو {hga}"
    Teams_new[f"{hg} referees"] = f"حكام {hga}"
# ---
for year in Years_List:
    Teams_new[f"under-{year} sport"] = "رياضة تحت %d سنة" % year
# ---
Teams_new["national youth sports teams of"] = "منتخبات رياضية وطنية شبابية في"
Teams_new["national sports teams of"] = "منتخبات رياضية وطنية في"
Teams_new["national sports teams"] = "منتخبات رياضية وطنية"
# Teams_new["men's national sports teams"] = "منتخبات رياضية وطنية رجالية"
# Teams_new["men's national sports teams of"] = "منتخبات رياضية وطنية رجالية في"
Teams_new["national men's sports teams"] = "منتخبات رياضية وطنية رجالية"
Teams_new["national men's sports teams of"] = "منتخبات رياضية وطنية رجالية في"
Teams_new["national women's sports teams"] = "منتخبات رياضية وطنية نسائية"
# Teams_new["women's national sports teams"] = "منتخبات رياضية وطنية نسائية"
Teams_new["national women's sports teams of"] = "منتخبات رياضية وطنية نسائية في"
# Teams_new["women's national sports teams of"] = "منتخبات رياضية وطنية نسائية في"
# ---
Teams = {
    "national sports teams": "منتخبات رياضية وطنية",
    "national teams": "منتخبات وطنية",
    "teams": "فرق",
    "sports teams": "فرق رياضية",
    "football clubs": "أندية كرة قدم",
    "clubs": "أندية",
}
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
    # Teams_new["{} video games".format(mem) ] = "ألعاب فيديو {}".format(labe)
    # ---
    labes = f"{Sports_Keys_For_Label[mem]} أولمبية"
    # ---
    if mem in Sports_Keys_For_olympic:
        labes = Sports_Keys_For_olympic[mem]
    # ---
    Teams_new[f"{mem} olympic champions"] = "أبطال " + labes
    Teams_new[f"{mem} olympics"] = labes
    Teams_new[f"{mem} olympic"] = labes
    Teams_new[f"olympic {mem}"] = labes
    Teams_new[f"olympics mens {mem}"] = labes
    Teams_new[f"international {mem}"] = labes.replace("أولمبي", "دولي")
    # ---
    Teams_new[f"olympics men's {mem}"] = labes + " للرجال"
    Teams_new[f"olympics women's {mem}"] = labes + " للسيدات"
# ---
Teams_new["international competitions"] = "منافسات دولية"
# ---
New_With_Women = dict(Sports_Keys_For_Jobs)
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
    for after in Football_Keys_players:
        PP_o = f"{sport} {after}"
        # ---
        llab = Football_Keys_players[after]["mens"]
        if PP_o.find("women's") != -1:
            llab = Football_Keys_players[after]["womens"]
        # ---
        Teams_new[PP_o] = f"{llab} {LAAP}"
# ---
Teams_new["men's footballers"] = "لاعبو كرة قدم رجالية"
# ---
len_print.data_len("sports.py", {
    "Teams_new": Teams_new,
})
# ---
__all__ = [
    "Teams_new",
]
