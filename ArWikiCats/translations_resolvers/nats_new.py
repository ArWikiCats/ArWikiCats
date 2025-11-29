#!/usr/bin/python3
""" """

from ..translations_formats.format_multi_data import FormatMultiData
from ..translations_formats.DataModel.format_data import FormatData
from ..translations.nats.Nationality import en_nats_to_ar_label
from ..translations.sports.Sport_key import SPORTS_KEYS_FOR_TEAM

format_labels_with_nat = {
    "natar national xoxo teams": "منتخبات xoxo وطنية natar",
    "natar xoxo championshipszz": "بطولة natar xoxo",
    "natar xoxo championships": "بطولة natar xoxo",
    "ladies natar xoxo championships": "بطولة natar xoxo للسيدات",
    "natar xoxo tour": "بطولة natar xoxo",
    "women's natar xoxo tour": "بطولة natar xoxo للسيدات",
    "ladies natar xoxo tour": "بطولة natar xoxo للسيدات",
}

# nat_bot = FormatData(format_labels_with_nat, en_nats_to_ar_label, key_placeholder="natar", value_placeholder="natar")
# sport_bot = FormatData({}, SPORTS_KEYS_FOR_TEAM, key_placeholder="xoxo", value_placeholder="xoxo")

both_bot = FormatMultiData(
    format_labels_with_nat,
    en_nats_to_ar_label,
    key_placeholder="natar",
    value_placeholder="natar",
    data_list2=SPORTS_KEYS_FOR_TEAM,
    key2_placeholder="xoxo",
    value2_placeholder="xoxo",
)

create_nat_label = both_bot.create_nat_label
create_label = both_bot.create_label
create_nat_label = both_bot.create_nat_label
normalize_nat_label = both_bot.normalize_nat_label
normalize_other_label = both_bot.normalize_other_label
normalize_both = both_bot.normalize_both


def nats_new_create_label(category: str):
    return both_bot.create_label(category)


__all__ = [
    "normalize_nat_label",
    "normalize_other_label",
    "normalize_both",
    "create_nat_label",
    "create_label",
    "nats_new_create_label",
]
