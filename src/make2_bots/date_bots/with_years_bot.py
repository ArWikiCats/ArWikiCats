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
    kak = {
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
    con_3_lab = ""

    contry = contry.strip()
    contry = contry.replace("−", "-")

    if lab2 := _handle_political_terms(contry):
        return lab2

    RE1 = RE1_compile.match(contry)
    RE2 = RE2_compile.match(contry)

    # Category:American Soccer League (1933–83)
    RE3 = RE33_compile.match(contry)
    # RE4 = RE4_compile.match(contry)

    lab2 = _handle_year_at_start(contry)
    if not lab2:
        lab2 = _handle_year_at_end(contry, RE2_compile, RE33_compile)

    if lab2:
        output_test(f'>>>>>> Try With Years lab2 "{lab2}" ')

    return lab2


def _handle_year_at_start(contry: str) -> str:
    """Handles cases where the year is at the start of the string."""
    year = re.sub(re_sub_year, r"\g<1>", contry)
    if year == contry:
        return ""

    con_3 = contry[len(year) :].strip()
    output_test(f">>> _handle_year_at_start: year:{year}, con_3:{con_3}")

    con_3_lab = ""
    if con_3 in Word_After_Years:
        con_3_lab = Word_After_Years[con_3]

    if not con_3_lab:
        con_3_lab = get_KAKO(con_3.lower())
        output_test(f">>> _handle_year_at_start get_KAKO con_3_lab:{con_3_lab}")

    if not con_3_lab:
        con_3_lab = translate_general_category(con_3)

    if not con_3_lab:
        con_3_lab = contry2_lab.get_lab_for_contry2(con_3)

    if con_3_lab:
        sus = " "
        if con_3_lab.strip() in ar_lab_before_year_to_add_in or con_3 in Add_in_table:
            sus = " في "
        return con_3_lab + sus + year

    return ""


def _handle_year_at_end(contry: str, RE2, RE3) -> str:
    """Handles cases where the year is at the end of the string."""
    year2 = RE2_compile.sub(r"\g<1>", contry.strip())

    if RE3:
        year2 = RE33_compile.sub(r"\g<1>", contry.strip())

    if year2 == contry:
        return ""

    year2_lab = year2
    output_test(f">>> _handle_year_at_end: year2:{year2}")
    con_4 = contry[: -len(year2)]

    con_4_lab = translate_general_category(con_4)

    if not con_4_lab:
        con_4_lab = contry2_lab.get_lab_for_contry2(con_4)

    if "–present" in year2_lab:
        year2_lab = year2_lab.replace("–present", "–الآن")

    if con_4_lab:
        return f"{con_4_lab} {year2_lab}"

    return ""
