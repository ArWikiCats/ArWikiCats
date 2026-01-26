#!/usr/bin/python3
""" """

import re

from ...fix import fixtitle
from ...format_bots.relation_mapping import translation_category_relations
from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...time_formats import convert_time_to_arabic, match_time_en_first
from ...translations import Nat_mens
from ..circular_dependency import country_bot
from ..make_bots import get_cats, get_reg_result
from .bot_2018 import get_pop_All_18
from .mk3 import new_func_mk2


def resolve_country_label(country_lower: str, country_not_lower: str, cate3: str, compare_lab: str) -> str:
    """Resolve a country label using population tables and fallbacks."""
    country_label = ""

    if country_lower:
        country_label = get_pop_All_18(country_lower, "")

        if not country_label:
            country_label = country_bot.get_country_label(country_not_lower)

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

        country_cleaned = result.country.strip()

        self.year_at_first = result.year_at_first
        self.In = result.In
        self.cat_test = result.cat_test

        self.country = country_cleaned
        self.country_lower = country_cleaned
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

        self.country_label = (
            ""
            or all_new_resolvers(self.country_lower)
            or resolve_country_label(self.country_lower, self.country_not_lower, self.cate3, cmp)
            or ""
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

        self.year_labe = convert_time_to_arabic(self.year_at_first)

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

        # TODO: delete it
        if self.country_lower == "x":
            if self.country_label:
                self.cat_test, self.arlabel = new_func_mk2(
                    self.cate,
                    self.cat_test,
                    self.year_at_first,
                    "",
                    self.In,
                    self.country_lower,
                    self.arlabel,
                    self.year_labe,
                    self.suf,
                    self.Add_In,
                    self.country_label,
                    self.Add_In_Done,
                )
                return

            logger.info(f"a<<lightblue>>>>>> No label., {self.country_lower=}")
            self.NoLab = True
            return

        logger.info("a<<lightblue>>>>>> No label.")
        self.NoLab = True

    # ----------------------------------------------------
    # 7 — APPLY FALLBACKS
    # ----------------------------------------------------

    def apply_fallbacks(self) -> None:
        """Run backup labeling logic when primary processing fails."""
        if self.NoLab and self.cat_test == "":
            if self.country_label and self.year_labe and self.In == "":
                self.arlabel = f"{self.country_label} {self.year_labe}"
                if self.arlabel:
                    self.NoLab = False

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
        # self.apply_fallbacks()

        return self.finalize()


def _label_for_startwith_year_or_typeo(category_r: str) -> str:
    """Return an Arabic label for categories that begin with years or types."""
    builder = LabelForStartWithYearOrTypeo()
    result = builder.build(category_r).strip()
    logger.debug(f"::_label_for_startwith_year_or_typeo: {category_r=} => {result=}")
    return result


def label_for_startwith_year_or_typeo(category_r: str) -> str:
    """Return an Arabic label for categories that begin with years or types."""

    category_r = re.sub(r"category:", "", category_r.lower()).strip()

    if match_time_en_first(category_r):
        return convert_time_to_arabic(category_r)

    result = _label_for_startwith_year_or_typeo(category_r)

    logger.debug(f":: label_for_startwith_year_or_typeo: {category_r=} => {result=}")
    return result
