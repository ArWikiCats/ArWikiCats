"""Party label helpers."""

from __future__ import annotations

from ...helps.log import logger
from ...ma_lists import Parties, party_end_keys
from .utils import resolve_suffix_template


def get_parties_lab(party: str) -> str:
    """Return the Arabic label for ``party`` using known suffixes.

    Args:
        party: The party name to resolve.

    Returns:
        The resolved Arabic label or an empty string if the suffix is unknown.
    """

    normalized_party = party.strip()
    logger.info("Resolving party label", extra={"party": normalized_party})

    def _lookup(prefix: str) -> str:
        return Parties.get(prefix, "")

    party_label = resolve_suffix_template(normalized_party, party_end_keys, _lookup)

    if party_label:
        logger.info("Resolved party label", extra={"party": normalized_party, "label": party_label})

    return party_label


__all__ = ["get_parties_lab"]
