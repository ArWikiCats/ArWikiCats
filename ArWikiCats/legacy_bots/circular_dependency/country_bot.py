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
from . import general_resolver, sub_general_resolver


def translate_general_category_wrap(category, start_get_country2=False) -> str:
    """
    Resolve an Arabic label for a general category using layered resolvers.

    Parameters:
        category (str): The input category string to resolve.
        start_get_country2 (bool): If True, allow the resolver to use country-based fallback during resolution.

    Returns:
        str: Arabic label for the category, or an empty string if unresolved.
    """
    arlabel = (
        ""
        or sub_general_resolver.sub_translate_general_category(category)
        or general_resolver.work_separator_names(category, start_get_country2=start_get_country2)
    )
    return arlabel


def _validate_separators(country: str) -> bool:
    """
    Return whether the input contains any disallowed separator phrases.

    Checks for presence of common separator words/phrases (for example " in ", " of ", or the special "-of ") and returns True only when none are found.

    Returns:
        True if no disallowed separators are present, False otherwise.
    """
    disallowed = [
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
    disallowed_seps = [f" {sep} " if sep != "-of " else sep for sep in disallowed]
    return not any(sep in country for sep in disallowed_seps)


def check_historical_prefixes(
    country: str,
    get_country_func: callable = None,
) -> str:
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
            remainder_label = Get_country2(remainder)

            if remainder_label:
                resolved_label = prefix_template.format(remainder_label)
                if remainder_label.strip().endswith(" في") and prefix.startswith("defunct "):
                    resolved_label = f"{remainder_label.strip()[: -len(' في')]} سابقة في"
                logger.info(f'>>>>>> cdcdc new cnt_la  "{resolved_label}" ')
                return resolved_label
    return ""


@functools.lru_cache(maxsize=10000)
def Get_country2(country: str, country_2_title_work_func: callable = None) -> str:
    """
    Resolve a country name to its Arabic label.

    The resolved label is formatted for title consistency and normalized.

    Args:
        country: Country name to resolve (case-insensitive; will be lower-cased and stripped)
        country_2_title_work_func: Optional function for country_2_title_work (to avoid circular import)

    Returns:
        The Arabic label with title formatting applied and normalized whitespace,
        or an empty string if unresolved
    """
    country = country.lower().strip()
    logger.info(f'>> Get_country2 "{country}":')

    # Try country_2_title_work if provided (optional dependency injection)
    if country_2_title_work_func:
        resolved_label = country_2_title_work_func(country, with_years=True)
        if resolved_label:
            if resolved_label:
                resolved_label = fixtitle.fixlabel(resolved_label, en=country)
            resolved_label = " ".join(resolved_label.strip().split())
            logger.info(f'>> Get_country2 "{country}": cnt_la: {resolved_label}')
            return resolved_label

    # Fallback chain
    resolved_label = (
        country_2_title_work(country, with_years=True)
        or get_lab_for_country2(country)
        or get_pop_All_18(country)
        or get_KAKO(country)
        or translate_general_category_wrap(country, start_get_country2=False)
        or ""
    )

    if resolved_label:
        resolved_label = fixtitle.fixlabel(resolved_label, en=country)

    resolved_label = " ".join(resolved_label.strip().split())

    logger.info(f'>> Get_country2 "{country}": cnt_la: {resolved_label}')

    return resolved_label


@functools.lru_cache(maxsize=1024)
def get_country_label(
    country: str,
    start_get_country2: bool = True,
    get_country_func: callable = None,
) -> str:
    """
    Resolve an Arabic label for a country name using layered lookup strategies.

    Args:
        country: Country name to resolve; case is normalized internally
        start_get_country2: If True, include the enhanced multi-source lookup path
        get_country_func: Optional function to use for country lookups (defaults to Get_country2)

    Returns:
        The resolved Arabic label, or an empty string if no label is found
    """
    # if get_country_func is None:
    get_country_func = Get_country2

    country = country.lower()

    logger.debug(">> ----------------- get_country start ----------------- ")
    logger.debug(f"<<yellow>> start get_country_label: {country=}")

    resolved_label = _check_basic_lookups(country)

    if resolved_label == "" and start_get_country2:
        resolved_label = get_country_func(country)

    if not resolved_label:
        resolved_label = (
            get_country_func(country)
            or _parent_resolver._check_prefixes(country)
            or check_historical_prefixes(country)
            or all_new_resolvers(country)
            or _parent_resolver._check_regex_years(country)
            or _parent_resolver._check_members(country)
            or ""
        )

    if resolved_label:
        if "سنوات في القرن" in resolved_label:
            resolved_label = re.sub(r"سنوات في القرن", "سنوات القرن", resolved_label)

    logger.info_if_or_debug(f"<<yellow>> end get_country_label: {country=}, {resolved_label=}", resolved_label)
    return resolved_label


# Create resolver instance with proper initialization
_parent_resolver = CountryLabelAndTermParent(_resolve_callable=Get_country2)


def _check_basic_lookups(country: str) -> str:
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


def get_term_label(
    term_lower: str,
    separator: str,
    lab_type: str = "",
    start_get_country2: bool = True,
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
                term_label = get_country_label(term_without_the, start_get_country2=start_get_country2)

    if not term_label:
        if re.sub(r"\d+", "", term_lower) == "":
            term_label = term_lower
        else:
            term_label = convert_time_to_arabic(term_lower)

    if term_label == "":
        term_label = get_country_label(term_lower, start_get_country2=start_get_country2)

    if not term_label and lab_type == "type_label":
        term_label = _handle_type_lab_logic(term_lower, separator, start_get_country2)

    if term_label:
        logger.info(f"get_term_label {term_label=} ")
    elif separator.strip() == "for" and term_lower.startswith("for "):
        return get_term_label(term_lower[len("for ") :], "", lab_type=lab_type)

    return term_label


def _handle_type_lab_logic(
    term_lower: str,
    separator: str,
    start_get_country2: bool,
) -> str:
    """
    Resolve a label for terms treated as types that end with suffixes like " of", " in", or " at".

    Attempts to translate the base term (term without the suffix) using job/person mappings, population translations, or country-label lookup and then appends the appropriate Arabic connector ("من" or "في"). If no suffixed form matches, optionally tries a population lookup for "in" separator and finally falls back to a general country-label lookup.

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
            translated_base = get_country_label(base_term, start_get_country2=start_get_country2)

        if term_label == "" and translated_base:
            if term_lower in keys_of_without_in:
                term_label = translated_base
                logger.info("skip add في to keys_of_without_in")
            else:
                term_label = f"{translated_base} في "
                logger.info(f"XX add في to {term_label=}, line:1596.")
            return term_label

    if term_label == "" and separator.strip() == "in":
        term_label = get_pop_All_18(f"{term_lower} in", "")

    if not term_label:
        term_label = get_country_label(term_lower, start_get_country2=start_get_country2)

    return term_label


# Public wrapper functions for backward compatibility
def get_country(country: str, start_get_country2: bool = True) -> str:
    """
    Retrieve the Arabic label for a given country name.

    Args:
        country: The country name to look up
        start_get_country2: Whether to use enhanced country lookup

    Returns:
        The Arabic label for the country or an empty string if not found
    """
    return get_country_label(country, start_get_country2)


def fetch_country_term_label(
    term_lower: str,
    separator: str,
    lab_type: str = "",
    start_get_country2: bool = True,
) -> str:
    """
    Retrieve an Arabic label for a given term or country name.

    Args:
        term_lower: The lowercase term to look up
        separator: Context separator used when resolving terms
        lab_type: Optional label type that enables special handling
        start_get_country2: If True, enable the enhanced country lookup path

    Returns:
        The resolved Arabic label for the term, or an empty string if no label is found
    """
    return get_term_label(term_lower, separator, lab_type=lab_type, start_get_country2=start_get_country2)


__all__ = [
    "Get_country2",
    "get_country",
    "get_country_label",
    "fetch_country_term_label",
    "check_historical_prefixes",
]
