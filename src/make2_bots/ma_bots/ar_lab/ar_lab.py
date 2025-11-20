#!/usr/bin/python3
"""
Arabic Label Builder Module
"""

import functools
import re
from dataclasses import dataclass
from typing import Tuple
from ....helps.log import logger
from ....main_processers import event2bot
from ....utils import check_key_in_tables_return_tuple, fix_minor
from ...format_bots import (
    Dont_Add_min,
    category_relation_mapping,
    for_table,
    pop_format,
    pop_format2,
    pop_format33,
)
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.bot import (
    Add_ar_in,
    Keep_it_frist,
    Keep_it_last,
    Table_for_frist_word,
)
from ...matables_bots.check_bot import check_key_new_players
from ....helps.jsonl_dump import dump_data

from .lab import (
    add_in_tab,
    get_type_lab,
    get_con_lab,
    get_type_country,
    tito_list_s_fixing,
)

TITO_LIST_S = [
    "in",
    "from",
    "at",
    "by",
    "of",
]


@dataclass
class ParsedCategory:
    """Represents a parsed category with its components."""
    category: str
    tito: str
    type_value: str
    country: str


@dump_data()
@functools.lru_cache(maxsize=10000)
def wrap_event2(category: str, tito: str = "") -> str:
    """Wraps the event2bot.event2 function with caching."""
    return event2bot.event2(category)


class CountryResolver:
    """Resolves country-related information for category labeling."""

    @staticmethod
    @functools.lru_cache(maxsize=10000)
    def resolve_labels(preposition: str, country: str, start_get_country2: bool = True) -> str:
        """Resolve the country label."""
        return get_con_lab(preposition, country, start_get_country2)


class TypeResolver:
    """Resolves type-related information for category labeling."""

    @staticmethod
    @functools.lru_cache(maxsize=10000)
    def resolve(preposition: str, type_value: str, country_lower: str, use_event2: bool = True) -> Tuple[str, bool]:
        """Resolve the type label and whether to append 'in' label."""
        type_lower = type_value.strip().lower()

        type_label, add_in_lab = get_type_lab(preposition, type_value)

        # Special handling for sport and by
        if type_lower == "sport" and country_lower.startswith("by "):
            type_label = "رياضة"

        # Use event2 if no type label found
        if not type_label and use_event2:
            type_label = wrap_event2(type_lower, preposition)

        return type_label, add_in_lab


class Fixing:
    def __init__(self):
        pass

    def determine_separator(self) -> str:
        """Determines the separator string between labels."""
        sps = " "
        if self.tito_stripped == "in":
            sps = " في "

        if self.country_in_table and self.add_in_lab:
            if (self.tito_stripped == "in" or self.tito_stripped == "at") and (" في" not in self.country_label or self.type_lower in Add_ar_in):
                sps = " في "
                logger.info("ssps:%s" % sps)
        else:
            if (self.tito_stripped == "in" or self.tito_stripped == "at") and (" في" not in self.type_label or self.type_lower in Add_ar_in):
                self.type_label = self.type_label + " في"

        if self.add_in_lab:
            logger.info(f">>>>> > add_in_lab ({self.tito_stripped=})")
            tito2_lab = category_relation_mapping.get(self.tito_stripped)

            if tito2_lab not in TITO_LIST_S:
                tatl = tito2_lab
                logger.info(f">>>>> > ({self.tito_stripped=}): tito_stripped in category_relation_mapping and tito_stripped not in TITO_LIST_S, {tatl=}")

                if self.tito_stripped == "for" and self.country_lower.startswith("for "):
                    if self.type_lower.strip().endswith("competitors") and "competitors for" in self.category:
                        tatl = "من"
                    if self.type_lower.strip().endswith("medalists") and "medalists for" in self.category:
                        tatl = "من"

                if self.tito_stripped == "to" and self.type_lower.strip().startswith("ambassadors of"):
                    tatl = "لدى"

                if self.country_label == "لعضوية البرلمان":
                    tatl = ""

                if self.tito_stripped == "for" and self.country_lower.startswith("for "):
                    p18lab = get_pop_All_18(self.country_lower)
                    if p18lab and p18lab == self.country_label:
                        tatl = ""

                if self.country_lower in for_table:
                    tatl = ""

                sps = f" {tatl} "
                logger.info("sps:%s" % sps)
                self.cate_test = self.cate_test.replace(self.tito, "")

        # in_tables_1 = check_key_new_players(self.country_lower)
        # in_tables_2 = check_key_new_players(self.type_lower)

        # if in_tables_1 and in_tables_2:
        logger.info(">>>> ================ ")
        logger.info(">>>>> > X:<<lightred>> type_lower and country_lower in players_new_keys.")
        logger.info(">>>> ================ ")

        faa = category_relation_mapping.get(self.tito_stripped) or category_relation_mapping.get(self.tito_stripped.replace("-", " ").strip())

        if not sps.strip() and faa:
            sps = f" {faa} "

        return sps


class LabelPipeline(Fixing):
    """
    A class to handle the construction of Arabic labels from category strings.
    """

    def __init__(
        self,
        category: str,
        tito: str,
        cate_test: str = "",
        start_get_country2: bool = True,
        use_event2: bool = True,
    ):
        self.category = category
        self.tito = tito
        self.cate_test = cate_test
        self.start_get_country2 = start_get_country2
        self.use_event2 = use_event2

        self.tito_stripped = tito.strip()
        self.category_type = ""
        self.country = ""
        self.type_lower = ""
        self.country_lower = ""

        self.type_label = ""
        self.country_label = ""
        self.should_append_in_label = True
        self.add_in_lab = True  # Renamed from add_in_lab for consistency but keeping logic

        self.country_in_table = False
        self.type_in_table = False

    def extract_components(self):
        """Extracts type and country components."""
        self.category_type, self.country = get_type_country(self.category, self.tito)
        self.type_lower = self.category_type.strip().lower()
        self.country_lower = self.country.strip().lower()

    def resolve_labels(self) -> bool:
        """Resolves type and country labels. Returns False if resolution fails."""

        # Resolve type
        self.type_label, self.add_in_lab = TypeResolver.resolve(self.tito_stripped, self.category_type, self.country_lower, self.use_event2)

        if self.type_label:
            self.cate_test = self.cate_test.replace(self.type_lower, "")

        # Resolve country
        self.country_label = CountryResolver.resolve_labels(self.tito_stripped, self.country, self.start_get_country2)

        if self.country_label:
            self.cate_test = self.cate_test.replace(self.country_lower, "")

        # Validation
        cao = True
        if not self.type_label:
            logger.info(f'>>>> type_lower "{self.type_lower}" not in pop_of_in')
            cao = False

        if not self.country_label:
            logger.info(f'>>>> country_lower not in pop new "{self.country_lower}"')
            cao = False

        if self.type_label or self.country_label:
            logger.info(f'<<lightgreen>>>>>> ------------- country_lower:"{self.country_lower}", country_label:"{self.country_label}"')
            logger.info(f'<<lightgreen>>>>>> ------------- type_lower:"{self.type_lower}", type_label:"{self.type_label}"')

        if not cao:
            return False

        logger.info(f'<<lightblue>> CAO: cat:"{self.category}":')

        if not self.type_label or not self.country_label:
            return False

        return True

    def refine_type_label(self):
        """Refines the type label with prepositions."""
        if self.add_in_lab:
            self.type_label = tito_list_s_fixing(self.type_label, self.tito_stripped, self.type_lower)
            if self.type_lower in Dont_Add_min:
                logger.info(f'>>>> type_lower "{self.type_lower}" in Dont_Add_min ')
            else:
                self.type_label = add_in_tab(self.type_label, self.type_lower, self.tito_stripped)

    def check_tables(self):
        """Checks if components are in specific tables."""
        self.country_in_table, table1 = check_key_in_tables_return_tuple(self.country_lower, Table_for_frist_word)
        self.type_in_table, table2 = check_key_in_tables_return_tuple(self.type_lower, Table_for_frist_word)

        if self.country_in_table:
            logger.info(f'>>>> X:<<lightpurple>> country_lower "{self.country_lower}" in {table1}.')
        if self.type_in_table:
            logger.info(f'>>>>xX:<<lightpurple>> type_lower "{self.type_lower}" in {table2}.')

    def join_labels(self, sps: str) -> str:
        """Constructs the final Arabic label."""
        keep_type_last = False
        keep_type_first = False

        arlabel = ""
        t_to = f"{self.type_lower} {self.tito_stripped}"

        if self.type_lower in Keep_it_last:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_last = True, type_lower:"{self.type_lower}" in Keep_it_last')
            keep_type_last = True

        elif self.type_lower in Keep_it_frist:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_first = True, type_lower:"{self.type_lower}" in Keep_it_frist')
            keep_type_first = True

        elif t_to in Keep_it_frist:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_first = True, t_to:"{t_to}" in Keep_it_frist')
            keep_type_first = True

        # Determine order
        if self.type_in_table and self.country_in_table:
            logger.info(">>> > X:<<lightpurple>> type_lower and country_lower in Table_for_frist_word.")
            in_tables = check_key_new_players(self.country_lower)
            if not keep_type_first and in_tables:
                arlabel = self.country_label + sps + self.type_label
            else:
                arlabel = self.type_label + sps + self.country_label
        else:
            if keep_type_first and self.country_in_table:
                arlabel = self.country_label + sps + self.type_label
            else:
                arlabel = self.type_label + sps + self.country_label

        if keep_type_last:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_last = True, type_lower:"{self.type_lower}" in Keep_it_last')
            arlabel = self.country_label + sps + self.type_label

        elif keep_type_first:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_first = True, type_lower:"{self.type_lower}" in Keep_it_frist')
            arlabel = self.type_label + sps + self.country_label

        if self.tito_stripped == "about" or (self.tito_stripped not in TITO_LIST_S):
            arlabel = self.type_label + sps + self.country_label

        if self.type_lower == "years" and self.tito_stripped == "in":
            arlabel = self.type_label + sps + self.country_label

        logger.debug(f">>>> {sps=}")
        logger.debug(f">>>> {arlabel=}")

        # Formatting replacements
        vr = re.sub(re.escape(self.country_lower), "{}", self.category.lower())
        if vr in pop_format2:
            logger.info(f'<<lightblue>>>>>> vr in pop_format2 "{pop_format2[vr]}":')
            logger.info(f'<<lightblue>>>>>>> vr: "{vr}":')
            arlabel = pop_format2[vr].format(self.country_label)
        elif self.type_lower in pop_format:
            if not self.country_label.startswith("حسب"):
                logger.info(f'>>>> <<lightblue>> type_lower in pop_format "{pop_format[self.type_lower]}":')
                arlabel = pop_format[self.type_lower].format(self.country_label)
            else:
                logger.info(f'>>>> <<lightblue>> type_lower in pop_format "{pop_format[self.type_lower]}" and country_label.startswith("حسب") ')

        elif self.tito_stripped in pop_format33:
            logger.info(f'>>>> <<lightblue>> tito in pop_format33 "{pop_format33[self.tito_stripped]}":')
            arlabel = pop_format33[self.tito_stripped].format(self.type_label, self.country_label)

        arlabel = " ".join(arlabel.strip().split())
        maren = re.match(r"\d\d\d\d", self.country_lower.strip())
        if self.type_lower.lower() == "the war of" and maren and arlabel == f"الحرب في {self.country_lower}":
            arlabel = f"حرب {self.country_lower}"
            logger.info(f'<<lightpurple>> >>>> change arlabel to "{arlabel}".')

        return arlabel

    def build(self) -> str:
        """Builds and returns the Arabic label."""
        logger.info(f'<<lightblue>>>>>> find_ar_label: category="{self.category}", tito="{self.tito}"')

        self.extract_components()

        if not self.resolve_labels():
            return ""

        self.refine_type_label()
        self.check_tables()

        sps = self.determine_separator()
        arlabel = self.join_labels(sps)

        logger.info(f'>>>> <<lightblue>>cate_test :"{self.cate_test}"')
        logger.info(f'>>>>>> <<lightyellow>>test: cat "{self.category}", arlabel:"{arlabel}"')

        arlabel = arlabel.strip()
        arlabel = fix_minor(arlabel, sps)

        return arlabel


@dump_data(["category", "tito"])
@functools.lru_cache(maxsize=10000)
def find_ar_label(
    category: str,
    tito: str,
    cate_test: str = "",
    start_get_country2: bool = True,
    use_event2: bool = True,
) -> str:
    """Find the Arabic label based on the provided parameters.

    This function now uses the LabelPipeline class to perform the logic.
    """
    builder = LabelPipeline(
        category=category,
        tito=tito,
        cate_test=cate_test,
        start_get_country2=start_get_country2,
        use_event2=use_event2
    )
    return builder.build()


__all__ = [
    "find_ar_label",
]
