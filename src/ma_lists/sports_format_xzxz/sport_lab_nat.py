#!/usr/bin/python3
"""


"""

import re
# ---
from .te2 import New_For_nat_female_xo_team
from ..Sport_key import Sports_Keys_For_Jobs, fanco_line
from ...helps.print_bot import print_put


def Get_sport_formts_female_nat(con_77):  # New_For_nat_female_xo_team
    # ---
    # قبل تطبيق الوظيفة
    # sports.py: len:"sport_formts_female_nat":  549000
    # ---
    # بعد تطبيق الوظيفة
    # sports.py: len:"New_For_nat_female_xo_team":  1528  , len:"sport_formts_female_nat":  0
    # ---
    label = ""
    faev = re.match(fanco_line, con_77, flags=re.IGNORECASE)
    # ---
    if faev:
        sport_key = faev.group(1)
        sp_lab = ""
        ar_label = ""
        # ---
        team_xz = con_77.replace(sport_key, "xzxz")
        team_xz = re.sub(sport_key, "xzxz", team_xz, flags=re.IGNORECASE)
        print_put(f'Get_Sport_Formats_For_nat female con_77:"{con_77}", sport_key:"{sport_key}", team_xz:"{team_xz}"')
        # ---
        if team_xz in New_For_nat_female_xo_team:
            sp_lab = Sports_Keys_For_Jobs.get(sport_key, "")
            # ---
            if not sp_lab:
                print_put(f' sport_key:"{sport_key}" not in Sports_Keys_For_Jobs ')
            # ---
            ar_label = New_For_nat_female_xo_team[team_xz]
            # ---
            if ar_label and sp_lab:
                bbvb = ar_label.replace("xzxz", sp_lab)
                if bbvb.find("xzxz") == -1:
                    label = bbvb
                    print_put(f'Get_Sport_Formats_For_nat female bbvb:"{label}"')
        else:
            print_put(f'Get_Sport_Formats_For_nat female team_xz:"{team_xz}" not in New_For_nat_female_xo_team')
            # ---
    if label:
        print_put(f'Get_Sport_Formats_For_nat female con_77:"{con_77}", label:"{label}"')
    # ---
    return label
