"""
from .te3 import SPORT_FORMTS_ENAR_P17_TEAM, New_team_xo_team_labels
"""

import re
from ...helps import len_print
from ...helps.log import logger
from ..sports.sports_lists import AFTER_KEYS_TEAM, menstt333

SPORT_FORMTS_ENAR_P17_TEAM = {}
New_team_xo_team_labels = {}
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

        New_team_xo_team_labels[f"world junior xoxo {ioi}"] = "بطولة العالم xoxo للناشئين"
        New_team_xo_team_labels[f"world xoxo junior {ioi}"] = "بطولة العالم xoxo للناشئين"
        New_team_xo_team_labels[f"xoxo world junior {ioi}"] = "بطولة العالم xoxo للناشئين"
        New_team_xo_team_labels[f"xoxo junior world {ioi}"] = "بطولة العالم xoxo للناشئين"

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
        New_team_xo_team_labels[f"women's xoxo {ioi}"] = "بطولة xoxo للسيدات"

        New_team_xo_team_labels[f"men's xoxo world {ioi}"] = "بطولة العالم xoxo للرجال"
        New_team_xo_team_labels[f"women's xoxo world {ioi}"] = "بطولة العالم xoxo للسيدات"

    # ---World champion national
    New_team_xo_team_labels["international xoxo council"] = "المجلس الدولي xoxo"
    New_team_xo_team_labels["xoxo world cup"] = "كأس العالم xoxo"
    New_team_xo_team_labels["xoxo world cup tournaments"] = "بطولات كأس العالم xoxo"

    # 'Wheelchair Rugby League World Cup': 'كأس العالم لدوري الرجبي على الكراسي المتحركة'
    # New_team_xo_team_labels["xoxo league"] = "دوري xoxo"
    # New_team_xo_team_labels["xoxo league world cup"] = "كأس العالم لدوري xoxo"
    # New_team_xo_team_labels["xoxo league finals"] = "نهائيات دوري xoxo"

    # 'football league': 'دوري لكرة القدم',
    # New_team_xo_team_labels["xoxo league"] = "دوري xoxo"

    # 'Wheelchair Rugby League World Cup': 'كأس العالم لدوري الرجبي على الكراسي المتحركة'
    New_team_xo_team_labels["xoxo world cup"] = "كأس العالم xoxo"

    New_team_xo_team_labels["amateur xoxo world cup"] = "كأس العالم xoxo للهواة"
    New_team_xo_team_labels["youth xoxo world cup"] = "كأس العالم xoxo للشباب"
    New_team_xo_team_labels["men's xoxo world cup"] = "كأس العالم xoxo للرجال"

    New_team_xo_team_labels["women's xoxo world cup"] = "كأس العالم xoxo للسيدات"
    New_team_xo_team_labels["women's xoxo world cup tournaments"] = "بطولات كأس العالم xoxo للسيدات"


def _build_nat_formats_for_p17():
    data = {}
    # ---
    NAT_PLACE_HOLDER = "{}"
    # ---
    data["xoxo league"] = "دوري {} xoxo "
    data["professional xoxo league"] = "دوري {} xoxo للمحترفين"
    # ---
    data["amateur xoxo cup"] = "كأس {} xoxo للهواة"
    data["youth xoxo cup"] = "كأس {} xoxo للشباب"
    data["men's xoxo cup"] = "كأس {} xoxo للرجال"
    data["women's xoxo cup"] = "كأس {} xoxo للسيدات"
    # ---
    data["amateur xoxo championships"] = "بطولة {} xoxo للهواة"
    data["youth xoxo championships"] = "بطولة {} xoxo للشباب"
    data["men's xoxo championships"] = "بطولة {} xoxo للرجال"
    data["women's xoxo championships"] = "بطولة {} xoxo للسيدات"
    # ---
    data["amateur xoxo championship"] = "بطولة {} xoxo للهواة"
    data["youth xoxo championship"] = "بطولة {} xoxo للشباب"
    data["men's xoxo championship"] = "بطولة {} xoxo للرجال"
    data["women's xoxo championship"] = "بطولة {} xoxo للسيدات"
    # ---
    data["xoxo cup"] = "كأس {} xoxo"
    data["xoxo cup"] = "كأس {} xoxo"

    number_xo = 0
    # ---
    for tyu, tyu_lab in New_Tato.items():
        logger.debug(" ========= country =========== ")
        K_at_p = tyu_lab.format("xoxo")
        number_xo += 1
        # ---
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
            data[Ab] = pre_lab2
    # ---national youth handball team
    data["xoxo national team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo"
    data["national xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo"
    # ---
    # Category:Denmark national football team staff
    data["xoxo national team staff"] = f"طاقم منتخب {NAT_PLACE_HOLDER} xoxo"
    # ---
    # Category:Denmark national football team non-playing staff
    data["xoxo national team non-playing staff"] = f"طاقم منتخب {NAT_PLACE_HOLDER} xoxo غير اللاعبين"
    # ---
    # Polish men's volleyball national team national junior men's
    data["national junior men's xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للناشئين"
    data["national junior xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للناشئين"
    data["national women's xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للسيدات"
    data["mennnn's national xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال"
    data["men's xoxo national team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال"
    data["national men's xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال"
    # ---
    # Australian men's U23 national road cycling team
    data["men's u23 national xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo تحت 23 سنة للرجال"
    # ---
    data["xoxo league"] = f"دوري {NAT_PLACE_HOLDER} xoxo"
    data["professional xoxo league"] = f"دوري {NAT_PLACE_HOLDER} xoxo للمحترفين"
    # ---
    data["national youth xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للشباب"

    data["national women's xoxo team managers"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات"
    data["national xoxo team managers"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo"

    data["national women's xoxo team coaches"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات"
    data["national xoxo team coaches"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo"

    data["national women's xoxo team trainers"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات"
    data["national xoxo team trainers"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo"
    return data


SPORT_FORMTS_ENAR_P17_TEAM = _build_nat_formats_for_p17()

len_print.data_len("te3.py", {
    "SPORT_FORMTS_ENAR_P17_TEAM": SPORT_FORMTS_ENAR_P17_TEAM,
    "New_team_xo_team_labels": New_team_xo_team_labels,
})
