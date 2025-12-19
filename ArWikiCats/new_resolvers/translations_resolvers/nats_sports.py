#!/usr/bin/python3
"""
Resolve national sports categories to their Arabic labels.
TODO: use nats_sport_multi_v2.py instead of this file
"""

from ..translations_resolvers_v2.nats_sport_multi_v2 import resolve_nats_sport_multi_v2


def nats_new_create_label(category: str) -> str:
    return resolve_nats_sport_multi_v2(category)


__all__ = [
    "nats_new_create_label",
]
