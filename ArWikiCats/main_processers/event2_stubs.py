#!/usr/bin/python3
"""

"""
from ..config import app_settings
from ..helps.log import logger
from ..make_bots import tmp_bot
from ..ma_bots.lab_seoo_bot import event_label_work


def stubs_label(category_r: str) -> str:
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

        sub_ar_label = event_label_work(category)

        if not sub_ar_label:
            sub_ar_label = tmp_bot.Work_Templates(category)

        if sub_ar_label and list_of_cat:
            ar_label = list_of_cat.format(sub_ar_label)
            logger.info(f"<<lightblue>> event2 add list_of_cat, {ar_label=}, {category=} ")

    return ar_label
