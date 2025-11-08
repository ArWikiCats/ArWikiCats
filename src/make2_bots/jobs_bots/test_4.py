"""Helpers used by the historical ``test_4`` jobs logic."""

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping

from ...ma_lists import All_Nat, Jobs_key_mens, Jobs_key_womens, Multi_sport_for_Jobs, Nat_mens
from ..jobs_bots.get_helps import get_con_3
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ..media_bots.film_keys_bot import Films
from ..o_bots import ethnic_bot
from .test4_bots.for_me import Work_for_me
from .test4_bots.t4_2018_jobs import test4_2018_Jobs
from .utils import cached_lookup, log_debug, normalize_cache_key

MULTI_SPORTS_CACHE: dict[str, str] = {}
NAT_MATCH_CACHE: dict[str, str] = {}
TEST4_2018_WITH_NAT_CACHE: dict[str, str] = {}

__all__ = ["Jobs_in_Multi_Sports", "jobs_in_multi_sports", "nat_match", "test4_2018_with_nat"]


def nat_match(
    category: str,
    out: bool = False,
    reference_category: str = "",
    tab: Mapping[str, str] | None = None,
) -> str:
    """Match a category string to a localized sentiment label."""

    del out, reference_category, tab  # Legacy parameters reserved for API compatibility

    cache_key = normalize_cache_key(category, "nat_match")
    return cached_lookup(
        NAT_MATCH_CACHE,
        (cache_key,),
        lambda: _resolve_nat_match(category),
    )


def _resolve_nat_match(category: str) -> str:
    """Resolve a nationality match without referencing caches."""

    category_lower = category.lower().replace("category:", "")
    log_debug('<<lightblue>> test_4: nat_match normalized_category :: "%s" ', category_lower)

    pattern = r"^anti\-(\w+) sentiment$"
    match = re.match(pattern, category_lower)
    if not match:
        return ""

    matched_country_key = match.group(1)
    log_debug('<<lightblue>> test_4: nat_match country_key :: "%s" ', matched_country_key)

    country_label_key = Nat_mens.get(matched_country_key, "")
    if not country_label_key:
        return ""

    country_label = f"مشاعر معادية لل{country_label_key}"
    log_debug('<<lightblue>> test_4: nat_match country_label :: "%s" ', country_label)
    return country_label


def test4_2018_with_nat(
    category: str,
    out: bool = False,
    reference_category: str = "",
    tab: Mapping[str, str] | None = None,
) -> str:
    """Retrieve legacy job labels enriched with nationality context."""

    del out, tab

    cache_key = normalize_cache_key(category, reference_category, "test4_2018_with_nat")
    return cached_lookup(
        TEST4_2018_WITH_NAT_CACHE,
        (cache_key,),
        lambda: _resolve_test4_2018_with_nat(category, reference_category),
    )


def _resolve_test4_2018_with_nat(category: str, reference_category: str) -> str:
    """Perform the heavy lifting for :func:`test4_2018_with_nat`."""

    log_debug(
        "<<lightyellow>>>> test4_2018_with_nat >> category:(%s), reference_category:%s..",
        category,
        reference_category,
    )

    normalized_category = re.sub(r"[-_]", " ", category.lower())

    label = Jobs_key_womens.get(normalized_category, "")
    if not label:
        label = Jobs_key_mens.get(normalized_category, "")

    key, nationality = get_con_3(normalized_category, All_Nat, "nat")
    if key:
        label = _resolve_label_from_context(
            label,
            normalized_category,
            nationality,
            key,
            reference_category,
        )

    if not label:
        label = priffix_Mens_work(normalized_category) or Women_s_priffix_work(normalized_category)

    if not label:
        label = Films(normalized_category, "", "", reference_category=reference_category)

    if label and key:
        log_debug(
            '<<lightblue>> test4_2018_with_nat startswith(%s),con_3:"%s"',
            "",
            key,
        )
    log_debug('<<lightblue>> test_4: test4_2018_with_nat :: "%s" ', label)
    return label


def _resolve_label_from_context(
    label: str,
    category: str,
    nationality: str,
    key: str,
    reference_category: str,
) -> str:
    """Derive label using helper modules when a nationality key is known."""

    if label:
        return label

    for resolver in _context_resolvers(reference_category):
        label = resolver(category, nationality, key)
        if label:
            return label
    return ""


def _context_resolvers(reference_category: str) -> Iterable:
    """Yield resolver callables for context dependent label lookups."""

    return (
        Work_for_me,
        lambda category, nat, key: Films(category, nat, key, reference_category=reference_category),
        ethnic_bot.Ethnic,
        nat_match,
    )


def jobs_in_multi_sports(
    category: str,
    out: bool = False,
    tab: Mapping[str, str] | None = None,
) -> str:
    """Retrieve job information related to multiple sports based on the category."""

    del out, tab

    normalized_category = re.sub(r"_", " ", category)
    cache_key = normalize_cache_key(normalized_category, "multi_sports")
    return cached_lookup(
        MULTI_SPORTS_CACHE,
        (cache_key,),
        lambda: _resolve_multi_sports(normalized_category),
    )


def Jobs_in_Multi_Sports(  # noqa: N802 - legacy name
    category: str,
    out: bool = False,
    tab: Mapping[str, str] | None = None,
) -> str:
    """Compatibility wrapper returning :func:`jobs_in_multi_sports`."""

    return jobs_in_multi_sports(category, out=out, tab=tab)


def _resolve_multi_sports(category: str) -> str:
    """Compute the label for :func:`jobs_in_multi_sports`."""

    log_debug("<<lightyellow>>>> Jobs_in_Multi_Sports >> category:(%s) ", category)

    job_key = ""
    game_label = ""
    for sport_prefix, potential_game_label in Multi_sport_for_Jobs.items():
        prefix = f"{sport_prefix} "
        if category.startswith(prefix):
            job_key = category[len(prefix) :].lower()
            game_label = potential_game_label
            log_debug(
                'Jobs_in_Multi_Sports category.startswith(game_prefix: "%s") game_label:"%s",job:"%s". ',
                prefix,
                game_label,
                job_key,
            )
            break

    if not job_key or not game_label:
        return ""

    job_label = test4_2018_Jobs(job_key)
    result = f"{job_label} في {game_label}" if job_label else ""
    log_debug('end Jobs_in_Multi_Sports "%s" , primary_label:"%s"', category, result)
    return result
