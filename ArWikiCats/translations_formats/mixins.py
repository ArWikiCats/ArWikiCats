"""
Shared mixins for category translation formatting.

This module provides mixin classes that contain common functionality
shared across multiple formatter classes, reducing code duplication.

Classes:
    CategoryPrefixMixin: Handles Arabic category prefix logic and placeholder validation.
"""

import logging

logger = logging.getLogger(__name__)

# Arabic category prefix constant
ARABIC_CATEGORY_PREFIX = "تصنيف:"
ENGLISH_CATEGORY_PREFIX = "category:"


class CategoryPrefixMixin:
    """
    Mixin providing common category prefix handling and placeholder validation.

    This mixin extracts duplicated methods from FormatDataBase and
    MultiDataFormatterBaseHelpers to provide a single implementation.

    Methods:
        prepend_arabic_category_prefix: Add Arabic prefix when English prefix exists.
        check_placeholders: Validate no unprocessed placeholders remain.
        strip_category_prefix: Remove the category prefix from a string.
        normalize_category_string: Normalize whitespace and optionally remove prefix.
    """

    def prepend_arabic_category_prefix(self, category: str, result: str) -> str:
        """
        Prepend the Arabic category prefix "تصنيف:" to `result` when `category`
        begins with "category:" and `result` is not already prefixed.

        Parameters:
            category (str): The original category string; checked case-insensitively
                for the "category:" prefix.
            result (str): The result string to modify.

        Returns:
            str: `result` with "تصنيف:" prepended when applicable, otherwise
                the original `result`.
        """
        if result and category.lower().startswith(ENGLISH_CATEGORY_PREFIX) and not result.startswith(
            ARABIC_CATEGORY_PREFIX
        ):
            return ARABIC_CATEGORY_PREFIX + result
        return result

    def check_placeholders(self, category: str, result: str) -> str:
        """
        Validate that the translated result contains no unprocessed placeholders.

        If the result contains a literal "{" character, a warning is logged
        (including the original category) and an empty string is returned;
        otherwise the original result is returned.

        Parameters:
            category (str): Original category string used for context in warnings.
            result (str): Translated/processed string to check for unprocessed placeholders.

        Returns:
            str: The original `result` if it contains no "{", otherwise an empty string.
        """
        if "{" in result:
            logger.warning(f">>> Found unprocessed placeholders in {category=}: {result=}")
            return ""
        return result

    @staticmethod
    def strip_category_prefix(category: str) -> str:
        """
        Remove the "category:" prefix from a category string if present.

        Parameters:
            category (str): The category string to process.

        Returns:
            str: The category string with "category:" prefix removed (case-insensitive).
        """
        lower = category.lower()
        if lower.startswith(ENGLISH_CATEGORY_PREFIX):
            return category[len(ENGLISH_CATEGORY_PREFIX) :]
        return category

    @staticmethod
    def normalize_category_string(category: str, strip_prefix: bool = False) -> str:
        """
        Normalize a category string by collapsing whitespace and optionally
        stripping the category prefix.

        Parameters:
            category (str): The category string to normalize.
            strip_prefix (bool): If True, also remove the "category:" prefix.

        Returns:
            str: The normalized category string.
        """
        normalized = " ".join(category.split())
        if strip_prefix:
            normalized = CategoryPrefixMixin.strip_category_prefix(normalized)
        return normalized
