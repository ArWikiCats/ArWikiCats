#!/usr/bin/python3
"""
Country Resolver Module

This module handles country-related label resolution using layered lookup strategies.
It is extracted from the legacy circular_dependency package to break the import cycle.

The key architectural change is that this module does NOT import from arabic_label_builder
or separator_based_resolver. Instead, it accepts callback functions for fallback resolution.
"""

from __future__ import annotations

import functools
import re
from typing import Callable, Optional

from ...config import app_settings
from ...fix import fixtitle
from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...sub_new_resolvers import team_work
from ...time_formats.time_to_arabic import convert_time_to_arabic
from ...translations import (
    New_female_keys,
    People_key,
    jobs_mens_data,
    keys_of_without_in,
    religious_entries,
)
from ..common_resolver_chain import get_lab_for_country2
from ..legacy_resolvers_bots.bot_2018 import get_pop_All_18
from ..legacy_resolvers_bots.country2_label_bot import country_2_title_work
from ..legacy_utils.joint_class import CountryLabelAndTermParent
from ..make_bots import get_KAKO

# Type alias for the fallback resolver callback
FallbackResolver = Callable[[str, bool], str]

# Module-level callback holder - set via set_fallback_resolver()
_fallback_resolver: Optional[FallbackResolver] = None


def set_fallback_resolver(resolver: FallbackResolver) -> None:
    """
    Set the fallback resolver callback.

    This is used to break the circular dependency. The fallback resolver
    (typically translate_general_category_wrap) is injected at runtime
    after all modules are loaded.

    Parameters:
        resolver: A callable that takes (category: str, start_get_country2: bool)
                  and returns an Arabic label string.
    """
    global _fallback_resolver
    _fallback_resolver = resolver


def _get_fallback_label(category: str, start_get_country2: bool = False) -> str:
    """
    Get label from the fallback resolver if one is set.

    Parameters:
        category: The category string to resolve.
        start_get_country2: Whether to use country2 fallback.

    Returns:
        The resolved label from the fallback resolver, or empty string if not set.
    """
    if _fallback_resolver is not None:
        return _fallback_resolver(category, start_get_country2)
    return ""


@functools.lru_cache(maxsize=10000)
def Get_country2(country: str) -> str:
    """
    Resolve a country name to its Arabic label.

    The resolved label is formatted for title consistency and normalized to remove extra whitespace.

    Parameters:
        country (str): Country name to resolve (case-insensitive; will be lower-cased and stripped).

    Returns:
        str: The Arabic label with title formatting applied and normalized whitespace, or an empty string if unresolved.
    """

    country = country.lower().strip()
    logger.info(f'>> Get_country2 "{country}":')

    resolved_label = (
        country_2_title_work(country, with_years=True)
        or get_lab_for_country2(country)
        or get_pop_All_18(country)
        or get_KAKO(country)
        or _get_fallback_label(country, start_get_country2=False)
        or ""
    )

    if resolved_label:
        resolved_label = fixtitle.fixlabel(resolved_label, en=country)

    resolved_label = " ".join(resolved_label.strip().split())

    logger.info(f'>> Get_country2 "{country}": cnt_la: {resolved_label}')

    return resolved_label


def _validate_separators(country: str) -> bool:
    """
    Return whether the input contains any disallowed separator phrases.

    Checks for presence of common separator words/phrases (for example " in ", " of ", or the special "-of ")
    and returns True only when none are found.

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
    Resolve Arabic labels for strings that start with a historical prefix.

    If the input begins with a recognized historical prefix (e.g., "defunct national ...")
    and the remainder resolves to a label, return the prefix-specific formatted Arabic label;
    otherwise return an empty string.

    Parameters:
        country (str): The input string to inspect and resolve.

    Returns:
        str: The formatted Arabic label for the historical-prefixed term,
             or an empty string if no prefix matched or the remainder could not be resolved.
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
            remainder_label = Get_country2(remainder)

            if remainder_label:
                resolved_label = prefix_template.format(remainder_label)
                if remainder_label.strip().endswith(" في") and prefix.startswith("defunct "):
                    resolved_label = f"{remainder_label.strip()[: -len(' في')]} سابقة في"
                logger.info(f'>>>>>> cdcdc new cnt_la  "{resolved_label}" ')
                return resolved_label
    return ""


class CountryLabelRetriever(CountryLabelAndTermParent):
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
        super().__init__(_resolve_callable=Get_country2)

    @functools.lru_cache(maxsize=1024)
    def get_country_label(self, country: str, start_get_country2: bool = True) -> str:
        """
        Resolve an Arabic label for a country name using layered lookup strategies.

        Parameters:
            country (str): Country name to resolve; case is normalized internally.
            start_get_country2 (bool): If True, include the enhanced multi-source lookup path
                                        (Get_country2) as a fallback.

        Returns:
            str: The resolved Arabic label, or an empty string if no label is found.
        """
        country = country.lower()

        logger.debug(">> ----------------- get_country_label start ----------------- ")
        logger.debug(f"<<yellow>> start get_country_label: {country=}")

        resolved_label = self._check_basic_lookups(country)

        if resolved_label == "" and start_get_country2:
            resolved_label = Get_country2(country)

        if not resolved_label:
            resolved_label = (
                Get_country2(country)
                or self._check_prefixes(country)
                or check_historical_prefixes(country)
                or all_new_resolvers(country)
                or self._check_regex_years(country)
                or self._check_members(country)
                or ""
            )

        if resolved_label:
            if "سنوات في القرن" in resolved_label:
                resolved_label = re.sub(r"سنوات في القرن", "سنوات القرن", resolved_label)

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
            or People_key.get(country)
            or all_new_resolvers(country)
            or team_work.resolve_clubs_teams_leagues(country)
        )
        return label

    def fetch_country_term_label(
        self, term_lower: str, separator: str, lab_type: str = "", start_get_country2: bool = True
    ) -> str:
        """
        Resolve an Arabic label for a given term (country, event, or category) using layered fallbacks.

        Parameters:
            term_lower (str): The input term in lowercase.
            separator (str): Context separator (e.g., "for", "in") that can affect resolution and recursion.
            lab_type (str): If "type_label", apply specialized suffix-handling logic to produce a type-related label.
            start_get_country2 (bool): If True, allow the enhanced country-resolution path as a fallback.

        Returns:
            str: The resolved Arabic label, or an empty string if no resolution is found.
        """
        logger.info(f'fetch_country_term_label {lab_type=}, {separator=}, c_ct_lower:"{term_lower}" ')

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
            logger.info(f"fetch_country_term_label {term_label=} ")
        elif separator.strip() == "for" and term_lower.startswith("for "):
            return self.fetch_country_term_label(term_lower[len("for ") :], "", lab_type=lab_type)

        return term_label

    def _handle_type_lab_logic(self, term_lower: str, separator: str, start_get_country2: bool) -> str:
        """
        Resolve a label for terms treated as types that end with suffixes like " of", " in", or " at".

        Parameters:
            term_lower (str): Lowercased term to process (may end with " of", " in", or " at").
            separator (str): Separator context such as "in" that can alter fallback behaviour.
            start_get_country2 (bool): If true, allow the enhanced country lookup path when resolving base terms.

        Returns:
            str: The resolved Arabic label for the term, or an empty string if no label is found.
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
                if term_lower in keys_of_without_in:
                    term_label = translated_base
                    logger.info("skip add في to keys_of_without_in")
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


def event2_d2(category_r: str) -> str:
    """Determine the category label based on the input string.

    Args:
        category_r: The raw category string to process

    Returns:
        The processed category label or an empty string if not found
    """
    cat3 = category_r.lower().replace("category:", "").strip()

    logger.info(f'<<lightred>>>>>> category33:"{cat3}" ')

    # Reject strings that contain common English prepositions
    blocked = ("in", "of", "from", "by", "at")
    if any(f" {word} " in cat3.lower() for word in blocked):
        return ""

    category_lab = ""
    if re.sub(r"^\d", "", cat3) == cat3:
        category_lab = get_country_label(cat3)

    return category_lab


def get_country_label(country: str, start_get_country2: bool = True) -> str:
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
        start_get_country2 (bool): If True, enable the enhanced country lookup path before
                                    falling back to other resolvers.

    Returns:
        str: The resolved Arabic label for the term, or an empty string if no label is found.
    """
    return _retriever.fetch_country_term_label(term_lower, separator, lab_type=lab_type, start_get_country2=start_get_country2)


__all__ = [
    "fetch_country_term_label",
    "get_country_label",
    "Get_country2",
    "event2_d2",
    "set_fallback_resolver",
]
