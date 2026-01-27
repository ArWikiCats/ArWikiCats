"""
Multi-data formatter for double-key patterns.
This module provides MultiDataFormatterDataDouble, which combines a standard
FormatData instance with a FormatDataDouble instance for complex categories.
"""

from typing import Dict

from ..DataModel import FormatData
from ..DataModelMulti import MultiDataFormatterBaseHelpers
from .model_data_double import FormatDataDouble


class MultiDataFormatterDataDouble(MultiDataFormatterBaseHelpers):
    """
    Combines FormatData with FormatDataDouble for double-key category translations.

    This class orchestrates a FormatData instance for nationality/country
    elements and a FormatDataDouble instance for elements that may have
    two adjacent keys (e.g., "action drama" in film genres). It handles
    categories like "british action drama films".

    Attributes:
        country_bot (FormatData): Formatter for nationality/country elements.
        other_bot (FormatDataDouble): Formatter for double-key elements (e.g., film genres).
        search_first_part (bool): If True, search using only the first part after normalization.
        data_to_find (Dict[str, str] | None): Optional direct lookup dictionary for category labels.

    Example:
        >>> bot = MultiDataFormatterDataDouble(country_bot, genre_bot)
        >>> bot.create_label("british action drama films")
        'أفلام أكشن دراما بريطانية'
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: FormatDataDouble,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] | None = None,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find
