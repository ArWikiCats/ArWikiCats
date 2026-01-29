#!/usr/bin/python3
"""
Module for dictionary-based category translation formatting (Version 2).

This module provides MultiDataFormatterBaseV2 classes for
advanced category translations where the data_list values can be dictionaries
with multiple placeholder replacements instead of simple strings.

Classes:
    MultiDataFormatterBaseV2: Combines two FormatDataV2 instances for complex translations.

Real world example:

from ArWikiCats.translations_formats.DataModel import FormatDataV2
formatted_data = {
    "{country} writers": "كتاب {demonym}",
}
data_list = {
    "yemeni": {"demonym": "يمنيون", "country_ar": "اليمن"},
    "egyptian": {"demonym": "مصريون", "country_ar": "مصر"},
}
bot = FormatDataV2(formatted_data, data_list, key_placeholder="{country}")
result = bot.search("yemeni writers")
assert result == "كتاب يمنيون"
"""

from typing import Dict

from ..DataModel import FormatDataV2
from .model_multi_data_base import MultiDataFormatterBaseHelpers


class MultiDataFormatterBaseV2(MultiDataFormatterBaseHelpers):
    """
    Combines two FormatDataV2 instances for complex category translations.

    This class orchestrates two FormatDataV2 formatter instances to handle
    categories that contain two dynamic elements (e.g., nationality and
    profession). It inherits from MultiDataFormatterBaseHelpers to provide
    the core translation logic.

    Attributes:
        country_bot (FormatDataV2): Formatter for the first dynamic element (e.g., nationality).
        other_bot (FormatDataV2): Formatter for the second dynamic element (e.g., profession).
        search_first_part (bool): If True, search using only the first part after normalization.
        data_to_find (Dict[str, str] | None): Optional direct lookup dictionary for category labels.

    Example:
        >>> bot = MultiDataFormatterBaseV2(country_bot, profession_bot)
        >>> bot.create_label("yemeni writers")
        'كتاب يمنيون'
    """

    def __init__(
        self,
        country_bot: FormatDataV2,
        other_bot: FormatDataV2,
        search_first_part: bool = False,
        data_to_find: Dict[str, str] | None = None,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
        self.data_to_find = data_to_find
