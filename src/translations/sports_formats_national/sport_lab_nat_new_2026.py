#!/usr/bin/python3
""" """

import functools
from ...helps.log import logger
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from .te2 import New_For_nat_female_xo_team

from ...translations import Nat_women
from ...translations_formats.format_data import FormatData

New_For_nat_female_xo_team_2 = {
    "{nat} xzxz": "xzxz {nat}",  # Category:American_basketball
    "{nat} xzxz championships": "بطولات xzxz {nat}",
    "{nat} national xzxz championships": "بطولات xzxz وطنية {nat}",
    "{nat} national xzxz champions": "أبطال بطولات xzxz وطنية {nat}",
    "{nat} amateur xzxz cup": "كأس {nat} xzxz للهواة",
    "{nat} youth xzxz cup": "كأس {nat} xzxz للشباب",
    "{nat} men's xzxz cup": "كأس {nat} xzxz للرجال",
    "{nat} women's xzxz cup": "كأس {nat} xzxz للسيدات",
    "{nat} xzxz super leagues": "دوريات سوبر xzxz {nat}",
}

New_For_nat_female_xo_team_2.update({
    f"{{nat}} {x}" : v for x, v in New_For_nat_female_xo_team.items()
})

# remove "the " from the start of all Nat_women_2 keys
Nat_women_2 = {k[4:] if k.startswith("the ") else k: v for k, v in Nat_women.items()}

nat_bot = FormatData(
    New_For_nat_female_xo_team_2, Nat_women_2, key_placeholder="{nat}", value_placeholder="{nat}",
    text_after=" people",
    text_before="the ",
)

sport_bot = FormatData({}, SPORTS_KEYS_FOR_JOBS, key_placeholder="xzxz", value_placeholder="xzxz")


# @dump_data(enable=True)
def normalize_nat_label(category):
    """
    Normalize nationality placeholders within a category string.

    Example:
        category:"Yemeni national football teams", result: "natar national football teams"
    """
    key = nat_bot.match_key(category)
    result = ""
    if key:
        result = nat_bot.normalize_category(category, key)
    logger.debug(f"normalize_nat_label: {result=}")

    return result


def normalize_sport_label(category):
    """
    Normalize sport placeholders within a category string.

    Example:
        category:"Yemeni national football teams", result: "Yemeni national xoxo teams"
    """
    key = sport_bot.match_key(category)
    result = ""
    if key:
        result = sport_bot.normalize_category(category, key)
    return result


# @dump_data(enable=True)
def normalize_both(category):
    """
    Normalize both nationality and sport tokens in the category.

    Example:
        category:"Yemeni national football teams", result: "natar national xoxo teams"
    """
    new_category = normalize_nat_label(category)
    new_category = normalize_sport_label(new_category)

    return new_category


def get_template(key, category):
    """Fetch the template label for the provided normalized key."""
    return nat_bot.get_template(key, category)


def create_nat_label(category):
    """Search for a nationality-aware label for the category."""
    return nat_bot.search(category)


# @dump_data(enable=True)
@functools.lru_cache(maxsize=None)
def sport_lab_nat_load_new(category):
    """
    Example:
        category:Yemeni under-13 baseball teams", result: "فرق كرة قاعدة يمنية تحت 13 سنة"
    This function appears to load and process a new sports category label in Arabic,
    replacing placeholders with nationality and sport information.
    """
    # category = Yemeni football championships
    template_label = normalize_both(category)  # Normalize the category to create a template label

    nationality_key = nat_bot.match_key(category)
    if not nationality_key:
        return ""

    category2 = nat_bot.normalize_category(category, nationality_key)

    sport_key = sport_bot.match_key(category2)

    logger.debug(f"sport_lab_nat_load_new {template_label=}: {nationality_key=} {sport_key=}")

    if not sport_key:
        return ""

    if not New_For_nat_female_xo_team_2.get(template_label):
        return ""

    # cate = {nat} sport championships
    template_ar = New_For_nat_female_xo_team_2[template_label]
    logger.debug(f"{template_ar=}")

    sport_label = sport_bot.get_key_label(sport_key)
    nationality_label = nat_bot.get_key_label(nationality_key)

    if not nationality_label or not sport_label:
        return ""

    label = template_ar.replace("{nat}", nationality_label).replace("xzxz", sport_label)

    logger.debug(f"{label=}")
    return label


__all__ = [
    "sport_lab_nat_load_new",
    "get_template",
]
