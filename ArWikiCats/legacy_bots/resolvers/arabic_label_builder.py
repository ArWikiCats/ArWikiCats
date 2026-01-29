#!/usr/bin/python3
"""
Arabic Label Builder Module
"""

import functools
import re
from dataclasses import dataclass
from typing import Tuple

from ...format_bots.relation_mapping import translation_category_relations
from ...helps import getLogger

logger = getLogger(__name__)
from ...patterns_resolvers.time_patterns_resolvers import resolve_lab_from_years_patterns
from ...sub_new_resolvers import university_resolver
from ...translations import keys_of_without_in
from .. import tmp_bot
from ..common_resolver_chain import get_con_label, get_type_lab
from ..legacy_resolvers_bots import bys, with_years_bot
from ..legacy_resolvers_bots.bot_2018 import get_pop_All_18
from ..legacy_resolvers_bots.year_or_typeo import label_for_startwith_year_or_typeo
from ..legacy_utils import Keep_it_frist, Keep_it_last, fix_minor, get_type_country, split_text_by_separator
from ..make_bots import check_key_new_players
from . import country_resolver

separators_lists_raw = [
    "in",
    "from",
    "at",
    "by",
    "of",
]


def _lookup_country_with_by(country: str) -> str:
    """Handle country labels with 'by' prefix or infix."""
    if country.startswith("by "):
        return bys.make_by_label(country)

    if " by " in country:
        return bys.get_by_label(country)

    return ""


class CountryResolver:
    """Resolves country-related information for category labeling."""

    @staticmethod
    @functools.lru_cache(maxsize=10000)
    def resolve_labels(preposition: str, country: str) -> str:
        """Resolve the country label."""

        for_table = {
            "for national teams": "للمنتخبات الوطنية",
            "for member-of-parliament": "لعضوية البرلمان",
        }

        result = for_table.get(country, "") if preposition.lower() == "for" else ""

        if not result:
            result = (
                get_pop_All_18(country)
                or country_resolver.fetch_country_term_label(country, preposition, "")
                or get_con_label(country)
                or tmp_bot.Work_Templates(country)
                or _lookup_country_with_by(country)
            )
        return result


def _should_add_preposition_fe(type_label: str, type_lower: str) -> bool:
    """Check if 'في' should be added to the label.

    Args:
        type_label: The Arabic label.
        type_lower: The lowercase type string.

    Returns:
        bool: True if 'في' should be added, False otherwise.
    """
    return " في" not in type_label and " in" in type_lower


def _handle_in_separator(type_label: str, separator_stripped: str, type_lower: str) -> str:
    """Handle 'in' separator logic.

    Args:
        type_label: The current Arabic label.
        separator_stripped: The stripped separator.
        type_lower: The lowercase type string.

    Returns:
        str: The modified type label.
    """
    # Skip if type is in exception list
    if type_lower in keys_of_without_in:
        logger.info(f'>>-- Skip add في to {type_label=}, "{type_lower}"')
        return type_label

    # Add 'في' if conditions are met
    if _should_add_preposition_fe(type_label, type_lower):
        logger.info(f'>>-- Add في to type_label:in"{type_label}", for "{type_lower}"')
        return f"{type_label} في"

    return type_label


def _handle_at_separator(type_label: str, type_lower: str) -> str:
    """Handle 'at' separator logic.

    Args:
        type_label: The current Arabic label.
        type_lower: The lowercase type string.

    Returns:
        str: The modified type label.
    """
    if " في" not in type_label:
        logger.info(f'>>>> Add في to type_label:at"{type_label}"')
        return f"{type_label} في"

    return type_label


def separator_lists_fixing(type_label: str, separator_stripped: str, type_lower: str) -> str:
    """Add appropriate Arabic preposition to the type label based on the separator.

    Adds 'في' (in/at) to the Arabic label when appropriate based on the English separator
    and the type string content.

    Args:
        type_label: The current Arabic label for the type (e.g., "منشآت عسكرية").
        separator_stripped: The stripped English separator (e.g., "in", "at").
        type_lower: The lowercase type string (e.g., "military installations").

    Returns:
        str: The modified type label with preposition if applicable.

    Example:
        >>> separator_lists_fixing("منشآت عسكرية", "in", "military installations")
        "منشآت عسكرية في"
    """
    # Early return if separator is not in the raw list
    if separator_stripped not in separators_lists_raw:
        return type_label

    # Handle 'in' separator
    if separator_stripped == "in" or " in" in type_lower:
        return _handle_in_separator(type_label, separator_stripped, type_lower)

    # Handle 'at' separator
    if separator_stripped == "at" or " at" in type_lower:
        return _handle_at_separator(type_label, type_lower)

    return type_label


def _should_add_min_for_from_separator(type_label: str) -> bool:
    """Check if 'من' should be added for 'from' separator.

    Args:
        type_label: The current Arabic label.

    Returns:
        bool: True if 'من' should be added, False otherwise.
    """
    return not type_label.strip().endswith(" من")


def _should_add_min_for_of_suffix(type_lower: str, ty_in18: str, type_label: str, type_lower_prefix: str = "") -> bool:
    """Check if 'من' should be added for ' of' suffix.

    Args:
        type_lower: The lowercase type string.
        ty_in18: The result from get_pop_All_18.
        type_label: The current Arabic label.

    Returns:
        bool: True if 'من' should be added, False otherwise.
    """
    # Check basic conditions
    if not ty_in18:
        return False

    if not type_lower.endswith(" of"):
        return False

    skip_in = [
        "مدربو",
    ]

    if type_label in skip_in:
        return False

    if keys_of_without_in.get(type_lower) or keys_of_without_in.get(type_lower_prefix):
        return False

    if " في" in type_label:
        return False

    return True


def add_in_tab(type_label: str, type_lower: str, separator_stripped: str) -> str:
    """Add 'من' (from) to the label if conditions are met.

    This function adds the Arabic preposition 'من' (from/of) to the type label based on:
    1. The separator being 'from'
    2. The type ending with ' of' and being found in certain tables

    Args:
        type_label: The current Arabic label for the type.
        type_lower: The lowercase type string.
        separator_stripped: The stripped delimiter.

    Returns:
        str: The modified type label with 'من' if applicable.

    Example:
        >>> add_in_tab("رياضيون", "athletes", "from")
        "رياضيون من "
    """
    # Handle 'from' separator
    if separator_stripped == "from":
        if _should_add_min_for_from_separator(type_label):
            logger.info(f">>>> Add من to type_label '{type_label}' (separator: from)")
            return f"{type_label} من "
        return type_label

    # Get population data for type
    ty_in18 = get_pop_All_18(type_lower)

    # Extract type without ' of' suffix
    type_lower_prefix = type_lower.removesuffix(" of")

    # Check if we should add 'من' for ' of' suffix
    if not _should_add_min_for_of_suffix(type_lower, ty_in18, type_label, type_lower_prefix):
        return type_label

    # Check if type (with or without ' of') is in tables
    in_tables = check_key_new_players(type_lower)
    in_tables_prefix = check_key_new_players(type_lower_prefix)

    if in_tables or in_tables_prefix:
        logger.info(f">>>> Add من to type_label '{type_label}' (ends with ' of')")
        return f"{type_label} من "

    return type_label


@functools.lru_cache(maxsize=10000)
def wrap_event2(category: str, separator: str = "") -> str:
    """
    Attempt to resolve a category label by trying several resolver functions in order.

    Parameters:
        category (str): The input category string to resolve.
        separator (str): Unused; kept for API compatibility.

    Returns:
        str: The first non-empty label returned by the resolvers, or an empty string if none match.
    """
    result = (
        university_resolver.resolve_university_category(category)
        or country_resolver.event2_d2(category)
        or with_years_bot.wrap_try_with_years(category)
        or label_for_startwith_year_or_typeo(category)
        or ""
    )
    return result


@dataclass
class ParsedCategory:
    """Represents a parsed category with its components."""

    category: str
    separator: str
    type_value: str
    country: str


class TypeResolver:
    """Resolves type-related information for category labeling."""

    @staticmethod
    @functools.lru_cache(maxsize=10000)
    def resolve(preposition: str, type_value: str, country_lower: str, use_event2: bool = True) -> Tuple[str, bool]:
        """Resolve the type label and whether to append 'in' label."""
        type_lower = type_value.strip().lower()

        logger.debug(f'>>>>> > Resolving type: "{type_lower}", preposition: "{preposition}"')

        type_label = resolve_lab_from_years_patterns(type_lower)
        if type_label:
            return type_label, True

        if type_lower == "people":
            return "أشخاص", False

        type_label = get_type_lab(type_value) or tmp_bot.Work_Templates(type_lower)

        # Special handling for sport and by
        if type_lower == "sport" and country_lower.startswith("by "):
            type_label = "رياضة"

        # Use event2 if no type label found
        if not type_label and use_event2:
            type_label = wrap_event2(type_lower, preposition)

        return type_label, True


class Fixing:
    def __init__(self) -> None:
        pass

    def determine_separator(self) -> str:
        """
        Choose the Arabic separator to place between the resolved type and country labels.

        This method selects the appropriate Arabic separator based on the parsed English separator and internal mappings. It may append the preposition " في" to self.type_label when applicable and remove the original English separator from self.cate_test when a mapped Arabic separator is applied. The method also consults translation_category_relations and other heuristics to handle special cases (e.g., "for", "to") and returns the finalized separator string including surrounding spaces when non-empty.

        Returns:
            ar_separator (str): The Arabic separator to join type and country labels (may be a single space or a spaced Arabic preposition).
        """
        ar_separator = " "
        if self.separator_stripped == "in":
            ar_separator = " في "

        if (self.separator_stripped == "in" or self.separator_stripped == "at") and (" في" not in self.type_label):
            self.type_label = self.type_label + " في"

        if self.add_in_lab:
            logger.info(f">>>>> > add_in_lab ({self.separator_stripped=})")
            separator2_lab = translation_category_relations.get(self.separator_stripped)

            if separator2_lab not in separators_lists_raw:
                tatl = separator2_lab
                logger.info(
                    f">>>>> > ({self.separator_stripped=}): separator_stripped in category_relation_mapping and separator_stripped not in separators_lists_raw, {tatl=}"
                )

                if self.separator_stripped == "for" and self.country_lower.startswith("for "):
                    if self.type_lower.strip().endswith("competitors") and "competitors for" in self.category:
                        tatl = "من"
                    if self.type_lower.strip().endswith("medalists") and "medalists for" in self.category:
                        tatl = "من"

                if self.separator_stripped == "to" and self.type_lower.strip().startswith("ambassadors of"):
                    tatl = "لدى"

                if self.country_label == "لعضوية البرلمان":
                    tatl = ""

                if self.separator_stripped == "for" and self.country_lower.startswith("for "):
                    p18lab = get_pop_All_18(self.country_lower)
                    if p18lab and p18lab == self.country_label:
                        tatl = ""

                for_table = {
                    "for national teams": "للمنتخبات الوطنية",
                    "for member-of-parliament": "لعضوية البرلمان",
                }

                if self.country_lower in for_table:
                    tatl = ""

                ar_separator = f" {tatl} "
                logger.info(f"ar_separator:{ar_separator}")
                self.cate_test = self.cate_test.replace(self.separator, "")

        # in_tables_1 = check_key_new_players(self.country_lower)
        # in_tables_2 = check_key_new_players(self.type_lower)

        # if in_tables_1 and in_tables_2:
        logger.info(">>>> ================ ")
        logger.info(">>>>> > X:<<lightred>> type_lower and country_lower in players_new_keys.")
        logger.info(">>>> ================ ")

        faa = translation_category_relations.get(self.separator_stripped) or translation_category_relations.get(
            self.separator_stripped.replace("-", " ").strip()
        )

        if not ar_separator.strip() and faa:
            ar_separator = f" {faa} "

        return ar_separator


class LabelPipeline(Fixing):
    """
    A class to handle the construction of Arabic labels from category strings.
    """

    def __init__(
        self,
        category: str,
        separator: str,
        cate_test: str = "",
        use_event2: bool = True,
    ):
        self.category = category
        self.separator = separator
        self.cate_test = cate_test
        self.use_event2 = use_event2

        self.separator_stripped = separator.strip()
        self.category_type = ""
        self.country = ""
        self.type_lower = ""
        self.country_lower = ""

        self.type_label = ""
        self.country_label = ""
        self.should_append_in_label = True
        self.add_in_lab = True  # Renamed from add_in_lab for consistency but keeping logic

    def extract_components(self) -> None:
        """Extracts type and country components."""
        self.category_type, self.country = get_type_country(self.category, self.separator)
        # self.category_type, self.country = split_text_by_separator(self.separator, self.category)

        self.type_lower = self.category_type.strip().lower()
        self.country_lower = self.country.strip().lower()

    def resolve_labels(self) -> bool:
        """Resolves type and country labels. Returns False if resolution fails."""

        # Resolve type
        self.type_label, self.add_in_lab = TypeResolver.resolve(
            self.separator_stripped, self.category_type, self.country_lower, self.use_event2
        )

        if self.type_label:
            self.cate_test = self.cate_test.replace(self.type_lower, "")

        # Resolve country
        self.country_label = CountryResolver.resolve_labels(self.separator_stripped, self.country)

        if self.country_label:
            self.cate_test = self.cate_test.replace(self.country_lower, "")

        # Validation
        cao = True
        if not self.type_label:
            logger.info(f">>>> no label for {self.type_lower=}")
            cao = False

        if not self.country_label:
            logger.info(f'>>>> country_lower not in pop new "{self.country_lower}"')
            cao = False

        if self.type_label or self.country_label:
            logger.info(
                f'<<lightgreen>>>>>> ------------- country_lower:"{self.country_lower}", country_label:"{self.country_label}"'
            )
            logger.info(
                f'<<lightgreen>>>>>> ------------- type_lower:"{self.type_lower}", type_label:"{self.type_label}"'
            )

        if not cao:
            return False

        logger.info(f'<<lightblue>> CAO: cat:"{self.category}":')

        if not self.type_label or not self.country_label:
            return False

        return True

    def refine_type_label(self) -> None:
        """Refines the type label with prepositions."""

        excluded_type_labels_from_min = [
            "women of",
            "founders of",
        ]

        if self.add_in_lab:
            self.type_label = separator_lists_fixing(self.type_label, self.separator_stripped, self.type_lower)
            if self.type_lower in excluded_type_labels_from_min:
                logger.info(f'>>>> type_lower "{self.type_lower}" in excluded_type_labels_from_min ')
            else:
                self.type_label = add_in_tab(self.type_label, self.type_lower, self.separator_stripped)

    def join_labels(self, ar_separator: str) -> str:
        """Constructs the final Arabic label."""
        keep_type_last = False
        keep_type_first = False

        arlabel = ""
        t_to = f"{self.type_lower} {self.separator_stripped}"

        if self.type_lower in Keep_it_last:
            logger.info(f">>>>> > X:<<lightred>> keep_type_last = True, {self.type_lower=} in Keep_it_last")
            keep_type_last = True

        elif self.type_lower in Keep_it_frist:
            logger.info(f">>>>> > X:<<lightred>> keep_type_first = True, {self.type_lower=} in Keep_it_frist")
            keep_type_first = True

        elif t_to in Keep_it_frist:
            logger.info(f">>>>> > X:<<lightred>> keep_type_first = True, {t_to=} in Keep_it_frist")
            keep_type_first = True

        arlabel = self.type_label + ar_separator + self.country_label

        if keep_type_last:
            logger.info(f">>>>> > X:<<lightred>> keep_type_last = True, {self.type_lower=} in Keep_it_last")
            arlabel = self.country_label + ar_separator + self.type_label

        elif keep_type_first:
            logger.info(f">>>>> > X:<<lightred>> keep_type_first = True, {self.type_lower=} in Keep_it_frist")
            arlabel = self.type_label + ar_separator + self.country_label

        if self.separator_stripped == "about" or (self.separator_stripped not in separators_lists_raw):
            arlabel = self.type_label + ar_separator + self.country_label

        if self.type_lower == "years" and self.separator_stripped == "in":
            arlabel = self.type_label + ar_separator + self.country_label

        logger.debug(f">>>> {ar_separator=}")
        logger.debug(f">>>> {arlabel=}")

        arlabel = " ".join(arlabel.strip().split())
        maren = re.match(r"\d\d\d\d", self.country_lower.strip())
        if self.type_lower.lower() == "the war of" and maren and arlabel == f"الحرب في {self.country_lower}":
            arlabel = f"حرب {self.country_lower}"
            logger.info(f'<<lightpurple>> >>>> change arlabel to "{arlabel}".')

        return arlabel

    def build(self) -> str:
        """Builds and returns the Arabic label."""
        logger.info(f'<<lightblue>>>>>> find_ar_label: category="{self.category}", separator="{self.separator}"')

        self.extract_components()

        if not self.resolve_labels():
            return ""

        self.refine_type_label()

        ar_separator = self.determine_separator()
        arlabel = self.join_labels(ar_separator)

        logger.info(f'>>>> <<lightblue>>cate_test :"{self.cate_test}"')
        logger.info(f'>>>>>> <<lightyellow>>test: cat "{self.category}", {arlabel=}')

        arlabel = arlabel.strip()
        arlabel = fix_minor(arlabel, ar_separator, self.category)

        return arlabel


@functools.lru_cache(maxsize=10000)
def find_ar_label(
    category: str,
    separator: str,
    cate_test: str = "",
    use_event2: bool = True,
) -> str:
    """Find the Arabic label based on the provided parameters.

    This function now uses the LabelPipeline class to perform the logic.
    """
    builder = LabelPipeline(
        category=category,
        separator=separator,
        cate_test=cate_test,
        use_event2=use_event2,
    )
    return builder.build()


__all__ = [
    "find_ar_label",
]
