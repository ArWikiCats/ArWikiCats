"""Party label helpers."""

from __future__ import annotations

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import PARTIES, party_end_keys
from .utils import resolve_suffix_template


@dump_data()
def get_parties_lab_old(party: str) -> str:
    """Return the Arabic label for ``party`` using known suffixes.

    Args:
        party: The party name to resolve.

    Returns:
        The resolved Arabic label or an empty string if the suffix is unknown.
    """

    normalized_party = party.strip()
    logger.info(f'get_parties_lab party:"{party}"')
    party_label = ""

    for suffix, suffix_template in party_end_keys.items():
        suffix_with_space = f" {suffix}"
        if party.endswith(suffix_with_space) and party_label == "":
            party_key = party[: -len(suffix_with_space)]
            logger.debug(f'party_uu:"{party_key}", tat:"{suffix}" ')
            label = PARTIES.get(party_key, "")
            if label:
                party_label = suffix_template % label if "%s" in suffix_template else suffix_template.format(label)
                break

    if party_label:
        logger.info(f'get_parties_lab party:"{party}", party_label:"{party_label}"')

    return party_label


@dump_data()
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
        return PARTIES.get(prefix, "")

    party_label = resolve_suffix_template(normalized_party, party_end_keys, _lookup)

    if party_label:
        logger.info(f'get_parties_lab party:"{party}", party_label:"{party_label}"')

    return party_label


__all__ = ["get_parties_lab"]
