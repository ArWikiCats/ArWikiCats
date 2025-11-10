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
def Get_Sport_Format_xo_en_ar_is_P17(con_3: str) -> str:  # sport_formts_enar_p17_jobs
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
        sport_label = ""
        template_label = ""
        # ---
        normalized_team_key = con_3.replace(sport_key, "xoxo")
        normalized_team_key = re.sub(sport_key, "xoxo", normalized_team_key, flags=re.IGNORECASE)
        # ---
        print_put(
            f'Get_Sport Format_xo_en_ar_is P17: con_3:"{con_3}", sport_key:"{sport_key}", team_xoxo:"{normalized_team_key}"'
        )
        # ---
        if normalized_team_key in sport_formts_enar_p17_jobs:
            sport_label = Sports_Keys_For_Jobs[sport_key]
            template_label = sport_formts_enar_p17_jobs.get(normalized_team_key, "")
        # ---
        # if team_xoxo == "music":
        # sport_label = Sports_Keys_For_Jobs[sport_key]
        # template_label = "موسيقى"
        # ---
        elif normalized_team_key in sport_formts_enar_p17_team:
            sport_label = Sports_Keys_For_Team[sport_key]
            template_label = sport_formts_enar_p17_team.get(normalized_team_key, "")
        # ---
        else:
            print_put(
                f'Get_Sport_Format_xo_en_ar_is P17 team_xoxo:"{normalized_team_key}" not in sport_formts_enar_p17_jobs or sport_formts_enar_p17_team'
            )
        # ---
        # if normalized_team_key in sport_formts_enar_p17_jobs:
        # sport_label = Sports_Keys_For_Jobs.get(sport_key , "")
        # ---
        # if not sport_label:
        # print_put(' sport_key:"%s" not in Sports_Keys_For_Jobs ' % sport_key)
        # ---
        # template_label = sport_formts_enar_p17_jobs[normalized_team_key]
        # ---
        if template_label and sport_label:
            resolved_label = template_label.replace("xoxo", sport_label)
            if resolved_label.find("xoxo") == -1:
                con_3_label = resolved_label
                print_put(f'Get_Sport_Format_xo_en_ar_is P17 blab:"{con_3_label}"')
        else:
            print_put(
                f'Get_Sport_Format_xo_en_ar_is P17 team_xoxo:"{normalized_team_key}" not in sport_formts_enar_p17_jobs'
            )
            # ---
    if con_3_label:
        print_put(f'Get_Sport_Format_xo_en_ar_is P17 con_3:"{con_3}", con_3_label:"{con_3_label}"')
    # ---
    return con_3_label


def Get_New_team_xo(team: str) -> str:
    # ---
    # إيجاد تسميات نصوص رياضية مثل
    # world champion national football teams
    # New_team_xo_team["world champion national {} teams".format(team2)] =  f"أبطال بطولة العالم {team2_lab}"
    # ---
    # print_put('Get_New_team_xo team:"%s"' % team)
    # ---
    # قبل تطبيق New_team_xo_jobs
    # sports.py: len:"Teams new":  695795
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
    normalized_team = team
    # normalized_team = team.replace("\b%s\b" % sport_key , "xoxo")
    normalized_team = re.sub(f" {sport_key} ", " xoxo ", f" {normalized_team.strip()} ", flags=re.IGNORECASE).strip()
    # ---
    # team_xo = re.sub(sport_key , 'xoxo' , team_xo, flags=re.IGNORECASE)
    # ---
    print_put(f'Get_Sport Get_New_team_xo P17: team:"{team}", sport_key:"{sport_key}", team_xo:"{normalized_team}"')
    # ---
    sport_label = ""
    template_label = ""
    # TTTY = ""
    sport_label_source = {}
    # ---
    if normalized_team in New_team_xo_team:
        # TTTY = "team"
        template_label = New_team_xo_team.get(normalized_team, "")
        # sport_label = Sports_Keys_For_Team.get(sport_key , "")
        sport_label_source = Sports_Keys_For_Team
    # ---
    elif normalized_team in New_team_xo_jobs:
        # TTTY = "jobs"
        template_label = New_team_xo_jobs.get(normalized_team, "")
        # sport_label = Sports_Keys_For_Jobs.get(sport_key , "")
        sport_label_source = Sports_Keys_For_Jobs
    # ---
    elif normalized_team in New_team_xo_labels:
        # TTTY = "labels"
        template_label = New_team_xo_labels.get(normalized_team, "")
        # sport_label = Sports_Keys_For_Label.get(sport_key , "")
        sport_label_source = Sports_Keys_For_Label
    # ---
    if sport_label_source != {}:
        sport_label = sport_label_source.get(sport_key, "")
        # ---
        if not sport_label:
            output_test(f'Get_New_team_xo sp_lab == "" , for sport_key "{sport_key}" ')
        # ---
    else:
        output_test(
            f'Get_New_team_xo team_xo:"{normalized_team}" not in (New_team_xo_jobs,New_team_xo_team,New_team_xo_labels)'
        )
        if nationality_match := re.match(nat_reg_line, f" {normalized_team.strip()} ", flags=re.IGNORECASE):
            output_test(f'nat_test:"{str(nationality_match)}"')
            nationality_key = nationality_match.group(1)
            # ---
            normalized_nationality_key = re.sub(
                f" {nationality_key} ", " natar ", f" {normalized_team.strip()} ", flags=re.IGNORECASE
            )
            normalized_nationality_key = normalized_nationality_key.strip()
            # ---
            if normalized_nationality_key != normalized_team:
                output_test(f'natreg:"{normalized_nationality_key}"')
                # ---
                if normalized_nationality_key in New_team_xo_team:
                    # TTTY = "team"
                    template_label = New_team_xo_team.get(normalized_nationality_key, "")
                    # ---
                    nationality_label = All_contry_with_nat_ar.get(nationality_key, {}).get("ar", "")
                    output_test(f'nat_lab:"{nationality_label}"')
                    # ---
                    sport_label = Sports_Keys_For_Team.get(sport_key, "")
                    output_test(f'sp_lab:"{sport_label}"')
                    # ---
                    if template_label and nationality_label:
                        template_label = template_label.replace("natar", nationality_label)
    # ---
    if template_label and sport_label:
        final_label = template_label.replace("xoxo", sport_label)
        if final_label.find("xoxo") == -1:
            team_lab = final_label
            output_test(f'Get_New_team_xo bbb:"{team_lab}"')
    # ---
    if team_lab:
        print_put(f'Get_New_team_xo: team_lab:"{team_lab}"')
    # ---
    return team_lab
