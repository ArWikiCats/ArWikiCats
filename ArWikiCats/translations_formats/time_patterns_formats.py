"""
LabsYearsFormat processing module.
"""

from typing import Callable, Optional
from ..helps import logger
from ..time_resolvers.time_to_arabic import (
    convert_time_to_arabic,
    match_time_ar_first,
    match_time_en_first,
)


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
        logger.debug(f"start lab_from_year: {category_r=}")
        from_year = ""
        cat_year = ""
        category_r = category_r.lower()
        year_match = self.match_en_time(category_r)

        if not year_match:
            logger.debug(f" end lab_from_year: {category_r=}, {cat_year=}")
            return cat_year, from_year

        cat_year = year_match
        cat_key = category_r.replace(cat_year, self.key_param_placeholder).lower().replace("category:", "").strip()

        cat_year_ar = convert_time_to_arabic(cat_year)

        canonical_label = self.category_templates.get(cat_key)

        if canonical_label and self.value_param_placeholder in canonical_label and cat_year_ar:

            from_year = canonical_label.format_map(
                {self.year_param_name: cat_year_ar}
            )

            if self.fixing_callback:
                from_year = self.fixing_callback(from_year)

            self.lookup_count += 1
            logger.info(f"<<green>> lab_from_year: {self.lookup_count}, {canonical_label=}")
            logger.info(f"\t<<green>> {category_r=} , {from_year=}")

        logger.debug(f"end lab_from_year: {category_r=}, {cat_year=}")
        return cat_year, from_year

    def lab_from_year_add(self, category_r: str, category_lab: str, en_year: str, ar_year: str = "") -> bool:
        """
        A function that converts the year in category_r and category_lab to self.key_param_placeholder and updates the category_templates dictionary accordingly.
        Parameters:
            category_r (str): The category from which to update the year.
            category_lab (str): The category from which to update the year.
            cat_year (str): The year to update in the categories.
        Returns:
            None
        """
        category_r = category_r.lower().replace("category:", "").strip()
        if not ar_year:
            category_lab_2 = category_lab.replace("بعقد ", "عقد ")
            ar_year = self.match_ar_time(category_lab_2)

        if not en_year:
            en_year = self.match_en_time(category_r)

        if en_year.isdigit() and not ar_year:
            ar_year = en_year

        if not ar_year or ar_year not in category_lab:
            return False

        if not en_year or en_year not in category_r:
            return False

        cat_key = category_r.replace(en_year, self.key_param_placeholder)
        lab_key = category_lab.replace(ar_year, self.value_param_placeholder)

        logger.debug("<<yellow>> lab_from_year_add:")
        logger.debug(f"\t<<yellow>> {cat_key=} , {lab_key=}")

        self.category_templates[cat_key.lower()] = lab_key
        return True
