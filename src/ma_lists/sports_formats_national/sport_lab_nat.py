#!/usr/bin/python3
"""


"""

import re
# ---
from .te2 import New_For_nat_female_xo_team
from ..sports.Sport_key import Sports_Keys_For_Jobs, fanco_line
from ...helps.print_bot import print_put


def Get_sport_formts_female_nat(con_77: str) -> str:  # New_For_nat_female_xo_team
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
        sport_arabic_label = ""
        template_label = ""
        # ---
        normalized_team_key = con_77.replace(sport_key, "xzxz")
        normalized_team_key = re.sub(sport_key, "xzxz", normalized_team_key, flags=re.IGNORECASE)
        print_put(
            f'Get_Sport_Formats_For_nat female con_77:"{con_77}", sport_key:"{sport_key}", team_xz:"{normalized_team_key}"'
        )
        # ---
        if normalized_team_key in New_For_nat_female_xo_team:
            sport_arabic_label = Sports_Keys_For_Jobs.get(sport_key, "")
            # ---
            if not sport_arabic_label:
                print_put(f' sport_key:"{sport_key}" not in Sports_Keys_For_Jobs ')
            # ---
            template_label = New_For_nat_female_xo_team[normalized_team_key]
            # ---
            if template_label and sport_arabic_label:
                resolved_label = template_label.replace("xzxz", sport_arabic_label)
                if resolved_label.find("xzxz") == -1:
                    label = resolved_label
                    print_put(f'Get_Sport_Formats_For_nat female bbvb:"{label}"')
        else:
            print_put(
                f'Get_Sport_Formats_For_nat female team_xz:"{normalized_team_key}" not in New_For_nat_female_xo_team'
            )
            # ---
    if label:
        print_put(f'Get_Sport_Formats_For_nat female con_77:"{con_77}", label:"{label}"')
    # ---
    return label
