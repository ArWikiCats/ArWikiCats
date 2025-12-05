#!/usr/bin/python3
"""
Handles prefix and suffix processing for job categories.

This module provides functions to translate job category strings by processing
prefixes and suffixes, handling nationality conversions, and applying gender-specific
transformations.
"""

import functools
from typing import Optional

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import (
    By_table,
    change_male_to_female,
    Female_Jobs,
    FILM_PRODUCTION_COMPANY,
    jobs_mens_data,
    jobs_womens_data,
    PLAYERS_TO_MEN_WOMENS_JOBS,
    Mens_prefix,
    Mens_suffix,
    Nat_mens,
    People_key,
    replace_labels_2022,
    short_womens_jobs,
    SPORTS_KEYS_FOR_LABEL,
    womens_prefixes,
)

from ..lazy_data_bots.bot_2018 import get_pop_All_18


# Constants
_PEOPLE_SUFFIX = " people"
_WOMEN_SUFFIX = " women"


@functools.lru_cache(maxsize=1)
def _extend_By_table() -> dict[str, str]:
    """
    Extend the By_table dictionary with sports teams, people, and production companies.

    Returns:
        dict[str, str]: Mapping of English "by X" strings to Arabic translations.
    """
    result = {}

    # Add sports team mappings
    for sport_key, sport_label in SPORTS_KEYS_FOR_LABEL.items():
        english_key = f"by {sport_key.lower()} team"
        result[english_key] = f"حسب فريق {sport_label}"

    # Add people mappings
    for person_key, person_label in People_key.items():
        english_key = f"by {person_key.lower()}"
        result[english_key] = f"بواسطة {person_label}"

    # Add film production company mappings
    for company_key, company_label in FILM_PRODUCTION_COMPANY.items():
        english_key = f"by {company_key.lower()}"
        result[english_key] = f"بواسطة {company_label}"

    return result


def _strip_people_suffix(text: str) -> str:
    """
    Remove ' people' suffix and attempt to resolve nationality.

    Args:
        text: The text to process.

    Returns:
        str: The text with nationality resolved if possible, or original text without suffix.
    """
    if not text.endswith(_PEOPLE_SUFFIX):
        return text

    nationality = text[:-len(_PEOPLE_SUFFIX)]

    # Check if this is a known nationality
    if nationality in Nat_mens:
        return nationality

    return nationality


def _get_job_label(job_key: str) -> Optional[str]:
    """
    Retrieve job label from available data sources.

    Args:
        job_key: The job identifier to look up.

    Returns:
        Optional[str]: The corresponding label or None if not found.
    """
    return jobs_mens_data.get(job_key) or Nat_mens.get(job_key)


def _apply_gender_transformation(prefix_label: str, job_key: str) -> str:
    """
    Apply gender transformation if the job is in Female_Jobs and transformation exists.

    Args:
        prefix_label: The prefix label to potentially transform.
        job_key: The job key to check against Female_Jobs.

    Returns:
        str: The transformed prefix label if applicable, otherwise original.
    """
    if job_key in Female_Jobs and prefix_label in change_male_to_female:
        return change_male_to_female[prefix_label]
    return prefix_label


def _apply_label_replacement(label: str) -> str:
    """
    Apply label replacement if defined in replace_labels_2022.

    Args:
        label: The label to potentially replace.

    Returns:
        str: The replaced label if applicable, otherwise original.
    """
    if label in replace_labels_2022:
        replaced = replace_labels_2022[label]
        logger.debug(f'<<lightgreen>> Changed label to "{replaced}" via replace_labels_2022.')
        return replaced
    return label


@functools.lru_cache(maxsize=None)
def work_mens_prefix(category: str) -> str:
    """
    Process category string with male job prefixes.

    This function checks if the category starts with any known male job prefix,
    extracts the job portion, resolves it through nationality or job mappings,
    and formats the appropriate label.

    Args:
        category: The category string to process.

    Returns:
        str: The formatted Arabic label or empty string if no match found.
    """
    for prefix, prefix_label in Mens_prefix.items():
        prefix_with_space = f"{prefix} "

        if not category.startswith(prefix_with_space):
            continue

        # Extract the job part after the prefix
        job_part = category[len(prefix_with_space):]

        # Try to resolve nationality from "X people" format
        job_key = _strip_people_suffix(job_part).strip()

        logger.debug(f'<<lightblue>> Processing prefix "{prefix_with_space}": job_part="{job_part}", job_key="{job_key}"')

        # Get job label
        job_label = _get_job_label(job_key)
        if not job_label:
            continue

        # Apply gender transformation if needed
        final_prefix_label = _apply_gender_transformation(prefix_label, job_key)

        # Format and apply replacements
        label = final_prefix_label.format(job_label)
        label = _apply_label_replacement(label)

        if label.strip():
            logger.debug(f'<<lightblue>> Found label via prefix: "{label}" for category "{category}"')
            return label

    return ""


@functools.lru_cache(maxsize=None)
def work_mens_suffix(category: str) -> str:
    """
    Process category string with male job suffixes.

    This function checks if the category ends with any known male job suffix,
    extracts the nationality/job portion, and formats the appropriate label.

    Args:
        category: The category string to process.

    Returns:
        str: The formatted Arabic label or empty string if no match found.
    """
    for suffix, suffix_label in Mens_suffix.items():
        suffix_with_space = f" {suffix}"

        if not category.endswith(suffix_with_space):
            continue

        # Extract the part before the suffix
        job_part = category[:-len(suffix_with_space)]

        # Try to resolve nationality from "X people" format
        job_key = _strip_people_suffix(job_part).strip()

        logger.debug(f'<<lightblue>> Processing suffix "{suffix_with_space}": job_key="{job_key}"')

        # Try multiple sources for the label
        job_label = (
            Nat_mens.get(job_key) or
            get_pop_All_18(job_key) or
            get_pop_All_18(job_part) or
            ""
        )

        if job_label:
            label = suffix_label.format(job_label)

            if label.strip():
                logger.debug(f'<<lightblue>> Found label via suffix: "{label}" for category "{category}"')
                return label

    return ""


@functools.lru_cache(maxsize=None)
def mens_prefixes_work(category: str) -> str:
    """
    Process and retrieve the appropriate label for a male job category.

    This function takes a category string and attempts to find a matching Arabic
    label by checking multiple strategies in order:
    1. Direct lookup in By_table and extended By_table
    2. Direct lookup in jobs_mens_data
    3. Prefix matching and transformation
    4. Suffix matching and transformation

    The function normalizes input, handles nationality conversions (e.g., "X people"),
    applies gender transformations, and caches results for performance.

    Args:
        category: The category string representing a job title or category.

    Returns:
        str: The formatted Arabic label corresponding to the category, or empty string if no match.
    """
    logger.debug(f'<<lightblue>> === Start: mens_prefixes_work for "{category}"')

    # Check direct table lookups first
    by_table_extended = _extend_By_table()
    label = By_table.get(category) or by_table_extended.get(category)
    if label:
        logger.debug(f'<<lightblue>> Found in By_table: "{label}"')
        return label

    # Check direct job data lookup
    label = jobs_mens_data.get(category)
    if label:
        logger.debug(f'<<lightblue>> Found in jobs_mens_data: "{label}"')
        return label

    # Try prefix matching
    label = work_mens_prefix(category)
    if label:
        return label

    # Try suffix matching
    label = work_mens_suffix(category)
    if label:
        return label

    logger.debug(f'<<lightblue>> === End: no match found for "{category}"')
    return ""


@functools.lru_cache(maxsize=None)
def womens_prefixes_work(category: str) -> str:
    """
    Retrieve the women's job label based on the category string.

    This function processes the category string to determine if it matches any
    predefined women's job prefixes. It checks:
    1. Direct lookup in short_womens_jobs
    2. Prefix matching with women's job prefixes
    3. Handles special cases like "women's" and "women's-" prefixes

    The function also handles categories ending with " women" and attempts to
    resolve the job through various data sources.

    Args:
        category: The category string representing a job or title related to women.

    Returns:
        str: The corresponding Arabic job label or empty string if no match found.
    """
    # Direct lookup in short jobs
    label = short_womens_jobs.get(category)
    if label:
        logger.debug(f'<<lightblue>> Found in short_womens_jobs: "{label}"')
        return label

    # Strip " women" suffix if present
    processed_category = category
    if category.endswith(_WOMEN_SUFFIX):
        processed_category = category[:-len(_WOMEN_SUFFIX)]

    # Try prefix matching
    for prefix, prefix_label in womens_prefixes.items():
        # Build list of prefix variants to check
        prefix_variants = [f"{prefix} "]
        if prefix == "women's":
            prefix_variants.append("women's-")

        for prefix_variant in prefix_variants:
            if not processed_category.startswith(prefix_variant):
                continue

            # Extract job key after prefix
            job_key = processed_category[len(prefix_variant):]

            # Look up job label from women's data or player mappings
            job_label = (
                jobs_womens_data.get(job_key) or
                PLAYERS_TO_MEN_WOMENS_JOBS.get(job_key, {}).get("females", "")
            )

            logger.debug(
                f'<<lightblue>> Processing prefix "{prefix_variant}": '
                f'job_key="{job_key}", job_label="{job_label}"'
            )

            if job_label:
                label = prefix_label.format(job_label)
                logger.debug(f'<<lightblue>> Found label via prefix: "{label}"')
                return label

    logger.debug(f'<<lightblue>> No match found for "{category}"')
    return ""


__all__ = [
    "mens_prefixes_work",
    "womens_prefixes_work",
    "work_mens_suffix",
    "work_mens_prefix",
]
