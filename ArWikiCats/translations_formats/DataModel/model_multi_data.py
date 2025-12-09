#!/usr/bin/python3
"""
Provides classes for formatting template-driven translation labels.
- format_multi_data: Handles complex formatting involving two sets of data lists (e.g., nationality and sport).

test at tests.translations_formats.test_format_2_data.py
"""

import functools
from dataclasses import dataclass

from .model_data_2 import FormatDataV2
from ...helps.log import logger
from .model_data import FormatData
from .model_data_time import YearFormatData
from .model_data_double import FormatDataDouble

# -----------------------
#
# -----------------------


@dataclass
class NormalizeResult:
    """Data structure representing each processed category."""

    template_key_first: str
    category: str
    template_key: str
    nat_key: str
    other_key: str


class MultiDataFormatterBaseHelpers:
    def __init__(self) -> None:
        pass
    # ------------------------------------------------------
    # COUNTRY/NAT NORMALIZATION
    # ------------------------------------------------------

    def normalize_nat_label(self, category: str) -> str:
        """
        Normalize nationality placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "natar national football teams"
        """
        key, new_category = self.country_bot.normalize_category_with_key(category)
        return new_category

    # ------------------------------------------------------
    # YEAR/SPORT NORMALIZATION
    # ------------------------------------------------------
    def normalize_other_label(self, category: str) -> str:
        """
        Normalize sport placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "Yemeni national xoxo teams"
        """
        key, new_category = self.other_bot.normalize_category_with_key(category)
        return new_category

    def normalize_both_new(self, category: str) -> NormalizeResult:
        """
        Normalize both nationality and sport tokens in the category.

        Example:
            input: "british softball championshipszz", output: "natar xoxo championshipszz"
        """
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        nat_key, template_key_first = self.country_bot.normalize_category_with_key(normalized_category)
        other_key, template_key = self.other_bot.normalize_category_with_key(template_key_first)

        return NormalizeResult(
            template_key_first=template_key_first,
            category=normalized_category,
            template_key=template_key,
            nat_key=nat_key,
            other_key=other_key,
        )

    def normalize_both(self, category: str) -> str:
        """
        Normalize both nationality and sport tokens in the category.

        Example:
            input: "british softball championshipszz", output: "natar xoxo championshipszz"
        """
        # Normalize the category by removing extra spaces
        normalized_category = " ".join(category.split())

        nat_key, template_key = self.country_bot.normalize_category_with_key(normalized_category)
        other_key, template_key = self.other_bot.normalize_category_with_key(template_key)

        return template_key

    @functools.lru_cache(maxsize=2000)
    def create_nat_label(self, category: str) -> str:
        return self.country_bot.search(category)

    def replace_placeholders(self, template_ar: str, country_ar: str, other_ar: str) -> str:
        label = self.country_bot.replace_value_placeholder(template_ar, country_ar)
        label = self.other_bot.replace_value_placeholder(label, other_ar)

        return label.strip()

    @functools.lru_cache(maxsize=1000)
    def create_label(self, category: str) -> str:
        """
        Create a localized label by combining nationality and sport templates.

        Example:
            category: "ladies british softball tour", output: "بطولة المملكة المتحدة للكرة اللينة للسيدات"
        """
        # category = Yemeni football championships
        template_data = self.normalize_both_new(category)

        logger.debug(f">>>create_label {template_data.nat_key=}, {template_data.other_key=}")
        # print(f"{template_data.template_key_first=}, {template_data.template_key=}\n"*20)

        if not template_data.nat_key or not template_data.other_key:
            return ""

        template_ar_first = self.country_bot.get_template_ar(template_data.template_key_first)
        template_ar = self.country_bot.get_template_ar(template_data.template_key)

        logger.debug(f">>>create_label {template_ar=}, {template_ar_first=}")

        if self.search_first_part and template_ar_first:
            return self.country_bot.search(category)

        # Get Arabic equivalents
        country_ar = self.country_bot.get_key_label(template_data.nat_key)
        other_ar = self.other_bot.get_key_label(template_data.other_key)

        logger.debug(f">>>create_label {country_ar=}, {other_ar=}")
        if not country_ar or not other_ar:
            return ""

        # Replace placeholders
        label = self.replace_placeholders(template_ar, country_ar, other_ar)

        logger.debug(f">>>create_label Translated {category=} → {label=}")
        return label

    def search(self, category: str) -> str:
        return self.create_label(category)

    def search_all(self, category: str) -> str:
        return self.create_label(category) \
            or self.country_bot.search(category) \
            or self.other_bot.search(category)


class MultiDataFormatterBase(MultiDataFormatterBaseHelpers):
    """
    Handles complex formatting involving two sets of data lists (e.g.,
    nationality and sport, or country and year). It orchestrates two
    formatter instances (`FormatData` or `YearFormatData`) to normalize
    and translate category strings.
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: FormatData,
        search_first_part: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        # Country bot (FormatData)
        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot


class MultiDataFormatterBaseYear(MultiDataFormatterBaseHelpers):
    """
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: YearFormatData,
        search_first_part: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot


class MultiDataFormatterBaseYearV2(MultiDataFormatterBaseHelpers):
    """
    """

    def __init__(
        self,
        country_bot: FormatDataV2,
        other_bot: YearFormatData,
        search_first_part: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot


class MultiDataFormatterDataDouble(MultiDataFormatterBaseHelpers):
    """
    Handles complex formatting involving two sets of data lists (e.g.,
    nationality and sport, or country and year). It orchestrates two
    formatter instances (`FormatData` or `YearFormatData`) to normalize
    and translate category strings.
    """

    def __init__(
        self,
        country_bot: FormatData,
        other_bot: FormatDataDouble,
        search_first_part: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot


class MultiDataFormatterBaseV2(MultiDataFormatterBaseHelpers):
    """
    """

    def __init__(
        self,
        country_bot: FormatDataV2,
        other_bot: FormatDataV2,
        search_first_part: bool = False,
    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""

        self.search_first_part = search_first_part
        self.country_bot = country_bot
        self.other_bot = other_bot
