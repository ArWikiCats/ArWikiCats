from dataclasses import dataclass, field
from typing import Any


@dataclass
class TranslationPair:
    """Represents a single English-Arabic translation pair.

    Attributes:
        en: The English key/label.
        ar: The Arabic translation.
        category: Optional category for classification (e.g., "geo", "sports", "jobs").
        metadata: Additional metadata (not used in comparisons).
    """

    en: str
    ar: str
    category: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict, compare=False, repr=False)


@dataclass
class FormatBotConfig:
    """Unified configuration for format bots.

    Attributes:
        nat_data_list: Data list for country/nationality formatter.
        nat_formatted_data: Formatted data for country/nationality formatter.
        second_data_list: Data list for second element (sport/year/genre) formatter.
        second_formatted_data: Formatted data for second element formatter.
        first_placeholder: Placeholder for the first element (default: "{nat}").
        second_placeholder: Placeholder for the second element (default: "{sport}").
        value_placeholder: Generic value placeholder (default: "{value}").
        search_first_part: If True, search using only the first part.
        other_key_first: If True, process second element before first.
        add_prefix: If True, add Arabic category prefix.
        regex_filter: Optional regex filter for filtering keys.
    """

    nat_data_list: dict[str, str] = field(default_factory=dict)
    nat_formatted_data: dict[str, str] = field(default_factory=dict)
    second_data_list: dict[str, str] = field(default_factory=dict)
    second_formatted_data: dict[str, str] = field(default_factory=dict)
    first_placeholder: str = "{nat}"
    second_placeholder: str = "{sport}"
    value_placeholder: str = "{value}"
    search_first_part: bool = False
    other_key_first: bool = False
    add_prefix: bool = True
    regex_filter: str | None = None


@dataclass
class CountryBotConfig:
    """Configuration for the country/nationality part of the formatter."""

    data_list: dict[str, str]
    formatted_data: dict[str, str]
    key_placeholder: str = "{nat_en}"
    value_placeholder: str = "{nat_ar}"
    text_after: str = ""
    text_before: str = ""


@dataclass
class GenreBotConfig:
    """Configuration for the genre/film_key part of the formatter."""

    data_list: dict[str, str] = field(default_factory=dict)
    formatted_data: dict[str, str] = field(default_factory=dict)
    key_placeholder: str = "{film_key}"
    value_placeholder: str = "{film_ar}"


@dataclass
class YearDataConfig:
    """Configuration for the year part in year-country formatters."""

    key_placeholder: str = "{year1}"
    value_placeholder: str = "{year1}"


@dataclass
class MultiDataFormatterSecondElementConfig:
    """Configuration for the second element (e.g., sport/year) in multi-data formatters."""

    data_list: dict[str, str] = field(default_factory=dict)
    formatted_data: dict[str, str] = field(default_factory=dict)
    key_placeholder: str = "xoxo"
    value_placeholder: str = "xoxo"
    text_after: str = ""
    text_before: str = ""
    regex_filter: str | None = None


@dataclass
class MultiDataFormatterConfig:
    """Configuration for the first element (e.g., country/nationality) in multi-data formatters."""

    data_list: dict[str, str]
    formatted_data: dict[str, str]
    key_placeholder: str = "natar"
    value_placeholder: str = "natar"
    text_after: str = ""
    text_before: str = ""
    regex_filter: str | None = None


@dataclass
class YearCountryDataConfig:
    """Configuration for the country/nationality part in year-country formatters."""

    data_list: dict[str, str]
    formatted_data: dict[str, str]
    key_placeholder: str = "{country1}"
    value_placeholder: str = "{country1}"
    text_after: str = ""
    text_before: str = ""


__all__ = [
    "TranslationPair",
    "FormatBotConfig",
    "CountryBotConfig",
    "GenreBotConfig",
    "YearDataConfig",
    "MultiDataFormatterSecondElementConfig",
    "MultiDataFormatterConfig",
    "YearCountryDataConfig",
]
