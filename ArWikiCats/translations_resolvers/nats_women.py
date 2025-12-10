"""
TODO: replaced by nats_v2.py (resolve_by_nats)
"""
import functools
from ..translations_formats import FormatData
from ..translations.nats.Nationality import Nat_women


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatData:
    """
    Create a shared FormatData instance for sports template resolution.
    """

    format_labels_with_nat = {
        "{nat_en} television series": "مسلسلات تلفزيونية {nat_ar}",
        "non {nat_en} television series": "مسلسلات تلفزيونية غير {nat_ar}",
    }

    return FormatData(format_labels_with_nat, Nat_women, key_placeholder="{nat_en}", value_placeholder="{nat_ar}")


def nats_women_label(category: str) -> str:
    bot = _load_bot()
    category = category.lower().replace("non-", "non ")
    return bot.search(category)


__all__ = [
    "nats_women_label",
]
