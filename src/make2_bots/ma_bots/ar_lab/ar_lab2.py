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

    def determine_separator(self, tito_stripped, country_label, type_label, type_lower, country_in_table, add_in_lab, tito, cate_test, for_table, country_lower, category):
        """Determines the separator string between labels."""
        sps = " "
        if tito_stripped == "in":
            sps = " في "

        if country_in_table and add_in_lab:
            if (tito_stripped == "in" or tito_stripped == "at") and (" في" not in country_label or type_lower in Add_ar_in):
                sps = " في "
                logger.info("ssps:%s" % sps)
        else:
            if (tito_stripped == "in" or tito_stripped == "at") and (" في" not in type_label or type_lower in Add_ar_in):
                type_label = type_label + " في"

        if add_in_lab:
            logger.info(f">>>>> > add_in_lab ({tito_stripped=})")
            tito2_lab = category_relation_mapping.get(tito_stripped)
            if tito2_lab not in TITO_LIST_S:
                tatl = tito2_lab
                logger.info(f">>>>> > ({tito_stripped=}): tito_stripped in category_relation_mapping and tito_stripped not in TITO_LIST_S, {tatl=}")

                if tito_stripped == "for" and country_lower.startswith("for "):
                    if type_lower.strip().endswith("competitors") and "competitors for" in category:
                        tatl = "من"

                    if type_lower.strip().endswith("medalists") and "medalists for" in category:
                        tatl = "من"

                if tito_stripped == "to" and type_lower.strip().startswith("ambassadors of"):
                    tatl = "لدى"

                if country_label == "لعضوية البرلمان":
                    tatl = ""

                if tito_stripped == "for" and country_lower.startswith("for "):
                    p18lab = get_pop_All_18(country_lower)
                    if p18lab and p18lab == country_label:
                        tatl = ""

                if country_lower in for_table:
                    tatl = ""

                sps = f" {tatl} "
                logger.info("sps:%s" % sps)
                cate_test = cate_test.replace(tito, "")

        # in_tables_1 = check_key_new_players(country_lower)
        # in_tables_2 = check_key_new_players(type_lower)

        # if in_tables_1 and in_tables_2:
        logger.info(">>>> ================ ")
        logger.info(">>>>> > X:<<lightred>> type_lower and country_lower in players_new_keys.")
        logger.info(">>>> ================ ")

        faa = category_relation_mapping.get(tito_stripped.strip()) or category_relation_mapping.get(tito_stripped.replace("-", " ").strip())
        # print(f"{tito_stripped=}, {faa=}, {sps=}")

        if not sps.strip() and faa:
            sps = f" {faa} "
        return sps, cate_test


class LabelPipeline:
    """
    A class to handle the construction of Arabic labels from category strings.
    """

    def build(
        category: str,
        tito: str,
        cate_test: str = "",
        start_get_country2: bool = True,
        use_event2: bool = True,
    ) -> str:
        """Find the Arabic label based on the provided parameters using the new pipeline."""

        logger.info(f'<<lightblue>>>>>> find_ar_label: {category=}, {tito=}')

        # Parse the category
        parsed = Parser.parse(category, tito)
        tito_stripped = parsed.tito.strip()

        # Resolve type
        type_label, add_in_lab = TypeResolver.resolve(tito_stripped, parsed.type_value, category.lower(), use_event2)

        # Handle special case for sport
        type_lower = parsed.type_value.strip().lower()
        if type_lower == "sport" and parsed.country.strip().lower().startswith("by "):
            type_label = "رياضة"

        # Resolve country
        country_label = CountryResolver.resolve_labels(tito_stripped, parsed.country, start_get_country2)

        # Check if we have valid labels
        CAO = True
        Cate_test_local = cate_test

        if type_label:
            Cate_test_local = Cate_test_local.replace(parsed.type_value.lower(), "")

        if country_label:
            Cate_test_local = Cate_test_local.replace(parsed.country.lower(), "")

        if not type_label:
            logger.info('>>>> type_lower "%s" not in pop_of_in' % type_lower)
            CAO = False

        if not country_label:
            logger.info('>>>> country_lower not in pop new "%s"' % parsed.country.lower())
            CAO = False

        if type_label or country_label:
            logger.info(f'<<lightgreen>>>>>> ------------- country_lower:"{parsed.country.lower()}", country_label:"{country_label}"')
            logger.info(f'<<lightgreen>>>>>> ------------- type_lower:"{type_lower}", type_label:"{type_label}"')

        if not CAO:
            return ""

        logger.info('<<lightblue>> CAO: cat:"%s":' % category)

        if not type_label or not country_label:
            return ""

        # Build the final label
        bot = LabelBuilder()
        arlabel = bot.build(
            tito=tito_stripped,
            type_label=type_label,
            country_label=country_label,
            type_lower=type_lower,
            country_lower=parsed.country.lower(),
            add_in_lab=add_in_lab,
            category=category,
            cate_test=Cate_test_local
        )

        return arlabel


class Parser:
    """Parses category information into structured components."""

    @staticmethod
    def parse(category: str, tito: str) -> ParsedCategory:
        """Parse the category string into its components."""
        type_value, country = get_type_country(category, tito)
        return ParsedCategory(
            category=category,
            tito=tito,
            type_value=type_value,
            country=country
        )


class LabelBuilder(Fixing):
    """Builds the final Arabic label from resolved components."""

    def __init__(self):
        pass

    def build(self, tito: str, type_label: str, country_label: str, type_lower: str, country_lower: str,
              add_in_lab: bool, category: str, cate_test: str = ""):
        """Build the final Arabic label."""
        tito_stripped = tito.strip()

        # Apply 'in' tab logic if needed
        if add_in_lab:
            type_label = tito_list_s_fixing(type_label, tito_stripped, type_lower)
            if type_lower in Dont_Add_min:
                logger.info(f'>>>> type_lower "{type_lower}" in Dont_Add_min ')
            else:
                type_label = add_in_tab(type_label, type_lower, tito_stripped)

        # Check tables
        country_in_table, type_in_table = self.check_tables(country_lower, type_lower)

        # Get sps (spacing)
        sps, cate_test = self.determine_separator(
            tito_stripped, country_label, type_label, type_lower, country_in_table,
            add_in_lab, tito, cate_test, for_table, country_lower, category)

        # Join labels
        arlabel = self.join_labels(
            tito_stripped, country_label, type_label, type_lower,
            country_in_table, type_in_table,
            country_lower, category, sps)

        logger.info(f'>>>> <<lightblue>>cate_test :"{cate_test}"')
        logger.info(f'>>>>>> <<lightyellow>>test: cat "{category}", arlabel:"{arlabel}"')
        logger.info(f'>>>> <<lightblue>>cate_test :"{cate_test}"')

        arlabel = arlabel.strip()
        arlabel = fix_minor(arlabel, sps)

        return arlabel

    def check_tables(self, country_lower, type_lower):
        """Checks if components are in specific tables."""
        country_in_table, table1 = check_key_in_tables_return_tuple(country_lower, Table_for_frist_word)
        type_in_table, table2 = check_key_in_tables_return_tuple(type_lower, Table_for_frist_word)
        if country_in_table:
            logger.info(f'>>>> X:<<lightpurple>> country_lower "{country_lower}" in {table1}.')

        if type_in_table:
            logger.info(f'>>>>xX:<<lightpurple>> type_lower "{type_lower}" in {table2}.')
        return country_in_table, type_in_table

    def join_labels(self, tito_stripped, country_label, type_label, type_lower, country_in_table, type_in_table, country_lower, category, sps):
        """Constructs the final Arabic label."""
        keep_type_last = False
        keep_type_first = False

        arlabel = ""
        t_to = f"{type_lower} {tito_stripped}"

        if type_lower in Keep_it_last:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_last = True, type_lower:"{type_lower}" in Keep_it_last')
            keep_type_last = True

        elif type_lower in Keep_it_frist:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_first = True, type_lower:"{type_lower}" in Keep_it_frist')
            keep_type_first = True

        elif t_to in Keep_it_frist:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_first = True, t_to:"{t_to}" in Keep_it_frist')
            keep_type_first = True

        # Determine order
        if type_in_table and country_in_table:
            logger.info(">>> > X:<<lightpurple>> type_lower and country_lower in Table_for_frist_word.")
            in_tables = check_key_new_players(country_lower)
            if not keep_type_first and in_tables:
                arlabel = country_label + sps + type_label
            else:
                arlabel = type_label + sps + country_label
        else:
            if keep_type_first and country_in_table:
                arlabel = country_label + sps + type_label
            else:
                arlabel = type_label + sps + country_label

        if keep_type_last:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_last = True, type_lower:"{type_lower}" in Keep_it_last')
            arlabel = country_label + sps + type_label

        elif keep_type_first:
            logger.info(f'>>>>> > X:<<lightred>> keep_type_first = True, type_lower:"{type_lower}" in Keep_it_frist')
            arlabel = type_label + sps + country_label

        if tito_stripped == "about" or (tito_stripped not in TITO_LIST_S):
            arlabel = type_label + sps + country_label

        if type_lower == "years" and tito_stripped == "in":
            arlabel = type_label + sps + country_label

        logger.debug(f">>>> {sps=}")
        logger.debug(f">>>> {arlabel=}")

        # Formatting replacements
        vr = re.sub(re.escape(country_lower), "{}", category.lower())
        if vr in pop_format2:
            logger.info(f'<<lightblue>>>>>> vr in pop_format2 "{pop_format2[vr]}":')
            logger.info(f'<<lightblue>>>>>>> vr: "{vr}":')
            arlabel = pop_format2[vr].format(country_label)
        elif type_lower in pop_format:
            if not country_label.startswith("حسب"):
                logger.info(f'>>>> <<lightblue>> type_lower in pop_format "{pop_format[type_lower]}":')
                arlabel = pop_format[type_lower].format(country_label)
            else:
                logger.info(f'>>>> <<lightblue>> type_lower in pop_format "{pop_format[type_lower]}" and country_label.startswith("حسب") ')

        elif tito_stripped in pop_format33:
            logger.info(f'>>>> <<lightblue>> tito in pop_format33 "{pop_format33[tito_stripped]}":')
            arlabel = pop_format33[tito_stripped].format(type_label, country_label)

        arlabel = " ".join(arlabel.split())
        maren = re.match(r"\d\d\d\d", country_lower.strip())
        if type_lower.lower() == "the war of" and maren and arlabel == f"الحرب في {country_lower}":
            arlabel = f"حرب {country_lower}"
            logger.info(f'<<lightpurple>> >>>> change arlabel to "{arlabel}".')
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
    builder = LabelPipeline.build(
        category=category,
        tito=tito,
        cate_test=cate_test,
        start_get_country2=start_get_country2,
        use_event2=use_event2
    )
    return builder


__all__ = [
    "find_ar_label",
]
