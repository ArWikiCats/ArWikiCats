"""
from .bots import tmp_bot
if not sub_ar_label:
    sub_ar_label = tmp_bot.Work_Templates(category)
"""

from ..format_bots import pp_start_with, pp_ends_with, pp_ends_with_pase
from ...helps.print_bot import print_put

from ..date_bots import with_years_bot

from ..ma_bots import contry2_lab
from ..ma_bots import ye_ts_bot

Work_Templates_cash = {}


def Work_Templates(SUUS):
    """Generate work templates based on the provided input string.

    This function takes an input string, processes it to determine if it
    matches any predefined templates based on its suffix or prefix. It
    attempts to extract relevant information and format the output
    accordingly. The function checks both suffixes and prefixes against a
    set of predefined mappings and utilizes helper functions to retrieve
    additional data as needed.

    Args:
        SUUS (str): The input string for which the work template is to be generated.

    Returns:
        str: The formatted work template based on the input string, or an empty
            string
        if no matching template is found.
    """

    # ---
    cash_key = SUUS.lower().strip()
    # ---
    if cash_key in Work_Templates_cash:
        return Work_Templates_cash[cash_key]
    # ---
    print_put(f">> ----------------- start Work_ Templates ----------------- SUUS:{SUUS}")
    PpP_lab = ""
    # pp_ends_with =  in pop_format

    # pp_ends_with_pase
    # pp_ends_with
    # merege pp_ends_with_pase and pp_ends_with
    meregd = {**pp_ends_with_pase, **pp_ends_with}

    for pri_ooo, pri_lll in meregd.items():
        if not SUUS.lower().endswith(pri_ooo.lower()):
            continue
        U_8 = SUUS[:-len(pri_ooo)]
        print_put(f'>>>><<lightblue>> Work_ Templates.endswith pri_ooo("{pri_ooo}"), U_8:"{U_8}"')

        U_lab = contry2_lab.get_lab_for_contry2(U_8)
        if not U_lab:
            U_lab = with_years_bot.Try_With_Years(U_8)

        if U_lab == "":
            # print("translate_general_category 2")
            U_lab = ye_ts_bot.translate_general_category(U_8)

        print_put(f'>>>><<lightblue>> Work_ Templates :"{SUUS}", U_8 :"{U_8}"')
        # ---
        if U_lab:
            print_put(f'>>>><<lightblue>> Work_ Templates.endswith pri_ooo("{pri_ooo}"), U_lab:"{U_lab}"')
            PpP_lab = pri_lll.format(U_lab)
            print_put(f'>>>> PpP_lab:"{PpP_lab}"')
            # ---
            break

    # pp_ends_with
    if PpP_lab:
        return PpP_lab

    # pp_start_with
    for pri_ss, pri_lll in pp_start_with.items():
        if not SUUS.startswith(pri_ss):
            continue
        U_c = SUUS[len(pri_ss):]

        U_lab = contry2_lab.get_lab_for_contry2(U_c)

        if not U_lab:
            U_lab = with_years_bot.Try_With_Years(U_c)

        if U_lab == "":
            # print("translate_general_category 3")
            U_lab = ye_ts_bot.translate_general_category(U_c)

        print_put(f'>>>><<lightblue>> Work_ Templates :"{SUUS}", U_c :"{U_c}"')
        if U_lab:
            print_put(f'>>>><<lightblue>> Work_ Templates.startswith pri_ss("{pri_ss}"), U_lab:"{U_lab}"')
            PpP_lab = pri_lll.format(U_lab)
            print_put(f'>>>> PpP_lab:"{PpP_lab}"')
            # ---
            break

    print_put(">> ----------------- end Work_ Templates ----------------- ")
    # ---
    return PpP_lab
