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
from .categories_patterns.YEAR import YEAR_DATA, YEAR_PARAM


class LabsYears:
    def __init__(self) -> None:
        """Prepare reusable lookup tables for year-based category labels."""
        self.lookup_count = 0
        self.category_templates = YEAR_DATA
        self.category_templates.update(
            {
                f"Category:{YEAR_PARAM}": f"تصنيف:{YEAR_PARAM}",
                f"Category:Films in {YEAR_PARAM}": f"تصنيف:أفلام في {YEAR_PARAM}",
                f"Category:{YEAR_PARAM} Films": f"تصنيف:أفلام إنتاج {YEAR_PARAM}",
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
        year_match = re.search(r"\d{4}", category_r)

        if not year_match:
            return cat_year, from_year

        cat_year = year_match.group()
        cat_key = category_r.replace(cat_year, YEAR_PARAM)

        canonical_label = self.category_templates.get(cat_key)

        if canonical_label and YEAR_PARAM in canonical_label:
            from_year = canonical_label.format(*{YEAR_PARAM: cat_year})
            self.lookup_count += 1
            logger.info(f"<<green>> lab_from_year: {self.lookup_count}")
            logger.info(f"\t<<green>> {category_r=} , {from_year=}")

        return cat_year, from_year

    def lab_from_year_add(self, category_r: str, category_lab: str, cat_year: str) -> None:
        """
        A function that converts the year in category_r and category_lab to YEAR_PARAM and updates the category_templates dictionary accordingly.
        Parameters:
            category_r (str): The category from which to update the year.
            category_lab (str): The category from which to update the year.
            cat_year (str): The year to update in the categories.
        Returns:
            None
        """
        if cat_year not in category_lab:
            return

        cat_key = category_r.replace(cat_year, YEAR_PARAM)
        lab_key = category_lab.replace(cat_year, YEAR_PARAM)

        logger.info("<<yellow>> lab_from_year_add:")
        logger.info(f"\t<<yellow>> {cat_key=} , {lab_key=}")

        self.category_templates[cat_key] = lab_key
