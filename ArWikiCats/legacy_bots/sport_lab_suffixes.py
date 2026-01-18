"""
Helpers for resolving sports teams and language categories.

TODO: compare this file with ArWikiCats/new/handle_suffixes.py
"""

from __future__ import annotations
from ast import dump
from ..helps import logger
from ..translations import SPORTS_KEYS_FOR_JOBS
from . import team_work


def match_suffix_template(name: str, suffixes: dump[str, str]):
    """
    Find the first suffix template that matches ``name``.

    input: 'football governing bodies'
    output: prefix='football governing' -> template='هيئات {}'
    """

    stripped = name.strip()
    # sorted by len of " " in key
    sorted_suffixes = dict(
        sorted(
            suffixes.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    )

    for suffix, template in sorted_suffixes.items():
        candidates = [suffix]
        if not suffix.startswith(" "):
            candidates.append(f" {suffix}")

        for candidate in candidates:
            if stripped.endswith(candidate):
                prefix = stripped[: -len(candidate)].strip()
                logger.debug(f"match_suffix_template: {name=} -> {candidate=} -> {prefix=}")
                return prefix, template
    return None


def resolve_team_suffix(normalized_team: str) -> str:
    """Resolve team suffix for sports categories.

    Args:
        normalized_team (str): The normalized team name.

    Returns:
        str: The resolved team suffix.
    """

    match = match_suffix_template(normalized_team, team_work.Teams_new_end_keys)
    if not match:
        return ""

    prefix, template = match

    lookup_value = SPORTS_KEYS_FOR_JOBS.get(prefix, "")
    logger.debug(f"resolve_suffix_template: {prefix=} -> {lookup_value=}")

    if not lookup_value:
        return ""

    result = template % lookup_value if "%s" in template else template.format(lookup_value)
    logger.debug(f"resolve_suffix_template: {result=}")

    return result


__all__ = [
    "resolve_team_suffix",
]
