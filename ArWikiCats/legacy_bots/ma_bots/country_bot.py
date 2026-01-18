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
    """Retrieve Arabic label information for a specified country."""
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
        or ""
    )
    logger.info(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')
    return resolved_label


@functools.lru_cache(maxsize=None)
def Get_country2(country: str) -> str:
    """Resolve the Arabic label for a country name using layered resolution."""
    normalized_country = country.lower().strip()
    logger.info(f'>> Get_country2 "{normalized_country}":')

    resolved_label = (
        country_2_title_work(country, with_years=True)
        or get_lab_for_country2(country)
        or general_resolver.translate_general_category(normalized_country, start_get_country2=False, fix_title=False)
        or ""
    )

    if resolved_label:
        resolved_label = fixtitle.fixlabel(resolved_label, en=normalized_country)
        resolved_label = " ".join(resolved_label.strip().split())

    logger.info(f'>> Get_country2 "{normalized_country}": cnt_la: {resolved_label}')
    return resolved_label


@functools.lru_cache(maxsize=10000)
def _resolve_remainder(remainder: str) -> str:
    """Helper to resolve the label for the remainder of a string."""
    return (
        Get_country2(remainder)
        or get_lab_for_country2(remainder)
        or general_resolver.translate_general_category(remainder, fix_title=False)
        or ""
    )


def _validate_separators(country: str) -> bool:
    """
    Return whether the input contains any disallowed separator phrases.

    Checks for presence of common separator words/phrases (for example " in ", " of ", or the special "-of ") and returns True only when none are found.

    Returns:
        True if no disallowed separators are present, False otherwise.
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
    """
    Resolve Arabic labels for strings that start with a historical prefix (for example, "defunct national ...").

    If the input begins with a recognized historical prefix and the remainder resolves to a label, return the prefix-specific formatted Arabic label; otherwise return an empty string.

    Parameters:
        country (str): The input string to inspect and resolve.

    Returns:
        str: The formatted Arabic label for the historical-prefixed term, or an empty string if no prefix matched or the remainder could not be resolved.
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
        """
        Initialize the CountryLabelRetriever.

        No runtime initialization is performed; the constructor exists to allow instantiation.
        """
        pass

    @functools.lru_cache(maxsize=1024)
    def get_country_label(self, country: str, start_get_country2: bool = True) -> str:
        """Resolve an Arabic label for a country name using layered lookup strategies."""
        country = country.lower().strip()

        logger.debug(f"<<yellow>> start get_country_label: {country=}")

        resolved_label = self._check_basic_lookups(country)

        if not resolved_label and start_get_country2:
            resolved_label = Get_country2(country)

        if not resolved_label:
            resolved_label = (
                self._check_prefixes(country)
                or check_historical_prefixes(country)
                or all_new_resolvers(country)
                or self._check_regex_years(country)
                or self._check_members(country)
                or SPORTS_KEYS_FOR_LABEL.get(country, "")
                or _resolve_remainder(country)
            )

        if resolved_label and "سنوات في القرن" in resolved_label:
            resolved_label = resolved_label.replace("سنوات في القرن", "سنوات القرن")

        logger.info_if_or_debug(f"<<yellow>> end get_country_label: {country=}, {resolved_label=}", resolved_label)
        return resolved_label

    def _check_basic_lookups(self, country: str) -> str:
        """
        Lookup a country in simple/local resolver tables and return the first matching label.

        If the input is a string of digits, it is returned unchanged.

        Parameters:
            country: Lowercase country/term as a string to resolve using basic lookup sources.

        Returns:
            The first matching label from basic lookup sources, or an empty string if none is found.
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
        """
        Handle English gender prefixes ("women's ", "men's ") by resolving the remainder and appending the appropriate Arabic gender adjective.

        Parameters:
            country: Input string to check for a known English gender prefix.

        Returns:
            The Arabic label formed by resolving the remainder and appending the gender adjective when a known prefix is found, empty string otherwise.
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
        """
        Detect year-related patterns in the input string and return a corresponding year-based label.

        Returns:
            The label produced by with_years_bot.Try_With_Years when a year pattern is present, or an empty string if no pattern matches.
        """
        RE1 = RE1_compile.match(country)
        RE2 = RE2_compile.match(country)
        RE3 = RE3_compile.match(country)

        if RE1 or RE2 or RE3:
            return with_years_bot.Try_With_Years(country)
        return ""

    def _check_members(self, country: str) -> str:
        """
        Handle inputs that end with " members of" by returning a corresponding Arabic member label.

        If the input string ends with " members of", the base term before that suffix is looked up in Nat_mens; when a mapping exists, returns the mapped Arabic label followed by " أعضاء في  ". Returns an empty string if the suffix is not present or no mapping is found.

        Returns:
            str: The constructed Arabic label when a mapping exists, otherwise an empty string.
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
        """Resolve an Arabic label for a given term (country, event, or category) using layered fallbacks."""
        term_lower = term_lower.strip()
        logger.info(f'get_term_label {lab_type=}, {separator=}, c_ct_lower:"{term_lower}" ')

        if app_settings.makeerr:
            start_get_country2 = True

        # Check for numeric/empty terms
        if not re.search(r"[a-z]", term_lower):
            return term_lower

        term_label = (
            New_female_keys.get(term_lower, "")
            or religious_entries.get(term_lower, "")
            or convert_time_to_arabic(term_lower)
        )

        if not term_label:
            if term_lower.startswith("the "):
                term_without_the = term_lower[4:]
                term_label = get_pop_All_18(term_without_the, "") or self.get_country_label(
                    term_without_the, start_get_country2=start_get_country2
                )
            else:
                term_label = self.get_country_label(term_lower, start_get_country2=start_get_country2)

        if not term_label and lab_type == "type_label":
            term_label = self._handle_type_lab_logic(term_lower, separator, start_get_country2)

        if term_label:
            logger.info(f"get_term_label {term_label=} ")
        elif separator.strip() == "for" and term_lower.startswith("for "):
            return self.get_term_label(term_lower[4:], "", lab_type=lab_type, start_get_country2=start_get_country2)

        return term_label

    def _handle_type_lab_logic(self, term_lower: str, separator: str, start_get_country2: bool) -> str:
        """Resolve a label for terms treated as types that end with specific suffixes."""
        for suffix, connector in [(" of", " في "), (" in", " في "), (" at", " في ")]:
            if not term_lower.endswith(suffix):
                continue

            base_term = term_lower[: -len(suffix)]
            translated_base = (
                jobs_mens_data.get(base_term, "")
                or get_pop_All_18(base_term, "")
                or self.get_country_label(base_term, start_get_country2=start_get_country2)
            )

            if translated_base:
                if term_lower in pop_of_without_in:
                    return translated_base
                return f"{translated_base}{connector}".strip()

        if separator.strip() == "in":
            term_label = get_pop_All_18(f"{term_lower} in", "")
            if term_label:
                return term_label

        return self.get_country_label(term_lower, start_get_country2=start_get_country2)


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
    """
    Retrieve an Arabic label for a given term or country name using layered resolution strategies.

    Parameters:
        term_lower (str): The lowercase term to look up.
        separator (str): Context separator used when resolving terms (e.g., "for", "in").
        lab_type (str): Optional label type that enables special handling (e.g., "type_label").
        start_get_country2 (bool): If True, enable the enhanced country lookup path before falling back to other resolvers.

    Returns:
        str: The resolved Arabic label for the term, or an empty string if no label is found.
    """
    return _retriever.get_term_label(term_lower, separator, lab_type=lab_type, start_get_country2=start_get_country2)


__all__ = [
    "fetch_country_term_label",
    "get_country",
]
