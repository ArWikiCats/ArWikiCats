#!/usr/bin/python3
""" """

from ..translations_formats import FormatData
from ..translations.nats.Nationality import Nat_women

format_labels_with_nat = {
    "non {nat} television series": "مسلسلات تلفزيونية غير {nat}",
}

nat_bot = FormatData(format_labels_with_nat, Nat_women, key_placeholder="{nat}", value_placeholder="{nat}")


def nats_women_label(category: str) -> str:
    category = category.lower().replace("non-", "non ")

    return nat_bot.search(category)


__all__ = [
    "nats_women_label",
]
