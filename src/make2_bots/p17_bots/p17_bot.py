"""

"""
import re
from ..jobs_bots.get_helps import get_con_3
from ..matables_bots.bot import All_P17, Add_to_main2_tab
from ..format_bots import Tit_ose_Nmaes, pop_format

from ...ma_lists import sport_formts_en_ar_is_p17
from ...ma_lists import en_is_P17_ar_is_mens, en_is_P17_ar_is_P17, en_is_P17_ar_is_al_women
from ...ma_lists import All_contry_with_nat_keys_is_en, contries_from_nat
from ... import malists_sport_lab as sport_lab  # sport_lab.Get_Sport_Format_xo_en_ar_is_P17(en) # sport_lab.Get_sport_formts_female_nat(en) # sport_lab.Get_New_team_xo(team, fafa_2 = False)


def print_put(s):
    # ---
    # printe.output(s)
    # ---
    return


def add_all(lab):
    lab_no_al = re.sub(r" ", " ال", lab)
    new_lab = f"ال{lab_no_al}"
    return new_lab


def Get_P17_2(cate):  # الإنجليزي اسم البلد والعربي جنسية رجال
    print_put(f'<<lightblue>>>>>> Get_P17_2 "{cate}" ')  # "united states government officials"

    # Category:United States government officials
    cnt_la = ""
    for nana, gak in en_is_P17_ar_is_mens.items():
        nana2 = f" {nana.strip().lower()}"
        if cate.lower().endswith(nana2):
            gagaga = cate[: -len(nana2)].strip()

            mens = All_contry_with_nat_keys_is_en.get(gagaga, {}).get("mens", "")
            if mens:
                # FOF = "<<lightgreen>>en_is_P17_ar_is_mens<<lightblue>> "
                print_put(f'<<lightblue>>>>>> mens: "{mens}" ')
                cnt_la = gak.format(mens)
                print_put(f'<<lightblue>>>>>> en_is_P17_ar_is_mens: new cnt_la  "{cnt_la}" ')
    # ---
    if not cnt_la:
        for nana, gak in en_is_P17_ar_is_al_women.items():
            nana2 = f" {nana.strip().lower()}"
            if cate.lower().endswith(nana2):
                gagaga = cate[: -len(nana2)].strip()

                women = All_contry_with_nat_keys_is_en.get(gagaga, {}).get("women", "")
                if women:
                    # FOF = "<<lightgreen>>en_is_P17_ar_is_al_women<<lightblue>> "
                    women = add_all(women)
                    print_put(f'<<lightblue>>>>>> women: "{women}" ')
                    cnt_la = gak.format(women)
                    print_put(f'<<lightblue>>>>>> en_is_P17_ar_is_al_women: new cnt_la  "{cnt_la}" ')

    return cnt_la


def Get_P17(cate):  # الإنجليزي جنسية والعربي اسم البلد
    cnt_la = ""
    con_3_lab = ""
    con_3 = ""
    contry_start = ""
    cate = cate.lower()
    contry_start_lab = ""
    con_3, contry_start = get_con_3(cate, All_P17, "All_P17")
    contry_start_lab = All_P17.get(contry_start, "")

    if con_3 == "" and contry_start == "":
        con_3, contry_start = get_con_3(cate, contries_from_nat, "contries_from_nat")
        contry_start_lab = contries_from_nat.get(contry_start, "")
    if con_3 and contry_start:
        print_put(f'<<lightpurple>>>>>> contry_start_lab:"{contry_start_lab}"')
        print_put(f'<<lightblue>> contry_start:"{contry_start}", con_3:"{con_3}"')

        FOF = ""
        if con_3 in Tit_ose_Nmaes:
            codd = Tit_ose_Nmaes[con_3]
            if codd.startswith("لل"):
                con_3_lab = "{} " + codd
                print_put(f'get lab from Tit_ose_Nmaes con_3_lab:"{con_3_lab}"')

        if not con_3_lab:
            con_3_lab = sport_formts_en_ar_is_p17.get(con_3.strip(), "")

        if not con_3_lab:
            con_3_lab = en_is_P17_ar_is_P17.get(con_3.strip(), "")

        if not con_3_lab:
            con_3_lab = sport_lab.Get_Sport_Format_xo_en_ar_is_P17(con_3.strip())

        if con_3_lab:
            FOF = "<<lightgreen>>sport_formts_en_ar_is_p17<<lightblue>>"
            Add_to_main2_tab(con_3, con_3_lab)

        if not con_3_lab:
            con_3_lab = pop_format.get(con_3, "")
            if con_3_lab:
                Add_to_main2_tab(con_3, con_3_lab)
                FOF = "<<lightgreen>>pop_format<<lightblue>>"

        if con_3_lab:
            print_put(f'<<lightblue>>>>>> {FOF} .startswith({contry_start}), con_3:"{con_3}"')
            if con_3_lab.find("{nat}") != -1:
                cnt_la = con_3_lab.format(nat=contry_start_lab)
            else:
                cnt_la = con_3_lab.format(contry_start_lab)
            Add_to_main2_tab(contry_start, contry_start_lab)

        if con_3_lab and cnt_la == "":
            cnt_la = con_3_lab.format(contry_start_lab)
            Add_to_main2_tab(contry_start, contry_start_lab)
        if con_3_lab:
            print_put(f'<<lightblue>>>>>> Get_P17: test_60: new cnt_la "{cnt_la}" ')
        print_put(f'<<lightred>>>>>> con_3_lab: "{con_3_lab}", cnt_la :"{cnt_la}" == ""')

    else:
        print_put(f'<<lightred>>>>>> con_3: "{con_3}" or contry_start :"{contry_start}" == ""')
    if cnt_la:
        print_put(f'<<lightblue>>>>>> Get_P17 cnt_la "{cnt_la}" ')

    return cnt_la
