"""
Utility for matching relationship words in category names.
This module provides functions to identify prepositions and other relation
tokens in English category strings and map them to their Arabic equivalents.
"""

#


def get_relation_word_new(category: str, data: dict[str, str]) -> tuple[str, str]:
    """
    Locate the first relation token enclosed by spaces in a category string and return it with its mapped name.

    Parameters:
        category (str): Category text to search for a relation token (tokens must be bounded by spaces).
        data (dict[str, str]): Mapping from relation tokens to their mapped names (e.g., English token -> Arabic name).

    Returns:
        tuple[str, str]: A pair (token, mapped_name). `token` is the matched separator including surrounding spaces (e.g., " of "), and `mapped_name` is its corresponding value from `data`. Returns ("", "") if no matching token is found.
    """
    # Find the first matching separator key in the category
    matched_separator = next((key for key in data if f" {key} " in category), None)
    # ---
    if matched_separator:
        separator_name = data[matched_separator]
        separator = f" {matched_separator} "
        return separator, separator_name
    # ---
    return "", ""


def get_relation_word(category: str, data: dict[str, str]) -> tuple[str, str]:
    """Find a relation token by iterating the provided mapping order."""
    for separator, separator_name in data.items():
        separator = f" {separator} "
        # if Keep_Work and separator in category:
        if separator in category:
            return separator, separator_name
    # ---
    return "", ""


__all__ = [
    "get_relation_word_new",
    "get_relation_word",
]
