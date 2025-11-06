"""
Usage:

from .make2_bots.date_bots.yearly_translator import YearlyCategoryTranslator
yearly_translator_bot = YearlyCategoryTranslator()
# ---
cat_year, from_year = yearly_translator_bot.get_translation_from_year(category_r)
if from_year:
    category_lab = from_year
# ---
...
get lab
...
# ---
if not from_year and cat_year:
    yearly_translator_bot.add_translation_for_year(category_r, category_lab, cat_year)
# ---

"""

import re
from ...helps.print_bot import output_main


class YearlyCategoryTranslator:
    def __init__(self):
        self.labs_done = {1: 0}
        self.cats_labels = {}

    def get_translation_from_year(self, category_r: str) -> tuple:
        """
        Given a string `category_r` representing a category, this function extracts the year from the category and returns a tuple containing the extracted year and the corresponding category key. If no year is found in the category, an empty string and an empty string are returned.

        Parameters:
        - `category_r` (str): The category from which to extract the year.

        Returns:
        - `tuple`: A tuple containing the extracted year and the corresponding category key. If no year is found, an empty string and an empty string are returned.
        """
        from_year = ""
        cat_year = ""

        m = re.search(r"\d{4}", category_r)

        if not m:
            return cat_year, from_year

        cat_year = m.group()
        cat_key = category_r.replace(cat_year, "2020")
        cat_key_value = self.cats_labels.get(cat_key)

        if cat_key_value:
            from_year = cat_key_value.replace("2020", cat_year)
            self.labs_done[1] += 1
            output_main(f"<<green>> get_translation_from_year: {self.labs_done[1]}")
            output_main(f"\t<<green>> {category_r=} , {from_year=}")

        return cat_year, from_year

    def add_translation_for_year(self, category_r: str, category_lab: str, cat_year: str) -> None:
        """
        A function that converts the year in category_r and category_lab to "2020" and updates the cats_labels dictionary accordingly.
        Parameters:
            category_r (str): The category from which to update the year.
            category_lab (str): The category from which to update the year.
            cat_year (str): The year to update in the categories.
        Returns:
            None
        """
        if cat_year not in category_lab:
            return

        cat_key = category_r.replace(cat_year, "2020")
        lab_key = category_lab.replace(cat_year, "2020")

        output_main("<<yellow>> add_translation_for_year:")
        output_main(f"\t<<yellow>> {cat_key=} , {lab_key=}")

        self.cats_labels[cat_key] = lab_key


yearly_translator = YearlyCategoryTranslator()

get_translation_from_year = yearly_translator.get_translation_from_year
add_translation_for_year = yearly_translator.add_translation_for_year
