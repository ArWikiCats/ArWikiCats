""" """

from typing import Any, Callable, Dict, Tuple


def _get_from_dict(
    category3: str,
    data: Dict[str, Dict[str, Any]],
    match_fn: Callable[[str, str], bool],
    slice_fn: Callable[[str, str, int], str],
) -> Tuple[str, str]:
    """
    Core function to strip matching prefixes or suffixes from category strings.

    Args:
        category3: The category string to process
        data: Dictionary mapping patterns to their metadata (lab, remove keys)
        match_fn: Function that tests if a pattern matches (startswith/endswith)
        slice_fn: Function that extracts the result (for prefix/suffix removal)

    Returns:
        Tuple of (modified_category, list_template)
    """
    list_of_cat = ""
    category3_original = category3

    try:
        sorted_data = sorted(
            data.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    except AttributeError:
        sorted_data = data.items()

    for key, tab in sorted_data:
        remove_key = tab.get("remove", key)

        if match_fn(category3_original, remove_key):
            list_of_cat = tab["lab"]
            category3 = slice_fn(category3_original, remove_key, len(remove_key))
            break

    return category3, list_of_cat


def get_from_starts_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str]:
    """Strip matching prefixes from ``category3`` based on provided patterns."""

    def starts_with(original: str, pattern: str) -> bool:
        return original.startswith(pattern)

    def slice_prefix(original: str, pattern: str, length: int) -> str:
        return original[length:]

    return _get_from_dict(category3, data, starts_with, slice_prefix)


def get_from_endswith_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str]:
    """Strip matching suffixes from ``category3`` based on provided patterns."""

    def ends_with(original: str, pattern: str) -> bool:
        return original.endswith(pattern)

    def slice_suffix(original: str, pattern: str, length: int) -> str:
        return original[: -length]

    return _get_from_dict(category3, data, ends_with, slice_suffix)
