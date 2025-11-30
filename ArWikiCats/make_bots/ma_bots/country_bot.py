#!/usr/bin/python3
"""
Country Label Bot Module
"""

import re
from typing import Dict

from ...config import app_settings
from ...helps.log import logger
from ...translations import (
    SPORTS_KEYS_FOR_LABEL,
    Nat_mens,
    New_female_keys,
    jobs_mens_data,
    pop_of_without_in,
)
from ..date_bots import with_years_bot
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..media_bots.films_bot import te_films
from ..p17_bots import nats
from ..reg_lines import RE1_compile, RE2_compile, RE3_compile
from ..sports_bots import team_work
from . import country2_bot, country2_lab, ye_ts_bot
from ...new.time_to_arabic import convert_time_to_arabic

get_country_done: Dict[str, str] = {}


class CountryLabelRetriever:
    """
    A class to handle the retrieval of country labels and related terms.
    """

    def __init__(self) -> None:
        pass

    def get_country_label(self, country: str, start_get_country2: bool = True) -> str:
        """Retrieve the label for a given country name."""
        country = country.lower()

        if country in get_country_done:
            logger.debug(f'>>>> get_country: "{country}" in get_country_done, lab:"{get_country_done[country]}"')
            return get_country_done[country]

        logger.debug(">> ----------------- get_country start ----------------- ")
        logger.debug(f'>>>> Get country for "{country}"')

        resolved_label = self._check_basic_lookups(country)
        if resolved_label == "" and start_get_country2:
            resolved_label = country2_bot.Get_country2(country)

        if not resolved_label:
            resolved_label = self._check_prefixes(country)

        is_valid = True
        if not resolved_label:
            is_valid = self._validate_separators(country)

        if not resolved_label and is_valid:
            resolved_label = self._check_historical_prefixes(country)

        if resolved_label:
            if "سنوات في القرن" in resolved_label:
                resolved_label = re.sub(r"سنوات في القرن", "سنوات القرن", resolved_label)

        if not resolved_label:
            resolved_label = self._check_regex_years(country)

        if not resolved_label:
            resolved_label = self._check_members(country)

        if not resolved_label:
            resolved_label = SPORTS_KEYS_FOR_LABEL.get(country, "")

        get_country_done[country] = resolved_label
        logger.debug(f'>>>> Get country "{resolved_label=}"')
        logger.debug(">> ----------------- end get_country ----------------- ")
        return resolved_label

    def _check_basic_lookups(self, country: str) -> str:
        """Check basic lookup tables and functions."""
        if country.strip().isdigit():
            return country

        label = New_female_keys.get(country, "")
        if not label:
            label = te_films(country)
        if not label:
            label = nats.find_nat_others(country)
        if not label:
            label = team_work.Get_team_work_Club(country)
        return label

    def _check_prefixes(self, country: str) -> str:
        """Check for specific prefixes like women's, men's, etc."""
        prefix_labels = {
            "women's ": "نسائية",
            "men's ": "رجالية",
            "non-combat ": "غير قتالية",
        }

        for prefix, prefix_label in prefix_labels.items():
            if country.startswith(prefix):
                logger.debug(f">>> country.startswith({prefix})")
                remainder = country[len(prefix) :]
                remainder_label = self._resolve_remainder(remainder)

                if remainder_label:
                    new_label = f"{remainder_label} {prefix_label}"
                    logger.info(f'>>>>>> xxx new cnt_la  "{new_label}" ')
                    return new_label

        return ""

    def _resolve_remainder(self, remainder: str) -> str:
        """Helper to resolve the label for the remainder of a string."""
        label = country2_bot.Get_country2(remainder)

        if label == "":
            label = country2_lab.get_lab_for_country2(remainder)

        if label == "":
            label = ye_ts_bot.translate_general_category(remainder, fix_title=False)
        return label

    def _validate_separators(self, country: str) -> bool:
        """Check if the country string contains invalid separators."""
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

    def _check_historical_prefixes(self, country: str) -> str:
        """Check for historical prefixes."""
        historical_prefixes = {
            "defunct national ": "{} وطنية سابقة",
        }

        for prefix, prefix_template in historical_prefixes.items():
            if country.startswith(prefix):
                logger.debug(f">>> country.startswith({prefix})")
                remainder = country[len(prefix) :]
                remainder_label = self._resolve_remainder(remainder)

                if remainder_label:
                    resolved_label = prefix_template.format(remainder_label)
                    if remainder_label.strip().endswith(" في") and prefix.startswith("defunct "):
                        resolved_label = f"{remainder_label.strip()[: -len(' في')]} سابقة في"
                    logger.info(f'>>>>>> cdcdc new cnt_la  "{resolved_label}" ')
                    return resolved_label
        return ""

    def _check_regex_years(self, country: str) -> str:
        """Check regex patterns for years."""
        RE1 = RE1_compile.match(country)
        RE2 = RE2_compile.match(country)
        RE3 = RE3_compile.match(country)

        if RE1 or RE2 or RE3:
            return with_years_bot.Try_With_Years(country)
        return ""

    def _check_members(self, country: str) -> str:
        """Check for 'members of' pattern."""
        if country.endswith(" members of"):
            country2 = country.replace(" members of", "")
            resolved_label = Nat_mens.get(country2, "")
            if resolved_label:
                resolved_label = f"{resolved_label} أعضاء في  "
                logger.info(f"a<<lightblue>>>2021 get_country lab = {resolved_label}")
                return resolved_label
        return ""

    def get_term_label(self, term_lower: str, tito: str, lab_type: str = "", start_get_country2: bool = True) -> str:
        """Retrieve the corresponding label for a given term."""
        logger.info(f'get_term_label lab_type:"{lab_type}", tito:"{tito}", c_ct_lower:"{term_lower}" ')

        if app_settings.makeerr:
            start_get_country2 = True

        # Check for numeric/empty terms
        test_numeric = re.sub(r"\d+", "", term_lower.strip())
        if test_numeric in ["", "-", "–", "−"]:
            return term_lower

        term_label = New_female_keys.get(term_lower, "")
        if not term_label:
            term_label = convert_time_to_arabic(term_lower)

        if term_label == "" and lab_type != "type_label":
            if term_lower.startswith("the "):
                logger.info(f'>>>> term_lower:"{term_lower}" startswith("the ")')
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
            term_label = self._handle_type_lab_logic(term_lower, tito, start_get_country2)

        if term_label:
            logger.info(f'get_term_label term_label:"{term_label}" ')
        elif tito.strip() == "for" and term_lower.startswith("for "):
            return self.get_term_label(term_lower[len("for ") :], "", lab_type=lab_type)

        return term_label

    def _handle_type_lab_logic(self, term_lower: str, tito: str, start_get_country2: bool) -> str:
        """Handle logic specific to type_label."""
        suffixes = [" of", " in", " at"]
        term_label = ""

        for suffix in suffixes:
            if not term_lower.endswith(suffix):
                continue

            base_term = term_lower[: -len(suffix)]
            translated_base = jobs_mens_data.get(base_term, "")

            logger.info(f'base_term:"{base_term}", translated_base:"{translated_base}", term_lower:"{term_lower}" ')

            if term_label == "" and translated_base:
                term_label = f"{translated_base} من "
                logger.info(f"jobs_mens_data:: add من to term_label:{term_label}, line:1583.")

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
                    logger.info(f"XX add في to term_label:{term_label}, line:1596.")
                return term_label  # Return immediately if found

        if term_label == "" and tito.strip() == "in":
            term_label = get_pop_All_18(f"{term_lower} in", "")

        if not term_label:
            term_label = self.get_country_label(term_lower, start_get_country2=start_get_country2)

        return term_label


# Instantiate the retriever
_retriever = CountryLabelRetriever()


def get_country(country: str, start_get_country2: bool = True) -> str:
    """Retrieve the label for a given country name."""
    return _retriever.get_country_label(country, start_get_country2)


def Get_c_t_lab(term_lower: str, tito: str, lab_type: str = "", start_get_country2: bool = True) -> str:
    """Retrieve the corresponding label for a given country or term."""
    return _retriever.get_term_label(term_lower, tito, lab_type=lab_type, start_get_country2=start_get_country2)


__all__ = [
    "Get_c_t_lab",
    "get_country",
]
