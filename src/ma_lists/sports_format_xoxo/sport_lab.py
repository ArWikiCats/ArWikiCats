#!/usr/bin/python3
"""


"""

import re

from .team_job import New_team_xo_jobs, New_team_xo_labels, sport_formts_enar_p17_jobs
from .te3 import New_team_xo_team

from ..sports import sport_formts_enar_p17_team
from ..sports.Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Team, Sports_Keys_For_Jobs, fanco_line
from ..nats.Nationality import All_contry_with_nat_ar
from ...helps.print_bot import print_put, output_test

# ---
pp = [[len(xy.split(" ")), xy] for xy in All_contry_with_nat_ar]
pp.sort(reverse=True)
texts_new = "22"
# ---
for lln, sp in pp:
    texts_new += f"|{sp}"
All_nat_to_ar = texts_new.replace("22|", "", 1)
All_nat_to_ar = All_nat_to_ar.replace("(", r"\(").replace(")", r"\)")
nat_reg_line = rf".*\s({All_nat_to_ar})\s.*"
# ---


# New_Sport_Format_team_xo_en_ar_is_P17
def Get_Sport_Format_xo_en_ar_is_P17(con_3):  # sport_formts_enar_p17_jobs
    # ---
    # len:"sport_formts_en_ar_is_p17":  572927 قبل بدء الوظيفة
    # ---
    # sports.py: len:"sport_formts_en_ar_is_p17":  175  , len:"sport_formts_enar_p17_team":  1434  , len:"sport_formts_enar_p17_jobs":  27
    # ---
    # labs = sport_formts_female_nat.get(con_3 , "")
    con_3_label = ""
    # ---
    faevv = re.match(fanco_line, con_3, flags=re.IGNORECASE)
    # ---
    if faevv:
        sport_key = faevv.group(1)
        ylab = ""
        mlab = ""
        # ---
        team_xoxo = con_3.replace(sport_key, "xoxo")
        team_xoxo = re.sub(sport_key, "xoxo", team_xoxo, flags=re.IGNORECASE)
        # ---
        print_put(f'Get_Sport Format_xo_en_ar_is P17: con_3:"{con_3}", sport_key:"{sport_key}", team_xoxo:"{team_xoxo}"')
        # ---
        if team_xoxo in sport_formts_enar_p17_jobs:
            ylab = Sports_Keys_For_Jobs[sport_key]
            mlab = sport_formts_enar_p17_jobs.get(team_xoxo, "")
        # ---
        # if team_xoxo == "music":
        # ylab = Sports_Keys_For_Jobs[sport_key]
        # mlab = "موسيقى"
        # ---
        elif team_xoxo in sport_formts_enar_p17_team:
            ylab = Sports_Keys_For_Team[sport_key]
            mlab = sport_formts_enar_p17_team.get(team_xoxo, "")
        # ---
        else:
            print_put(f'Get_Sport_Format_xo_en_ar_is P17 team_xoxo:"{team_xoxo}" not in sport_formts_enar_p17_jobs or sport_formts_enar_p17_team')
        # ---
        # if team_xoxo in sport_formts_enar_p17_jobs:
        # ylab = Sports_Keys_For_Jobs.get(sport_key , "")
        # ---
        # if not ylab:
        # print_put(' sport_key:"%s" not in Sports_Keys_For_Jobs ' % sport_key)
        # ---
        # mlab = sport_formts_enar_p17_jobs[team_xoxo]
        # ---
        if mlab and ylab:
            blab = mlab.replace("xoxo", ylab)
            if blab.find("xoxo") == -1:
                con_3_label = blab
                print_put(f'Get_Sport_Format_xo_en_ar_is P17 blab:"{con_3_label}"')
        else:
            print_put(f'Get_Sport_Format_xo_en_ar_is P17 team_xoxo:"{team_xoxo}" not in sport_formts_enar_p17_jobs')
            # ---
    if con_3_label:
        print_put(f'Get_Sport_Format_xo_en_ar_is P17 con_3:"{con_3}", con_3_label:"{con_3_label}"')
    # ---
    return con_3_label


def Get_New_team_xo(team):
    # ---
    # إيجاد تسميات نصوص رياضية مثل
    # world champion national football teams
    # New_team_xo_team["world champion national {} teams".format(team2)] =  f"أبطال بطولة العالم {team2_lab}"
    # ---
    # print_put('Get_New_team_xo team:"%s"' % team)
    # ---
    # قبل تطبيق New_team_xo_jobs
    # sports.py: len:"Teams_new":  695795
    # بعد تطبيق New_team_xo_jobs and New_team_xo_team
    # sports.py: len:"New_team_xo_jobs":  1462 , len:"New_team_xo_team":  21
    # ---
    team_lab = ""
    # ---
    fav = re.match(fanco_line, team, flags=re.IGNORECASE)
    # ---
    sport_key = ""
    # ---
    if fav:
        sport_key = fav.group(1)
    else:
        # print("")
        return ""
    # ---summer olympics
    team_xo = team
    # team_xo = team.replace("\b%s\b" % sport_key , "xoxo")
    team_xo = re.sub(f" {sport_key} ", " xoxo ", f" {team_xo.strip()} ", flags=re.IGNORECASE).strip()
    # ---
    # team_xo = re.sub(sport_key , 'xoxo' , team_xo, flags=re.IGNORECASE)
    # ---
    print_put(f'Get_Sport Get_New_team_xo P17: team:"{team}", sport_key:"{sport_key}", team_xo:"{team_xo}"')
    # ---
    sp_lab = ""
    ar_label = ""
    # TTTY = ""
    sp_lab_tab = {}
    # ---
    if team_xo in New_team_xo_team:
        # TTTY = "team"
        ar_label = New_team_xo_team.get(team_xo, "")
        # sp_lab = Sports_Keys_For_Team.get(sport_key , "")
        sp_lab_tab = Sports_Keys_For_Team
    # ---
    elif team_xo in New_team_xo_jobs:
        # TTTY = "jobs"
        ar_label = New_team_xo_jobs.get(team_xo, "")
        # sp_lab = Sports_Keys_For_Jobs.get(sport_key , "")
        sp_lab_tab = Sports_Keys_For_Jobs
    # ---
    elif team_xo in New_team_xo_labels:
        # TTTY = "labels"
        ar_label = New_team_xo_labels.get(team_xo, "")
        # sp_lab = Sports_Keys_For_Label.get(sport_key , "")
        sp_lab_tab = Sports_Keys_For_Label
    # ---
    if sp_lab_tab != {}:
        sp_lab = sp_lab_tab.get(sport_key, "")
        # ---
        if not sp_lab:
            output_test(f'Get_New_team_xo sp_lab == "" , for sport_key "{sport_key}" ')
        # ---
    else:
        output_test(f'Get_New_team_xo team_xo:"{team_xo}" not in (New_team_xo_jobs,New_team_xo_team,New_team_xo_labels)')
        if nat_test := re.match(nat_reg_line, f" {team_xo.strip()} ", flags=re.IGNORECASE):
            output_test(f'nat_test:"{str(nat_test)}"')
            nat_ky = nat_test.group(1)
            # ---
            natreg = re.sub(f" {nat_ky} ", " natar ", f" {team_xo.strip()} ", flags=re.IGNORECASE)
            natreg = natreg.strip()
            # ---
            if natreg != team_xo:
                output_test(f'natreg:"{natreg}"')
                # ---
                if natreg in New_team_xo_team:
                    # TTTY = "team"
                    ar_label = New_team_xo_team.get(natreg, "")
                    # ---
                    nat_lab = All_contry_with_nat_ar.get(nat_ky, {}).get("ar", "")
                    output_test(f'nat_lab:"{nat_lab}"')
                    # ---
                    sp_lab = Sports_Keys_For_Team.get(sport_key, "")
                    output_test(f'sp_lab:"{sp_lab}"')
                    # ---
                    if ar_label and nat_lab:
                        ar_label = ar_label.replace("natar", nat_lab)
    # ---
    if ar_label and sp_lab:
        bbb = ar_label.replace("xoxo", sp_lab)
        if bbb.find("xoxo") == -1:
            team_lab = bbb
            output_test(f'Get_New_team_xo bbb:"{team_lab}"')
    # ---
    if team_lab:
        print_put(f'Get_New_team_xo: team_lab:"{team_lab}"')
    # ---
    return team_lab
