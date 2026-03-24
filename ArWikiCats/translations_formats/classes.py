from dataclasses import dataclass, field


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
