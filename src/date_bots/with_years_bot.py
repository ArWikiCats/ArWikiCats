"""
from  ..date_bots.with_years_bot import Try_With_Years
"""

import functools
import re

# ---
from ..ma_lists_bots import change_numb_to_word
from ..ma_lists_bots import Word_After_Years
from ..format_bots import ar_lab_before_year_to_add_in
from ..matables_bots.bot import Add_in_table
from ..matables_bots.table1_bot import get_KAKO

from ..ma_bots import contry2_lab
from ..ma_bots.ye_ts_bot import translate_general_category

Try_With_Years_cash = {}


def print_put(s):
    # ---
    # printe.output(s)
    # ---
    return


@functools.lru_cache(maxsize=None)
def Try_With_Years(contry):
    """Retrieve a formatted label for a given country based on its historical
    context.

    This function processes the input country string to extract relevant
    year information and formats it according to predefined rules. It checks
    for specific patterns in the input string, such as congressional terms
    or year ranges, and returns a corresponding label. If the input does not
    match any known patterns, an empty string is returned. The function also
    caches results for efficiency.

    Args:
        contry (str): The name of the country or a related term that may include year
            information.

    Returns:
        str: A formatted label that includes the country name and associated year
            information,
        or an empty string if no valid information is found.
    """

    # ---
    print_put(f">>> Try With Years contry ({contry})")
    # pop_final_Without_Years

    lab2 = ""
    con_3_lab = ""

    contry = contry.strip()
    contry = contry.replace("−", "-")

    # كونغرس
    # cs = re.match(r"^(\d+)(th|nd|st|rd) united states congress", contry)
    kak = {
        # "term of the Iranian Majlis" : "المجلس الإيراني",
        "iranian majlis": "المجلس الإيراني",
        "united states congress": "الكونغرس الأمريكي",
    }
    if cs := re.match(r"^(\d+)(th|nd|st|rd) (%s)$" % "|".join(kak.keys()), contry):
        ye = cs.group(1)
        hh = cs.group(3)
        # ---
        hh_Lab = kak[hh]
        num_lab = change_numb_to_word.get(ye, f"الـ{ye}")
        # ---
        lab2 = f"{hh_Lab} {num_lab}"
        print_put(f">>> 1591 lab2 ({lab2}),contry: ({contry})")
        # ---
        return lab2

    RE1 = re.match(r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d).*", contry)
    RE2 = re.match(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)$", contry)

    # Category:American Soccer League (1933–83)
    RE3 = re.match(r"^.*?\s*(\((?:\d\d\d\d|\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+)\))$", contry)
    # RE4 = re.match(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d) season$", contry)

    if not RE1 and not RE2 and not RE3:  # and not RE4
        # ---
        return ""

    # year = re.sub(r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)\s*.*$", r"\g<1>", contry)
    year = re.sub(r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)\s.*$", r"\g<1>", contry)
    if year == contry:
        year = ""

    if year:
        con_3 = contry[len(year):]
        con_3 = con_3.strip()
        print_put(f">>> Try With Years contry.startswith(year:{year}) con_3:{con_3}")

        if con_3 in Word_After_Years:
            con_3_lab = Word_After_Years[con_3]

        if not con_3_lab:
            con_3_lab = get_KAKO(con_3.strip().lower())
            print_put(f">>> Try With Years get_KAKO con_3_lab:{con_3_lab}")

        if con_3_lab == "":
            # print("translate_general_category 4")
            con_3_lab = translate_general_category(con_3)

        if not con_3_lab:
            con_3_lab = contry2_lab.get_lab_for_contry2(con_3)

        sus = " "

        if con_3_lab.strip() in ar_lab_before_year_to_add_in:
            print_put("ar_lab_before_year_to_add_in Add في to arlabel sus.")
            sus = " في "

        elif con_3 in Add_in_table:
            print_put("a<<lightblue>>>>>> Add في to suf")
            sus = " في "

        if con_3_lab:
            lab2 = con_3_lab + sus + year
            print_put(f'>>>>>> Try With Years new lab2  "{lab2}" ')

    if not lab2:
        year2 = re.sub(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)$", r"\g<1>", contry.strip())

        if RE3:
            year2 = re.sub(r"^.*?\s*(\((?:\d\d\d\d|\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+)\))$", r"\g<1>", contry.strip())
            year2 = re.sub(r"^.*?\s*(\((?:\d\d\d\d|\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+)\))$", r"\g<1>", contry.strip())

        # if RE4:
        # year2 = "موسم " + re.sub(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d) season$", r"\g<1>", contry.strip() )

        if year2 == contry:
            year2 = ""

        if year2:
            year2_lab = year2
            print_put(f">>> Try With Years contry.startswith(year2:{year2})")
            con_4 = contry[:-len(year2)]

            # print("translate_general_category 5")
            con_4_lab = translate_general_category(con_4)

            if con_4_lab == "":
                con_4_lab = contry2_lab.get_lab_for_contry2(con_4)

            if year2_lab.find("–present") != -1:
                year2_lab = year2_lab.replace("–present", "–الآن")

            if con_4_lab:
                lab2 = f"{con_4_lab} {year2_lab}"
                print_put(f'>>>>>> Try With Years new lab4  "{lab2}" ')

    if lab2:
        print_put(f'>>>>>> Try With Years lab2 "{lab2}" ')

    return lab2
