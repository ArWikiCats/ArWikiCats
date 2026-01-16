#!/usr/bin/python3
"""
Usage:
from .bot_lab import label_for_startwith_year_or_typeo

"""

import re

from ...fix import fixtitle
from ...format_bots.relation_mapping import translation_category_relations
from ...helps import logger
from ...new_resolvers.reslove_all import new_resolvers_all
from ...time_resolvers import time_to_arabic
from ...translations import Nat_mens
from ..ma_bots.country_bot import get_country
from ..make_bots.bot_2018 import get_pop_All_18
from .reg_result import get_cats, get_reg_result


def get_country_label(country_lower: str, country_not_lower: str, cate3: str, compare_lab: str) -> str:
    """Resolve a country label using population tables and fallbacks."""
    country_label = ""

    if country_lower:
        country_label = get_pop_All_18(country_lower, "")

        if not country_label:
            country_label = get_country(country_not_lower)

        if country_label == "" and cate3 == compare_lab:
            country_label = Nat_mens.get(country_lower, "")
            if country_label:
                country_label = country_label + " في"
                logger.info(f"a<<lightblue>>>2021 cnt_la == {country_label=}")

    return country_label


class LabelForStartWithYearOrTypeo:
    def __init__(self) -> None:
        """Set up placeholders used while constructing category labels."""
        self.cate = ""
        self.cate3 = ""
        self.year_at_first = ""
        self.In = ""
        self.country = ""
        self.country_lower = ""
        self.country_not_lower = ""
        self.cat_test = ""
        self.category_r = ""

        self.arlabel = ""
        self.suf = ""
        self.year_labe = ""

        self.country_label = ""
        self.Add_In = True
        self.Add_In_Done = False
        self.NoLab = False

    # ----------------------------------------------------
    # HELPERS
    # ----------------------------------------------------

    @staticmethod
    def replace_cat_test(cat_test: str, text: str) -> str:
        """Remove a substring from the category test helper in a case-insensitive way."""
        return cat_test.lower().replace(text.lower().strip(), "")

    # ----------------------------------------------------
    # 1 — PARSE
    # ----------------------------------------------------

    def parse_input(self, category_r: str) -> None:
        """Extract base components (year, type, country) from the category."""
        self.category_r = category_r

        self.cate, self.cate3 = get_cats(category_r)
        result = get_reg_result(category_r)

        self.year_at_first = result.year_at_first
        self.In = result.In
        self.country = result.country
        self.cat_test = result.cat_test

        self.country_lower = self.country.lower()
        self.country_not_lower = self.country

        logger.debug(f'>>>> {self.year_at_first=}, "{self.In=}, {self.country=}, {self.cat_test=}')

    # ----------------------------------------------------
    # 3 — HANDLE COUNTRY
    # ----------------------------------------------------

    def handle_country(self) -> None:
        """Look up and store the country label derived from the category."""
        if not self.country_lower:
            return

        cmp = self.year_at_first.strip() + " " + self.country_lower

        self.country_label = new_resolvers_all(self.country_lower) or get_country_label(
            self.country_lower, self.country_not_lower, self.cate3, cmp
        )

        if self.country_label:
            self.cat_test = self.replace_cat_test(self.cat_test, self.country_lower)
            logger.info(f"a<<lightblue>>> {self.country_label=}, {self.cate3=}")

    # ----------------------------------------------------
    # 4 — HANDLE YEAR
    # ----------------------------------------------------

    def handle_year(self) -> None:
        """Append year-based labels and mark prepositions when needed."""
        if not self.year_at_first:
            return

        self.year_labe = time_to_arabic.convert_time_to_arabic(self.year_at_first)

        if not self.year_labe:
            logger.info(f"No label for year_at_first({self.year_at_first}), {self.arlabel=}")
            return

        self.cat_test = self.replace_cat_test(self.cat_test, self.year_at_first)
        self.arlabel += " " + self.year_labe

        logger.info(
            f'252: year_at_first({self.year_at_first}) != "" arlabel:"{self.arlabel}",In.strip() == "{self.In.strip()}"'
        )

        if (self.In.strip() in ("in", "at")) and not self.suf.strip():
            logger.info(f"Add في to arlabel:in, at: {self.arlabel}")

            self.arlabel += " في "
            self.cat_test = self.replace_cat_test(self.cat_test, self.In)
            self.Add_In = False
            self.Add_In_Done = True

    # ----------------------------------------------------
    # 5 — RELATION MAPPING
    # ----------------------------------------------------

    def handle_relation_mapping(self) -> None:
        """Remove relation keywords that have already influenced the label."""
        if not self.In.strip():
            return

        if self.In.strip() in translation_category_relations:
            if translation_category_relations[self.In.strip()].strip() in self.arlabel:
                self.cat_test = self.replace_cat_test(self.cat_test, self.In)
        else:
            self.cat_test = self.replace_cat_test(self.cat_test, self.In)

        self.cat_test = re.sub(r"category:", "", self.cat_test)

        logger.debug(f'<<lightblue>>>>>> cat_test: "{self.cat_test}" ')

    # ----------------------------------------------------
    # 6 — APPLY LABEL RULES
    # ----------------------------------------------------

    def apply_label_rules(self) -> None:
        """Apply validation rules and build labels using available data."""

        if self.year_at_first and not self.year_labe:
            self.NoLab = True
            logger.info('year_labe = ""')
            return

        if (not self.year_at_first or not self.year_labe) and self.cat_test.strip():
            self.NoLab = True
            logger.info('year_at_first ==  or year_labe == ""')
            return

        if not self.country_lower and not self.In:
            logger.info('a<<lightblue>>>>>> country_lower == "" and In ==  "" ')
            if self.suf:
                self.arlabel = self.arlabel + " " + self.suf
            self.arlabel = re.sub(r"\s+", " ", self.arlabel)
            logger.debug("a<<lightblue>>>>>> No country_lower.")
            return

        logger.info(f"a<<lightblue>>>>>> No label., {self.country_lower=}")
        self.NoLab = True

    # ----------------------------------------------------
    # 8 — FINALIZE
    # ----------------------------------------------------

    def finalize(self) -> str:
        """Perform final validation and return the completed label."""
        if not self.arlabel:
            return ""

        category2 = (
            self.cate[len("category:") :].lower() if self.cate.lower().startswith("category:") else self.cate.lower()
        )

        if not self.cat_test.strip():
            logger.debug("<<lightgreen>>>>>> arlabel " + self.arlabel)

        elif self.cat_test == self.country_lower or self.cat_test == ("in " + self.country_lower):
            logger.debug("<<lightgreen>>>>>> cat_test False.. ")
            logger.debug(f"<<lightblue>>>>>> cat_test = {self.country_lower=} ")
            self.NoLab = True

        elif self.cat_test.lower() == category2.lower():
            logger.debug("<<lightblue>>>>>> cat_test = category2 ")

        else:
            logger.debug("<<lightgreen>>>> >> cat_test False result.. ")
            logger.debug(f" {self.cat_test=} ")
            logger.debug("<<lightgreen>>>>>> arlabel " + self.arlabel)
            self.NoLab = True

        logger.debug("<<lightgreen>>>>>> arlabel " + self.arlabel)

        if not self.NoLab:
            if re.sub("[abcdefghijklmnopqrstuvwxyz]", "", self.arlabel, flags=re.IGNORECASE) == self.arlabel:
                self.arlabel = fixtitle.fixlabel(self.arlabel, en=self.category_r)

                logger.info(f"a<<lightred>>>>>> arlabel ppoi:{self.arlabel}")
                logger.info(f'>>>> <<lightyellow>> cat:"{self.category_r}", category_lab "{self.arlabel}"')
                logger.info("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")

                return self.arlabel

        return ""

    # ----------------------------------------------------
    # MASTER FUNCTION
    # ----------------------------------------------------

    def build(self, category_r: str) -> str:
        """Construct the final label for categories starting with a year or type."""
        self.parse_input(category_r)

        if not self.year_at_first:
            return ""

        self.handle_country()
        self.handle_year()
        self.handle_relation_mapping()
        self.apply_label_rules()

        return self.finalize()


def label_for_startwith_year_or_typeo(category_r: str) -> str:
    """Return an Arabic label for categories that begin with years or types."""
    builder = LabelForStartWithYearOrTypeo()

    result = ""
    result = builder.build(category_r).strip()
    logger.debug(f":: label_for_startwith_year_or_typeo: {category_r=} => {result=}")
    return result
