"""
from . import fax2
"""

import logging
from typing import Tuple

from .end_start_match import (
    footballers_get_endswith,
    to_get_endswith,
    to_get_startswith,
)
from .utils import get_from_endswith_dict, get_from_starts_dict

logger = logging.getLogger(__name__)


def get_list_of_and_cat3(category3: str, category3_nolower: str = "") -> Tuple[str, bool, str]:
    """Return list templates and metadata extracted from category suffix/prefix."""
    foot_ballers = False
    list_of_cat = ""

    if not category3_nolower:
        category3_nolower = category3

    category3_nolower = category3_nolower.strip()
    category3 = category3.strip()
    # print(f"get_list_of_and_cat3: {category3=}\n" * 10)

    category3, list_of_cat = get_from_starts_dict(category3, to_get_startswith)

    if not list_of_cat:
        if category3.startswith("coaches of "):
            list_of_cat = "مدربو {}"
            category3 = category3[len("coaches of ") :]

        elif category3.startswith("women members of "):
            list_of_cat = "عضوات {}"
            category3 = category3[len("women members of ") :]

        elif category3.endswith(" footballers"):
            foot_ballers = True
            category3, list_of_cat = get_from_endswith_dict(category3, footballers_get_endswith)

        elif category3.endswith(" players") or category3.endswith(" playerss"):
            list_of_cat = "لاعبو {}"

            if category3.endswith("c. playerss") or category3.endswith(" playerss"):
                category3 = category3_nolower[: -len(" playerss")]

            elif category3.endswith("c. players") or category3.endswith(" players"):
                category3 = category3_nolower[: -len(" players")]

    if not list_of_cat:
        category3, list_of_cat = get_from_endswith_dict(category3, to_get_endswith)

    if list_of_cat:
        logger.info(f"<<lightblue>> {list_of_cat=}, {category3=}")

    return list_of_cat, foot_ballers, category3
