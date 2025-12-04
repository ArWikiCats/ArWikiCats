
from . nats import nats_women_label
from . import federation_bot, squads_olympics_bot


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
