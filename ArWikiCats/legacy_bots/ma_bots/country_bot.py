#!/usr/bin/python3
"""
Country Label Bot Module
"""

import functools
import re

from ...config import app_settings
from ...fix import fixtitle
from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...new_resolvers.languages_resolves import resolve_languages_labels_with_time
from ...time_formats.time_to_arabic import convert_time_to_arabic
from ...translations import (
    SPORTS_KEYS_FOR_LABEL,
    Nat_mens,
    New_female_keys,
    People_key,
    get_from_pf_keys2,
    jobs_mens_data,
    pop_of_without_in,
    religious_entries,
)
from .. import sport_lab_suffixes, team_work, with_years_bot
from ..ma_bots2.country2_label_bot import country_2_title_work
from ..make_bots.bot_2018 import get_pop_All_18
from ..make_bots.reg_lines import RE1_compile, RE2_compile, RE3_compile
from ..matables_bots.table1_bot import get_KAKO
from ..o_bots import parties_resolver, university_resolver
from ...new_resolvers.other_resolvers.peoples_resolver import work_peoples
from . import general_resolver


@functools.lru_cache(maxsize=10000)
def get_lab_for_country2(country: str) -> str:
    """Retrieve Arabic label information for a specified country.

    This function attempts to find the Arabic label for a given country
    by querying multiple data sources in sequence.

    Args:
        country: The country name to look up

    Returns:
        The Arabic label for the country or an empty string if not found
    """

    country2 = country.lower().strip()

    resolved_label = (
        all_new_resolvers(country2)
        or get_from_pf_keys2(country2)
        or get_pop_All_18(country2)
        or resolve_languages_labels_with_time(country2)
        or People_key.get(country2)
        or sport_lab_suffixes.get_teams_new(country2)
        or parties_resolver.get_parties_lab(country2)
        or team_work.Get_team_work_Club(country2)
        or university_resolver.resolve_university_category(country2)
        or work_peoples(country2)
        or get_KAKO(country2)
        or convert_time_to_arabic(country2)
        or get_pop_All_18(country2)
        or ""
    )
    logger.info(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label


@functools.lru_cache(maxsize=None)
def Get_country2(country: str) -> str:
    """Retrieve Arabic label information for a specified country with enhanced processing.

    This function attempts to find the Arabic label for a given country
    using multiple processing strategies including title work and normalization.

    Args:
        country: The country name to look up

    Returns:
        The Arabic label for the country or an empty string if not found
    """

    normalized_country = country.lower().strip()
    logger.info(f'>> Get_country2 "{normalized_country}":')

    resolved_label = (
        country_2_title_work(country, with_years=True)
        or get_lab_for_country2(country)
        or general_resolver.translate_general_category(normalized_country, start_get_country2=False, fix_title=False)
        or get_pop_All_18(normalized_country.lower(), "")
        or ""
    )

    if resolved_label:
        resolved_label = fixtitle.fixlabel(resolved_label, en=normalized_country)

    resolved_label = " ".join(resolved_label.strip().split())

    logger.info(f'>> Get_country2 "{normalized_country}": cnt_la: {resolved_label}')

    return resolved_label


@functools.lru_cache(maxsize=10000)
def _resolve_remainder(remainder: str) -> str:
    """Helper to resolve the label for the remainder of a string.

    Args:
        remainder: The remaining part of the string to process

    Returns:
        The resolved Arabic label or an empty string if not found
    """
    label = (
        Get_country2(remainder)
        or get_lab_for_country2(remainder)
        or general_resolver.translate_general_category(remainder, fix_title=False)
        or ""
    )
    return label


def _validate_separators(country: str) -> bool:
    """Check if the country string contains invalid separators.

    Args:
        country: The country string to validate

    Returns:
        True if the string doesn't contain invalid separators, False otherwise
    """
    separators = [
        "based in",
        "in",
        "by",
        "about",
        "to",
        "of",
        "-of ",  # special case
        "from",
        "at",
        "on",
    ]
    separators = [f" {sep} " if sep != "-of " else sep for sep in separators]
    for sep in separators:
        if sep in country:
            return False
    return True


def check_historical_prefixes(country: str) -> str:
    """Check for historical prefixes in the country string.

    Args:
        country: The country string to check for historical prefixes

    Returns:
        The processed label if a historical prefix is found, otherwise an empty string
    """
    historical_prefixes = {
        "defunct national": "{} وطنية سابقة",
    }
    country = country.lower().strip()
    if not _validate_separators(country):
        return ""

    for prefix, prefix_template in historical_prefixes.items():
        if country.startswith(f"{prefix} "):
            logger.debug(f">>> country.startswith({prefix})")
            remainder = country[len(prefix) :].strip()
            remainder_label = _resolve_remainder(remainder)

            if remainder_label:
                resolved_label = prefix_template.format(remainder_label)
                if remainder_label.strip().endswith(" في") and prefix.startswith("defunct "):
                    resolved_label = f"{remainder_label.strip()[: -len(' في')]} سابقة في"
                logger.info(f'>>>>>> cdcdc new cnt_la  "{resolved_label}" ')
                return resolved_label
    return ""


class CountryLabelRetriever:
    """A class to handle the retrieval of country labels and related terms.

    This class provides methods to look up and process country names,
    applying various transformations and resolution strategies to generate
    appropriate Arabic labels.
    """

    def __init__(self) -> None:
        pass

    @functools.lru_cache(maxsize=1024)
    def get_country_label(self, country: str, start_get_country2: bool = True) -> str:
        """Retrieve the Arabic label for a given country name.

        Args:
            country: The country name to look up
            start_get_country2: Whether to use the enhanced country lookup

        Returns:
            The Arabic label for the country or an empty string if not found
        """
        country = country.lower()

        logger.debug(">> ----------------- get_country start ----------------- ")
        logger.debug(f"<<yellow>> start get_country_label: {country=}")

        resolved_label = self._check_basic_lookups(country)

        if resolved_label == "" and start_get_country2:
            resolved_label = Get_country2(country)

        if not resolved_label:
            resolved_label = (
                _resolve_remainder(country)
                or self._check_prefixes(country)
                or check_historical_prefixes(country)
                or all_new_resolvers(country)
                or self._check_regex_years(country)
                or self._check_members(country)
                or SPORTS_KEYS_FOR_LABEL.get(country, "")
                or ""
            )

        if resolved_label:
            if "سنوات في القرن" in resolved_label:
                resolved_label = re.sub(r"سنوات في القرن", "سنوات القرن", resolved_label)

        logger.info_if_or_debug(f"<<yellow>> end get_country_label: {country=}, {resolved_label=}", resolved_label)
        return resolved_label

    def _check_basic_lookups(self, country: str) -> str:
        """Check basic lookup tables and functions.

        Args:
            country: The country string to look up in basic tables

        Returns:
            The found label or empty string if not found
        """
        if country.strip().isdigit():
            return country

        label = (
            New_female_keys.get(country, "")
            or religious_entries.get(country, "")
            or resolve_languages_labels_with_time(country)
            or People_key.get(country)
            or all_new_resolvers(country)
            or team_work.Get_team_work_Club(country)
        )
        return label

    def _check_prefixes(self, country: str) -> str:
        """Check for specific prefixes like women's, men's, etc.

        Args:
            country: The country string to check for prefixes

        Returns:
            The processed label if a prefix is found, otherwise an empty string
        """
        prefix_labels = {
            "women's ": "نسائية",
            "men's ": "رجالية",
        }

        for prefix, prefix_label in prefix_labels.items():
            if country.startswith(prefix):
                logger.debug(f">>> country.startswith({prefix})")
                remainder = country[len(prefix) :]
                remainder_label = _resolve_remainder(remainder)

                if remainder_label:
                    new_label = f"{remainder_label} {prefix_label}"
                    logger.info(f'>>>>>> xxx new cnt_la  "{new_label}" ')
                    return new_label

        return ""

    def _check_regex_years(self, country: str) -> str:
        """Check regex patterns for years.

        Args:
            country: The country string to check for year patterns

        Returns:
            The processed label if year patterns are found, otherwise an empty string
        """
        RE1 = RE1_compile.match(country)
        RE2 = RE2_compile.match(country)
        RE3 = RE3_compile.match(country)

        if RE1 or RE2 or RE3:
            return with_years_bot.Try_With_Years(country)
        return ""

    def _check_members(self, country: str) -> str:
        """Check for 'members of' pattern.

        Args:
            country: The country string to check for 'members of' pattern

        Returns:
            The processed label if the pattern is found, otherwise an empty string
        """
        if country.endswith(" members of"):
            country2 = country.replace(" members of", "")
            resolved_label = Nat_mens.get(country2, "")
            if resolved_label:
                resolved_label = f"{resolved_label} أعضاء في  "
                logger.info(f"a<<lightblue>>>2021 get_country lab = {resolved_label}")
                return resolved_label
        return ""

    def get_term_label(
        self, term_lower: str, separator: str, lab_type: str = "", start_get_country2: bool = True
    ) -> str:
        """Retrieve the corresponding label for a given term.

        Args:
            term_lower: The lowercase term to look up
            separator: The separator to use in processing
            lab_type: The type of label to retrieve
            start_get_country2: Whether to use enhanced country lookup

        Returns:
            The processed label or an empty string if not found
        """
        logger.info(f'get_term_label {lab_type=}, {separator=}, c_ct_lower:"{term_lower}" ')

        if app_settings.makeerr:
            start_get_country2 = True

        # Check for numeric/empty terms
        test_numeric = re.sub(r"\d+", "", term_lower.strip())
        if test_numeric in ["", "-", "–", "−"]:
            return term_lower

        term_label = New_female_keys.get(term_lower, "") or religious_entries.get(term_lower, "")
        if not term_label:
            term_label = convert_time_to_arabic(term_lower)

        if term_label == "" and lab_type != "type_label":
            if term_lower.startswith("the "):
                logger.info(f'>>>> {term_lower=} startswith("the ")')
                term_without_the = term_lower[len("the ") :]
                term_label = get_pop_All_18(term_without_the, "")
                if not term_label:
                    term_label = self.get_country_label(term_without_the, start_get_country2=start_get_country2)

        if not term_label:
            if re.sub(r"\d+", "", term_lower) == "":
                term_label = term_lower
            else:
                term_label = convert_time_to_arabic(term_lower)

        if term_label == "":
            term_label = self.get_country_label(term_lower, start_get_country2=start_get_country2)

        if not term_label and lab_type == "type_label":
            term_label = self._handle_type_lab_logic(term_lower, separator, start_get_country2)

        if term_label:
            logger.info(f"get_term_label {term_label=} ")
        elif separator.strip() == "for" and term_lower.startswith("for "):
            return self.get_term_label(term_lower[len("for ") :], "", lab_type=lab_type)

        return term_label

    def _handle_type_lab_logic(self, term_lower: str, separator: str, start_get_country2: bool) -> str:
        """Handle logic specific to type_label.

        Args:
            term_lower: The lowercase term to process
            separator: The separator to use in processing
            start_get_country2: Whether to use enhanced country lookup

        Returns:
            The processed label or an empty string if not found
        """
        suffixes = [" of", " in", " at"]
        term_label = ""

        for suffix in suffixes:
            if not term_lower.endswith(suffix):
                continue

            base_term = term_lower[: -len(suffix)]
            translated_base = jobs_mens_data.get(base_term, "")

            logger.info(f" {base_term=}, {translated_base=}, {term_lower=} ")

            if term_label == "" and translated_base:
                term_label = f"{translated_base} من "
                logger.info(f"jobs_mens_data:: add من to {term_label=}, line:1583.")

            if not translated_base:
                translated_base = get_pop_All_18(base_term, "")

            if not translated_base:
                translated_base = self.get_country_label(base_term, start_get_country2=start_get_country2)

            if term_label == "" and translated_base:
                if term_lower in pop_of_without_in:
                    term_label = translated_base
                    logger.info("skip add في to pop_of_without_in")
                else:
                    term_label = f"{translated_base} في "
                    logger.info(f"XX add في to {term_label=}, line:1596.")
                return term_label  # Return immediately if found

        if term_label == "" and separator.strip() == "in":
            term_label = get_pop_All_18(f"{term_lower} in", "")

        if not term_label:
            term_label = self.get_country_label(term_lower, start_get_country2=start_get_country2)

        return term_label


# Instantiate the retriever
_retriever = CountryLabelRetriever()


def event2_d2(category_r) -> str:
    """Determine the category label based on the input string.

    Args:
        category_r: The raw category string to process

    Returns:
        The processed category label or an empty string if not found
    """
    cat3 = category_r.lower().replace("category:", "").strip()

    logger.info(f'<<lightred>>>>>> category33:"{cat3}" ')

    # TODO: THIS NEED REVIEW
    # Reject strings that contain common English prepositions
    blocked = ("in", "of", "from", "by", "at")
    if any(f" {word} " in cat3.lower() for word in blocked):
        return ""

    category_lab = ""
    if re.sub(r"^\d", "", cat3) == cat3:
        category_lab = get_country(cat3)

    return category_lab


def get_country(country: str, start_get_country2: bool = True) -> str:
    """Retrieve the Arabic label for a given country name.

    Args:
        country: The country name to look up
        start_get_country2: Whether to use enhanced country lookup

    Returns:
        The Arabic label for the country or an empty string if not found
    """
    return _retriever.get_country_label(country, start_get_country2)


def fetch_country_term_label(
    term_lower: str, separator: str, lab_type: str = "", start_get_country2: bool = True
) -> str:
    """Retrieve the corresponding label for a given country or term.

    Args:
        term_lower: The lowercase term to look up
        separator: The separator to use in processing
        lab_type: The type of label to retrieve
        start_get_country2: Whether to use enhanced country lookup

    Returns:
        The processed label or an empty string if not found
    """
    return _retriever.get_term_label(term_lower, separator, lab_type=lab_type, start_get_country2=start_get_country2)


__all__ = [
    "fetch_country_term_label",
    "get_country",
]
