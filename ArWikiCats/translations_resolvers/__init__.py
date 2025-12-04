
from . nats import nats_women_label
from . import contries_names, federation_bot


def resolved_sports_formats_labels(normalized_category) -> str:

    resolved_label = federation_bot.resolve_federation_label(normalized_category)

    if not resolved_label:
        resolved_label = nats_women_label(normalized_category)

    if not resolved_label:
        resolved_label = contries_names.resolve_by_contries_names(normalized_category)

    return resolved_label


__all__ = [
    "nats_women_label",
    "resolved_sports_formats_labels",
]
