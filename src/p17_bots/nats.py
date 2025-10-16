"""
from ..p17_bots import nats
"""

import re
from .. import printe
from ..ma_lists import sport_formts_for_p17, nat_p17_oioi
from ..ma_lists import fanco_line, Sports_Keys_For_Team
from ..matables_bots.bot import New_players, Add_to_main2_tab  # Add_to_main2_tab()
from .. import malists_sport_lab as sport_lab
from ..ma_lists import All_Nat, Nat_women
from ..jobs_bots.get_helps import get_con_3


nat_others_cash = {}


def print_put(s):
    # ---
    # printe.output(s)
    # ---
    return


def make_sport_formts_p17(co89):
    # ---
    # make_sport_formts_p17("football junior championships")
    # ---
    print_put(f'<<lightblue>>>>>> make_sport_formts_p17: co89:"{co89}"')
    # ---
    co89_lab = sport_formts_for_p17.get(co89, "")
    # ---
    if co89_lab:
        print_put(f"\tfind lab in sport_formts_for_p17: {co89_lab}")
        return co89_lab
    # ---
    # قبل تطبيق الوظيفة
    # len sport_formts_for_p17: 66435
    # ---
    # بعد تطبيق الوظيفة
    # len sport_formts_for_p17: 1
    # len nat_p17_oioi: 100
    # ---
    co89_lab = ""
    # ---
    faev = re.match(fanco_line, co89, flags=re.IGNORECASE)
    # ---
    if not faev:
        return ""
    # ---
    sport_key = faev.group(1)
    sport_key_lab = ""
    ar_label = ""
    # ---
    team_xz = co89.replace(sport_key, "oioioi")
    team_xz = re.sub(sport_key, "oioioi", team_xz, flags=re.IGNORECASE)
    print_put(f'make_sport_formts_p17 co89:"{co89}", sport_key:"{sport_key}", team_xz:"{team_xz}"')
    # ---
    if team_xz in nat_p17_oioi:
        sport_key_lab = Sports_Keys_For_Team.get(sport_key, "")
        # ---
        if not sport_key_lab:
            print_put(f' sport_key:"{sport_key}" not in Sports_Keys_For_Team ')
        # ---
        ar_label = nat_p17_oioi[team_xz]
        # ---
        if ar_label and sport_key_lab:
            bbvb = ar_label.replace("oioioi", sport_key_lab)
            if bbvb.find("oioioi") == -1:
                co89_lab = bbvb
                print_put(f'make_sport_formts_p17 bbvb:"{co89_lab}"')
    else:
        print_put(f'make_sport_formts_p17 team_xz:"{team_xz}" not in nat_p17_oioi')
    # ---
    if co89_lab:
        print_put(f'make_sport_formts_p17 co89:"{co89}", co89_lab:"{co89_lab}"')
    # ---
    return co89_lab


def find_nat_others(cate, fa=""):
    if cate in nat_others_cash:
        return nat_others_cash[cate]

    print_put(f"<<lightblue>>>> vvvvvvvvvvvv find_nat_others cate:{cate} vvvvvvvvvvvv ")

    cnt_la = ""

    cate = cate.lower()

    con_77, contry_start = get_con_3(cate, Nat_women, "nat")

    if con_77 and contry_start:
        # con_77_lab = sport_formts_female_nat.get(con_77, "")
        con_77_lab = sport_lab.Get_sport_formts_female_nat(con_77)
        if con_77_lab:
            cnt_la = con_77_lab.format(nat=Nat_women[contry_start])
            print_put(f'<<lightblue>>xxx sport_formts_female_nat: new cnt_la  "{cnt_la}"')

    if con_77 and contry_start and cnt_la == "":
        con_77_lab = make_sport_formts_p17(con_77)
        # ---
        P17_lab = All_Nat[contry_start].get("ar", "")
        # ---
        if con_77_lab and P17_lab:
            Add_to_main2_tab(con_77, con_77_lab)

            cnt_la = con_77_lab.format(nat=P17_lab)
            Add_to_main2_tab(cnt_la, P17_lab)
            print_put(f'<<lightblue>>>>>> sport_formts_for_p17: new cnt_la  "{cnt_la}"')
            New_players[cate] = cnt_la
    # ---
    print_put("<<lightblue>>>> ^^^^^^^^^ find_nat_others end ^^^^^^^^^ ")

    nat_others_cash[cate] = cnt_la

    return cnt_la


if __name__ == "__main__":
    print_put = printe.output
    print("_________________")
    # python3 core8/pwb.py make/bots/nats
    op = make_sport_formts_p17("football junior championships")
    print(op)

    zo = find_nat_others("yemeni football junior championships")
    print(zo)
