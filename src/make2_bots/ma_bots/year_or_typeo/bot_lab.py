#!/usr/bin/python3
"""
Usage:
from .bot_lab import label_for_startwith_year_or_typeo

"""

import re

from ....fix import fixtitle
from ....helps.log import logger
from ....translations import Nat_mens, typeTable
from ....utils import check_key_in_tables
from ...date_bots import year_lab
from ...format_bots import category_relation_mapping
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.bot import Films_O_TT, New_Lan
from ...matables_bots.check_bot import check_key_new_players
from ..country_bot import get_country
from .dodo_2019 import work_2019
from .mk3 import new_func_mk2
from .reg_result import get_cats, get_reg_result

type_after_country = ["non-combat"]


def get_country_label(country_lower, country_not_lower, cate3, compare_lab):
    country_label = ""

    if country_lower:
        country_label = get_pop_All_18(country_lower, "")

        if not country_label:
            country_label = get_country(country_not_lower)

        if country_label == "" and cate3 == compare_lab:
            country_label = Nat_mens.get(country_lower, "")
            if country_label:
                country_label = country_label + " في"
                logger.info("a<<lightblue>>>2021 cnt_la == %s" % country_label)

    return country_label


def do_ar(typeo, country_label, typeo_lab, category_r):

    in_tables_lowers = check_key_new_players(typeo.lower())
    in_tables = check_key_in_tables(typeo, [Films_O_TT, typeTable])

    if typeo in type_after_country:
        ar = f"{country_label} {typeo_lab}"
    elif in_tables or in_tables_lowers:
        ar = f"{typeo_lab} {country_label}"
    else:
        ar = f"{country_label} {typeo_lab}"

    New_Lan[category_r.lower()] = ar

    logger.info(f'>>>> <<lightyellow>> typeo_lab:"{typeo_lab}", cnt_la "{country_label}"')
    logger.info(f'>>>> <<lightyellow>> New_Lan[{category_r}] = "{ar}" ')


class LabelForStartWithYearOrTypeo:

    def __init__(self):
        self.cate = ""
        self.cate3 = ""
        self.year_at_first = ""
        self.typeo = ""
        self.In = ""
        self.country = ""
        self.country_lower = ""
        self.country_not_lower = ""
        self.cat_test = ""
        self.category_r = ""

        self.arlabel = ""
        self.typeo_lab = ""
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
    def replace_cat_test(cat_test, text):
        return cat_test.lower().replace(text.lower().strip(), "")

    # ----------------------------------------------------
    # 1 — PARSE
    # ----------------------------------------------------

    def parse_input(self, category_r):

        self.category_r = category_r

        self.cate, self.cate3 = get_cats(category_r)
        result = get_reg_result(category_r)

        self.year_at_first = result.year_at_first
        self.typeo = result.typeo
        self.In = result.In
        self.country = result.country
        self.cat_test = result.cat_test

        self.country_lower = self.country.lower()
        self.country_not_lower = self.country

        logger.info(f'>>>> year_at_first:"{self.year_at_first}", ' f'typeo:"{self.typeo}", In:"{self.In}", country_lower:"{self.country_lower}"')

    # ----------------------------------------------------
    # 2 — HANDLE TYPEO
    # ----------------------------------------------------

    def handle_typeo(self):

        if not self.typeo:
            return

        if self.typeo in typeTable:

            logger.info('a<<lightblue>>>>>> typeo "{}" in typeTable "{}"'.format(self.typeo, typeTable[self.typeo]["ar"]))

            self.typeo_lab = typeTable[self.typeo]["ar"]
            self.cat_test = self.replace_cat_test(self.cat_test, self.typeo)

            if self.typeo in ("sports events", "sorts-events") and self.year_at_first:
                self.typeo_lab = "أحداث"

            self.arlabel += self.typeo_lab

            logger.info("a<<lightblue>>>typeo_lab : %s" % self.typeo_lab)

            if "s" in typeTable[self.typeo]:
                self.suf = typeTable[self.typeo]["s"]

        else:
            logger.info(f'a<<lightblue>>>>>> typeo "{self.typeo}" not in typeTable')

    # ----------------------------------------------------
    # 3 — HANDLE COUNTRY
    # ----------------------------------------------------

    def handle_country(self):

        if not self.country_lower:
            return

        cmp = self.year_at_first + " " + self.country_lower

        self.country_label = get_country_label(self.country_lower, self.country_not_lower, self.cate3, cmp)

        if self.country_label:
            self.cat_test = self.replace_cat_test(self.cat_test, self.country_lower)
            logger.info("a<<lightblue>>>cnt_la : %s" % self.country_label)

    # ----------------------------------------------------
    # 4 — HANDLE YEAR
    # ----------------------------------------------------

    def handle_year(self):

        if not self.year_at_first:
            return

        self.year_labe = year_lab.make_year_lab(self.year_at_first)

        if not self.year_labe:
            return

        self.cat_test = self.replace_cat_test(self.cat_test, self.year_at_first)
        self.arlabel += " " + self.year_labe

        logger.info(f'252: year_at_first({self.year_at_first}) != "" ' f'arlabel:"{self.arlabel}",In.strip() == "{self.In.strip()}"')

        if (self.In.strip() in ("in", "at")) and not self.suf.strip():
            logger.info('Add في to arlabel:in,at"%s"' % self.arlabel)

            self.arlabel += " في "
            self.cat_test = self.replace_cat_test(self.cat_test, self.In)
            self.Add_In = False
            self.Add_In_Done = True

    # ----------------------------------------------------
    # 5 — RELATION MAPPING
    # ----------------------------------------------------

    def handle_relation_mapping(self):

        if not self.In.strip():
            return

        if self.In.strip() in category_relation_mapping:
            if category_relation_mapping[self.In.strip()].strip() in self.arlabel:
                self.cat_test = self.replace_cat_test(self.cat_test, self.In)
        else:
            self.cat_test = self.replace_cat_test(self.cat_test, self.In)

        self.cat_test = re.sub(r"category:", "", self.cat_test)

        logger.debug(f'<<lightblue>>>>>> cat_test: "{self.cat_test}" ')

    # ----------------------------------------------------
    # 6 — APPLY LABEL RULES
    # ----------------------------------------------------

    def apply_label_rules(self):

        if (not self.year_at_first or not self.year_labe) and self.cat_test.strip():
            self.NoLab = True
            logger.info("year_at_first == " ' or year_labe == ""')
            return

        if not self.country_lower and not self.In:
            logger.info('a<<lightblue>>>>>> country_lower == "" and In ==  "" ')
            if self.suf:
                self.arlabel = self.arlabel + " " + self.suf
            self.arlabel = re.sub(r"\s+", " ", self.arlabel)
            logger.debug("a<<lightblue>>>>>> No country_lower.")
            return

        if self.country_lower:

            if self.country_label:
                self.cat_test, self.arlabel = new_func_mk2(self.cate, self.cat_test, self.year_at_first, self.typeo, self.In, self.country_lower, self.arlabel, self.year_labe, self.suf, self.Add_In, self.country_label, self.Add_In_Done)
                return

            logger.info('a<<lightblue>>>>>> Cant id country_lower : "%s" ' % self.country_lower)
            self.NoLab = True
            return

        logger.info("a<<lightblue>>>>>> No label.")
        self.NoLab = True

    # ----------------------------------------------------
    # 7 — APPLY FALLBACKS
    # ----------------------------------------------------

    def apply_fallbacks(self):

        if self.NoLab and self.cat_test == "":
            if self.country_label and self.typeo_lab and not self.year_at_first and self.In == "":
                do_ar(self.typeo, self.country_label, self.typeo_lab, self.category_r)

    # ----------------------------------------------------
    # 8 — FINALIZE
    # ----------------------------------------------------

    def finalize(self):

        category2 = self.cate[len("category:") :].lower() if self.cate.lower().startswith("category:") else self.cate.lower()

        if not self.cat_test.strip():
            logger.debug("<<lightgreen>>>>>> arlabel " + self.arlabel)

        elif self.cat_test == self.country_lower or self.cat_test == ("in " + self.country_lower):
            logger.debug("<<lightgreen>>>>>> cat_test False.. ")
            logger.debug('<<lightblue>>>>>> cat_test = country_lower : "%s" ' % self.country_lower)
            self.NoLab = True

        elif self.cat_test.lower() == category2.lower():
            logger.debug("<<lightblue>>>>>> cat_test = category2 ")

        else:
            logger.debug("<<lightgreen>>>> >> cat_test False result.. ")
            logger.debug(' cat_test : "%s" ' % self.cat_test)
            logger.debug("<<lightgreen>>>>>> arlabel " + self.arlabel)
            self.NoLab = True

        logger.debug("<<lightgreen>>>>>> arlabel " + self.arlabel)

        # special 2019 handler
        if self.NoLab and self.year_at_first and self.year_labe:
            cat4_lab = work_2019(self.cate3, self.year_at_first, self.year_labe)
            if cat4_lab:
                New_Lan[self.category_r.lower()] = cat4_lab

        if not self.NoLab:
            if re.sub("[abcdefghijklmnopqrstuvwxyz]", "", self.arlabel, flags=re.IGNORECASE) == self.arlabel:

                self.arlabel = fixtitle.fixlab(self.arlabel, en=self.category_r)

                logger.info("a<<lightred>>>>>> arlabel ppoi:%s" % self.arlabel)
                logger.info(f'>>>> <<lightyellow>> cat:"{self.category_r}", ' f'category_lab "{self.arlabel}"')
                logger.info("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")

                return self.arlabel

        return ""

    # ----------------------------------------------------
    # MASTER FUNCTION
    # ----------------------------------------------------

    def build(self, category_r: str) -> str:

        self.parse_input(category_r)

        if not self.year_at_first and not self.typeo:
            return ""

        self.handle_typeo()
        self.handle_country()
        self.handle_year()
        self.handle_relation_mapping()
        self.apply_label_rules()
        self.apply_fallbacks()

        return self.finalize()


def label_for_startwith_year_or_typeo(category_r: str) -> str:

    builder = LabelForStartWithYearOrTypeo()

    return builder.build(category_r)
