"""
from .te3 import SPORT_FORMTS_ENAR_P17_TEAM, New_team_xo_team_labels
"""

import re
import sys
from ...helps import len_print
from ...helps.log import logger
from ..sports.sports_lists import AFTER_KEYS_TEAM, menstt333

# ---
SPORT_FORMTS_ENAR_P17_TEAM = {}
New_team_xo_team_labels = {}
# ---
# sf_en_ar_is_p17 لدمجها مع SPORT_FORMTS_EN_AR_IS_P17 في sports.py
sf_en_ar_is_p17 = {}
# ---
YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# السنة الواحدة تساوي 45,560 مدخلة
# ---
New_Tato = {}
# ---
for mrr, mrr_lab in menstt333.items():
    New_Tato[mrr] = mrr_lab
    for year in YEARS_LIST:
        # or year in [23]:
        ylab = "تحت %d سنة" % year
        New_Tato[f"{mrr} under-{year}"] = mrr_lab.replace("{}", "{} %s " % ylab)
# ---
New_Tato["men's under-23 national"] = "{} تحت 23 سنة للرجال"
New_Tato["men's u23 national"] = "{} تحت 23 سنة للرجال"
New_Tato["men's u23 national"] = "{} تحت 23 سنة للرجال"

# ---

# ---
team2 = "xoxo"
team2_lab = "xoxo"
# ---
if True:
    New_team_xo_team_labels["natar xoxo championships"] = "بطولة natar xoxo"
    New_team_xo_team_labels["ladies natar xoxo championships"] = "بطولة natar xoxo للسيدات"
    New_team_xo_team_labels["natar xoxo tour"] = "بطولة natar xoxo"
    New_team_xo_team_labels["natar xoxo tour"] = "بطولة natar xoxo"
    New_team_xo_team_labels["women's natar xoxo tour"] = "بطولة natar xoxo للسيدات"
    New_team_xo_team_labels["ladies natar xoxo tour"] = "بطولة natar xoxo للسيدات"
    # ---
    # New_team_xo_team_labels["asian xoxo tour"] =  "بطولة آسيا xoxo"
    # New_team_xo_team_labels["women's asian xoxo tour"] =  "بطولة آسيا xoxo للسيدات"
    # New_team_xo_team_labels["ladies asian xoxo tour"] =  "بطولة آسيا xoxo للسيدات"
    # ---
    typies = {
        "cups": "كؤوس",
        "clubs": "أندية",
        "competitions": "منافسات",
        "leagues": "دوريات",
        "coaches": "مدربو",  # Category:Indoor soccer coaches in the United States by club
    }
    # ---
    SPORT_FORMTS_ENAR_P17_TEAM["xoxo league"] = "دوري {} xoxo "
    SPORT_FORMTS_ENAR_P17_TEAM["professional xoxo league"] = "دوري {} xoxo للمحترفين"
    # ---tournaments
    New_team_xo_team_labels["world champion national xoxo teams"] = "أبطال بطولة العالم xoxo"
    # ---
    for ioi in ["championships", "championship"]:
        New_team_xo_team_labels[f"world xoxo {ioi} competitors"] = "منافسو بطولة العالم xoxo"
        New_team_xo_team_labels[f"world xoxo {ioi} medalists"] = "فائزون بميداليات بطولة العالم xoxo"
        # outdoor
        New_team_xo_team_labels[f"world wheelchair xoxo {ioi}"] = "بطولة العالم xoxo على الكراسي المتحركة"
        New_team_xo_team_labels[f"world xoxo {ioi}"] = "بطولة العالم xoxo"

        New_team_xo_team_labels[f"xoxo world {ioi}"] = "بطولة العالم xoxo"

        New_team_xo_team_labels[f"world junior xoxo {ioi}"] = "بطولة العالم %s xoxo للناشئين"
        New_team_xo_team_labels[f"world xoxo junior {ioi}"] = "بطولة العالم %s xoxo للناشئين"
        New_team_xo_team_labels[f"xoxo world junior {ioi}"] = "بطولة العالم %s xoxo للناشئين"
        New_team_xo_team_labels[f"xoxo junior world {ioi}"] = "بطولة العالم %s xoxo للناشئين"

        New_team_xo_team_labels[f"world outdoor xoxo {ioi}"] = "بطولة العالم xoxo في الهواء الطلق"
        New_team_xo_team_labels[f"outdoor world xoxo {ioi}"] = "بطولة العالم xoxo في الهواء الطلق"

        New_team_xo_team_labels[f"world amateur xoxo {ioi}"] = "بطولة العالم xoxo للهواة"
        New_team_xo_team_labels[f"world xoxo amateur {ioi}"] = "بطولة العالم xoxo للهواة"
        New_team_xo_team_labels[f"xoxo world amateur {ioi}"] = "بطولة العالم xoxo للهواة"
        New_team_xo_team_labels[f"xoxo amateur world {ioi}"] = "بطولة العالم xoxo للهواة"

        New_team_xo_team_labels[f"world youth xoxo {ioi}"] = "بطولة العالم xoxo للشباب"
        New_team_xo_team_labels[f"world xoxo youth {ioi}"] = "بطولة العالم xoxo للشباب"
        New_team_xo_team_labels[f"xoxo world youth {ioi}"] = "بطولة العالم xoxo للشباب"
        New_team_xo_team_labels[f"xoxo youth world {ioi}"] = "بطولة العالم xoxo للشباب"

        New_team_xo_team_labels[f"men's xoxo {ioi}"] = "بطولة xoxo للرجال"
        New_team_xo_team_labels[f"women's xoxo {ioi}"] = "بطولة %s xoxo للسيدات"

        New_team_xo_team_labels[f"men's xoxo world {ioi}"] = "بطولة العالم xoxo للرجال"
        New_team_xo_team_labels[f"women's xoxo world {ioi}"] = "بطولة العالم %s xoxo للسيدات"

    # ---World champion national
    New_team_xo_team_labels["international xoxo council"] = "المجلس الدولي xoxo"
    New_team_xo_team_labels["xoxo world cup"] = "كأس العالم xoxo"
    New_team_xo_team_labels["xoxo world cup tournaments"] = "بطولات كأس العالم xoxo"

    New_team_xo_team_labels["xoxo league"] = "دوري xoxo"
    New_team_xo_team_labels["xoxo league world cup"] = "كأس العالم لدوري xoxo"
    New_team_xo_team_labels["xoxo league finals"] = "نهائيات دوري xoxo"

    New_team_xo_team_labels["amateur xoxo world cup"] = "كأس العالم xoxo للهواة"
    New_team_xo_team_labels["youth xoxo world cup"] = "كأس العالم xoxo للشباب"
    New_team_xo_team_labels["men's xoxo world cup"] = "كأس العالم xoxo للرجال"

    New_team_xo_team_labels["women's xoxo world cup"] = "كأس العالم %s xoxo للسيدات"
    New_team_xo_team_labels["women's xoxo world cup tournaments"] = "بطولات كأس العالم %s xoxo للسيدات"
    # ---
    SPORT_FORMTS_ENAR_P17_TEAM["amateur xoxo cup"] = "كأس {} xoxo للهواة"
    SPORT_FORMTS_ENAR_P17_TEAM["youth xoxo cup"] = "كأس {} xoxo للشباب"
    SPORT_FORMTS_ENAR_P17_TEAM["men's xoxo cup"] = "كأس {} xoxo للرجال"
    SPORT_FORMTS_ENAR_P17_TEAM["women's xoxo cup"] = "كأس {} %s xoxo للسيدات"
    # ---
    SPORT_FORMTS_ENAR_P17_TEAM["amateur xoxo championships"] = "بطولة {} xoxo للهواة"
    SPORT_FORMTS_ENAR_P17_TEAM["youth xoxo championships"] = "بطولة {} xoxo للشباب"
    SPORT_FORMTS_ENAR_P17_TEAM["men's xoxo championships"] = "بطولة {} xoxo للرجال"
    SPORT_FORMTS_ENAR_P17_TEAM["women's xoxo championships"] = "بطولة {} %s xoxo للسيدات"
    # ---
    SPORT_FORMTS_ENAR_P17_TEAM["amateur xoxo championship"] = "بطولة {} xoxo للهواة"
    SPORT_FORMTS_ENAR_P17_TEAM["youth xoxo championship"] = "بطولة {} xoxo للشباب"
    SPORT_FORMTS_ENAR_P17_TEAM["men's xoxo championship"] = "بطولة {} xoxo للرجال"
    SPORT_FORMTS_ENAR_P17_TEAM["women's xoxo championship"] = "بطولة {} %s xoxo للسيدات"
    # ---
    SPORT_FORMTS_ENAR_P17_TEAM["xoxo cup"] = "كأس {} xoxo"
    SPORT_FORMTS_ENAR_P17_TEAM["xoxo cup"] = "كأس {} xoxo"

# ---
if True:
    number_xo = 0
    # ---
    for tyu, tyu_lab in New_Tato.items():
        logger.debug(" ========= country =========== ")
        K_at_p = tyu_lab.format("xoxo")
        number_xo += 1
        # if team2 == "road cycling":
        # print("tyu: %s" % (tyu_lab) )
        # ---
        # nat_Lab = "منتخب {} الوطني " + K_at_p
        nat_Lab = "منتخب {} " + K_at_p
        for pre, pre_lab in AFTER_KEYS_TEAM.items():
            number_xo += 1
            pre_lab2 = pre_lab.format(nat_Lab)
            Ab = f"{tyu} xoxo {pre}"
            # ---
            if pre == "team players" and "women's" in Ab:
                pre_lab2 = re.sub(r"لاعبو ", "لاعبات ", pre_lab2)
            # ---
            elif "لاعبو " in pre_lab2 and "women's" in Ab:
                pre_lab2 = re.sub(r"لاعبو ", "لاعبات ", pre_lab2)
            # ---
            printo = f"nat_Lab: [{Ab}] : " + pre_lab2
            # if team2 == "road cycling"and pre == "team":
            # print("%d: %s" % (number_xo , printo) )
            logger.debug("%d: %s" % (number_xo, printo))
            SPORT_FORMTS_ENAR_P17_TEAM[Ab] = pre_lab2
    # ---
    _format_ = "{}"
    # ---national youth handball team
    SPORT_FORMTS_ENAR_P17_TEAM["xoxo national team"] = f"منتخب {_format_} xoxo"
    SPORT_FORMTS_ENAR_P17_TEAM["national xoxo team"] = f"منتخب {_format_} xoxo"
    # ---
    # Category:Denmark national football team staff
    SPORT_FORMTS_ENAR_P17_TEAM["xoxo national team staff"] = f"طاقم منتخب {_format_} xoxo"
    # ---
    # Category:Denmark national football team non-playing staff
    SPORT_FORMTS_ENAR_P17_TEAM["xoxo national team non-playing staff"] = f"طاقم منتخب {_format_} xoxo غير اللاعبين"
    # ---
    Fap = f"منتخب {_format_} xoxo"
    # ---
    # Polish men's volleyball national team national junior men's
    SPORT_FORMTS_ENAR_P17_TEAM["national junior men's xoxo team"] = f"منتخب {_format_} xoxo للناشئين"
    SPORT_FORMTS_ENAR_P17_TEAM["national junior xoxo team"] = f"منتخب {_format_} xoxo للناشئين"
    SPORT_FORMTS_ENAR_P17_TEAM["national women's xoxo team"] = f"منتخب {_format_} xoxo للسيدات"
    SPORT_FORMTS_ENAR_P17_TEAM["mennnn's national xoxo team"] = f"منتخب {_format_} xoxo للرجال"
    SPORT_FORMTS_ENAR_P17_TEAM["men's xoxo national team"] = f"منتخب {_format_} xoxo للرجال"
    SPORT_FORMTS_ENAR_P17_TEAM["national men's xoxo team"] = f"منتخب {_format_} xoxo للرجال"
    # ---
    # Australian men's U23 national road cycling team
    SPORT_FORMTS_ENAR_P17_TEAM["men's u23 national xoxo team"] = f"منتخب {_format_} xoxo تحت 23 سنة للرجال"
    # ---
    SPORT_FORMTS_ENAR_P17_TEAM["xoxo league"] = f"دوري {_format_} xoxo"
    SPORT_FORMTS_ENAR_P17_TEAM["professional xoxo league"] = f"دوري {_format_} xoxo للمحترفين"
    # ---
    SPORT_FORMTS_ENAR_P17_TEAM["national youth xoxo team"] = f"منتخب {_format_} xoxo للشباب"

    SPORT_FORMTS_ENAR_P17_TEAM["national women's xoxo team managers"] = f"مدربو منتخب {_format_} xoxo للسيدات"
    SPORT_FORMTS_ENAR_P17_TEAM["national xoxo team managers"] = f"مدربو منتخب {_format_} xoxo"

    SPORT_FORMTS_ENAR_P17_TEAM["national women's xoxo team coaches"] = f"مدربو منتخب {_format_} xoxo للسيدات"
    SPORT_FORMTS_ENAR_P17_TEAM["national xoxo team coaches"] = f"مدربو منتخب {_format_} xoxo"

    SPORT_FORMTS_ENAR_P17_TEAM["national women's xoxo team trainers"] = f"مدربو منتخب {_format_} xoxo للسيدات"
    SPORT_FORMTS_ENAR_P17_TEAM["national xoxo team trainers"] = f"مدربو منتخب {_format_} xoxo"

len_print.data_len("te3.py", {
    "SPORT_FORMTS_ENAR_P17_TEAM": SPORT_FORMTS_ENAR_P17_TEAM,
    "New_team_xo_team_labels": New_team_xo_team_labels,
})
