#!/usr/bin/python3
""" """

import re

from ..nats.Nationality import all_country_with_nat_ar
from .patterns import load_keys_to_pattern

new_pattern = load_keys_to_pattern(all_country_with_nat_ar)

RE_KEYS_NEW = re.compile(new_pattern, re.I)


def match_nat_key(category: str) -> str:
    """Return the nationality key found in ``category`` or an empty string."""
    match = RE_KEYS_NEW.search(f" {category} ")
    if match:
        return match.group(1)
    return ""


__all__ = [
    "match_nat_key",
]
