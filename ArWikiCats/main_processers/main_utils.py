"""
Utility functions for category label formatting.
This module provides helper functions to wrap Arabic labels in common
list-style templates (e.g., "لاعبو {}") with special handling for sports.
"""

from typing import Tuple

from ..helps import dump_data, logger

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
    Core function to format category labels using list templates.

    Args:
        category_r: Original category string for logging/debugging
        category_lab: The Arabic label to format
        list_of_cat: Template string with {} placeholder
        foot_ballers: If True, add "football" prefix for categories missing it

    Returns:
        Formatted Arabic category label
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
    """Format category labels using list templates tweaks."""
    return _format_category_with_list_template(category_r, category_lab, list_of_cat, foot_ballers=False)


def list_of_cat_func_foot_ballers(category_r: str, category_lab: str, list_of_cat: str) -> str:
    """
    Format category labels using list templates and football-specific tweaks.

    {"category_r": "guernsey footballers", "category_lab": "غيرنزي", "list_of_cat": "لاعبو {}", "output": "لاعبو  كرة قدم غيرنزي"}
    """
    return _format_category_with_list_template(category_r, category_lab, list_of_cat, foot_ballers=True)


def list_of_cat_func(category_r: str, category_lab: str, list_of_cat: str, foot_ballers: bool) -> Tuple[str, str]:
    """Format category labels using list templates and football-specific tweaks."""
    category_lab = _format_category_with_list_template(category_r, category_lab, list_of_cat, foot_ballers)
    return category_lab, list_of_cat
