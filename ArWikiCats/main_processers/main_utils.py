"""

"""

from typing import Tuple

from ..helps import dump_data, logger


# @dump_data(1)
def list_of_cat_func_new(category_r: str, category_lab: str, list_of_cat: str) -> str:
    """Format category labels using list templates tweaks."""
    category_lab_or = category_lab
    list_of_cat_x = list_of_cat.split("{}")[0].strip()

    logger.info(f"<<lightblue>> list_of_cat_func_new {category_lab=}, {list_of_cat=}, {list_of_cat_x=}")

    if not category_lab.startswith(list_of_cat_x) or list_of_cat_x == "":
        category_lab = list_of_cat.format(category_lab)

    logger.info(f"<<lightblue>> list_of_cat_func_new add {category_lab=}, {category_lab_or=}, {category_r=} ")

    return category_lab


# @dump_data(1)
def list_of_cat_func_foot_ballers(category_r: str, category_lab: str, list_of_cat: str) -> str:
    """
    Format category labels using list templates and football-specific tweaks.

    {"category_r": "guernsey footballers", "category_lab": "غيرنزي", "list_of_cat": "لاعبو {}", "output": "لاعبو  كرة قدم غيرنزي"}
    """
    category_lab_or = category_lab
    list_of_cat_x = list_of_cat.split("{}")[0].strip()

    logger.info(f"<<lightblue>> list_of_cat_func_foot_ballers {category_lab=}, {list_of_cat=}, {list_of_cat_x=}")

    if not category_lab.startswith(list_of_cat_x):
        category_lab = list_of_cat.format(category_lab)

    logger.info(f"<<lightblue>> list_of_cat_func_foot_ballers add {category_lab=}, {category_lab_or=}, {category_r=} ")
    # fix tab[Category:Guernsey footballers] = "تصنيف:لاعبو غيرنزي"

    if "كرة" not in category_lab:
        list_of_cat = list_of_cat.replace("{}", " كرة قدم {}")
        category_lab = list_of_cat.format(category_lab_or)
        logger.info(f"<<lightblue>> list_of_cat_func_foot_ballers add {list_of_cat=}, {category_lab=}, {category_r=} ")

    return category_lab


def list_of_cat_func(category_r: str, category_lab: str, list_of_cat: str, foot_ballers: bool) -> Tuple[str, str]:
    """Format category labels using list templates and football-specific tweaks."""
    category_lab_or = category_lab
    list_of_cat_x = list_of_cat.split("{}")[0].strip()

    logger.info(f"<<lightblue>> list_of_cat_func {category_lab=}, {list_of_cat=}, {list_of_cat_x=}")

    if not category_lab.startswith(list_of_cat_x):
        category_lab = list_of_cat.format(category_lab)

    logger.info(f"<<lightblue>> list_of_cat_func add {category_lab=}, {category_lab_or=}, {category_r=} ")
    # fix tab[Category:Guernsey footballers] = "تصنيف:لاعبو غيرنزي"

    if foot_ballers and "كرة" not in category_lab:
        list_of_cat = list_of_cat.replace("{}", " كرة قدم {}")
        category_lab = list_of_cat.format(category_lab_or)
        logger.info(f"<<lightblue>> list_of_cat_func add {list_of_cat=}, {category_lab=}, {category_r=} ")

    return category_lab, list_of_cat
