#!/usr/bin/python3
"""
!
"""


import re
import functools

from ..helps import printe

from .. import app_settings
from ..fix import fixtitle
from ..helps.print_bot import print_put
from ..make2_bots import tmp_bot
from ..make2_bots.date_bots import with_years_bot
from ..make2_bots.o_bots import univer  # univer.te_universities(cate)
from ..make2_bots.ma_bots.country_bot import get_country
from ..make2_bots.ma_bots.year_or_typeo.bot_lab import label_for_startwith_year_or_typeo
from ..make2_bots.ma_bots.lab_seoo_bot import event_Lab_seoo

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


def event2_d2(category_r) -> str:
    """
    Determine the category label based on the input string.
    """
    # ---
    cat3 = category_r.lower()

    print_put(f'<<lightred>>>>>> category33:"{cat3}" ')

    # TODO: THIS NEED REVIEW
    # Reject strings that contain common English prepositions
    blocked = ("in", "of", "from", "by", "at")
    if any(f" {word} " in cat3.lower() for word in blocked):
        return ""

    category_lab = ""
    if re.sub(r"^\d", "", cat3) == cat3:
        category_lab = get_country(cat3)
    else:
        category_lab = with_years_bot.Try_With_Years(cat3)
        if category_lab:
            category_lab = f"تصنيف:{category_lab}"

    return category_lab


def dodo(category_r: str) -> str:
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

    category = category_r.lower()

    if category.endswith(" stubs") and app_settings.find_stubs:
        list_of_cat = "بذرة {}"
        category = category[: -len(" stubs")]

        sub_ar_label = event_Lab_seoo("", category)

        if not sub_ar_label:
            sub_ar_label = tmp_bot.Work_Templates(category)

        if sub_ar_label and list_of_cat:
            ar_label = list_of_cat.format(sub_ar_label)
            printe.output(f'<<lightblue>> event2 add list_of_cat, ar_label:"{ar_label}", category:{category} ')

    return ar_label


@functools.lru_cache(maxsize=None)
def event2(category_r: str) -> str:
    """Process a category string and return a corresponding label.

    This function takes a category string as input, processes it to extract
    relevant information, and attempts to generate a label based on
    predefined patterns and rules. It utilizes regular expressions to
    identify various time periods, such as centuries and millennia, and
    uses @functools.lru_cache for performance optimization. If no label can be generated,
    it defaults to a fallback mechanism.

    Args:
        category_r (str): The category string to be processed.

    Returns:
        str: The generated label corresponding to the input category string, or an
            empty string if no label could be determined.
    """

    if not category_r:
        return ""

    print_put("<<lightblue>>>> vvvvvvvvvvvv event2 start vvvvvvvvvvvv ")
    print_put(f'<<lightyellow>>>>>> event2 :"{category_r}"')
    # ---
    category_r = re.sub(r"category:", "", category_r, flags=re.IGNORECASE)
    # ---
    ar_label = univer.te_universities(category_r)
    # ---
    if ar_label:
        return ar_label
    # ---
    category_lab = event2_d2(category_r)

    if category_lab:
        if re.sub(en_literes, "", category_lab, flags=re.IGNORECASE) == category_lab:
            category_lab = fixtitle.fixlab(category_lab, en=category_r)
            print_put(f'>>>> <<lightyellow>> cat:"{category_r}", category_lab "{category_lab}"')
            print_put("<<lightblue>>>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
            return category_lab

    ar_label = label_for_startwith_year_or_typeo(category_r)

    if not ar_label:
        ar_label = dodo(category_r)

    print_put("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")

    return ar_label
