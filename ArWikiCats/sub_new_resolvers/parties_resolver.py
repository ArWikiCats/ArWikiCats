"""Party label helpers."""

from __future__ import annotations

import logging
from ..translations import PARTIES
from ..translations_formats import FormatData

logger = logging.getLogger(__name__)

formatted_data = {
    "{party_key} candidates for member of parliament": "مرشحو {party_label} لعضوية البرلمان",
    "{party_key} candidates for member-of-parliament": "مرشحو {party_label} لعضوية البرلمان",
    "{party_key} candidates": "مرشحو {party_label}",
    "{party_key} leaders": "قادة {party_label}",
    "{party_key} politicians": "سياسيو {party_label}",
    "{party_key} members": "أعضاء {party_label}",
    "{party_key} state governors": "حكام ولايات من {party_label}",
}

_parties_bot = FormatData(
    formatted_data=formatted_data,
    data_list=PARTIES,
    key_placeholder="{party_key}",
    value_placeholder="{party_label}",
)


def get_parties_lab(party: str) -> str:
    """Return the Arabic label for ``party`` using known suffixes.

    Args:
        party: The party name to resolve.

    Returns:
        The resolved Arabic label or an empty string if the suffix is unknown.
    """

    normalized_party = party.strip()
    logger.debug(f"get_parties_lab {party=}")

    # Try FormatData first
    label = _parties_bot.search(normalized_party)
    logger.info(f"get_parties_lab {party=}, {label=}")

    return label


__all__ = ["get_parties_lab"]
