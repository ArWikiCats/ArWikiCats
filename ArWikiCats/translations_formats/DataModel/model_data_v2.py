#!/usr/bin/python3
"""
"""

import re
from typing import Dict, Union

from ...helps.log import logger
from .model_data_base import FormatDataBase
from .model_multi_data_base import MultiDataFormatterBaseHelpers


class FormatDataV2(FormatDataBase):
    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, Union[str, Dict[str, str]]],
        key_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",
        **kwargs,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""
        super().__init__(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder=key_placeholder,
            text_after=text_after,
            text_before=text_before,
        )
        self.alternation: str = self.create_alternation()
        self.pattern = self.keys_to_pattern()

    def apply_pattern_replacement(self, template_label: str, sport_label: Union[str, Dict[str, str]]) -> str:
        """Replace value placeholder once template is chosen."""
        final_label = template_label
        if isinstance(sport_label, dict):
            for key, value in sport_label.items():
                final_label = final_label.replace(f"{{{key}}}", value)

        return final_label.strip()

    def replace_value_placeholder(self, label: str, value: Union[str, Dict[str, str]]) -> str:
        """
        Used in MultiDataFormatterBaseV2 / MultiDataFormatterBaseHelpers
        """
        final_label = label
        if isinstance(value, dict):
            for key, val in value.items():
                final_label = final_label.replace(f"{{{key}}}", val)

        return final_label


class MultiDataFormatterBaseV2(MultiDataFormatterBaseHelpers):
    """
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
