#!/usr/bin/python3
"""
Module for single-placeholder category translation formatting.

This module provides the FormatData class for translating category strings
using a single key-value placeholder pattern. It is the primary class for
simple category translations where one dynamic element (e.g., sport name,
nationality) needs to be replaced with its Arabic equivalent.

Classes:
    FormatData: Handles single-placeholder template-driven category translations.

Real world example:

formatted_data = {
    "{sport} players": "لاعبو {sport_label}",
    "{sport} coaches": "مدربو {sport_label}",
}
data_list = {
    "football": "كرة القدم",
    "basketball": "كرة السلة",
}
bot = FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")
result = bot.search("football players")
assert result == "لاعبو كرة القدم"

"""

import logging
from typing import Dict

from .model_data_base import FormatDataBase

logger = logging.getLogger(__name__)


class FormatData(FormatDataBase):
    """
    Handles single-placeholder template-driven category translations.

    This class extends FormatDataBase to provide functionality for translating
    category strings where a single dynamic element needs to be replaced. It
    uses regex pattern matching to find keys in input categories and replaces
    them with their Arabic equivalents using template strings.

    Attributes:
        formatted_data (Dict[str, str]): Template patterns mapping English patterns to Arabic templates.
        data_list (Dict[str, str]): Key-to-Arabic-label mappings for replacements.
        key_placeholder (str): Placeholder used in formatted_data keys (e.g., "{sport}").
        value_placeholder (str): Placeholder used in formatted_data values (e.g., "{sport_label}").
        text_after (str): Optional text that appears after the key in patterns.
        text_before (str): Optional text that appears before the key in patterns.
        regex_filter (str): Regex pattern for word boundary detection.

    Example:
        >>> bot = FormatData(
        ...     formatted_data={"{sport} players": "لاعبو {sport_label}"},
        ...     data_list={"football": "كرة القدم"},
        ...     key_placeholder="{sport}",
        ...     value_placeholder="{sport_label}",
        ... )
        >>> bot.search("football players")
        'لاعبو كرة القدم'
    """

    def __init__(
        self,
        formatted_data: Dict[str, str],
        data_list: Dict[str, str],
        key_placeholder: str = "xoxo",
        value_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",
        regex_filter: str = "",
    ) -> None:
        """
        Initialize a FormatData instance for single-placeholder, template-driven translations.

        Parameters:
            formatted_data: Mapping of template keys to Arabic template strings that include the value placeholder.
            data_list: Mapping of source keys (e.g., English terms) to their replacement labels (e.g., Arabic labels).
            key_placeholder: Placeholder string used inside template keys to mark the dynamic element to match.
            value_placeholder: Placeholder string used inside template values to mark where the replacement label will be inserted.
            text_after: Optional text that must follow the matched key when building match patterns.
            text_before: Optional text that must precede the matched key when building match patterns.
            regex_filter: Optional regular expression used to constrain or filter matched keys.
        """
        super().__init__(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder=key_placeholder,
            text_after=text_after,
            text_before=text_before,
            regex_filter=regex_filter,
        )
        self.value_placeholder = value_placeholder
        self.alternation: str = self.create_alternation()
        self.pattern = self.keys_to_pattern()

    def apply_pattern_replacement(self, template_label: str, sport_label: str) -> str:
        """
        Format the given template by replacing the instance of the value placeholder with the provided value.

        Parameters:
            template_label (str): Template string expected to contain `self.value_placeholder`.
            sport_label (str): Replacement text to substitute for the value placeholder.

        Returns:
            str: The formatted label with the placeholder replaced and surrounding whitespace trimmed if the placeholder was successfully removed; an empty string if the placeholder still remains.
        """
        final_label = template_label.replace(self.value_placeholder, sport_label)

        if self.value_placeholder not in final_label:
            return final_label.strip()

        return ""

    def replace_value_placeholder(self, label: str, value: str) -> str:
        """
        Replace the instance's configured value placeholder in a label with the provided value.

        Parameters:
            label (str): The text containing the value placeholder to be replaced.
            value (str): The string to substitute for the value placeholder.

        Returns:
            str: The label with the value placeholder replaced by `value`.
        """
        logger.debug(f"!!!! replace_value_placeholder: {self.value_placeholder=}, {label=}, {value=}")
        # Replace placeholder
        return label.replace(self.value_placeholder, value)


def format_data_sample() -> bool:
    """
    This function demonstrates how to use the FormatData class to format and transform data.
    It creates a mapping of template patterns to their localized versions and applies them.
    """
    # Define a dictionary of formatted patterns with placeholders
    formatted_data = {
        "{sport}": "{sport_label}",
        "{sport} managers": "مدربو {sport_label}",
        "{sport} coaches": "مدربو {sport_label}",
        "{sport} people": "أعلام {sport_label}",
        "{sport} playerss": "لاعبو {sport_label}",
        "{sport} players": "لاعبو {sport_label}",
        "men's {sport} matches": "مباريات {sport_label} رجالية",
        "men's {sport} navigational boxes": "صناديق تصفح {sport_label} رجالية",
        "men's {sport} lists": "قوائم {sport_label} رجالية",
        "amateur {sport} home stadiums": "ملاعب {sport_label} للهواة",
        "amateur {sport} templates": "قوالب {sport_label} للهواة",
        "amateur {sport} rivalries": "دربيات {sport_label} للهواة",
        "amateur {sport} receivers": "مستقبلو {sport_label} للهواة",
        "amateur {sport} wide receivers": "مستقبلون واسعون {sport_label} للهواة",
        "amateur {sport} tackles": "مصطدمو {sport_label} للهواة",
        "amateur {sport} utility players": "لاعبو مراكز متعددة {sport_label} للهواة",
    }

    # Define a dictionary with actual sport name mappings
    data_list = {
        "gridiron football": "كرة قدم أمريكية شمالية",
        "american football": "كرة قدم أمريكية",
        "canadian football": "كرة قدم كندية",
        "wheelchair australian rules football": "كرة قدم أسترالية على كراسي متحركة",
        "volleyball racing": "سباق كرة طائرة",
        "wheelchair volleyball": "كرة طائرة على كراسي متحركة",
        "middle-distance running racing": "سباق ركض مسافات متوسطة",
        "wheelchair gaelic football": "كرة قدم غالية على كراسي متحركة",
        "kick boxing racing": "سباق كيك بوكسينغ",
        "wheelchair cycling road race": "سباق دراجات على الطريق على كراسي متحركة",
        "wheelchair auto racing": "سباق سيارات على كراسي متحركة",
    }

    # Create a FormatData instance with the defined patterns and mappings
    bot = FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")

    # Search for a specific pattern and get its localized version
    label = bot.search("american football players")
    # Verify if the result matches the expected output
    result = label == "لاعبو كرة قدم أمريكية"

    # Return the formatted label
    return result
