"""
Usage:

from .make2_bots.date_bots.labs_years import LabsYears
labs_years_bot = LabsYears()
# ---
cat_year, from_year = labs_years_bot.lab_from_year(category_r)
if from_year:
    category_lab = from_year
# ---
...
get lab
...
# ---
if not from_year and cat_year:
    labs_years_bot.lab_from_year_add(category_r, category_lab, cat_year)
# ---

"""

import re

from ..helps.log import logger
from ..new.time_to_arabic import (
    convert_time_to_arabic,
    match_time_ar_first,
    match_time_en_first,
)
from .categories_patterns.YEAR_PATTERNS import YEAR_DATA, YEAR_PARAM_NAME

YEAR_PARAM = "{year1}"


class MatchTimes:
    def __init__(self) -> None:
        pass

    def match_en_time(self, text: str) -> str:
        """Match English time in text."""
        # year_match = re.search(r"\d{4}", text)
        # if year_match: return year_match.group()
        result = match_time_en_first(text)
        logger.debug(f"match_en_time: {result=}")
        return result

    def match_ar_time(self, text: str) -> str:
        """Match Arabic time in text."""
        result = match_time_ar_first(text)
        logger.debug(f"match_ar_time: {result=}")
        return result

    def fixing(self, text: str) -> str:
        """Fix text."""
        text = re.sub(r"(انحلالات|تأسيسات)\s*سنة\s*(عقد|القرن|الألفية)", r"\g<1> \g<2>", text)
        return text


class LabsYears(MatchTimes):
    def __init__(self) -> None:
        """Prepare reusable lookup tables for year-based category labels."""
        self.lookup_count = 0
        self.category_templates = dict(YEAR_DATA)
        self.category_templates.update(
            {
                f"category:{YEAR_PARAM}": f"تصنيف:{YEAR_PARAM}",
                f"category:films in {YEAR_PARAM}": f"تصنيف:أفلام في {YEAR_PARAM}",
                f"category:{YEAR_PARAM} films": f"تصنيف:أفلام إنتاج {YEAR_PARAM}",
            }
        )

    def lab_from_year(self, category_r: str) -> tuple:
        """
        Given a string `category_r` representing a category, this function extracts the year from the category and returns a tuple containing the extracted year and the corresponding category key. If no year is found in the category, an empty string and an empty string are returned.

        Parameters:
        - `category_r` (str): The category from which to extract the year.

        Returns:
        - `tuple`: A tuple containing the extracted year and the corresponding category key. If no year is found, an empty string and an empty string are returned.
        """
        from_year = ""
        cat_year = ""
        category_r = category_r.lower()
        year_match = self.match_en_time(category_r)

        if not year_match:
            return cat_year, from_year

        cat_year = year_match
        cat_key = category_r.replace(cat_year, YEAR_PARAM)

        cat_year_ar = ""
        if cat_year.isdigit():
            cat_year_ar = cat_year
        else:
            cat_year_ar = convert_time_to_arabic(cat_year)

        canonical_label = self.category_templates.get(cat_key)

        if canonical_label and YEAR_PARAM in canonical_label and cat_year_ar:
            from_year = canonical_label.format_map({YEAR_PARAM_NAME: cat_year_ar})
            from_year = self.fixing(from_year)
            self.lookup_count += 1
            logger.info(f"<<green>> lab_from_year: {self.lookup_count}")
            logger.info(f"\t<<green>> {category_r=} , {from_year=}")

        return cat_year, from_year

    def lab_from_year_add(self, category_r: str, category_lab: str, en_year: str, ar_year: str = "") -> None:
        """
        A function that converts the year in category_r and category_lab to YEAR_PARAM and updates the category_templates dictionary accordingly.
        Parameters:
            category_r (str): The category from which to update the year.
            category_lab (str): The category from which to update the year.
            cat_year (str): The year to update in the categories.
        Returns:
            None
        """
        if not ar_year:
            ar_year = self.match_ar_time(category_lab)

        if en_year.isdigit() and not ar_year:
            ar_year = en_year

        if not ar_year or ar_year not in category_lab:
            return

        cat_key = category_r.replace(en_year, YEAR_PARAM)
        lab_key = category_lab.replace(ar_year, YEAR_PARAM)

        logger.debug("<<yellow>> lab_from_year_add:")
        logger.debug(f"\t<<yellow>> {cat_key=} , {lab_key=}")

        self.category_templates[cat_key.lower()] = lab_key
