"""
from . import fax2
# list_of_cat, Find_wd, Find_ko, foot_ballers, category_lab = fax2.get_list_of_and_cat3(category3, category3_nolower)

"""

import sys
from typing import Dict, Any, Tuple
from ...helps.print_bot import print_put
from .fax2_bots.squad_title_bot import get_squad_title

Find_stubs: Dict[int, bool] = {1: "-stubs" in sys.argv}

to_get_endswith: Dict[str, Dict[str, Any]] = {
    "squad navigational boxes": {
        "lab": "صناديق تصفح تشكيلات {}",
        "Find_wd": False,
        "example": "Category:1996 Basketball Olympic squad navigational boxes",
    },
    "sports navigational boxes": {
        "lab": "صناديق تصفح الرياضة في {}",
        "Find_wd": False,
        "example": "Category:Yemen sports navigational boxes",
    },
    "navigational boxes": {
        "lab": "صناديق تصفح {}",
        "Find_wd": False,
        "example": "",
    },
    "leagues seasons": {
        "lab": "مواسم دوريات {}",
        "Find_wd": True,
        "example": "",
    },
    "alumni": {
        "lab": "خريجو {}",
        "Find_wd": True,
        "example": "",
    },
    "board members": {
        "lab": "أعضاء مجلس {}",
        "Find_wd": True,
        "example": "",
    },
    "faculty": {
        "lab": "أعضاء هيئة تدريس {}",
        "Find_wd": True,
        "example": "",
    },
    "trustees": {
        "lab": "أمناء {}",
        "Find_wd": True,
        "example": "",
    },
    "award winners": {
        "lab": "حائزو جوائز {}",
        "Find_wd": False,
        "example": "",
    },
    "awards winners": {
        "lab": "حائزو جوائز {}",
        "Find_wd": False,
        "example": "",
    },
    "sidebars": {
        "lab": "أشرطة جانبية {}",
        "Find_wd": False,
        "example": "",
    },
    "charts": {
        "lab": "مخططات {}",
        "Find_wd": False,
        "example": "",
    },
    "commissioners": {
        "lab": "مفوضو {}",
        "Find_wd": False,
        "example": "Category:Major Indoor Soccer League (1978–1992) commissioners",
    },
    "commentators": {
        "lab": "معلقو {}",
        "Find_wd": False,
        "example": "Category:Major Indoor Soccer League (1978–1992) commentators",
    },
    "events": {
        "lab": "أحداث {}",
        "Find_wd": False,
        "example": "",
    },
    "tournaments": {
        "lab": "بطولات {}",
        "Find_wd": False,
        "example": "",
    },
}

to_get_startswith: Dict[str, Dict[str, Any]] = {
    "association football matches navigational boxes by teams:": {
        "lab": "صناديق تصفح مباريات كرة قدم حسب الفرق:{}",
        "Find_wd": False,
        "example": "Category:Association football matches navigational boxes by teams:Egypt",
    },
    "21st century members of ": {
        "lab": "أعضاء {} في القرن 21",
        "Find_wd": False,
        "example": "Category:21st-century members of the Louisiana State Legislature",
    },
    "20th century members of ": {"lab": "أعضاء {} في القرن 20", "Find_wd": False, "example": ""},
    "19th century members of ": {"lab": "أعضاء {} في القرن 19", "Find_wd": False, "example": ""},
    "18th century members of ": {"lab": "أعضاء {} في القرن 18", "Find_wd": False, "example": ""},
    "17th century members of ": {"lab": "أعضاء {} في القرن 17", "Find_wd": False, "example": ""},
    "21st century women members of ": {"lab": "عضوات {} في القرن 21", "Find_wd": False, "example": ""},
    "20th century women members of ": {"lab": "عضوات {} في القرن 20", "Find_wd": False, "example": ""},
    "19th century women members of ": {"lab": "عضوات {} في القرن 19", "Find_wd": False, "example": ""},
    "18th century women members of ": {"lab": "عضوات {} في القرن 18", "Find_wd": False, "example": ""},
    "17th century women members of ": {"lab": "عضوات {} في القرن 17", "Find_wd": False, "example": ""},
    "presidents of ": {"lab": "رؤساء {}", "Find_wd": False, "example": ""},
    "family of ": {"lab": "عائلة {}", "Find_wd": False, "example": ""},
    "lists of ": {"lab": "قوائم {}", "Find_wd": False, "example": ""},
    "children of ": {"lab": "أطفال {}", "Find_wd": False, "example": ""},
    "discoveries by ": {"lab": "اكتشافات بواسطة {}", "Find_wd": True, "example": ""},
}


def get_episodes(category3: str, category3_nolower: str) -> Tuple[str, str]:
    """
    examples:
    Category:2016 American television episodes
    Category:Game of Thrones (season 1) episodes
    Category:Game of Thrones season 1 episodes
    """

    list_of_cat = ""

    seasons: Dict[str, str] = {}

    for i in range(1, 11):
        label = f"حلقات {{}} الموسم {i}"
        key1 = f" (season {i}) episodes"
        key2 = f" season {i} episodes"
        seasons[key1] = label
        seasons[key2] = label

    for key, lab in seasons.items():
        if category3.endswith(key):
            list_of_cat = lab
            category3 = category3_nolower.replace(key, "", 1).strip()
            break

    if not list_of_cat:
        list_of_cat = "حلقات {}"
        category3 = category3_nolower.replace("episodes", "", 1).strip()

    return list_of_cat, category3


def get_from_starts_dict(category3: str) -> Tuple[str, str, bool]:
    list_of_cat = ""
    Find_wd = False

    for key, tab in to_get_startswith.items():
        lab = tab["lab"]

        if category3.startswith(key):
            list_of_cat = lab
            category3 = category3.replace(key, "", 1)
            if tab.get("Find_wd") is True:
                Find_wd = True
            break

    return category3, list_of_cat, Find_wd


def get_from_endswith_dict(category3: str) -> Tuple[str, str, bool]:
    list_of_cat = ""
    Find_wd = False

    for key, tab in to_get_endswith.items():
        lab = tab["lab"]

        if category3.endswith(key):
            list_of_cat = lab
            category3 = category3.replace(key, "", 1)
            if tab.get("Find_wd") is True:
                Find_wd = True
            break

    return category3, list_of_cat, Find_wd


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
        # print_put(f'<<lightblue>>get_list_of_and_cat3_with_lab(): {list_of_cat=}, {category3=}, {category_lab=}')
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

        elif category3.endswith(" stubs") and Find_stubs[1]:
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
        print_put(f'<<lightblue>> list_of_cat:"{list_of_cat}", category3:"{category3}",Find_wd:{str(Find_wd)},Find_ko:{str(Find_ko)} ')

    return list_of_cat, Find_wd, Find_ko, foot_ballers, category3
