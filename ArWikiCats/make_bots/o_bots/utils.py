"""Shared utilities for the :mod:`make_bots.o_bots` package."""

from __future__ import annotations

import re
from typing import Callable, Mapping, Optional, Sequence, Tuple

from ...helps import logger

ValueLookup = Callable[[str], str]


def match_suffix_template(name: str, suffixes: Mapping[str, str]) -> Optional[Tuple[str, str]]:
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


def resolve_suffix_template(name: str, suffix_templates: Mapping[str, str], lookup: ValueLookup) -> str:
    """Resolve ``name`` using ``suffix_templates`` and ``lookup``."""

    match = match_suffix_template(name, suffix_templates)
    if not match:
        return ""

    prefix, template = match

    lookup_value = lookup(prefix)
    logger.debug(f"resolve_suffix_template: {prefix=} -> {lookup_value=}")

    if not lookup_value:
        return ""

    result = template % lookup_value if "%s" in template else template.format(lookup_value)
    logger.debug(f"resolve_suffix_template: {result=}")

    return result


def first_non_empty(key: str, tables: Sequence[Mapping[str, str]]) -> str:
    """Return the first non-empty label for ``key`` from ``tables``."""

    for table in tables:
        value = table.get(key, "")
        if value:
            return value
    return ""


def apply_arabic_article(label: str) -> str:
    """Prefix ``label`` with the Arabic definite article for each word."""

    if not label:
        return ""

    added = "ال"
    article_applied = re.sub(r" ", f" {added}", label)

    result = f"{added}{article_applied}".strip()
    result = result.replace(f" {added}{added}", f" {added}")

    return result
