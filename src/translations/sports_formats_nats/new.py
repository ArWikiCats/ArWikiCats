#!/usr/bin/python3
""" """

from ...translations_formats.format_data import FormatData
from ..nats.Nationality import en_nats_to_ar_label
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM

format_labels_with_nat = {
    "natar national xoxo teams": "منتخبات xoxo وطنية natar",
    "natar xoxo championships": "بطولة natar xoxo",
    "ladies natar xoxo championships": "بطولة natar xoxo للسيدات",
    "natar xoxo tour": "بطولة natar xoxo",
    "women's natar xoxo tour": "بطولة natar xoxo للسيدات",
    "ladies natar xoxo tour": "بطولة natar xoxo للسيدات",
}


nat_bot = FormatData(format_labels_with_nat, en_nats_to_ar_label, key_placeholder="natar", value_placeholder="natar")
sport_bot = FormatData({}, SPORTS_KEYS_FOR_TEAM, key_placeholder="xoxo", value_placeholder="xoxo")


def normalize_nat_label(category):
    key = nat_bot.match_key(category)
    result = ""
    if key:
        result = nat_bot.normalize_category(category, key)
    return result


def normalize_sport_label(category):
    key = sport_bot.match_key(category)
    result = ""
    if key:
        result = sport_bot.normalize_category(category, key)
    return result


def normalize_both(category):
    category = normalize_nat_label(category)
    category = normalize_sport_label(category)
    return category


def get_template_label_new(key, category):
    return nat_bot.get_template(key, category)


def create_nat_label(category):
    return nat_bot.search(category)


def create_label(category):
    # category = Yemeni football championships
    template_label = normalize_both(category)

    natar_key = nat_bot.match_key(category)
    xoxo_key = sport_bot.match_key(category)

    if not format_labels_with_nat.get(template_label):
        return ""

    # cate = natar xoxo championships
    template_ar = format_labels_with_nat[template_label]
    print(f"{template_ar=}")

    sport_label = sport_bot.get_key_label(xoxo_key)
    nat_label = nat_bot.get_key_label(natar_key)

    if not nat_label or not sport_label:
        return ""

    label = template_ar.replace("natar", nat_label).replace("xoxo", sport_label)

    print(f"{label=}")
    return label
