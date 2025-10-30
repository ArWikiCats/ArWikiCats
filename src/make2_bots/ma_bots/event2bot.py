#!/usr/bin/python3
"""
Usage:
from ..ma_bots import event2bot
# category_lab = event2bot.event2(category_r)

"""


import re
import sys

from ... import printe
from ...fix import fixtitle
from ..bots import tmp_bot
from ..date_bots import with_years_bot
from .lab_seoo_bot import event_Lab_seoo
from ..o_bots import univer  # univer.test_Universities(cate)

from ..matables_bots.bot import safo, titttto
from ...helps.print_bot import print_put
from .contry_bot import Get_contry
from .dodo_bots.event2bot_dodo import make_lab_dodo

en_literes = "[abcdefghijklmnopqrstuvwxyz]"
event2_cash = {}

Find_stubs = {1: "-stubs" in sys.argv}


def event2_d2(cat3, category3_not_lower):
    """Determine the category label based on the input string.

    This function analyzes the input string `cat3` to determine a
    corresponding category label. It checks for specific keywords to decide
    how to process the input. If none of the keywords are found, it attempts
    to derive the category label using a helper function based on whether
    the input starts with a digit or not. The resulting category label is
    prefixed with "تصنيف:" if it is successfully determined.

    Args:
        cat3 (str): The input string representing a category.
        category3_not_lower (str): A string used for country determination.

    Returns:
        str: The determined category label, or an empty string if no category
        could be determined.
    """

    category_lab = ""

    if cat3.find(" in ") == -1 and cat3.find(" of ") == -1 and cat3.find(" from ") == -1:
        if cat3.find(" by ") == -1 and cat3.find(" at ") == -1:
            if re.sub(r"^\d", "", cat3) == cat3:
                category_lab = Get_contry(category3_not_lower)
            else:
                category_lab = with_years_bot.Try_With_Years(cat3)
                if category_lab:
                    category_lab = f"تصنيف:{category_lab}"

    return category_lab


def event2(category_r):
    """Process a category string and return a corresponding label.

    This function takes a category string as input, processes it to extract
    relevant information, and attempts to generate a label based on
    predefined patterns and rules. It utilizes regular expressions to
    identify various time periods, such as centuries and millennia, and
    checks against existing labels in a cache. If no label can be generated,
    it defaults to a fallback mechanism.

    Args:
        category_r (str): The category string to be processed.

    Returns:
        str: The generated label corresponding to the input category string, or an
            empty string if no label could be determined.
    """

    NoLab_list = {}
    cash_key = category_r.replace("category:", "").lower().strip()

    if not category_r:
        return ""

    if cash_key in event2_cash:
        return event2_cash[cash_key]

    print_put("<<lightblue>>>> vvvvvvvvvvvv event2 start vvvvvvvvvvvv ")
    print_put(f'<<lightyellow>>>>>> event2 :"{category_r}"')
    yy = (
        r"\d+th century BCE|\d+th millennium BCE|\d+th century BC|\d+th millennium BC|\d+th century|\d+th millennium"
        + r"|\d+st century BCE|\d+st millennium BCE|\d+st century BC|\d+st millennium BC|\d+st century|\d+st millennium"
        + r"|\d+rd century BCE|\d+rd millennium BCE|\d+rd century BC|\d+rd millennium BC|\d+rd century|\d+rd millennium"
        + r"|\d+nd century BCE|\d+nd millennium BCE|\d+nd century BC|\d+nd millennium BC|\d+nd century|\d+nd millennium"
        + r"|\d+ century BCE|\d+ millennium BCE|\d+ century BC|\d+ millennium BC"
        + r"|\d+ century|\d+ millennium|\d+s BCE|\d+ BCE|\d+s BC|\d+ BC"
    )
    en_dash = r"|\d+\–\d+"
    MINUS = r"|\d+\−\d+"
    keybord = r"|\d+\-\d+"
    yy += en_dash
    yy += MINUS
    yy += keybord
    yy += r"|\d+s"
    yy += r"|\d+"
    # yyx = r"(\w+\s*\d+|\d+(th|st|rd)|\d+s\s*|\d+|)(\s*BCE|\s*BC|)(\s*century|\s*millennium)"
    MONTHSTR2 = "(january |february |march |april |may |june |july |august |september |october |november |december |)"
    tita_year = r"Category\:" + MONTHSTR2 + "(" + yy + "|).*"
    tita_year = tita_year.lower()
    tita_other = r"\s*(" + safo + r"|)\s*(" + titttto + r"|)\s*(.*|).*"
    tita = r"Category\:" + MONTHSTR2 + "(" + yy.lower() + "|)" + tita_other
    tita = tita.lower()
    # tit = {}

    ar_label = ""
    ar_label = univer.test_Universities(category_r)
    # ---
    if not ar_label:
        category = category_r
        category = category.replace("−century", " century")
        category = category.replace("–century", " century")
        if not category.lower().startswith("category:"):
            category = f"Category:{category}"

        Tita_year = tita_year
        ddd = r"category\:(january|february|march|april|may|june|july|august|september|october|november|december|)\s*"
        test_month = re.sub(ddd, "", category.lower())

        if test_month == category:
            Tita_year = r"category\:(|)\s*(" + yy + ").*"
        Tita_year = Tita_year.lower()

        _category_ = category
        _category_ = re.sub(r"-century", " century", _category_)
        _category_ = re.sub(r"-millennium", " millennium", _category_)

        category3_not_lower = re.sub(r"category:", "", _category_, flags=re.IGNORECASE)

        _category_ = _category_.lower()
        category3 = re.sub(r"category:", "", _category_, flags=re.IGNORECASE)
        cat_test = category3

        print_put(f'<<lightred>>>>>> category33:"{category3}" ')

        category_lab = event2_d2(category3, category3_not_lower)

        if category_lab:
            if re.sub(en_literes, "", category_lab, flags=re.IGNORECASE) == category_lab:
                category_lab = fixtitle.fixlab(category_lab, en=category_r)
                print_put(f'>>>> <<lightyellow>> cat:"{_category_}", category_lab "{category_lab}"')
                print_put("<<lightblue>>>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
                event2_cash[cash_key] = category_lab
                return category_lab
        # ---
        ar_label = make_lab_dodo(_category_, Tita_year, tita, tita_other, category3, category, cat_test, category_r)
    # ---
    if not ar_label:
        ar_label = dodo(category_r)
    # ---
    if not ar_label:
        NoLab_list[category_r] = ""

    print_put("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
    event2_cash[cash_key] = ar_label

    return ar_label


def dodo(category_r):
    """Generate an Arabic label for a given category.

    This function processes a category string to generate an Arabic label,
    particularly for categories that indicate they are stubs. It checks the
    input category for specific patterns and modifies it to ensure it is in
    the correct format. If the category ends with "stubs", the function
    attempts to find a corresponding label using helper functions. If no
    label is found, it falls back to a default template.

    Args:
        category_r (str): The input category string to be processed.

    Returns:
        str: The generated Arabic label for the category, or an empty string if no
            label is generated.
    """

    ar_label = ""
    sub_ar_label = ""
    list_of_cat = ""

    category = category_r
    category = category.replace("−century", " century")
    category = category.replace("–century", " century")
    if not category.lower().startswith("category:"):
        category = f"Category:{category}"

    if category.endswith(" stubs") and Find_stubs[1]:
        list_of_cat = "بذرة {}"
        category = category.replace(" stubs", "", 1)

        sub_ar_label = event_Lab_seoo("", category)

        if not sub_ar_label:
            sub_ar_label = tmp_bot.Work_Templates(category)

        if sub_ar_label and list_of_cat:
            ar_label = list_of_cat.format(sub_ar_label)
            printe.output(f'<<lightblue>> event2 add list_of_cat, ar_label:"{ar_label}", category:{category} ')

    return ar_label
