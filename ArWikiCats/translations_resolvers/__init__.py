
import functools
from ..translations_formats import FormatData
from ..translations.nats.Nationality import Nat_women
from . import federation_bot, squads_olympics_bot


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatData:
    """
    Create a shared FormatData instance for sports template resolution.
    """

    format_labels_with_nat = {
        "non {nat} television series": "مسلسلات تلفزيونية غير {nat}",
    }

    return FormatData(format_labels_with_nat, Nat_women, key_placeholder="{nat}", value_placeholder="{nat}")


def nats_women_label(category: str) -> str:
    bot = _load_bot()
    category = category.lower().replace("non-", "non ")
    return bot.search(category)


def resolved_sports_formats_labels(normalized_category) -> str:

    resolved_label = federation_bot.resolve_federation_label(normalized_category)

    if not resolved_label:
        resolved_label = nats_women_label(normalized_category)

    if not resolved_label:
        resolved_label = squads_olympics_bot.resolve_en_is_P17_ar_is_P17_SPORTS(normalized_category)

    return resolved_label


__all__ = [
    "nats_women_label",
    "resolved_sports_formats_labels",
]
