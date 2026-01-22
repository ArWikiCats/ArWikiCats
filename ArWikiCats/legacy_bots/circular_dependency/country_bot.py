#!/usr/bin/python3
"""
Country Label Bot Module
"""

import functools
import re
from ...fix import fixtitle
from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...sub_new_resolvers import team_work
from ...translations import (
    Nat_mens,
    New_female_keys,
    People_key,
    religious_entries,
)
from ..common_resolver_chain import get_lab_for_country2
from ..legacy_resolvers_bots import with_years_bot
from ..legacy_resolvers_bots.bot_2018 import get_pop_All_18
from ..legacy_resolvers_bots.country2_label_bot import country_2_title_work
from ..make_bots import get_KAKO
from ..utils import RE1_compile, RE2_compile, RE3_compile

from . import general_resolver
from .joint_class import CountryLabelAndTermParent


@functools.lru_cache(maxsize=None)
def Get_country2(country: str) -> str:
    """
    Resolve the Arabic label for a country name using layered resolution and normalization.

    Parameters:
        country (str): The country name to resolve.

    Returns:
        str: The Arabic label for the country if found, otherwise an empty string. The returned label is post-processed for title fixes and normalized whitespace.
    """

    normalized_country = country.lower().strip()
    logger.info(f'>> Get_country2 "{normalized_country}":')

    resolved_label = (
        country_2_title_work(country, with_years=True)
        or get_lab_for_country2(country)
        or get_KAKO(country)
        or get_pop_All_18(country)
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
        or get_KAKO(remainder)
        or get_pop_All_18(remainder)
        or general_resolver.translate_general_category(remainder, fix_title=False)
        or ""
    )
    return label


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
        super().__init__(_resolve_callable=_resolve_remainder)

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

    @functools.lru_cache(maxsize=1024)
    def get_country_label(self, country: str, start_get_country2: bool = True) -> str:
        """
        Resolve an Arabic label for a country name using layered lookup strategies.

        Parameters:
            country (str): Country name to resolve; case is normalized internally.
            start_get_country2 (bool): If True, include the enhanced multi-source lookup path (Get_country2) as a fallback.

        Returns:
            str: The resolved Arabic label, or an empty string if no label is found.
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
                or all_new_resolvers(country)
                or self._check_regex_years(country)
                or self._check_members(country)
                # or SPORTS_KEYS_FOR_LABEL.get(country, "")
                or ""
            )

        if resolved_label:
            if "سنوات في القرن" in resolved_label:
                resolved_label = re.sub(r"سنوات في القرن", "سنوات القرن", resolved_label)

        logger.info_if_or_debug(f"<<yellow>> end get_country_label: {country=}, {resolved_label=}", resolved_label)
        return resolved_label


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


__all__ = [
    "get_country",
    "event2_d2",
]
