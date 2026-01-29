"""
Package for Arabic Wikipedia category translation formatting.

This package provides classes and factory functions for translating English
Wikipedia category names to Arabic using template-driven pattern matching.
It supports various translation scenarios including:

- **Single-element translations**: Categories with one dynamic element (e.g., sport name)
- **Dual-element translations**: Categories with two dynamic elements (e.g., nationality + sport)
- **Year-based translations**: Categories with temporal patterns (e.g., "14th-century")
- **Double-key translations**: Categories with adjacent keys (e.g., "action drama films")

Main Classes (from DataModel):
    FormatData: Single-placeholder template translations
    FormatDataV2: Dictionary-based template translations
    FormatDataDouble: Double-key pattern matching
    YearFormatData: Year/decade/century pattern handling
    MultiDataFormatterBase: Combines two FormatData instances
    MultiDataFormatterBaseV2: Combines two FormatDataV2 instances
    MultiDataFormatterBaseYear: Combines FormatData with YearFormatData
    MultiDataFormatterBaseYearV2: Combines FormatDataV2 with YearFormatData
    MultiDataFormatterDataDouble: Combines FormatData with FormatDataDouble
    MultiDataFormatterYearAndFrom: Year + "from" relation translations
    FormatDataFrom: Callback-based format handling
    NormalizeResult: Dataclass for normalization results

Factory Functions:
    format_multi_data: Creates MultiDataFormatterBase from parameters
    format_multi_data_v2: Creates MultiDataFormatterBaseV2 from parameters
    format_year_country_data: Creates MultiDataFormatterBaseYear from parameters
    format_year_country_data_v2: Creates MultiDataFormatterBaseYearV2 from parameters
    format_films_country_data: Creates MultiDataFormatterDataDouble for film categories

Example:
    >>> from ArWikiCats.translations_formats import format_multi_data
    >>> formatted_data = {"{nat} players": "لاعبو {nat_ar}"}
    >>> data_list = {"british": "بريطانيون"}
    >>> data_list2 = {"football": "كرة القدم"}
    >>> bot = format_multi_data(
    ...     formatted_data=formatted_data,
    ...     data_list=data_list,
    ...     data_list2=data_list2,
    ...     key_placeholder="{nat}",
    ...     value_placeholder="{nat_ar}",
    ... )
    >>> bot.search("british football players")
    'لاعبو كرة القدم بريطانيون'
"""

from .data_new_model import format_films_country_data
from .data_with_time import format_year_country_data, format_year_country_data_v2
from .DataModel import (
    FormatData,
    FormatDataFrom,
    FormatDataV2,
    YearFormatData,
)
from .DataModelDouble import (
    FormatDataDouble,
    FormatDataDoubleV2,
    MultiDataFormatterDataDouble,
)
from .DataModelMulti import (
    MultiDataFormatterBase,
    MultiDataFormatterBaseV2,
    MultiDataFormatterBaseYear,
    MultiDataFormatterBaseYearV2,
    MultiDataFormatterYearAndFrom,
    MultiDataFormatterYearAndFrom2,
    NormalizeResult,
)
from .multi_data import format_multi_data, format_multi_data_v2
from .time_patterns_formats import LabsYearsFormat

__all__ = [
    "LabsYearsFormat",
    "MultiDataFormatterBaseYear",
    "MultiDataFormatterBaseYearV2",
    "MultiDataFormatterYearAndFrom",
    "MultiDataFormatterYearAndFrom2",
    "FormatDataFrom",
    "MultiDataFormatterDataDouble",
    "FormatDataV2",
    "FormatDataDouble",
    "FormatDataDoubleV2",
    "YearFormatData",
    "FormatData",
    "NormalizeResult",
    "MultiDataFormatterBase",
    "MultiDataFormatterBaseV2",
    "format_year_country_data",
    "format_year_country_data_v2",
    "format_films_country_data",
    "format_multi_data",
    "format_multi_data_v2",
]
