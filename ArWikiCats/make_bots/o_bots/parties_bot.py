"""Party label helpers."""

from __future__ import annotations

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import PARTIES, PARTY_ROLE_SUFFIXES
from .utils import resolve_suffix_template


def get_parties_lab(party: str) -> str:
    """Return the Arabic label for ``party`` using known suffixes.

    Args:
        party: The party name to resolve.

    Returns:
        The resolved Arabic label or an empty string if the suffix is unknown.
    """

    normalized_party = party.strip()
    logger.info(f'get_parties_lab party:"{party}"')

    def _lookup(prefix: str) -> str:
        """Retrieve a party label by suffix prefix key."""
        return PARTIES.get(prefix, "")

    party_label = resolve_suffix_template(normalized_party, PARTY_ROLE_SUFFIXES, _lookup)

    if party_label:
        logger.info(f'get_parties_lab party:"{party}", party_label:"{party_label}"')

    return party_label


__all__ = ["get_parties_lab"]
