#!/usr/bin/python3
""" """

from ...helps.log import logger
from ...translations_formats.format_2_data import FormatMultiData
from ...translations_formats.format_data import FormatData
from ..nats.Nationality import en_nats_to_ar_label
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM

format_labels_with_nat = {
    "natar national xoxo teams": "منتخبات xoxo وطنية natar",
    "natar xoxo championshipszz": "بطولة natar xoxo",
    "natar xoxo championships": "بطولة natar xoxo",
    "ladies natar xoxo championships": "بطولة natar xoxo للسيدات",
    "natar xoxo tour": "بطولة natar xoxo",
    "women's natar xoxo tour": "بطولة natar xoxo للسيدات",
    "ladies natar xoxo tour": "بطولة natar xoxo للسيدات",
}

nat_bot = FormatData(format_labels_with_nat, en_nats_to_ar_label, key_placeholder="natar", value_placeholder="natar")
sport_bot = FormatData({}, SPORTS_KEYS_FOR_TEAM, key_placeholder="xoxo", value_placeholder="xoxo")

both_bot = FormatMultiData(
    format_labels_with_nat,
    en_nats_to_ar_label,
    key_placeholder="natar",
    value_placeholder="natar",
    data_list2=SPORTS_KEYS_FOR_TEAM,
    key2_placeholder="xoxo",
    value2_placeholder="xoxo",
)




def _normalize_nat_label(category) -> str:
    """Normalize nationality placeholders within a category string."""
    key = nat_bot.match_key(category)
    result = ""
    if key:
        result = nat_bot.normalize_category(category, key)
    return result


def _normalize_sport_label(category) -> str:
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



def _normalize_both(category) -> str:
    """
    Normalize both nationality and sport tokens in the category.

    input: "british softball championshipszz", output: "natar xoxo championshipszz"
    """
    new_category = normalize_nat_label(category)
    new_category = normalize_sport_label(new_category)

    return new_category


def _create_nat_label(category) -> str:
    """Search for a nationality-aware label for the category."""
    return nat_bot.search(category)


def _create_label(category) -> str:
    """
    Create a localized label by combining nationality and sport templates.

    Example:
        category: "ladies british softball tour", output: "بطولة المملكة المتحدة للكرة اللينة للسيدات"

    # TODO: Replaced by FormatMultiData
    """
    # category = Yemeni football championships
    template_label = normalize_both(category)

    nationality_key = nat_bot.match_key(category)
    xoxo_key = sport_bot.match_key(category)

    if not format_labels_with_nat.get(template_label):
        return ""

    # cate = natar xoxo championships
    template_ar = format_labels_with_nat[template_label]
    logger.debug(f"{template_ar=}")

    sport_label = sport_bot.get_key_label(xoxo_key)
    nationality_label = nat_bot.get_key_label(nationality_key)

    if not nationality_label or not sport_label:
        return ""

    label = template_ar.replace("natar", nationality_label).replace("xoxo", sport_label)

    logger.debug(f"{label=}")
    return label


create_nat_label = both_bot.create_nat_label
create_label = both_bot.create_label
create_nat_label = both_bot.create_nat_label
normalize_nat_label = both_bot.normalize_nat_label
normalize_sport_label = both_bot.normalize_sport_label
normalize_both = both_bot.normalize_both

__all__ = [
    "normalize_nat_label",
    "normalize_sport_label",
    "normalize_both",
    "create_nat_label",
    "create_label",
]
