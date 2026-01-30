#!/usr/bin/python3
""" """

import logging
from typing import Callable

from ...translations import (
    Nat_mens,
)
from ..legacy_resolvers_bots import with_years_bot
from ..utils import RE1_compile, RE2_compile, RE3_compile

logger = logging.getLogger(__name__)


class CountryLabelAndTermParent:
    """ """

    def __init__(self, _resolve_callable: Callable = None) -> None:
        """
        Initialize the CountryLabelAndTermParent.

        No runtime initialization is performed; the constructor exists to allow instantiation.
        """
        self._resolve_callable = _resolve_callable

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
        if not self._resolve_callable:
            logger.error(">>> Error: _resolve_callable method is not defined.")
            return ""

        for prefix, prefix_label in prefix_labels.items():
            if country.startswith(prefix):
                logger.debug(f">>> country.startswith({prefix})")
                remainder = country[len(prefix) :]
                remainder_label = self._resolve_callable(remainder)

                if remainder_label:
                    new_label = f"{remainder_label} {prefix_label}"
                    logger.info(f'>>>>>> xxx new cnt_la "{new_label}" ')
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
            country2 = country.removesuffix(" members of").strip()
            resolved_label = Nat_mens.get(country2, "")
            if resolved_label:
                resolved_label = f"{resolved_label} أعضاء في  "
                logger.info(f"a<<lightblue>>>2021 get_country_label lab = {resolved_label}")
                return resolved_label
        return ""


__all__ = [
    "CountryLabelAndTermParent",
]
