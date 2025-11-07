"""Prefix helpers for converting job related categories into labels."""

from __future__ import annotations

from ...ma_lists import By_table, Female_Jobs, Jobs_key_mens, Jobs_key_womens, Mens_priffix, Mens_suffix, Nat_mens, Women_s_priffix, change_male_to_female, replace_labels_2022, womens_Jobs_2017
from ..matables_bots.bot_2018 import pop_All_2018
from .utils import cached_lookup, log_debug, normalize_cache_key

PRIFFIX_MEN_CACHE: dict[str, str] = {}
PRIFFIX_WOMEN_CACHE: dict[str, str] = {}

__all__ = ["Women_s_priffix_work", "priffix_Mens_work"]


def priffix_Mens_work(con_33: str) -> str:  # noqa: N802 - legacy name
    """Process and retrieve the appropriate label for a given input string."""

    cache_key = normalize_cache_key(con_33)
    return cached_lookup(
        PRIFFIX_MEN_CACHE,
        (cache_key,),
        lambda: _resolve_mens_prefix(con_33),
    )


def Women_s_priffix_work(con_3: str) -> str:  # noqa: N802 - legacy name
    """Retrieve the women's prefix work label based on the input string."""

    cache_key = normalize_cache_key(con_3)
    return cached_lookup(
        PRIFFIX_WOMEN_CACHE,
        (cache_key,),
        lambda: _resolve_womens_prefix(con_3),
    )


def _resolve_mens_prefix(con_33: str) -> str:
    """Compute the prefix for male job categories without caching."""

    log_debug('<<lightblue>> --- start: priffix_Mens_work :"%s"', con_33)
    direct_match = By_table.get(con_33, "") or Jobs_key_mens.get(con_33, "")
    if direct_match:
        if direct_match in replace_labels_2022:
            direct_match = replace_labels_2022[direct_match]
        if Jobs_key_mens.get(con_33):
            log_debug('<<lightblue>> Jobs_key_mens: con_33_lab:"%s"', direct_match)
        return direct_match

    derived_label = _match_prefix_with_table(con_33)
    if derived_label:
        return derived_label

    suffix_label = _match_suffix(con_33)
    if suffix_label:
        return suffix_label

    log_debug('<<lightblue>> ----- end: priffix_Mens_work :con_33_lab:"%s",con_33:"%s"..', "", con_33)
    return ""


def _match_prefix_with_table(con_33: str) -> str:
    """Try to match male prefixes using ``Mens_priffix`` definitions."""

    for prefix, prefix_label in Mens_priffix.items():
        token = f"{prefix} "
        if not con_33.startswith(token):
            continue

        remainder = con_33[len(token) :]
        normalized_remainder = _strip_people_suffix(remainder)
        log_debug('<<lightblue>> con_33.startswith pri ("%s"), con_88:"%s"', token, normalized_remainder)

        remainder_label = Jobs_key_mens.get(normalized_remainder, "") or Nat_mens.get(normalized_remainder, "")
        if not remainder_label:
            continue

        replacement_template = prefix_label
        if normalized_remainder in Female_Jobs and prefix_label in change_male_to_female:
            replacement_template = change_male_to_female[prefix_label]
        label = replacement_template.format(remainder_label)
        if label in replace_labels_2022:
            label = replace_labels_2022[label]
            log_debug('<<lightgreen>> change con_33_lab to "%s" replace_labels_2022.', label)
        return label
    return ""


def _match_suffix(con_33: str) -> str:
    """Try to match male suffix patterns using ``Mens_suffix``."""

    for suffix, suffix_template in Mens_suffix.items():
        expected_suffix = f" {suffix}"
        if not con_33.endswith(expected_suffix):
            continue

        leading = con_33[: -len(expected_suffix)]
        normalized_leading = _strip_people_suffix(leading)
        nat_label = Nat_mens.get(normalized_leading, "")
        if not nat_label:
            nat_label = pop_All_2018.get(normalized_leading) or pop_All_2018.get(leading, "")
        if not nat_label:
            continue

        log_debug(
            '<<lightblue>> con_33.startswith_suffix2("%s"), con_88_lab:"%s"',
            expected_suffix,
            nat_label,
        )
        return suffix_template.format(nat_label)
    return ""


def _resolve_womens_prefix(con_3: str) -> str:
    """Compute the prefix for female job categories without caching."""

    direct_match = Jobs_key_womens.get(con_3, "")
    if direct_match:
        return direct_match

    candidate = con_3[: -len(" women")] if con_3.endswith(" women") else con_3
    for prefix, template in Women_s_priffix.items():
        token = "women's-" if prefix == "women's" else f"{prefix} "
        if not candidate.startswith(token):
            continue
        suffix = candidate[len(token) :]
        lookup = womens_Jobs_2017.get(suffix, "")
        log_debug(
            '<<lightblue>> con_33.startswith_Wriff2("%s"),con_4:"%s", con_8_Wb:"%s"',
            token,
            suffix,
            lookup,
        )
        if lookup:
            return template.format(lookup)
    return ""


def _strip_people_suffix(value: str) -> str:
    """Remove trailing ``"people"`` suffix while keeping nationality hints."""

    if value.endswith(" people"):
        nationality = value[: -len(" people")]
        if Nat_mens.get(nationality):
            return nationality.strip()
    return value.strip()
