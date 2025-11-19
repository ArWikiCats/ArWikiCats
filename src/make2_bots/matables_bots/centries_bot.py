#!/usr/bin/python3
"""
Usage:
from ...matables_bots.centries_bot import centries_years_dec
"""

from typing import Dict

centries_years_dec: Dict[str, str] = {}

elfffff = {
    1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    2: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    3: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
}
for elff, tabe in elfffff.items():
    millennium = elff

    st = "th"  # the 1st millennium bc
    millennium_lab = f"الألفية {millennium}"
    millennium_lab_bc = f"الألفية {millennium} ق م"

    first_later = ""
    if len(str(millennium)) == 1:
        first_later = str(millennium)
    elif len(str(millennium)) == 2:
        first_later = str(millennium)[1]

    if first_later == "2":
        st = "nd"
    elif first_later == "1":
        st = "st"

    millennium_t = f"{millennium}{st} millennium"
    millennium_t_bc = f"{millennium}{st} millennium bc"

    centries_years_dec[f"the {millennium_t}"] = millennium_lab
    centries_years_dec[millennium_t] = millennium_lab

    centries_years_dec[f"the {millennium}{st} millennium bc"] = millennium_lab_bc
    centries_years_dec[millennium_t_bc] = millennium_lab_bc

    for centry in tabe:
        centry2 = str(centry - 1)
        if centry2 == "0":
            centry2 = ""

        decades = [f"{centry2}{x}0" for x in range(0, 10)]

        th = "th"

        first_later = ""
        if len(str(centry)) == 1:
            first_later = str(centry)
        elif len(str(centry)) == 2:
            first_later = str(centry)[1]

        if first_later == "2":
            th = "nd"
        elif first_later == "1":
            th = "st"

        centry_t = f"{centry}{th} century"
        centry_lab = f"القرن {centry}"
        centries_years_dec[centry_t] = centry_lab
        centries_years_dec[f"{centry}{th}−century"] = centry_lab
        centries_years_dec[f"{centry}{th}–century"] = centry_lab
        centries_years_dec[f"{centry}{th}-century"] = centry_lab

        centry_lab_bc = f"القرن {centry} ق م"
        centry_t_bc = f"the {centry}{th} century bc"
        centries_years_dec[centry_t_bc] = centry_lab_bc
        centries_years_dec[f"{centry}{th} century bc"] = centry_lab_bc

        for dic in decades:
            dic_lab = f"عقد {dic}"

            centries_years_dec[f"{dic}s bc"] = f"عقد {dic} ق م"
            centries_years_dec[f"{dic}s"] = dic_lab
