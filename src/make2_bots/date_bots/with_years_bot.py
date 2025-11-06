"""
from  ..make2_bots.date_bots.with_years_bot import Try_With_Years
"""

import functools
import re

# ---
from ...ma_lists import change_numb_to_word
from ...ma_lists import Word_After_Years
from ..format_bots import ar_lab_before_year_to_add_in
from ..matables_bots.bot import Add_in_table
from ..matables_bots.table1_bot import get_KAKO

from ..ma_bots import contry2_lab
from ..ma_bots.ye_ts_bot import translate_general_category
from ...helps.print_bot import output_test
from ..reg_lines import re_sub_year, RE1_compile, RE2_compile, RE33_compile

Try_With_Years_cash = {}


def _handle_political_terms(contry: str) -> str:
    """Handles political terms like 'united states congress'."""
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
        hh_Lab = kak[hh]
        num_lab = change_numb_to_word.get(ye, f"الـ{ye}")
        lab = f"{hh_Lab} {num_lab}"
        output_test(f">>> _handle_political_terms lab ({lab}), contry: ({contry})")
        return lab
    return ""


def _handle_year_at_start(contry: str) -> str:
    """Handles cases where the year is at the start of the string."""
    lab2 = ""
    year = re.sub(re_sub_year, r"\g<1>", contry)
    if year == contry:
        year = ""

    if not year:
        return ""

    con_3 = contry[len(year):]
    con_3 = con_3.strip()
    output_test(f">>> _handle_year_at_start: year:{year}, con_3:{con_3}")

    con_3_lab = ""
    if con_3 in Word_After_Years:
        con_3_lab = Word_After_Years[con_3]

    if not con_3_lab:
        con_3_lab = get_KAKO(con_3.strip().lower())
        output_test(f">>> Try With Years get_KAKO con_3_lab:{con_3_lab}")

    if con_3_lab == "":
        # print("translate_general_category 4")
        con_3_lab = translate_general_category(con_3)

    if not con_3_lab:
        con_3_lab = contry2_lab.get_lab_for_contry2(con_3)

    sus = " "

    if con_3_lab.strip() in ar_lab_before_year_to_add_in:
        output_test("ar_lab_before_year_to_add_in Add في to arlabel sus.")
        sus = " في "

    elif con_3 in Add_in_table:
        output_test("a<<lightblue>>>>>> Add في to suf")
        sus = " في "

    if con_3_lab:
        lab2 = con_3_lab + sus + year
        output_test(f'>>>>>> Try With Years new lab2  "{lab2}" ')

    return lab2


def _handle_year_at_end(contry, RE2_compile, RE33_compile) -> str:
    """Handles cases where the year is at the end of the string."""
    year2 = RE2_compile.sub(r"\g<1>", contry.strip())

    year_at_end2 = RE33_compile.match(contry)

    if year_at_end2:
        year2 = RE33_compile.sub(r"\g<1>", contry.strip())
        year2 = RE33_compile.sub(r"\g<1>", contry.strip())

    # if RE4:
    # year2 = "موسم " + RE4_compile.sub(r"\g<1>", contry.strip())

    if year2 == contry:
        year2 = ""

    if not year2:
        return ""

    year2_lab = year2
    output_test(f">>> _handle_year_at_end: year2:{year2}")
    con_4 = contry[:-len(year2)]

    # print("translate_general_category 5")
    con_4_lab = translate_general_category(con_4)

    if con_4_lab == "":
        con_4_lab = contry2_lab.get_lab_for_contry2(con_4)

    if year2_lab.find("–present") != -1:
        year2_lab = year2_lab.replace("–present", "–الآن")

    if con_4_lab:
        lab2 = f"{con_4_lab} {year2_lab}"
        output_test(f'>>>>>> Try With Years new lab4  "{lab2}" ')
    return lab2


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
    output_test(f">>> Try With Years contry ({contry})")
    # pop_final_Without_Years

    lab2 = ""
    contry = contry.strip()
    contry = contry.replace("−", "-")

    if lab2 := _handle_political_terms(contry):
        return lab2

    year_at_start = RE1_compile.match(contry)
    year_at_end = RE2_compile.match(contry)
    # Category:American Soccer League (1933–83)
    year_at_end2 = RE33_compile.match(contry)
    # RE4 = RE4_compile.match(contry)

    if not year_at_start and not year_at_end and not year_at_end2:  # and not RE4
        # ---
        return ""

    lab2 = _handle_year_at_start(contry)

    if not lab2:
        lab2 = _handle_year_at_end(contry, RE2_compile, RE33_compile)

    if lab2:
        output_test(f'>>>>>> Try With Years lab2 "{lab2}" ')

    return lab2
