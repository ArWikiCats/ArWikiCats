#


def get_relation_word_new(category: str, data: dict[str, str]) -> tuple[str, str]:
    """Find the first relation token present in ``category`` using comprehension."""
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
