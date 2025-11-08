"""Primary logic for generating job labels."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Callable

from ...ma_lists import Jobs_key_mens, Jobs_key_womens, Men_Womens_with_nato, Nat_Before_Occ, Nat_mens, Nat_Womens
from .priffix_bot import Women_s_priffix_work, priffix_Mens_work
from .utils import cached_lookup, log_debug, normalize_cache_key

JOBS_CACHE: dict[str, str] = {}

_SuffixAdjuster = Callable[[str, str], str]

WOMEN_ALIASES = {"women", "female", "women's"}
GENDER_SUFFIXES = (" مغتربون", " مغتربات")

__all__ = ["Jobs", "Jobs2", "jobs", "jobs_secondary"]


def jobs_secondary(category: str, country: str, key: str) -> str:
    """Return a secondary job label for men.

    Args:
        category: The raw category label.
        country: The ISO-like key identifying the country.
        key: The job key that should be matched against ``Jobs_key_mens``.

    Returns:
        The formatted country label, or an empty string when no match exists.
    """

    key_label = Jobs_key_mens.get(key, "")
    if key_label and Nat_mens.get(country):
        label = f"{key_label} {Nat_mens[country]}"
        log_debug("<<lightblue>> jobs_secondary produced label: %s", label)
        return label
    return ""


def jobs(
    category: str,
    country: str,
    key: str,
    *,
    category_type: str = "",
    overrides: Mapping[str, str] | None = None,
) -> str:
    """Retrieve job labels based on category and country.

    Args:
        category: The category of the job.
        country: The starting country for the job label.
        key: Additional context for the job label.
        category_type: An optional type parameter. Defaults to an empty string.
        overrides: Optional mapping providing explicit ``"mens"`` or
            ``"womens"`` labels.

    Returns:
        The generated job label based on the input parameters.
    """

    cache_key = normalize_cache_key(category, country, category_type, key)
    return cached_lookup(
        JOBS_CACHE,
        (cache_key,),
        lambda: _resolve_job_label(category, country, key, category_type=category_type, overrides=overrides),
    )


def _resolve_job_label(
    category: str,
    country: str,
    key: str,
    *,
    category_type: str,
    overrides: Mapping[str, str] | None,
) -> str:
    """Resolve job labels without touching the cache layer."""

    log_debug(
        '<<lightblue>> jobs: category: "%s", country: "%s", key: "%s"',
        category,
        country,
        key,
    )

    overrides = overrides or {}
    normalized_key = key[len("people ") :].strip() if key.startswith("people ") else key

    label = _build_gendered_label(
        category=category,
        country=country,
        key=key,
        normalized_key=normalized_key,
        overrides=overrides,
    )

    if label:
        return label

    label = _build_gendered_label(
        category=category,
        country=country,
        key=key,
        normalized_key=normalized_key,
        overrides=overrides,
        feminine=True,
    )

    return label


def _build_gendered_label(
    *,
    category: str,
    country: str,
    key: str,
    normalized_key: str,
    overrides: Mapping[str, str],
    feminine: bool = False,
) -> str:
    """Construct the gender-specific portion of the label."""

    nat_lookup = Nat_Womens if feminine else Nat_mens
    override_key = "womens" if feminine else "mens"
    nat_label = overrides.get(override_key) or nat_lookup.get(country, "")

    if not nat_label:
        return ""

    if feminine and key.strip() in WOMEN_ALIASES:
        return nat_label

    prefix = Jobs_key_womens.get(key, "") if feminine else Jobs_key_mens.get(key, "")
    if not prefix:
        prefix = Women_s_priffix_work(key) if feminine else priffix_Mens_work(key)

    if not prefix:
        return ""

    label = _format_label(prefix, nat_label, feminine=feminine)

    if not feminine:
        label = _apply_mens_rules(label, nat_label, prefix, key, normalized_key, category)
    else:
        label = _apply_womens_rules(label, nat_label, prefix)

    return label


def _format_label(prefix: str, nat_label: str, *, feminine: bool) -> str:
    """Format the label with the nationality, respecting placeholders."""

    if "{nato}" in prefix:
        return prefix.format(nato=nat_label)
    if prefix.startswith("حسب"):
        return f"{nat_label} {prefix}"
    return f"{prefix} {nat_label}"


def _apply_mens_rules(
    label: str,
    nat_label: str,
    prefix: str,
    key: str,
    normalized_key: str,
    category: str,
) -> str:
    """Apply the men-specific adjustments and suffix handling."""

    if key.strip() in Nat_Before_Occ or normalized_key.strip() in Nat_Before_Occ:
        label = f"{nat_label} {prefix}"

    nato_template = Men_Womens_with_nato.get(key, {}).get("mens", "")
    if "{nato}" in nato_template:
        label = nato_template.format(nato=nat_label)
        log_debug('<<lightblue>> Men_Womens_with_nato template applied: "%s"', label)

    for suffix in GENDER_SUFFIXES:
        if prefix.endswith(suffix):
            base_prefix = prefix[: -len(suffix)]
            label = f"{base_prefix} {nat_label}{suffix}"
            break

    log_debug('\t<<lightblue>> men job label produced for "%s": "%s"', category, label)
    return label


def _apply_womens_rules(label: str, nat_label: str, prefix: str) -> str:
    """Apply transformations specific to women's labels."""

    for suffix in GENDER_SUFFIXES:
        if prefix.endswith(suffix):
            base_prefix = prefix[: -len(suffix)]
            return f"{base_prefix} {nat_label}{suffix}"
    return label


# Backwards compatible aliases -------------------------------------------------


def Jobs2(cate: str, Start: str, con_3: str) -> str:  # noqa: N802 - legacy name
    """Compatibility wrapper for historical API usage."""

    return jobs_secondary(cate, Start, con_3)


def Jobs(  # noqa: N802 - legacy name
    cate: str,
    Start: str,
    con_3: str,
    Type: str = "",
    tab: Mapping[str, str] | None = None,
) -> str:
    """Compatibility wrapper around :func:`jobs`."""

    return jobs(cate, Start, con_3, category_type=Type, overrides=tab)
