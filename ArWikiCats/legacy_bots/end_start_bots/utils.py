""" """

from typing import Any, Callable, Dict, Tuple


def _get_from_dict(
    category3: str,
    data: Dict[str, Dict[str, Any]],
    match_fn: Callable[[str, str], bool],
    slice_fn: Callable[[str, str, int], str],
) -> Tuple[str, str]:
    """
    Strip the first matching pattern from a category string and return the remainder with the matched entry's lab.

    Processes `data` items sorted by descending number of spaces in the key and then by descending key length; the first entry whose `remove` value (or the key) satisfies `match_fn` against the original `category3` is used. If a match is found, the function returns the category after applying `slice_fn` and the matched entry's `lab`; otherwise the original category and an empty string are returned.

    Parameters:
        category3 (str): Input category string to process.
        data (Dict[str, Dict[str, Any]]): Mapping of pattern keys to metadata dicts. Each metadata dict must include `"lab"` and may include `"remove"` to override the key used for matching.
        match_fn (Callable[[str, str], bool]): Predicate that returns True when a pattern (second arg) matches the original category (first arg), e.g., startswith or endswith.
        slice_fn (Callable[[str, str, int], str]): Function that returns the modified category after removing the matched pattern; it receives (original_category, pattern, pattern_length).

    Returns:
        Tuple[str, str]: `(modified_category, list_template)` where `list_template` is the matched entry's `"lab"`, or an empty string if no match was found.
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
    """
    Strip a matching prefix from category3 and return the remainder with its associated label.

    Parameters:
        category3 (str): The category string to inspect and possibly trim.
        data (Dict[str, Dict[str, Any]]): Mapping of pattern keys to metadata dicts. Each metadata dict must contain a "lab" value and may include a "remove" key that overrides the pattern to match.

    Returns:
        tuple: (modified_category, list_template) where `modified_category` is `category3` with the matched prefix removed (or the original `category3` if no pattern matched), and `list_template` is the matching entry's `"lab"` value or an empty string if no match was found.
    """

    def starts_with(original: str, pattern: str) -> bool:
        """
        Check whether a string begins with the specified pattern.

        Parameters:
            original (str): The string to check.
            pattern (str): The prefix pattern to test for.

        Returns:
            True if `original` starts with `pattern`, False otherwise.
        """
        return original.startswith(pattern)

    def slice_prefix(original: str, pattern: str, length: int) -> str:
        """
        Remove the leading substring of the specified length from `original`.

        Parameters:
            original (str): The input string.
            pattern (str): The matched prefix pattern (provided for API consistency; not used).
            length (int): Number of characters to remove from the start of `original`.

        Returns:
            str: The substring of `original` after removing the first `length` characters.
        """
        return original[length:]

    return _get_from_dict(category3, data, starts_with, slice_prefix)


def get_from_endswith_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str]:
    """
    Strip a matching suffix from `category3` using pattern entries in `data`.

    Parameters:
        category3 (str): The input category string to process.
        data (Dict[str, Dict[str, Any]]): Mapping of pattern keys to metadata dictionaries. Each metadata dict must contain a `"lab"` value and may include a `"remove"` key specifying an alternative pattern to match.

    Returns:
        Tuple[str, str]: A tuple `(modified_category, list_template)` where `modified_category` is `category3` with the matched suffix removed (or the original `category3` if no match was found), and `list_template` is the `"lab"` value from the matching metadata (or an empty string if no match was found).
    """

    def ends_with(original: str, pattern: str) -> bool:
        """
        Determine whether the string `original` ends with `pattern`.

        Returns:
            `true` if `original` ends with `pattern`, `false` otherwise.
        """
        return original.endswith(pattern)

    def slice_suffix(original: str, pattern: str, length: int) -> str:
        """
        Remove the trailing `length` characters from `original`.

        Parameters:
            original (str): The input string to trim.
            pattern (str): Unused; kept for compatibility with the slicer signature.
            length (int): Number of characters to remove from the end of `original`.

        Returns:
            str: `original` with its last `length` characters removed.
        """
        return original[:-length]

    return _get_from_dict(category3, data, ends_with, slice_suffix)
