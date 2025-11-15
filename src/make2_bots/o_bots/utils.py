"""Shared utilities for the :mod:`make2_bots.o_bots` package."""

from __future__ import annotations

import re
from typing import Callable, Mapping, Optional, Sequence, Tuple

ValueLookup = Callable[[str], str]


def match_suffix_template(name: str, suffixes: Mapping[str, str]) -> Optional[Tuple[str, str]]:
    """Find the first suffix template that matches ``name``."""

    stripped = name.strip()
    for suffix, template in suffixes.items():
        candidates = [suffix]
        if not suffix.startswith(" "):
            candidates.append(f" {suffix}")
        for candidate in candidates:
            if stripped.endswith(candidate):
                prefix = stripped[: -len(candidate)].strip()
                return prefix, template
    return None


def resolve_suffix_template(name: str, suffix_templates: Mapping[str, str], lookup: ValueLookup) -> str:
    """Resolve ``name`` using ``suffix_templates`` and ``lookup``."""

    match = match_suffix_template(name, suffix_templates)
    if not match:
        return ""

    prefix, template = match
    lookup_value = lookup(prefix)
    if not lookup_value:
        return ""

    return template % lookup_value if "%s" in template else template.format(lookup_value)


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
    article_applied = re.sub(r" ", " ال", label)
    return f"ال{article_applied}".strip()
