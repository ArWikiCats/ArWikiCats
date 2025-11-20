#!/usr/bin/python3
"""
Arabic Label Builder Module
"""

import functools
import re
from typing import Tuple

from ...helps.log import logger
from ...main_processers import event2bot
from ...translations import (
    RELIGIOUS_KEYS_PP,
    New_female_keys,
    New_P17_Finall,
    pf_keys2,
    pop_of_without_in,
)
from ...utils import check_key_in_tables_return_tuple, fix_minor
from .. import tmp_bot
from ..date_bots import year_lab
from ..format_bots import (
    Dont_Add_min,
    Tabl_with_in,
    category_relation_mapping,
    for_table,
    pop_format,
    pop_format2,
    pop_format33,
)
from ..jobs_bots.te4_bots.t4_2018_jobs import te4_2018_Jobs
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.bot import (
    Add_ar_in,
    Keep_it_frist,
    Keep_it_last,
    Table_for_frist_word,
)
from ..matables_bots.check_bot import check_key_new_players
from ..media_bots.films_bot import te_films
from ..o_bots import bys
from ..o_bots.popl import make_people_lab
from ..p17_bots import nats
from ..sports_bots import team_work
from . import country2_lab
from .country_bot import Get_c_t_lab, get_country
from ...helps.jsonl_dump import dump_data, save

TITO_LIST_S = [
    "in",
    "from",
    "at",
    "by",
    "of",
]


@dump_data()
@functools.lru_cache(maxsize=10000)
def wrap_event2(category: str, tito: str = "") -> str:
    """Wraps the event2bot.event2 function with caching."""
    return event2bot.event2(category)


def get_type_country(category: str, tito: str) -> Tuple[str, str]:
    """Extract the type and country from a given category string.

    Args:
        category (str): The category string containing type and country information.
        tito (str): The delimiter used to separate the type and country.

    Returns:
        Tuple[str, str]: A tuple containing the processed type and country.
    """
    category_type, country = "", ""
    if tito and tito in category:
        parts = category.split(tito, 1)
        category_type = parts[0]
        country = parts[1] if len(parts) > 1 else ""
    else:
        category_type = category

    country = country.lower()

    # Attempt to clean up using regex
    # Escape tito to prevent regex errors if it contains special chars
    tito_escaped = re.escape(tito) if tito else ""
    mash_pattern = f"^(.*?)(?:{tito_escaped}?)(.*?)$"

    test_remainder = category.lower()
    type_regex, country_regex = "", ""

    try:
        type_regex = re.sub(mash_pattern, r"\g<1>", category.lower())
        country_regex = re.sub(mash_pattern, r"\g<2>", category.lower())

        # Remove extracted parts from the test string to see what's left
        test_remainder = re.sub(re.escape(category_type.lower()), "", test_remainder)
        test_remainder = re.sub(re.escape(country.lower()), "", test_remainder)

    except Exception as e:
        logger.info(f"<<lightred>>>>>> except test_remainder: {e}")

    test_remainder = test_remainder.strip()
    tito_stripped = tito.strip()

    # Adjustments based on tito
    if tito_stripped == "in" and category_type.endswith(" playerss"):
        category_type = category_type.replace(" playerss", " players")

    tito_ends = f" {tito_stripped}"
    tito_starts = f"{tito_stripped} "

    if tito_stripped == "of" and not category_type.endswith(tito_ends):
        category_type = f"{category_type} of"
    elif tito_stripped == "spies for" and not category_type.endswith(" spies"):
        category_type = f"{category_type} spies"

    elif tito_stripped == "by" and not country.startswith(tito_starts):
        country = f"by {country}"
    elif tito_stripped == "for" and not country.startswith(tito_starts):
        country = f"for {country}"

    logger.info(f'>xx>>> Type: "{category_type.strip()}", country: "{country.strip()}", {tito=} ')

    if test_remainder and test_remainder != tito_stripped:
        logger.info(f'>>>> test_remainder != "", type_regex:"{type_regex}", tito:"{tito}", country_regex:"{country_regex}" ')

        if tito_stripped == "of" and not type_regex.endswith(tito_ends):
            type_regex = f"{type_regex} of"
        elif tito_stripped == "by" and not country_regex.startswith(tito_starts):
            country_regex = f"by {country_regex}"
        elif tito_stripped == "for" and not country_regex.startswith(tito_starts):
            country_regex = f"for {country_regex}"

        category_type = type_regex
        country = country_regex

        logger.info(f'>>>> yementest: type_regex:"{type_regex}", country_regex:"{country_regex}"')
    else:
        logger.info(f'>>>> test_remainder:"{test_remainder}" == tito')

    return category_type, country


# @dump_data(enable=True)
def get_Type_lab(preposition: str, type_value: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters.

    Args:
        preposition (str): The preposition/delimiter (tito).
        type_value (str): The type part of the category.

    Returns:
        Tuple[str, bool]: The label and a boolean indicating if 'in' should be appended.
    """
    normalized_preposition = preposition.strip()
    type_lower = type_value.lower()

    label = ""
    if type_lower == "women" and normalized_preposition == "from":
        label = "نساء"
        logger.info(f'>> >> >> Make label "{label}".')

    elif type_lower == "women of":
        label = "نساء من"
        logger.info(f'>> >> >> Make label "{label}".')

    should_append_in_label = True
    type_lower_with_prep = type_lower.strip()

    if not type_lower_with_prep.endswith(f" {normalized_preposition}"):
        type_lower_with_prep = f"{type_lower.strip()} {normalized_preposition}"

    if not label:
        label = Tabl_with_in.get(type_lower_with_prep, "")
        if label:
            should_append_in_label = False
            logger.info(f'<<<< type_lower_with_preposition "{type_lower_with_prep}", label : "{label}"')

    if not label:
        label = New_P17_Finall.get(type_lower, "")
        if label:
            logger.debug(f'<< type_lower_with_preposition "{type_lower_with_prep}", label : "{label}"')

    if label == "" and type_lower.startswith("the "):
        type_lower_no_article = type_lower[len("the ") :]
        label = New_P17_Finall.get(type_lower_no_article, "")
        if label:
            logger.debug(f'<<< type_lower_with_preposition "{type_lower_with_prep}", label : "{label}"')

    if label == "" and type_lower.strip().endswith(" people"):
        label = make_people_lab(type_lower)

    if not label:
        label = RELIGIOUS_KEYS_PP.get(type_lower, {}).get("mens", "")
    if not label:
        label = New_female_keys.get(type_lower, "")
    if not label:
        label = te_films(type_lower)
    if not label:
        label = nats.find_nat_others(type_lower)
    if not label:
        label = team_work.Get_team_work_Club(type_lower)

    if not label:
        label = tmp_bot.Work_Templates(type_lower)

    if not label:
        label = Get_c_t_lab(type_lower, normalized_preposition, Type="Type_lab")

    if not label:
        label = te4_2018_Jobs(type_lower)

    if not label:
        label = country2_lab.get_lab_for_country2(type_lower)

    logger.info(f"?????? get_Type_lab: {type_lower=}, {label=}")

    return label, should_append_in_label


# @dump_data(enable=True)
def get_con_lab(preposition: str, country: str, start_get_country2: bool = False) -> str:
    """Retrieve the corresponding label for a given country.

    Args:
        preposition (str): The preposition/delimiter.
        country (str): The country part of the category.
        start_get_country2 (bool): Whether to use the secondary country lookup.

    Returns:
        str: The Arabic label for the country.
    """
    preposition = preposition.strip()
    country_lower = country.strip().lower()
    label = ""
    country_lower_no_dash = country_lower.replace("-", " ")

    if not label:
        label = New_P17_Finall.get(country_lower, "")
    if not label:
        label = pf_keys2.get(country_lower, "")
    if not label:
        label = get_pop_All_18(country_lower, "")

    if not label and "-" in country_lower:
        label = get_pop_All_18(country_lower_no_dash, "")
        if not label:
            label = New_female_keys.get(country_lower_no_dash, "")

    if label == "" and "kingdom-of" in country_lower:
        label = get_pop_All_18(country_lower.replace("kingdom-of", "kingdom of"), "")

    if label == "" and country_lower.startswith("by "):
        label = bys.make_by_label(country_lower)

    if label == "" and " by " in country_lower:
        label = bys.get_by_label(country_lower)

    if preposition.lower() == "for":
        label = for_table.get(country_lower, "")

    if label == "" and country_lower.strip().startswith("in "):
        cco2 = country_lower.strip()[len("in ") :].strip()
        cco2_ = get_country(cco2)
        if not cco2_:
            cco2_ = country2_lab.get_lab_for_country2(cco2)
        if cco2_:
            label = f"في {cco2_}"

    if not label:
        label = year_lab.make_month_lab(country_lower)
    if not label:
        label = te_films(country)
    if not label:
        label = nats.find_nat_others(country)
    if not label:
        label = team_work.Get_team_work_Club(country.strip())

    if not label:
        label = Get_c_t_lab(country_lower, preposition, start_get_country2=start_get_country2)

    if not label:
        label = tmp_bot.Work_Templates(country_lower)

    if not label:
        label = country2_lab.get_lab_for_country2(country_lower)

    logger.info(f"?????? get_con_lab: {country_lower=}, {label=}")

    return label or ""


def add_in_tab(type_label: str, type_lower: str, tito2: str) -> str:
    """Add 'من' (from) to the label if conditions are met.

    Args:
        type_label (str): The current Arabic label for the type.
        type_lower (str): The lowercase type string.
        tito2 (str): The stripped delimiter.

    Returns:
        str: The modified type label.
    """
    ty_in18 = get_pop_All_18(type_lower)

    if tito2 == "from":
        if not type_label.strip().endswith(" من"):
            logger.info(f">>>> nAdd من to type_label '{type_label}' line:44")
            type_label = f"{type_label} من "
        return type_label

    if not ty_in18 or not type_lower.endswith(" of") or " في" in type_label:
        return type_label

    type_lower_prefix = type_lower[: -len(" of")]
    in_tables = check_key_new_players(type_lower)
    in_tables2 = check_key_new_players(type_lower_prefix)

    if in_tables or in_tables2:
        logger.info(f">>>> nAdd من to type_label '{type_label}' line:59")
        type_label = f"{type_label} من "

    return type_label


class ArabicLabelBuilder:
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
        """Initialize builder state from the incoming category context."""
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
        self.add_in_lab = True  # Renamed from Add_in_lab for consistency but keeping logic

        self.country_in_table = False
        self.type_in_table = False

    def extract_components(self):
        """Extracts type and country components."""
        self.category_type, self.country = get_type_country(self.category, self.tito)
        self.type_lower = self.category_type.strip().lower()
        self.country_lower = self.country.strip().lower()

    def resolve_labels(self) -> bool:
        """Resolves type and country labels. Returns False if resolution fails."""
        self.type_label, self.add_in_lab = get_Type_lab(self.tito, self.category_type)

        if self.type_lower == "sport" and self.country_lower.startswith("by "):
            self.type_label = "رياضة"

        if not self.type_label and self.use_event2:
            self.type_label = wrap_event2(self.type_lower, self.tito)

        if self.type_label:
            self.cate_test = self.cate_test.replace(self.type_lower, "")

        self.country_label = get_con_lab(
            self.tito, self.country, start_get_country2=self.start_get_country2
        )

        if self.country_label:
            self.cate_test = self.cate_test.replace(self.country_lower, "")

        # Validation
        cao = True
        if not self.type_label:
            logger.info(f'>>>> Type_lower "{self.type_lower}" not in pop_of_in')
            cao = False

        if not self.country_label:
            logger.info(f'>>>> country_lower not in pop new "{self.country_lower}"')
            cao = False

        if self.type_label or self.country_label:
            logger.info(f'<<lightgreen>>>>>> ------------- country_lower:"{self.country_lower}", con_lab:"{self.country_label}"')
            logger.info(f'<<lightgreen>>>>>> ------------- Type_lower:"{self.type_lower}", Type_lab:"{self.type_label}"')

        if not cao:
            return False

        logger.info(f'<<lightblue>> CAO: cat:"{self.category}":')

        if not self.type_label or not self.country_label:
            return False

        return True

    def refine_type_label(self):
        """Refines the type label with prepositions."""
        if self.add_in_lab:
            self.type_label = self._tito_list_s_fixing(self.type_label, self.tito_stripped, self.type_lower)
            if self.type_lower in Dont_Add_min:
                logger.info(f'>>>> Type_lower "{self.type_lower}" in Dont_Add_min ')
            else:
                self.type_label = add_in_tab(self.type_label, self.type_lower, self.tito_stripped)

    def _tito_list_s_fixing(self, type_lab: str, tito2: str, type_lower: str) -> str:
        """
        Fixes 'in', 'at' prepositions in the label.
        """
        if tito2 in TITO_LIST_S:
            if tito2 == "in" or " in" in type_lower:
                if type_lower in pop_of_without_in:
                    logger.info(f'>>-- Skip aAdd في to Type_lab:"{type_lab}", "{type_lower}"')
                else:
                    if " في" not in type_lab and " in" in type_lower:
                        logger.info(f'>>-- aAdd في to Type_lab:in"{type_lab}", for "{type_lower}"')
                        type_lab = type_lab + " في"
                    elif tito2 == "in" and " in" in type_lower:
                        logger.info(f'>>>> aAdd في to Type_lab:in"{type_lab}", for "{type_lower}"')
                        type_lab = type_lab + " في"

            elif (tito2 == "at" or " at" in type_lower) and (" في" not in type_lab):
                logger.info('>>>> Add في to Type_lab:at"%s"' % type_lab)
                type_lab = type_lab + " في"
        return type_lab

    def check_tables(self):
        """Checks if components are in specific tables."""
        self.country_in_table, table1 = check_key_in_tables_return_tuple(self.country_lower, Table_for_frist_word)
        self.type_in_table, table2 = check_key_in_tables_return_tuple(self.type_lower, Table_for_frist_word)

        if self.country_in_table:
            logger.info(f'>>>> X:<<lightpurple>> country_lower "{self.country_lower}" in {table1}.')
        if self.type_in_table:
            logger.info(f'>>>>xX:<<lightpurple>> Type_lower "{self.type_lower}" in {table2}.')

        in_tables_1 = check_key_new_players(self.country_lower)
        in_tables_2 = check_key_new_players(self.type_lower)

        if in_tables_1 and in_tables_2:
            logger.info(">>>> ================ ")
            logger.info(">>>>> > X:<<lightred>> Type_lower and country_lower in players_new_keys.")
            logger.info(">>>> ================ ")

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
            logger.info(f">>>>> > Add_in_lab ({self.tito_stripped=})")
            tito2_lab = category_relation_mapping.get(self.tito_stripped)

            if tito2_lab not in TITO_LIST_S:
                tatl = tito2_lab
                logger.info(f">>>>> > ({self.tito_stripped=}): tito2 in category_relation_mapping and tito2 not in tito_list_s, {tatl=}")

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

        faa = category_relation_mapping.get(self.tito_stripped) or category_relation_mapping.get(self.tito_stripped.replace("-", " ").strip())

        if not sps.strip() and faa:
            sps = f" {faa} "

        return sps

    def construct_final_label(self, sps: str) -> str:
        """Constructs the final Arabic label."""
        keep_type_last = False
        keep_type_first = False

        arlabel = ""
        t_to = f"{self.type_lower} {self.tito_stripped}"

        if self.type_lower in Keep_it_last:
            logger.info(f'>>>>> > X:<<lightred>> Keep_Type_last = True, Type_lower:"{self.type_lower}" in Keep_it_last')
            keep_type_last = True

        elif self.type_lower in Keep_it_frist:
            logger.info(f'>>>>> > X:<<lightred>> keep_Type_first = True, Type_lower:"{self.type_lower}" in Keep_it_frist')
            keep_type_first = True

        elif t_to in Keep_it_frist:
            logger.info(f'>>>>> > X:<<lightred>> keep_Type_first = True, t_to:"{t_to}" in Keep_it_frist')
            keep_type_first = True

        # Determine order
        if self.type_in_table and self.country_in_table:
            logger.info(">>> > X:<<lightpurple>> Type_lower and country_lower in Table_for_frist_word.")
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
            logger.info(f'>>>>> > X:<<lightred>> Keep_Type_last = True, Type_lower:"{self.type_lower}" in Keep_it_last')
            arlabel = self.country_label + sps + self.type_label

        elif keep_type_first:
            logger.info(f'>>>>> > X:<<lightred>> keep_Type_first = True, Type_lower:"{self.type_lower}" in Keep_it_frist')
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
                logger.info(f'>>>> <<lightblue>> Type_lower in pop_format "{pop_format[self.type_lower]}":')
                arlabel = pop_format[self.type_lower].format(self.country_label)
            else:
                logger.info(f'>>>> <<lightblue>> Type_lower in pop_format "{pop_format[self.type_lower]}" and con_lab.startswith("حسب") ')

        elif self.tito_stripped in pop_format33:
            logger.info(f'>>>> <<lightblue>> tito in pop_format33 "{pop_format33[self.tito_stripped]}":')
            arlabel = pop_format33[self.tito_stripped].format(self.type_label, self.country_label)

        arlabel = arlabel.replace("  ", " ")
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
        arlabel = self.construct_final_label(sps)

        logger.info(f'>>>> <<lightblue>>Cate_test :"{self.cate_test}"')
        logger.info(f'>>>>>> <<lightyellow>>test: cat "{self.category}", arlabel:"{arlabel}"')

        arlabel = arlabel.strip()
        arlabel = fix_minor(arlabel, sps)

        return arlabel


@dump_data(["category", "tito"])
@functools.lru_cache(maxsize=10000)
def find_ar_label(
    category: str,
    tito: str,
    Cate_test: str = "",
    start_get_country2: bool = True,
    use_event2: bool = True,
) -> str:
    """Find the Arabic label based on the provided parameters.

    This function now uses the ArabicLabelBuilder class to perform the logic.
    """
    builder = ArabicLabelBuilder(
        category=category,
        tito=tito,
        cate_test=Cate_test,
        start_get_country2=start_get_country2,
        use_event2=use_event2
    )
    return builder.build()


__all__ = [
    "find_ar_label",
    "add_in_tab",
    "get_Type_lab",
    "get_con_lab",
    "get_type_country",
]
