#!/usr/bin/python3
""" """

from ..translations_formats import format_multi_data

from ..translations.nats.Nationality import en_nats_to_ar_label
from ..translations.sports.Sport_key import SPORTS_KEYS_FOR_TEAM

format_labels_with_nat = {
    "{nat_en} national {sport_en} teams": "منتخبات {sport_ar} وطنية {nat_ar}",
    "{nat_en} {sport_en} championshipszz": "بطولة {nat_ar} {sport_ar}",
    "{nat_en} {sport_en} championships": "بطولة {nat_ar} {sport_ar}",
    "ladies {nat_en} {sport_en} championships": "بطولة {nat_ar} {sport_ar} للسيدات",
    "{nat_en} {sport_en} tour": "بطولة {nat_ar} {sport_ar}",
    "women's {nat_en} {sport_en} tour": "بطولة {nat_ar} {sport_ar} للسيدات",
    "ladies {nat_en} {sport_en} tour": "بطولة {nat_ar} {sport_ar} للسيدات",
}

both_bot = format_multi_data(
    format_labels_with_nat,
    en_nats_to_ar_label,
    key_placeholder="{nat_en}",
    value_placeholder="{nat_ar}",
    data_list2=SPORTS_KEYS_FOR_TEAM,
    key2_placeholder="{sport_en}",
    value2_placeholder="{sport_ar}",
)

create_nat_label = both_bot.create_nat_label
create_label = both_bot.create_label
create_nat_label = both_bot.create_nat_label
normalize_nat_label = both_bot.normalize_nat_label
normalize_other_label = both_bot.normalize_other_label
normalize_both = both_bot.normalize_both


def nats_new_create_label(category: str) -> str:
    return both_bot.create_label(category)


__all__ = [
    "normalize_nat_label",
    "normalize_other_label",
    "normalize_both",
    "create_nat_label",
    "create_label",
    "nats_new_create_label",
]
