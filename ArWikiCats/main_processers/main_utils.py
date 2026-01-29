"""
Utility functions for category label formatting.
This module provides helper functions to wrap Arabic labels in common
list-style templates (e.g., "لاعبو {}") with special handling for sports.
"""

from typing import Tuple

from ..helps import getLogger

logger = getLogger(__name__)
# Constants
FOOTBALL_ARABIC = "كرة"
FOOTBALL_TEMPLATE = " كرة قدم {}"


def _format_category_with_list_template(
    category_r: str,
    category_lab: str,
    list_of_cat: str,
    foot_ballers: bool = False,
) -> str:
    """
    Format an Arabic category label using a list-style template and optionally ensure a football descriptor is included.

    If the label does not start with the template prefix (the text before `{}`), the template is applied. When `foot_ballers` is True and the formatted label does not contain the Arabic word for football, the function substitutes the template to include the football descriptor before formatting.

    Parameters:
        category_r (str): Original category string (used for logging/debugging).
        category_lab (str): Arabic label to format.
        list_of_cat (str): Template string containing a single `{}` placeholder.
        foot_ballers (bool): If True, ensure the football descriptor is included when missing.

    Returns:
        str: The resulting formatted Arabic category label.
    """
    category_lab_or = category_lab
    list_of_cat_x = list_of_cat.split("{}")[0].strip()

    logger.info(f"<<lightblue>> _format_category_with_list_template {category_lab=}, {list_of_cat=}, {list_of_cat_x=}")

    # Apply the template if the label doesn't already start with the prefix
    if not category_lab.startswith(list_of_cat_x) or list_of_cat_x == "":
        category_lab = list_of_cat.format(category_lab)

    logger.info(
        f"<<lightblue>> _format_category_with_list_template add {category_lab=}, {category_lab_or=}, {category_r=}"
    )

    # Football-specific handling: add "football" if not present
    if foot_ballers and FOOTBALL_ARABIC not in category_lab:
        list_of_cat = list_of_cat.replace("{}", FOOTBALL_TEMPLATE)
        category_lab = list_of_cat.format(category_lab_or)
        logger.info(
            f"<<lightblue>> _format_category_with_list_template football add {list_of_cat=}, {category_lab=}, {category_r=}"
        )

    return category_lab


def list_of_cat_func_new(category_r: str, category_lab: str, list_of_cat: str) -> str:
    """
    Format an Arabic category label using a list-style template without football-specific adjustments.

    Parameters:
        category_r (str): Original category identifier or raw category string (used for context/logging).
        category_lab (str): Arabic label to be formatted into the template.
        list_of_cat (str): Template string containing a single `{}` placeholder used to produce the list-style label.

    Returns:
        formatted_label (str): The resulting formatted Arabic category label.
    """
    return _format_category_with_list_template(category_r, category_lab, list_of_cat, foot_ballers=False)


def list_of_cat_func_foot_ballers(category_r: str, category_lab: str, list_of_cat: str) -> str:
    """
    Format an Arabic category label using a list-style template with football-specific adjustments.

    Parameters:
        category_r (str): Original category identifier or name (kept for context/logging).
        category_lab (str): Arabic category label to be formatted.
        list_of_cat (str): Template containing a single `{}` placeholder applied to `category_lab` (e.g., "لاعبو {}").

    Returns:
        str: The formatted category label; when appropriate and missing the football word, the template is adjusted to include the football descriptor.
    """
    return _format_category_with_list_template(category_r, category_lab, list_of_cat, foot_ballers=True)


def list_of_cat_func(category_r: str, category_lab: str, list_of_cat: str, foot_ballers: bool) -> Tuple[str, str]:
    """
    Format an Arabic category label using a list-style template, optionally applying football-specific adjustments.

    Parameters:
        category_lab (str): The Arabic label to format.
        list_of_cat (str): Template string containing a single `{}` placeholder used to produce the formatted label.
        foot_ballers (bool): If `True`, ensure the formatted label includes the football descriptor when appropriate.

    Returns:
        tuple: A pair `(formatted_category_lab, list_of_cat)` where `formatted_category_lab` is the resulting formatted label and `list_of_cat` is the original template string.
    """
    category_lab = _format_category_with_list_template(category_r, category_lab, list_of_cat, foot_ballers)
    return category_lab, list_of_cat
