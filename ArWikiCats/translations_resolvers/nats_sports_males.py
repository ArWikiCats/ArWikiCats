#!/usr/bin/python3
""" """
import re
from ..translations_formats import format_multi_data
from ..translations.nats.Nationality import all_country_with_nat
from ..translations.sports.Sport_key import SPORTS_KEYS_FOR_TEAM

format_labels_with_nat = {
    "{en_nat} {en_sport} federation": "الاتحاد {ar_nat} {ar_sport}",
}


def add_definite_article(label: str) -> str:
    """Prefix each word in ``label`` with the Arabic definite article."""
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label


nats_data = {x: add_definite_article(v["male"]) for x, v in all_country_with_nat.items() if v.get("male")}

both_bot = format_multi_data(
    format_labels_with_nat,
    nats_data,
    key_placeholder="{en_nat}",
    value_placeholder="{ar_nat}",
    data_list2=SPORTS_KEYS_FOR_TEAM,
    key2_placeholder="{en_sport}",
    value2_placeholder="{ar_sport}",
)


def resolve_federation_label(category: str) -> str:
    return both_bot.create_label(category)


__all__ = [
    "resolve_federation_label",
]
