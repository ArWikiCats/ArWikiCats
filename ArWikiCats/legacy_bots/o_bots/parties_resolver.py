"""Party label helpers."""

from __future__ import annotations

from ...helps import logger
from ...translations import PARTIES
from .utils import resolve_suffix_template

PARTY_ROLE_SUFFIXES = {
    "candidates for member of parliament": "مرشحو %s لعضوية البرلمان",
    "candidates for member-of-parliament": "مرشحو %s لعضوية البرلمان",
    "candidates": "مرشحو %s",
    "leaders": "قادة %s",
    "politicians": "سياسيو %s",
    "members": "أعضاء %s",
    "state governors": "حكام ولايات من %s",
}


def get_parties_lab(party: str) -> str:
    """Return the Arabic label for ``party`` using known suffixes.

    Args:
        party: The party name to resolve.

    Returns:
        The resolved Arabic label or an empty string if the suffix is unknown.
    """

    normalized_party = party.strip()
    logger.debug(f"get_parties_lab {party=}")

    def _lookup(prefix: str) -> str:
        """Retrieve a party label by suffix prefix key."""
        return PARTIES.get(prefix, "")

    party_label = resolve_suffix_template(normalized_party, PARTY_ROLE_SUFFIXES, _lookup)

    if party_label:
        logger.info(f"get_parties_lab {party=}, {party_label=}")

    return party_label


__all__ = ["get_parties_lab"]
