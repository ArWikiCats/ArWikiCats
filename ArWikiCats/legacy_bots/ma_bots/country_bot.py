#!/usr/bin/python3
"""
Country Label Bot Module
"""

import functools
import re

from ...config import app_settings
from ...fix import fixtitle
from ...helps import logger
from ...new_resolvers.reslove_all import new_resolvers_all
from ...time_resolvers.time_to_arabic import convert_time_to_arabic
from ...translations import (
    SPORTS_KEYS_FOR_LABEL,
    Nat_mens,
    New_female_keys,
    get_from_pf_keys2,
    jobs_mens_data,
    pop_of_without_in,
    religious_entries,
)
from .. import sport_lab_suffixes, team_work, with_years_bot
from ..films_and_others_bot import te_films
from ..ma_bots2.country2_label_bot import country_2_title_work
from ..make_bots.bot_2018 import get_pop_All_18
from ..make_bots.reg_lines import RE1_compile, RE2_compile, RE3_compile
from ..matables_bots.table1_bot import get_KAKO
from ..o_bots import parties_bot, univer
from ..o_bots.peoples_resolver import work_peoples
from . import ye_ts_bot


@functools.lru_cache(maxsize=10000)
def get_lab_for_country2(country: str) -> str:
    """
    TODO: should be moved to functions directory.
    Retrieve laboratory information for a specified country.
    """

    country2 = country.lower().strip()

    resolved_label = (
        new_resolvers_all(country2)
        or get_from_pf_keys2(country2)
        or get_pop_All_18(country2)
        or te_films(country2)
        or sport_lab_suffixes.get_teams_new(country2)
        or parties_bot.get_parties_lab(country2)
        or team_work.Get_team_work_Club(country2)
        or univer.te_universities(country2)
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
    """
    TODO: should be moved to functions directory.
    Retrieve information related to a specified country.
    """

    normalized_country = country.lower().strip()
    logger.info(f'>> Get_country2 "{normalized_country}":')

    resolved_label = (
        country_2_title_work(country, with_years=True)
        or get_lab_for_country2(country)
        or ye_ts_bot.translate_general_category(normalized_country, start_get_country2=False, fix_title=False)
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
    """Helper to resolve the label for the remainder of a string."""
    label = (
        Get_country2(remainder)
        or get_lab_for_country2(remainder)
        or ye_ts_bot.translate_general_category(remainder, fix_title=False)
        or ""
    )
    return label


def _validate_separators(country: str) -> bool:
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


def check_historical_prefixes(country: str) -> str:
    """Check for historical prefixes."""
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
    """
    A class to handle the retrieval of country labels and related terms.
    """

    def __init__(self) -> None:
        pass

    @functools.lru_cache(maxsize=1024)
    def get_country_label(self, country: str, start_get_country2: bool = True) -> str:
        """Retrieve the label for a given country name."""
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
                or new_resolvers_all(country)
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
        """Check basic lookup tables and functions."""
        if country.strip().isdigit():
            return country

        label = (
            New_female_keys.get(country, "")
            or religious_entries.get(country, "")
            or te_films(country)
            or new_resolvers_all(country)
            or team_work.Get_team_work_Club(country)
        )
        return label

    def _check_prefixes(self, country: str) -> str:
        """Check for specific prefixes like women's, men's, etc."""
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

    def get_term_label(
        self, term_lower: str, separator: str, lab_type: str = "", start_get_country2: bool = True
    ) -> str:
        """Retrieve the corresponding label for a given term."""
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
        """Handle logic specific to type_label."""
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
    """
    Determine the category label based on the input string.
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
    """Retrieve the label for a given country name."""
    return _retriever.get_country_label(country, start_get_country2)


def Get_c_t_lab(term_lower: str, separator: str, lab_type: str = "", start_get_country2: bool = True) -> str:
    """Retrieve the corresponding label for a given country or term."""
    return _retriever.get_term_label(term_lower, separator, lab_type=lab_type, start_get_country2=start_get_country2)


__all__ = [
    "Get_c_t_lab",
    "get_country",
]
