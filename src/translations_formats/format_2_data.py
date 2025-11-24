#!/usr/bin/python3
""" """

import functools
from typing import Dict

from ..helps.log import logger
from .format_data import FormatData


class FormatComparisonHelper:
    def __init__(self):
        ...

    def get_start_p17(self, cate):
        new_category = self.normalize_nat_label(cate)
        key = self.nat_bot.match_key(cate)
        return new_category, key


class FormatMultiData(FormatComparisonHelper):
    def __init__(
        self,
        formated_data: Dict[str, str],
        data_list: Dict[str, str],
        key_placeholder: str = "natar",
        value_placeholder: str = "natar",
        data_list2: Dict[str, str] = {},
        key2_placeholder: str = "xoxo",
        value2_placeholder: str = "xoxo",
        text_after: str = "",
        text_before: str = "",

    ) -> None:
        """Prepare helpers for matching and formatting template-driven labels."""
        # Store originals
        self.formated_data = formated_data

        self.value_placeholder = value_placeholder
        self.key_placeholder = key_placeholder

        self.value2_placeholder = value2_placeholder
        self.key2_placeholder = key2_placeholder

        self.nat_bot = FormatData(
            self.formated_data,
            data_list,
            key_placeholder=self.key_placeholder,
            value_placeholder=self.value_placeholder,
            text_after=text_after,
            text_before=text_before
        )

        self.sport_bot = FormatData(
            {},
            data_list2,
            key_placeholder=self.key2_placeholder,
            value_placeholder=self.value2_placeholder
        )

        # @dump_data(enable=True)

    def normalize_nat_label(self, category):
        """
        Normalize nationality placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "natar national football teams"
        """
        key = self.nat_bot.match_key(category)
        result = ""
        if key:
            result = self.nat_bot.normalize_category(category, key)
        return result

    def normalize_sport_label(self, category):
        """
        Normalize sport placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "Yemeni national xoxo teams"
        """
        key = self.sport_bot.match_key(category)
        result = ""
        if key:
            result = self.sport_bot.normalize_category(category, key)
        return result

    def normalize_both(self, category):
        """
        Normalize both nationality and sport tokens in the category.

        Example:
            input: "british softball championshipszz", output: "natar xoxo championshipszz"
        """
        new_category = self.normalize_nat_label(category)
        new_category = self.normalize_sport_label(new_category)

        return new_category

    @functools.lru_cache(maxsize=1000)
    def create_nat_label(self, category):
        return self.nat_bot.search(category)

    @functools.lru_cache(maxsize=1000)
    def create_label(self, category):
        """
        Create a localized label by combining nationality and sport templates.

        Example:
            category: "ladies british softball tour", output: "بطولة المملكة المتحدة للكرة اللينة للسيدات"
        """
        # category = Yemeni football championships
        template_label = self.normalize_both(category)

        nationality_key = self.nat_bot.match_key(category)

        if not nationality_key:
            return ""

        category2 = self.nat_bot.normalize_category(category, nationality_key)

        xoxo_key = self.sport_bot.match_key(category2)

        if not self.formated_data.get(template_label):
            return ""

        # cate = natar xoxo championships
        template_ar = self.formated_data[template_label]
        logger.debug(f"{template_ar=}")

        sport_label = self.sport_bot.get_key_label(xoxo_key)
        nationality_label = self.nat_bot.get_key_label(nationality_key)

        if not nationality_label or not sport_label:
            return ""

        label = template_ar.replace(self.value_placeholder, nationality_label).replace(self.value2_placeholder, sport_label)

        logger.debug(f"{label=}")

        return label
