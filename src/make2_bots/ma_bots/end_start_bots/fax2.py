"""
from . import fax2
# list_of_cat, Find_wd, Find_ko, foot_ballers, category_lab = fax2.get_list_of_and_cat3(category3, category3_nolower)

"""

from typing import Tuple
from ....helps.log import logger
from .... import app_settings

from .squad_title_bot import get_squad_title
from .end_start_match import to_get_startswith, to_get_endswith, footballers_get_endswith
from .utils import get_from_starts_dict, get_from_endswith_dict
from .fax2_temp import get_templates_fo


def get_episodes(category3: str, category3_nolower: str="") -> Tuple[str, str]:
    """
    examples:
    Category:2016 American television episodes
    Category:Game of Thrones (season 1) episodes
    Category:Game of Thrones season 1 episodes
    """

    list_of_cat = ""
    if not category3_nolower:
        category3_nolower = category3

    # Generate episode patterns for seasons 1–10
    for i in range(1, 11):
        label = f"حلقات {{}} الموسم {i}"

        # Generate both key patterns
        patterns = [
            f" (season {i}) episodes",
            f" season {i} episodes",
        ]

        for key in patterns:
            # Use lower() once for comparison
            if category3.lower().endswith(key.lower()):
                list_of_cat = label
                category3 = category3_nolower[: -len(key)].strip()
                return list_of_cat, category3

    list_of_cat = "حلقات {}"
    category3 = category3_nolower[: -len("episodes")].strip()

    return list_of_cat, category3


def get_list_of_and_cat3_with_lab2(category3_o: str) -> str:
    category_lab = ""
    list_of_cat = ""
    category3 = category3_o

    if category3.endswith(" squad templates"):
        list_of_cat = "قوالب تشكيلات {}"
        category3 = category3[: -len(" squad templates")]
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = f"قوالب {cate_labs}"

    elif category3.endswith(" squad navigational boxes"):
        list_of_cat = "صناديق تصفح تشكيلات {}"
        category3 = category3[: -len(" squad navigational boxes")]
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = f"صناديق تصفح {cate_labs}"

    if category_lab:
        logger.debug(f'<<lightblue>>get_list_of_and_cat3_with_lab(): {list_of_cat=}, {category3=}, {category_lab=}')
        print(f"<<lightblue>>(): {category3_o=}, {category_lab=}")

    return category_lab


def get_list_of_and_cat3(category3: str, category3_nolower: str) -> Tuple[str, bool, bool, bool, str]:
    foot_ballers = False
    Find_wd = False
    Find_ko = False
    list_of_cat = ""

    if not category3_nolower:
        category3_nolower = category3

    # print(f"get_list_of_and_cat3: {category3=}\n" * 10)

    category3, list_of_cat, Find_wd = get_from_starts_dict(category3, to_get_startswith)

    if not list_of_cat:
        if category3.startswith("women members of "):
            list_of_cat = "عضوات {}"
            category3 = category3[: -len("women members of ")]

        elif category3.endswith(" episodes"):
            Find_wd = True
            list_of_cat, category3 = get_episodes(category3, category3_nolower)

        elif category3.endswith(" footballers"):
            foot_ballers = True
            category3, list_of_cat, Find_wd, Find_ko = get_from_endswith_dict(category3, footballers_get_endswith)

        elif category3.endswith(" templates"):
            list_of_cat, category3 = get_templates_fo(category3)

        elif category3.endswith(" stubs") and app_settings.find_stubs:
            list_of_cat = "بذرة {}"
            category3 = category3[: -len(" stubs")]

        elif category3.endswith(" players") or category3.endswith(" playerss"):
            Find_wd = True
            Find_ko = True
            list_of_cat = "لاعبو {}"

            if category3.endswith("c. playerss") or category3.endswith(" playerss"):
                category3 = category3_nolower[: -len(" playerss")]

            elif category3.endswith("c. players") or category3.endswith(" players"):
                category3 = category3_nolower[: -len(" players")]

    if not list_of_cat:
        category3, list_of_cat, Find_wd, Find_ko = get_from_endswith_dict(category3, to_get_endswith)

    if list_of_cat:
        logger.info(f'<<lightblue>> list_of_cat:"{list_of_cat}", category3:"{category3}",Find_wd:{str(Find_wd)},Find_ko:{str(Find_ko)} ')

    return list_of_cat, Find_wd, Find_ko, foot_ballers, category3
