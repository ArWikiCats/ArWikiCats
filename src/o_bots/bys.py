"""
from  make.bots import bys
"""

import re

# ---
from ..ma_lists import By_table, By_orginal2, By_table_orginal
from ..ma_lists import New_P17_Finall
from ..matables_bots.bot_2018 import pop_All_2018
from ..p17_bots.nats import find_nat_others
from ..media_bots.films_bot import test_films


def print_put(s):
    # ---
    # printe.output(s)
    # ---
    return


def Make_By_lab(cate):
    print_put(f"<<lightred>>>> vvvvvvvvvvvv Make_By_lab start, cate:{cate} vvvvvvvvvvvv ")
    cnt_la = ""

    if cate.startswith("by "):
        con_lab2 = test_films(cate.replace("by ", ""))
        if con_lab2:
            cnt_la = f"بواسطة {con_lab2}"
        else:
            con_lab2 = find_nat_others(cate.replace("by ", ""))
            if con_lab2:
                cnt_la = f"بواسطة {con_lab2}"

    Match = re.match(r"^by (.*?) and (.*?)$", cate.lower())
    if not cnt_la and Match:
        by1 = Match.group(1)
        by2 = Match.group(2)

        by1_lab = By_orginal2.get(by1, "")
        by2_lab = By_orginal2.get(by2, "")

        print_put(f"<<lightred>>>> by:{by1},lab:{by1_lab}.")
        print_put(f"<<lightred>>>> by:{by2},lab:{by2_lab}.")

        if by2_lab and by1_lab:
            cnt_la = f"حسب {by1_lab} و{by2_lab}"

    if cnt_la:
        print_put(f"<<lightblue>>>> ^^^^^^^^^ Make_By_lab lab:{cnt_la}.")

    print_put("<<lightblue>>>> ^^^^^^^^^ Make_By_lab end ^^^^^^^^^ ")
    return cnt_la


def Get_by_label(cat):
    lab = ""
    by = ""
    frist = ""

    print_put(f"<<lightyellow>>>>Get_by_label {cat}")

    frist_lab = ""
    by_lab = ""

    if mama := re.match(r"^(.*?) (by .*)$", cat, flags=re.IGNORECASE):
        frist = mama.group(1)
        by = mama.group(2)

        print_put(f"<<lightyellow>>>>frist:{frist},by:{by}")

    if frist.startswith("the "):
        frist = frist[len("the ") :]

    if frist:
        if not frist_lab:
            frist_lab = New_P17_Finall.get(frist.lower(), "")

        if not frist_lab:
            frist_lab = pop_All_2018.get(frist.lower(), "")

    if by:
        if not by_lab:
            by_lab = By_table.get(by.lower(), "")

        if not by_lab:
            by_lab = By_table_orginal.get(by.lower(), "")

    if frist_lab and by_lab:
        lab = f"{frist_lab} {by_lab}"
        print_put(f"<<lightyellow>>>>Get_by_label lab {lab}")

    return lab


def Get_and_label(cat):
    lab = ""
    frist = ""
    last = ""

    print_put(f"<<lightyellow>>>>Get_and_label {cat}")

    frist_lab = ""
    last_lab = ""

    if mama := re.match(r"(.*?) and (.*)", cat, flags=re.IGNORECASE):
        frist = mama.group(1)
        last = mama.group(2)

        print_put(f"<<lightyellow>>>>frist:{frist},last:{last}")

    if frist:
        if not frist_lab:
            frist_lab = New_P17_Finall.get(frist.lower(), "")

        if not frist_lab:
            frist_lab = pop_All_2018.get(frist.lower(), "")

    if last:
        if not last_lab:
            last_lab = New_P17_Finall.get(last.lower(), "")

        if not last_lab:
            last_lab = pop_All_2018.get(last.lower(), "")

    if frist_lab and last_lab:
        lab = f"{frist_lab} و{last_lab}"
        print_put(f"<<lightyellow>>>>Get_and_label lab {lab}")

    return lab
