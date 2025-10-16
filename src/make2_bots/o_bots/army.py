"""
from ..o_bots.army import test_Army
"""

import re

from ...ma_lists import All_contry_with_nat, All_contry_with_nat_keys_is_en
from ...ma_lists import sport_formts_en_p17_ar_nat

from ...ma_lists import military_format_women_without_al_from_end, military_format_women_without_al, military_format_women, military_format_men

from ...helps.log import logger
test_Army_Cash = {}



def test_Army(cate):
    if cate in test_Army_Cash:
        if test_Army_Cash[cate]:
            logger.debug(f"<<lightblue>>>> ============== test_Army_Cash : {test_Army_Cash[cate]}")
        return test_Army_Cash[cate]

    cate = cate.lower()
    # test_cate = re.sub(r"(%s)" % army_line.lower(), "", cate)
    con_77 = ""
    cnt_la = ""
    women_lab = ""
    men_lab = ""

    logger.info(f"<<lightblue>>>> vvvvvvvvvvvv test_Army start, (cate:{cate}) vvvvvvvvvvvv ")

    for contry, contry_dict in All_contry_with_nat.items():
        if cnt_la:
            break
        # ---
        contry2 = contry_dict.get("en", "")
        women_labs = contry_dict.get("women", "")
        men_labs = contry_dict.get("men", "")

        if contry2:
            contry2 = f"{contry2.lower()} "

        contry2_end = f" {contry2.lower()}"

        contry4 = f"{contry.lower()} "

        contry_3 = contry2
        if contry_3.startswith("the "):
            contry_3 = contry_3[len("the ") :].strip()

        if cate.endswith(contry2_end):
            print("cate.endswith(contry2_end)")

        if women_labs == "" and men_labs == "":
            logger.debug('women_labs and men_labs == ""')
            continue

        if cate.startswith(contry2) or cate.startswith(contry_3) or cate.startswith(contry4):
            women_lab = women_labs
            men_lab = men_labs

            cota = ""
            if cate.startswith(contry2):
                con_77 = cate[len(contry2) :].strip()
                cota = contry2

            elif cate.startswith(contry_3):
                con_77 = cate[len(contry_3) :].strip()
                cota = contry_3

            elif cate.startswith(contry4):
                con_77 = cate[len(contry4) :].strip()
                cota = contry4

            logger.debug(f'<<lightblue>>>>>> get startswith All_contry_with_nat ({cota}), con_77:"{con_77}"')
            break

    # con_77 = cate[len(contry2):].strip()

    if not cnt_la:
        # 16-11-2020
        # Category:Unmanned_aerial_vehicles_of_Jordan > طائرات بدون طيار أردنية
        for nana, nanalab in military_format_women_without_al_from_end.items():
            nana2 = f"{nana} "
            if not cate.startswith(nana2):
                continue
            # ---
            gagaga = cate[len(nana2) :].strip()
            con_labe = All_contry_with_nat_keys_is_en.get(gagaga, {}).get("women", "")
            if con_labe:
                logger.debug(f'<<lightblue>>>>>> con_labe: "{con_labe}" ')
                cnt_la = nanalab.format(nat=con_labe)
                logger.debug(f'<<lightblue>>>>>> con_77_from_end: new cnt_la  "{cnt_la}" ')

    if not cnt_la:
        con_77_lab = military_format_women_without_al.get(con_77, "")
        if con_77_lab:
            # FOF = "<<lightgreen>>military_format_women_without_al<<lightblue>> "
            logger.debug('<<lightblue>>>>>> women_lab: "{women_lab}" ')

            cnt_la = con_77_lab.format(nat=women_lab)
            logger.debug(f'<<lightblue>>>>>> test_880: new cnt_la  "{cnt_la}" ')

    con_88 = con_77
    con_88_priff = ""  # بادئة
    con_88_lab = ""

    if not cnt_la:
        endswith_table = {
            " civilians": "مدنيو {}",
            " generals": "جنرالات {}",
            " accidents and incidents": "حوادث {}",
        }
        for xi, xi_lab in endswith_table.items():
            if not con_88.endswith(xi):
                continue
            if cnt_la:
                break
            con_88 = con_88.replace(xi, "", 1)
            con_88_priff = xi_lab
            con_88_lab = military_format_women.get(con_88, "")

            if con_88_lab:
                # FOF = "<<lightgreen>>military_format_women<<lightblue>> "
                logger.debug(f'<<lightblue>>>>>> women_lab: "{women_lab}" ')
                women_lab_no_al = re.sub(r" ", " ال", women_lab)
                women_lab = f"ال{women_lab_no_al}"
                cnt_la = con_88_lab.format(nat=women_lab)
                logger.debug(f'<<lightblue>>>>>> test_880: new cnt_la  "{cnt_la}" ')
                cnt_la = con_88_priff.format(cnt_la)
            # ---

    # military_format_men :
    # Category:French_labour_law
    if not cnt_la:  #
        con_77_lab = military_format_men.get(con_77, "")
        if con_77_lab and men_lab:
            # FOF = "<<lightgreen>>military_format_men<<lightblue>>"
            men_lab_no_al = re.sub(r" ", " ال", men_lab)
            men_lab = f"ال{men_lab_no_al}"
            cnt_la = con_77_lab.format(nat=men_lab)
            logger.debug(f'<<lightblue>>>>>> test_880: new cnt_la  "{cnt_la}" ')

    # sport_formts_en_p17_ar_nat :
    # Category:China Basketball Federation
    if not cnt_la:  #
        con_77_lab = sport_formts_en_p17_ar_nat.get(con_77, "")
        if con_77_lab and men_lab:
            # FOF = "<<lightgreen>>sport_formts_en_p17_ar_nat<<lightblue>>"
            men_lab_no_al = re.sub(r" ", " ال", men_lab)
            men_lab = f"ال{men_lab_no_al}"
            cnt_la = con_77_lab.format(nat=men_lab)
            logger.debug(f'<<lightblue>>>>>> test_880: new cnt_la  "{cnt_la}" ')

    if cnt_la:
        test_Army_Cash[cate] = cnt_la

    logger.info("<<lightblue>>>> ^^^^^^^^^ test_Army end ^^^^^^^^^ ")
    return cnt_la
