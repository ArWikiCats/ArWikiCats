#!/usr/bin/python3
"""
Module for dictionary-based category translation formatting (Version 2).

This module provides FormatDataV2 classe for
advanced category translations where the data_list values can be dictionaries
with multiple placeholder replacements instead of simple strings.

Classes:
    FormatDataV2: Handles dictionary-based template-driven category translations.

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

from typing import Dict, Union

from .model_data_base import FormatDataBase


class FormatDataV2(FormatDataBase):
    """
    Handles dictionary-based template-driven category translations.

    This class extends FormatDataBase to support data_list values that are
    dictionaries containing multiple placeholders. This allows for more
    complex translations where multiple parts of the template need to be
    replaced with different values from the same key's data.

    Attributes:
        formatted_data (Dict[str, str]): Template patterns mapping English patterns to Arabic templates.
        data_list (Dict[str, Union[str, Dict[str, str]]]): Key mappings where values can be
            simple strings or dictionaries with multiple placeholder values.
        key_placeholder (str): Placeholder used in formatted_data keys.
        text_after (str): Optional text that appears after the key in patterns.
        text_before (str): Optional text that appears before the key in patterns.

    Example:
        >>> bot = FormatDataV2(
        ...     formatted_data={"{country} writers": "{demonym} كتاب"},
        ...     data_list={"yemen": {"demonym": "يمنيون"}},
        ...     key_placeholder="{country}",
        ... )
        >>> bot.search("yemen writers")
        'يمنيون كتاب'
    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, Union[str, Dict[str, str]]],
        key_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",
        regex_filter: str = r"\w",
        **kwargs,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""
        super().__init__(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder=key_placeholder,
            text_after=text_after,
            text_before=text_before,
            regex_filter=regex_filter,
        )
        self.alternation: str = self.create_alternation()
        self.pattern = self.keys_to_pattern()

    def apply_pattern_replacement(self, template_label: str, sport_label: Union[str, Dict[str, str]]) -> str:
        """Replace value placeholder once template is chosen."""
        if not isinstance(sport_label, dict):
            return template_label

        final_label = template_label

        if isinstance(sport_label, dict):
            for key, val in sport_label.items():
                if isinstance(val, str) and val:
                    final_label = final_label.replace(f"{{{key}}}", val)

        # if any(f"{key}" in final_label for key in sport_label.keys()):
        #     logger.warning(f"Not all placeholders replaced in {final_label=}, {sport_label=}")
        #     # If not all placeholders were replaced, we can choose to either
        #     # leave the label as is or apply some default behavior.
        #     # For now, we'll just log a warning and return the label.
        #     return ""

        return final_label.strip()

    def replace_value_placeholder(self, label: str, value: Union[str, Dict[str, str]]) -> str:
        """
        Used in MultiDataFormatterBaseV2 / MultiDataFormatterBaseHelpers
        """
        if not isinstance(value, dict):
            return label

        final_label = label
        for key, val in value.items():
            if isinstance(val, str) and val:
                final_label = final_label.replace(f"{{{key}}}", val)

        # if any(f"{key}" in final_label for key in value.keys()):
        #     logger.warning(f"Not all placeholders replaced in {final_label=}, {value=}")
        #     # If not all placeholders were replaced, we can choose to either
        #     # leave the label as is or apply some default behavior.
        #     # For now, we'll just log a warning and return the label.
        #     return ""

        return final_label
