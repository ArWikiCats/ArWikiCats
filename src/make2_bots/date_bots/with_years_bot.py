"""
from  ..make2_bots.date_bots.with_years_bot import get_label_with_years
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

get_label_with_years_cash = {}


def _handle_political_terms(text: str) -> str:
    """Handles political terms like 'united states congress'."""
    # كونغرس
    # cs = re.match(r"^(\d+)(th|nd|st|rd) united states congress", text)
    political_terms = {
        # "term of the Iranian Majlis" : "المجلس الإيراني",
        "iranian majlis": "المجلس الإيراني",
        "united states congress": "الكونغرس الأمريكي",
    }
    if cs := re.match(r"^(\d+)(th|nd|st|rd) (%s)$" % "|".join(political_terms.keys()), text):
        year = cs.group(1)
        term_string = cs.group(3)
        term_label = political_terms[term_string]
        number_label = change_numb_to_word.get(year, f"الـ{year}")
        label = f"{term_label} {number_label}"
        output_test(f">>> _handle_political_terms label ({label}), text: ({text})")
        return label
    return ""


def _handle_year_at_start(text: str) -> str:
    """Handles cases where the year is at the start of the string."""
    label = ""
    year = re.sub(re_sub_year, r"\g<1>", text)
    if year == text or not year:
        return ""

    substring_after_year = text[len(year):].strip()
    output_test(f">>> _handle_year_at_start: year:{year}, substring_after_year:{substring_after_year}")

    substring_label = ""
    if substring_after_year in Word_After_Years:
        substring_label = Word_After_Years[substring_after_year]

    if not substring_label:
        substring_label = get_KAKO(substring_after_year.strip().lower())
        output_test(f">>> _handle_year_at_start get_KAKO substring_label:{substring_label}")

    if not substring_label:
        substring_label = translate_general_category(substring_after_year)

    if not substring_label:
        substring_label = contry2_lab.get_lab_for_contry2(substring_after_year)

    if not substring_label:
        return ""

    separator = " "

    if substring_label.strip() in ar_lab_before_year_to_add_in:
        output_test("ar_lab_before_year_to_add_in Add في to arlabel separator.")
        separator = " في "

    elif substring_after_year in Add_in_table:
        output_test("a<<lightblue>>>>>> Add في to suf")
        separator = " في "

    label = substring_label + separator + year
    output_test(f'>>>>>> get_label_with_years new label  "{label}" ')

    return label


def _handle_year_at_end(text, RE2_compile, RE33_compile) -> str:
    """Handles cases where the year is at the end of the string."""
    year = RE2_compile.sub(r"\g<1>", text.strip())

    year_at_end_match = RE33_compile.match(text)

    if year_at_end_match:
        year = RE33_compile.sub(r"\g<1>", text.strip())
        year = RE33_compile.sub(r"\g<1>", text.strip())

    # if RE4:
    # year = "موسم " + RE4_compile.sub(r"\g<1>", text.strip())

    if year == text or not year:
        return ""

    year_label = year
    output_test(f">>> _handle_year_at_end: year:{year}")
    substring_before_year = text[: -len(year)]

    # print("translate_general_category 5")
    substring_label = translate_general_category(substring_before_year)

    if not substring_label:
        substring_label = contry2_lab.get_lab_for_contry2(substring_before_year)

    if "–present" in year_label:
        year_label = year_label.replace("–present", "–الآن")

    if substring_label:
        label = f"{substring_label} {year_label}"
        output_test(f'>>>>>> get_label_with_years new lab4  "{label}" ')
    return label


@functools.lru_cache(maxsize=None)
def get_label_with_years(text):
    """Retrieve a formatted label for a given country based on its historical
    context.

    This function processes the input country string to extract relevant
    year information and formats it according to predefined rules. It checks
    for specific patterns in the input string, such as congressional terms
    or year ranges, and returns a corresponding label. If the input does not
    match any known patterns, an empty string is returned. The function also
    caches results for efficiency.

    Args:
        text (str): The name of the country or a related term that may include year
            information.

    Returns:
        str: A formatted label that includes the country name and associated year
            information,
        or an empty string if no valid information is found.
    """

    # ---
    output_test(f">>> get_label_with_years text ({text})")
    # pop_final_Without_Years

    label = ""
    text = text.strip()
    text = text.replace("−", "-")

    if label := _handle_political_terms(text):
        return label

    year_at_start = RE1_compile.match(text)
    year_at_end = RE2_compile.match(text)
    # Category:American Soccer League (1933–83)
    year_at_end2 = RE33_compile.match(text)
    # RE4 = RE4_compile.match(text)

    if not year_at_start and not year_at_end and not year_at_end2:  # and not RE4
        # ---
        return ""

    label = _handle_year_at_start(text)

    if not label:
        label = _handle_year_at_end(text, RE2_compile, RE33_compile)

    if label:
        output_test(f'>>>>>> get_label_with_years label "{label}" ')

    return label
