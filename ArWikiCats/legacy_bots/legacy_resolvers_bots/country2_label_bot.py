#!/usr/bin/python3
"""
This module provides functions for processing and generating labels for country names based on separators.

Note: This module uses a callback pattern for `fetch_country_term_label` to avoid circular imports.
The callback is set at runtime via `set_term_label_resolver()`.
"""

import functools
import re
from typing import Callable, Optional, Tuple

from ...format_bots.relation_mapping import translation_category_relations
from ...helps import getLogger
from ...new_resolvers import all_new_resolvers
from ...new_resolvers.bys_new import resolve_by_labels
from ...sub_new_resolvers import parties_resolver, team_work
from ...translations import People_key
from ...translations.funcs import get_and_label, get_from_pf_keys2
from ..legacy_utils import fix_minor, split_text_by_separator
from ..make_bots import add_to_Films_O_TT, check_key_new_players, get_KAKO
from . import bys, with_years_bot
from .bot_2018 import get_pop_All_18

logger = getLogger(__name__)

# Type alias for the term label resolver callback
TermLabelResolver = Callable[[str, str, str], str]

# Module-level callback holder - set via set_term_label_resolver()
_term_label_resolver: Optional[TermLabelResolver] = None


def set_term_label_resolver(resolver: TermLabelResolver) -> None:
    """
    Set the term label resolver callback.

    This is used to break the circular dependency. The resolver
    (typically fetch_country_term_label) is injected at runtime
    after all modules are loaded.

    Parameters:
        resolver: A callable that takes (term_lower: str, separator: str, lab_type: str)
                  and returns an Arabic label string.
    """
    global _term_label_resolver
    _term_label_resolver = resolver


def _get_term_label(term: str, separator: str = "", lab_type: str = "") -> str:
    """
    Get label from the term label resolver if one is set.

    Parameters:
        term: The term to resolve.
        separator: The separator context.
        lab_type: The label type (e.g., "type_label").

    Returns:
        The resolved label from the term label resolver, or empty string if not set.
    """
    if _term_label_resolver is not None:
        return _term_label_resolver(term, separator, lab_type)
    return ""


def get_table_with_in(cone_1: str, separator: str) -> str:
    """
    Map a composite key of cone_1 and separator to a predefined Arabic label.

    Parameters:
        cone_1 (str): Left-hand token to combine with the separator (e.g., "sport").
        separator (str): Separator token (e.g., "in").

    Returns:
        str: The mapped Arabic label for "{cone_1} {separator}", or an empty string if no mapping exists.
    """
    table_with_in = {
        "sport in": "الرياضة في",
    }
    con_1_in = f"{cone_1.strip()} {separator.strip()}"
    part_1_label = table_with_in.get(con_1_in, "")
    logger.debug(f"<<<< {con_1_in=}, {part_1_label=}")

    return part_1_label


@functools.lru_cache(maxsize=10000)
def resolve_part_1_label(country2, separator="", lab_type="type_label", with_years=False):
    """
    Resolve the Arabic label for the first part of a compound title given its English token and separator.

    Parameters:
        separator (str): The textual separator between parts (e.g., "in", "from", "to"); used to influence resolution for some tokens.
        country2 (str): The first English part to resolve (case-insensitive).

    Returns:
        str: The resolved Arabic label for `country2`, or an empty string if no mapping is found.

    Notes:
        - Special-case: when `country2` equals "women" and `separator` is "from", returns "نساء".

    Example:
        {"separator": " in ", "country2": "cultural depictions of competitors", "output": "تصوير ثقافي عن منافسون"},
    """
    if country2 == "women" and separator.strip() == "from":
        part_1_label = "نساء"
        logger.debug(f">> >> >> Make {country2=}.")
        return part_1_label

    country2_label = (
        ""
        or all_new_resolvers(country2)
        or get_pop_All_18(country2)
        or People_key.get(country2)
        or parties_resolver.get_parties_lab(country2)
        or team_work.resolve_clubs_teams_leagues(country2)
        or get_table_with_in(country2, separator)
        or get_from_pf_keys2(country2)
        or get_KAKO(country2)
        or _get_term_label(country2, "", lab_type=lab_type)
        or bys.get_by_label(country2)
        or get_and_label(country2)
        or (with_years_bot.Try_With_Years(country2) if with_years else "")
        or ""
    )

    return country2_label


def _resolve_war(resolved_label: str, part_2_normalized: str, part_1_normalized: str) -> str:
    """
    Return a corrected Arabic war label when appropriate.

    If `part_2_normalized` is a four-digit year and `part_1_normalized` equals `"war of"`,
    converts `"الحرب في {year}"` to `"حرب {year}"`. Otherwise returns `resolved_label` unchanged.

    Parameters:
        resolved_label (str): Current resolved Arabic label.
        part_2_normalized (str): Normalized second part (often a year).
        part_1_normalized (str): Normalized first part.

    Returns:
        str: The possibly modified label.
    """
    maren = re.match(r"\d\d\d\d", part_2_normalized)
    if maren:
        if part_1_normalized == "war of" and resolved_label == f"الحرب في {part_2_normalized}":
            resolved_label = f"حرب {part_2_normalized}"
            logger.info(f'<<lightpurple>> >>>> change cnt_la to "{resolved_label}".')

    return resolved_label


def make_cnt_lab(
    country: str,
    part_2_label: str,
    part_1_label: str,
    part_1_normalized: str,
    part_2_normalized: str,
    ar_separator: str,
) -> str:
    """
    Builds a final Arabic label by combining part_1_label and part_2_label and applying contextual adjustments and normalizations.

    Parameters:
        country (str): Original country string used to record mappings when applicable.
        part_2_label (str): Resolved label for the second part (right-hand side).
        part_1_label (str): Resolved label for the first part (left-hand side).
        part_1_normalized (str): Normalized form of the first part used to decide special formatting rules.
        part_2_normalized (str): Normalized form of the second part used to decide recording and war-related rewrites.
        ar_separator (str): Arabic separator to join the two parts (e.g., " في ", " إلى ", " لدى ").

    Description:
        - Concatenates part_1_label, ar_separator, and part_2_label to form an initial label.
        - For entries flagged as "new players" (checked via part_1_normalized), conditionally inserts "من " before part_2_label when it starts with "أصل ", otherwise appends " في" if not already present; and records the computed label for the country unless the part_2_normalized exists in the main resolver.
        - Applies predefined format mappings for specific part_1_normalized keys (e.g., politics/military patterns).
        - Collapses duplicated " في في " sequences and normalizes whitespace.
        - Calls internal war-resolution logic to rewrite phrases like "الحرب في {year}" to "حرب {year}" when applicable.
        - Removes a trailing " في " if present.

    Returns:
        str: The final, normalized Arabic label.
    """
    country2 = country.lower().strip()

    resolved_label = part_1_label + ar_separator + part_2_label
    in_players = check_key_new_players(part_1_normalized.lower())

    if in_players:
        if in_players:
            if part_2_label.startswith("أصل "):
                logger.info(f">>>>>> Add من to {part_1_normalized=} part_1_normalized in New_players:")
                resolved_label = f"{part_1_label}{ar_separator}من {part_2_label}"
            else:
                logger.info(f">>>>>> Add في to {part_1_normalized=} part_1_normalized in New_players:")
                if not resolved_label.strip().endswith(" في"):
                    resolved_label += " في "

        if not resolve_by_labels(part_2_normalized):
            # Films_O_TT[country2] = resolved_label
            add_to_Films_O_TT(country2, resolved_label)
        else:
            logger.info("<<lightblue>>>>>> part_2_normalized in By table main")

    if part_2_label:
        label_format_mappings = {
            "politics of {}": "سياسة {}",
            "military installations of": "منشآت {} العسكرية",
        }
        if part_1_normalized in label_format_mappings:
            logger.info(
                f'<<lightblue>>>>>> part_1_normalized in label_format_mappings "{label_format_mappings[part_1_normalized]}":'
            )
            resolved_label = label_format_mappings[part_1_normalized].format(part_2_label)

    # NOTE: important to fix bug like: [sport in ottoman] = "الرياضة في في الدولة العثمانية" !

    resolved_label = resolved_label.replace(" في في ", " في ")

    logger.info(f'<<lightpurple>> >>>> country 2_tit "{country2}": label: {resolved_label}')

    resolved_label = " ".join(resolved_label.strip().split())
    resolved_label = _resolve_war(resolved_label, part_2_normalized, part_1_normalized)

    if resolved_label.endswith(" في "):
        resolved_label = resolved_label[: -len(" في ")]

    return resolved_label


def separator_arabic_resolve(separator: str) -> str:
    """
    Map an English separator token to its Arabic equivalent, including surrounding spaces when appropriate.

    Parameters:
        separator (str): English separator token to map (e.g., "to", "on", "about", "based in").

    Returns:
        str: Arabic separator string (defaults to a single space if no mapping exists).
    """
    ar_separator = " "
    separator = separator.strip()

    if separator == "to":
        ar_separator = " إلى "
    elif separator == "on":
        ar_separator = " على "
    elif separator == "about":
        ar_separator = " عن "
    elif separator in translation_category_relations and separator != "by":
        ar_separator = f" {translation_category_relations[separator]} "
    elif separator == "based in":
        ar_separator = " مقرها في "

    return ar_separator


def make_parts_labels(part_1, part_2, separator, with_years) -> Tuple[str, str]:
    """
    Resolve Arabic labels for two text parts and return them as a pair.

    Attempts to derive each part's Arabic label from several resolvers and fallbacks; if either label cannot be resolved, returns two empty strings. When resolved, normalizes inputs and, depending on the English separator or trailing tokens, appends the Arabic preposition " في" to the first label for "in" contexts or prepends "من " to the second label for "from" contexts.

    Parameters:
        part_1 (str): The first text fragment to resolve (e.g., a role or type).
        part_2 (str): The second text fragment to resolve (e.g., a place or entity).
        separator (str): The English separator token between parts (affects Arabic preposition handling).
        with_years (bool): If true, allow an additional "with years" resolver when resolving part_2.

    Returns:
        Tuple[str, str]: (part_1_label, part_2_label) with resolved Arabic labels, or ("", "") if either could not be resolved.
    """
    part_2_label = resolve_part_1_label(part_2, with_years=with_years)

    if part_2_label == "" and "-" in part_2:
        part_2_label = resolve_part_1_label(part_2.replace("-", " "), with_years=with_years)

    part_1_label = resolve_part_1_label(part_1, separator)

    if part_1_label == "" and "-" in part_1:
        part_1_label = resolve_part_1_label(part_1.replace("-", " "), separator)

    if part_2_label == "" or part_1_label == "":
        logger.info(f">>>> XX--== <<lightgreen>> {part_1=}, {part_1_label=}, {part_2=}, {part_2_label=}")
        return "", ""

    part_1_normalized = part_1.strip().lower()
    part_2_normalized = part_2.strip().lower()

    if (separator.strip() == "in" or part_1_normalized.endswith(" in")) and (not part_1_normalized.endswith(" في")):
        logger.debug(f">>>> Add في to {part_1_label=}")
        part_1_label = f"{part_1_label} في"

    elif (separator.strip() == "from" or part_2_normalized.endswith(" from")) and (not part_2_label.endswith(" من")):
        logger.debug(f">>>> Add من to {part_2_label=}")
        part_2_label = f"من {part_2_label}"

    return part_1_label, part_2_label


def get_separator(country: str) -> str:
    """Get the separator from a country string.

    Args:
        country: The country string to check for separators

    Returns:
        The found separator or an empty string if none found
    """
    title_separators = [
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

    normalized_country = country.lower().strip()

    for sep in title_separators:
        separator = f" {sep} " if sep != "-of " else sep
        if separator in normalized_country:
            return separator

    return ""


def country_2_title_work(country: str, with_years: bool = True) -> str:
    separator = get_separator(country)

    if not separator:
        logger.info(f">>>> country_2_title_work <<red>> {separator=}")
        return ""

    part_1, part_2 = split_text_by_separator(separator, country)

    logger.info(f"2060 {part_1=}, {part_2=}, {separator=}")

    part_1_label, part_2_label = make_parts_labels(part_1, part_2, separator, with_years)

    if part_2_label == "" or part_1_label == "":
        logger.info(f">>>> XX--== <<lightgreen>> {part_1=}, {part_1_label=}, {part_2=}, {part_2_label=}")
        return ""

    part_1_normalized = part_1.strip().lower()
    part_2_normalized = part_2.strip().lower()

    logger.info(
        f">>>> XX--== <<lightgreen>> {part_1_normalized=}, {part_1_label=}, {part_2_normalized=}, {part_2_label=}"
    )

    if separator.strip() == "to" and (
        part_1_label.startswith("سفراء ") or part_1_normalized.strip() == "ambassadors of"
    ):
        ar_separator = " لدى "
    else:
        ar_separator = separator_arabic_resolve(separator)

    resolved_label = make_cnt_lab(
        country=country,
        part_2_label=part_2_label,
        part_1_label=part_1_label,
        part_1_normalized=part_1_normalized,
        part_2_normalized=part_2_normalized,
        ar_separator=ar_separator,
    )

    resolved_label = fix_minor(resolved_label, separator)

    return resolved_label


__all__ = [
    "country_2_title_work",
    "set_term_label_resolver",
]
