#!/usr/bin/python3
""" """

import re

from ..helps import logger
from ..translations import change_numb_to_word

known_bodies = {
    # "term of the Iranian Majlis" : "المجلس الإيراني",
    "iranian majlis": "المجلس الإيراني",
    "united states congress": "الكونغرس الأمريكي",
}


pattern_str = rf"^(\d+)(th|nd|st|rd) ({'|'.join(known_bodies.keys())})$"
_political_terms_pattern = re.compile(pattern_str, re.IGNORECASE)


def handle_political_terms(category_text: str) -> str:
    """Handles political terms like 'united states congress'."""
    # كونغرس
    # cs = re.match(r"^(\d+)(th|nd|st|rd) united states congress", category_text)
    match = _political_terms_pattern.match(category_text.lower())
    if not match:
        return ""
    ordinal_number = match.group(1)
    body_key = match.group(3)

    body_label = known_bodies.get(body_key, "")
    if not body_label:
        return ""

    ordinal_label = change_numb_to_word.get(ordinal_number, f"الـ{ordinal_number}")

    label = f"{body_label} {ordinal_label}"
    logger.debug(f">>> _handle_political_terms lab ({label}), country: ({category_text})")
    return label


__all__ = [
    "handle_political_terms",
]
