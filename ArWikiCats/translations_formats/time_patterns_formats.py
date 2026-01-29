"""
LabsYearsFormat processing module.
"""

import logging
from typing import Callable, Optional

logger = logging.getLogger(__name__)

from ..time_formats.time_to_arabic import (
    convert_time_to_arabic,
    match_time_ar_first,
    match_time_en_first,
)


class MatchTimes:
    """Class for matching time patterns in text."""

    def __init__(self) -> None:
        """
        Initialize a MatchTimes instance.

        This initializer performs no setup and exists to allow subclasses to define their own initialization behavior.
        """
        pass

    def match_en_time(self, text: str) -> str:
        """Match English time in text."""
        result = match_time_en_first(text)
        logger.debug(f"match_en_time: result={result}")
        return result

    def match_ar_time(self, text: str) -> str:
        """Match Arabic time in text."""
        result = match_time_ar_first(text)
        logger.debug(f"match_ar_time: result={result}")
        return result


class LabsYearsFormat(MatchTimes):
    def __init__(
        self,
        category_templates: dict[str, str],
        key_param_placeholder: str = "{year1}",
        value_param_placeholder: str = "{year1}",
        year_param_name: str = "year1",
        fixing_callback: Optional[Callable] = None,
    ) -> None:
        """Prepare reusable lookup tables for year-based category labels."""
        self.lookup_count = 0
        self.category_templates = category_templates
        self.year_param_name = year_param_name
        self.key_param_placeholder = key_param_placeholder
        self.value_param_placeholder = value_param_placeholder
        self.fixing_callback = fixing_callback

    def lab_from_year(self, category_r: str) -> tuple:
        """
        Given a string `category_r` representing a category, this function extracts the year from the category and returns a tuple containing the extracted year and the corresponding category key. If no year is found in the category, an empty string and an empty string are returned.

        Parameters:
        - `category_r` (str): The category from which to extract the year.

        Returns:
        - `tuple`: A tuple containing the extracted year and the corresponding category key. If no year is found, an empty string and an empty string are returned.
        """
        logger.debug(f"start lab_from_year: category_r={category_r}")
        from_year = ""
        cat_year = ""
        category_r = category_r.lower()
        year_match = self.match_en_time(category_r)
        logger.debug(f"lab_from_year matched year: year_match={year_match}")

        if not year_match:
            logger.debug(f"end lab_from_year: no year match found for {category_r}")
            return cat_year, from_year

        cat_year = year_match
        cat_key = category_r.replace(cat_year, self.key_param_placeholder).lower().replace("category:", "").strip()
        logger.debug(f"lab_from_year created key: cat_key={cat_key}")

        cat_year_ar = convert_time_to_arabic(cat_year)
        logger.debug(f"lab_from_year arabic year: cat_year_ar={cat_year_ar}")

        canonical_label = self.category_templates.get(cat_key)
        logger.debug(f"lab_from_year template lookup: canonical_label={canonical_label}")

        if canonical_label and self.value_param_placeholder in canonical_label and cat_year_ar:
            from_year = canonical_label.format_map({self.year_param_name: cat_year_ar})
            logger.debug(f"lab_from_year formatted: from_year={from_year}")

            if self.fixing_callback:
                from_year = self.fixing_callback(from_year)
                logger.debug(f"lab_from_year after callback: from_year={from_year}")

            self.lookup_count += 1
            logger.info(f"<<green>> lab_from_year: {self.lookup_count}, canonical_label={canonical_label}")
            logger.info(f"\t<<green>> category_r={category_r} , from_year={from_year}")

        logger.debug(f"end lab_from_year: category_r={category_r}, cat_year={cat_year}")
        return cat_year, from_year

    def lab_from_year_add(self, category_r: str, category_lab: str, en_year: str, ar_year: str = "") -> bool:
        """
        A function that converts the year in category_r and category_lab to self.key_param_placeholder and updates the category_templates dictionary accordingly.

        Parameters:
            category_r (str): The category from which to update the year.
            category_lab (str): The category from which to update the year.
            en_year (str): The English year to update in the categories.
            ar_year (str): The Arabic year (optional, derived if not provided).
        Returns:
            bool: True if the template was added successfully, False otherwise.
        """
        logger.debug(f"start lab_from_year_add: category_r={category_r}, category_lab={category_lab}")
        category_r = category_r.lower().replace("category:", "").strip()

        if not ar_year:
            category_lab_2 = category_lab.replace("بعقد ", "عقد ")
            ar_year = self.match_ar_time(category_lab_2)
            logger.debug(f"lab_from_year_add matched ar_year: ar_year={ar_year}")

        if not en_year:
            en_year = self.match_en_time(category_r)
            logger.debug(f"lab_from_year_add matched en_year: en_year={en_year}")

        if en_year.isdigit() and not ar_year:
            ar_year = en_year
            logger.debug(f"lab_from_year_add digit fallback: ar_year={ar_year}")

        if not ar_year or ar_year not in category_lab:
            logger.debug(f"lab_from_year_add failed: ar_year={ar_year} not in category_lab")
            return False

        if not en_year or en_year not in category_r:
            logger.debug(f"lab_from_year_add failed: en_year={en_year} not in category_r")
            return False

        cat_key = category_r.replace(en_year, self.key_param_placeholder)
        lab_key = category_lab.replace(ar_year, self.value_param_placeholder)

        logger.debug("<<yellow>> lab_from_year_add logic:")
        logger.debug(f"\t<<yellow>> cat_key={cat_key} , lab_key={lab_key}")

        self.category_templates[cat_key.lower()] = lab_key
        logger.debug(f"end lab_from_year_add: updated templates with {cat_key.lower()}")
        return True
