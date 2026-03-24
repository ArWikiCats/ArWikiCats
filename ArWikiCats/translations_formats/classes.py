

from dataclasses import dataclass, field


@dataclass
class CountryBotConfig:
    """Configuration for the country/nationality part of the formatter."""

    formatted_data: dict[str, str]
    data_list: dict[str, str]
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
class PlaceHolderConfig:
    """Configuration for """
    key_placeholder: str = "{}"
    value_placeholder: str = "{}"
