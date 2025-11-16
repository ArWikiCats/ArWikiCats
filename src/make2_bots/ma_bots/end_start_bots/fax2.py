"""
from . import fax2
# list_of_cat, Find_wd, Find_ko, foot_ballers, category_lab = fax2.get_list_of_and_cat3(category3, category3_nolower)

"""

from typing import Dict, Tuple
from ....helps.log import logger
from .... import app_settings

from .squad_title_bot import get_squad_title
from .end_start_match import get_from_starts_dict, get_from_endswith_dict


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
                category3 = category3_nolower.replace(key, "", 1).strip()
                return list_of_cat, category3

    list_of_cat = "حلقات {}"
    category3 = category3_nolower.replace("episodes", "", 1).strip()

    return list_of_cat, category3


def get_templates_fo(category3: str) -> Tuple[str, str]:
    """
    examples:
    Category:2016 American television episodes
    Category:Game of Thrones (season 1) episodes
    Category:Game of Thrones season 1 episodes
    """

    list_of_cat = ""

    dict_temps: Dict[str, str] = {
        "sidebar templates": "قوالب اشرطة جانبية {}",
        "politics and government templates": "قوالب سياسة وحكومة {}",
        "infobox templates": "قوالب معلومات {}",
        "squad templates": "قوالب تشكيلات {}",
    }

    for key, lab in dict_temps.items():
        if category3.endswith(key):
            list_of_cat = lab
            category3 = category3.replace(key, "", 1).strip()
            break

    if not list_of_cat:
        list_of_cat = "قوالب {}"
        category3 = category3.replace(" templates", "", 1).strip()

    return list_of_cat, category3


def get_list_of_and_cat3_with_lab2(category3_o: str, category3_nolower: str) -> str:
    category_lab = ""
    list_of_cat = ""
    category3 = category3_o

    if category3.endswith(" squad templates"):
        list_of_cat = "قوالب تشكيلات {}"
        category3 = category3.replace(" squad templates", "", 1)
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = f"قوالب {cate_labs}"

    elif category3.endswith(" squad navigational boxes"):
        list_of_cat = "صناديق تصفح تشكيلات {}"
        category3 = category3.replace(" squad navigational boxes", "", 1)
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

    # print(f"get_list_of_and_cat3: {category3=}\n" * 10)

    category3, list_of_cat, Find_wd = get_from_starts_dict(category3)

    if not list_of_cat:
        if category3.startswith("women members of "):
            list_of_cat = "عضوات {}"
            category3 = category3.replace("women members of ", "", 1)

        elif category3.endswith(" episodes"):
            Find_wd = True
            list_of_cat, category3 = get_episodes(category3, category3_nolower)

        elif category3.endswith(" footballers"):
            foot_ballers = True
            if category3.endswith(" women's footballers"):
                Find_wd = True
                Find_ko = True
                list_of_cat = "لاعبات {}"
                category3 = category3_nolower.replace(" women's footballers", "", 1)

            elif category3.endswith(" female footballers"):
                Find_wd = True
                Find_ko = True
                list_of_cat = "لاعبات {}"
                category3 = category3_nolower.replace(" female footballers", "", 1)

            elif category3.endswith("c. footballers"):
                Find_wd = True
                list_of_cat = "لاعبو {}"
                category3 = category3_nolower.replace(" footballers", "", 1)

            elif category3.endswith(" footballers"):
                Find_wd = True
                Find_ko = True
                list_of_cat = "لاعبو {}"
                category3 = category3_nolower.replace(" footballers", "", 1)

        elif category3.endswith(" templates"):
            list_of_cat, category3 = get_templates_fo(category3)

        elif category3.endswith(" stubs") and app_settings.find_stubs:
            list_of_cat = "بذرة {}"
            category3 = category3.replace(" stubs", "", 1)

        elif category3.endswith(" players") or category3.endswith(" playerss"):
            Find_wd = True
            Find_ko = True
            list_of_cat = "لاعبو {}"

            if category3.endswith("c. playerss"):
                category3 = category3_nolower.replace(" playerss", "", 1)

            elif category3.endswith("c. players"):
                list_of_cat = "لاعبو {}"
                category3 = category3_nolower.replace(" players", "", 1)

            elif category3.endswith(" playerss"):
                list_of_cat = "لاعبو {}"
                category3 = category3_nolower.replace(" playerss", "", 1)

            elif category3.endswith(" players"):
                list_of_cat = "لاعبو {}"
                category3 = category3_nolower.replace(" players", "", 1)

    if not list_of_cat:
        category3, list_of_cat, Find_wd = get_from_endswith_dict(category3)

    if list_of_cat:
        logger.info(f'<<lightblue>> list_of_cat:"{list_of_cat}", category3:"{category3}",Find_wd:{str(Find_wd)},Find_ko:{str(Find_ko)} ')

    return list_of_cat, Find_wd, Find_ko, foot_ballers, category3
