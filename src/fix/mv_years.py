"""Utilities for normalizing year placement within Arabic labels."""

from __future__ import annotations

import re
from ..helps.print_bot import output_test
from ..make2_bots.reg_lines import YEARS_REGEX


def move_by_in(text_str: str) -> str:
    """
    A function that takes in a string and searches for a specific pattern within it. The function replaces underscores in the string with spaces and then uses a regular expression to search for a pattern of the form '{first_part} حسب {by_part} في {date}'.

    Parameters:
    - text_str (str): The input string.

    Returns:
    - str: The modified string if a match is found, otherwise the original string.
    """

    # ---
    # تصنيف:اتحاد الرجبي حسب البلد في 1989
    text_str = text_str.replace("_", " ")
    new_text = text_str
    pattern = rf"^(?P<first_part>.*)\sحسب\s(?P<by_part>[\s\w]+)\sفي\s(?P<date>{YEARS_REGEX})$"
    if result := re.search(pattern, text_str):
        # [[تصنيف:اتحاد الرجبي في 1989 حسب البلد]]
        # ---
        first_part = result.group("first_part")
        by_part = result.group("by_part")
        date = result.group("date")
        new_text = f"{first_part} في {date} حسب {by_part}"
        output_test(f"move_by_in: new_text: {new_text}")
    else:
        output_test(f"move_by_in: no match for {text_str}")

    if new_text != text_str:
        new_text = re.sub(r"\s+", " ", new_text)
        new_text = re.sub(r"\bق\.م\b", "ق م", new_text)
        new_text = new_text.replace(" في في ", " في ")
    return new_text


def move_years_first(text_str: str) -> str:
    """Move leading year fragments to the end of the label when applicable.

    Args:
        text_str: Raw label text.

    Returns:
        A normalized string with the year moved after the subject.
    """

    new_text = text_str
    pattern = rf"^(?P<first_part>{YEARS_REGEX})\sفي\s(?P<second_part>[^0-9]*)$"
    if match := re.match(pattern, text_str):
        first_part = match.group("first_part").strip()
        second_part = match.group("second_part").strip()
        output_test(f"move_years_first: first_part={first_part} second_part={second_part}")
        skip_it = [
            "أفلام",
            "الأفلام",
        ]
        if second_part in skip_it:
            return text_str
        if " في x" in second_part:
            output_test("move_years_first: skipping due to nested preposition")
            return text_str

        new_text = f"{second_part} في {first_part}"
        if result := re.search(r"^(?P<subject>.*)\sحسب\s(?P<by>[\s\w]+)$", second_part):
            output_test("move_years_first: found حسب clause")
            subject = result.group("subject")
            by_part = result.group("by")
            new_text = f"{subject} في {first_part} حسب {by_part}"
    else:
        output_test(f'move_years_first: no match for "{text_str}"')

    if new_text != text_str:
        new_text = re.sub(r"\s+", " ", new_text)
        new_text = re.sub(r"\bق\.م\b", "ق م", new_text)
        new_text = new_text.replace(" في في ", " في ")
    return new_text


def move_years(text_str: str) -> str:
    """Normalize the placement of year fragments within the label.

    Args:
        text_str: Raw label text.

    Returns:
        The normalized label with category namespace preserved.
    """

    text_str = text_str.replace("_", " ").strip()
    is_category_namespace = False
    if text_str.startswith("تصنيف:"):
        is_category_namespace = True
        text_str = text_str.replace("تصنيف:", "")

    new_text = move_years_first(text_str)
    if new_text == text_str:
        new_text = move_by_in(text_str)

    if is_category_namespace:
        new_text = f"تصنيف:{new_text}"
    return new_text


__all__ = [
    "move_by_in",
    "move_years",
    "move_years_first",
]
