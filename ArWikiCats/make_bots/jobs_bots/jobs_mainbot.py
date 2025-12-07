#!/usr/bin/python3
"""
Jobs nationality labeling module.

This module provides functionality to generate gender-aware job labels combining
nationality and occupation data. It handles special cases like expatriates,
gender-specific templates, and Arabic language formatting conventions.
"""

import functools
from typing import Optional

from ...helps.log import logger
from ...translations import (
    NAT_BEFORE_OCC,
    Nat_mens,
    Nat_Womens,
    jobs_mens_data,
    short_womens_jobs,
)
from .prefix_bot import mens_prefixes_work, womens_prefixes_work

# ============================================================================
# Constants
# ============================================================================

# Gender keys for dictionary lookups
GENDER_MALE = "males"
GENDER_FEMALE = "females"

# Special category keywords
CATEGORY_PEOPLE = "people"
CATEGORY_WOMEN = "women"
CATEGORY_FEMALE = "female"
CATEGORY_WOMENS_POSSESSIVE = "women's"

# Prefix to strip from category suffix
PEOPLE_PREFIX = "people "

# Arabic text constants
ARABIC_PREFIX_BY = "حسب"
EXPATRIATE_MALE = "مغتربون"
EXPATRIATE_FEMALE = "مغتربات"

# Nationality placeholder in templates
NATO_PLACEHOLDER = "{nato}"

# Special job templates with nationality placeholders
GENDER_NATIONALITY_TEMPLATES = {
    "eugenicists": {
        GENDER_MALE: "علماء {nato} متخصصون في تحسين النسل",
        GENDER_FEMALE: "عالمات {nato} متخصصات في تحسين النسل",
    },
    "politicians who committed suicide": {
        GENDER_MALE: "سياسيون {nato} أقدموا على الانتحار",
        GENDER_FEMALE: "سياسيات {nato} أقدمن على الانتحار",
    },
    "contemporary artists": {
        GENDER_MALE: "فنانون {nato} معاصرون",
        GENDER_FEMALE: "فنانات {nato} معاصرات",
    },
}

# List of female-specific categories
FEMALE_CATEGORIES = [CATEGORY_WOMEN, CATEGORY_FEMALE, CATEGORY_WOMENS_POSSESSIVE]

# Expatriate terms for normalization
EXPATRIATE_TERMS = [EXPATRIATE_MALE, EXPATRIATE_FEMALE]


# ============================================================================
# Helper Functions
# ============================================================================


def _normalize_expatriate_label(
    country_label: str,
    nationality_label: str,
    current_label: str,
) -> str:
    """
    Normalize expatriate phrasing in country labels.

    Handles special cases where labels contain expatriate terms (مغتربون/مغتربات)
    and ensures proper formatting with nationality labels.

    Args:
        country_label: Original country label from translation data
        nationality_label: Nationality adjective (e.g., مصريون)
        current_label: Current constructed label to potentially modify

    Returns:
        Normalized label with proper expatriate phrasing
    """
    for expatriate_term in EXPATRIATE_TERMS:
        suffix = f" {expatriate_term}"

        if country_label.endswith(suffix):
            # Remove expatriate term from end and reconstruct
            base_label = country_label[: -len(expatriate_term)].strip()
            return f"{base_label} {nationality_label} {expatriate_term}"

        if current_label.endswith(suffix):
            # Keep expatriate term at the end
            base_label = current_label[: -len(expatriate_term)].strip()
            return f"{base_label} {expatriate_term}"

    return current_label


def _construct_country_nationality_label(
    country_label: str,
    nationality_label: str,
    category_suffix: str,
) -> str:
    """
    Combine country and nationality labels according to Arabic grammar rules.

    The word order depends on context:
    - "nationality country" when country_label starts with "حسب" (by)
    - "nationality country" when category is in NAT_BEFORE_OCC list
    - "country nationality" otherwise (default)

    Args:
        country_label: Country or occupation label
        nationality_label: Nationality adjective
        category_suffix: Category identifier for rule lookup

    Returns:
        Properly formatted combined label
    """
    # Check if nationality should come before occupation
    should_reverse = (
        country_label.startswith(ARABIC_PREFIX_BY)
        or category_suffix in NAT_BEFORE_OCC
    )

    if should_reverse:
        return f"{nationality_label} {country_label}"

    return f"{country_label} {nationality_label}"


def _apply_gender_nationality_template(
    gender_key: str,
    category_suffix: str,
    nationality_label: str,
) -> Optional[str]:
    """
    Apply a gender-specific nationality template if available.

    Some occupations have special templates that include the nationality
    placeholder {nato} which gets replaced with the actual nationality.

    Args:
        gender_key: Either "males" or "females"
        category_suffix: Category key to look up template
        nationality_label: Nationality to substitute into template

    Returns:
        Formatted label if template exists, None otherwise
    """
    template = GENDER_NATIONALITY_TEMPLATES.get(category_suffix, {}).get(gender_key, "")

    if template and NATO_PLACEHOLDER in template:
        formatted_label = template.format(nato=nationality_label)
        logger.debug(
            f"<<lightblue>> Applied template for [{gender_key}]: "
            f"has {NATO_PLACEHOLDER} -> {formatted_label}"
        )
        return formatted_label

    return None


def _build_gender_occupation_label(
    gender_key: str,
    category_suffix: str,
    nationality_label: str,
    country_label: str,
) -> str:
    """
    Build a complete gender-aware occupation label.

    This function coordinates the label building process:
    1. Check for special templates with nationality placeholders
    2. If no template, construct from country and nationality labels
    3. Apply expatriate normalization if needed

    Args:
        gender_key: Either "males" or "females"
        category_suffix: Category identifier
        nationality_label: Nationality adjective
        country_label: Country or occupation label

    Returns:
        Complete formatted label, or empty string if not possible
    """
    # Try to use a special template first
    template_label = _apply_gender_nationality_template(
        gender_key, category_suffix, nationality_label
    )
    if template_label:
        return template_label

    # No template or country label available
    if not country_label:
        return ""

    # Construct the label from components
    constructed_label = _construct_country_nationality_label(
        country_label, nationality_label, category_suffix
    )

    # Apply expatriate normalization
    final_label = _normalize_expatriate_label(
        country_label, nationality_label, constructed_label
    )

    logger.debug(
        f'\t<<lightblue>> Built {gender_key} occupation label: "{final_label}"'
    )

    return final_label


def _get_nationality_label(
    country_prefix: str,
    manual_override: str,
    nationality_dict: dict[str, str],
    should_lookup: bool,
) -> str:
    """
    Retrieve nationality label with fallback logic.

    Args:
        country_prefix: Country identifier to look up
        manual_override: Manual nationality label (takes precedence)
        nationality_dict: Dictionary to look up nationality
        should_lookup: Whether to perform dictionary lookup

    Returns:
        Nationality label or empty string
    """
    if manual_override:
        return manual_override

    if should_lookup:
        return nationality_dict.get(country_prefix, "")

    return ""


def _normalize_category_suffix(category_suffix: str) -> str:
    """
    Normalize category suffix by trimming and standardizing.

    Args:
        category_suffix: Raw category suffix

    Returns:
        Normalized category suffix (lowercase, trimmed, prefix removed)
    """
    normalized = category_suffix.strip().lower()

    # Remove "people " prefix if present
    if normalized.startswith(PEOPLE_PREFIX):
        normalized = normalized[len(PEOPLE_PREFIX):]

    return normalized


def _get_occupation_label_for_gender(
    category_suffix: str,
    is_male: bool,
) -> str:
    """
    Retrieve occupation label for specific gender.

    Args:
        category_suffix: Normalized category identifier
        is_male: True for male, False for female

    Returns:
        Occupation label or empty string
    Examples:
        >>> _get_occupation_label_for_gender("writers", is_male=True)
        "كتاب رجال"

        >>> _get_occupation_label_for_gender('female sports coaches', is_male=True)
        'مدربات رياضة'

        >>> _get_occupation_label_for_gender("actresses", is_male=False)
        "ممثلات نساء"
    """
    if is_male:
        return (
            jobs_mens_data.get(category_suffix, "")
            or mens_prefixes_work(category_suffix)
            or ""
        )
    else:
        return (
            short_womens_jobs.get(category_suffix, "")
            or womens_prefixes_work(category_suffix)
            or ""
        )


# ============================================================================
# Main Public Function
# ============================================================================

def _handle_male_label(country_prefix, males, normalized_suffix, find_nats) -> str:
    male_nationality = _get_nationality_label(
        country_prefix, males, Nat_mens, find_nats
    )

    if not male_nationality:
        return ""

    # Special case: generic "people" category
    if normalized_suffix == CATEGORY_PEOPLE:
        return f"أعلام {male_nationality}"

    # Get occupation label and build complete label
    male_occupation = _get_occupation_label_for_gender(normalized_suffix, is_male=True)
    logger.debug(f"{male_occupation=}, {normalized_suffix=}")

    male_label = _build_gender_occupation_label(
        GENDER_MALE, normalized_suffix, male_nationality, male_occupation
    )

    return male_label


def _handle_female_label(country_prefix, females, normalized_suffix, find_nats) -> str:

    female_nationality = _get_nationality_label(
        country_prefix, females, Nat_Womens, find_nats
    )

    if not female_nationality:
        return ""

    # Special case: female-specific categories
    if normalized_suffix in FEMALE_CATEGORIES:
        return female_nationality

    # Get occupation label and build complete label

    female_occupation = _get_occupation_label_for_gender(normalized_suffix, is_male=False)
    logger.debug(f"{female_occupation=}, {normalized_suffix=}")

    female_label = _build_gender_occupation_label(
        GENDER_FEMALE, normalized_suffix, female_nationality, female_occupation
    )

    return female_label


@functools.lru_cache(maxsize=None)
def jobs_with_nat_prefix(
    cate: str,
    country_prefix: str,
    category_suffix: str,
    males: str = "",
    females: str = "",
    find_nats: bool = True,
) -> str:
    """
    Generate gender-aware job labels combining nationality and occupation.

    This is the main entry point for creating localized job category labels.
    It handles both male and female variants, special templates, and Arabic
    language conventions.

    The function uses LRU cache for performance optimization, storing results
    of previous calls to avoid redundant processing.

    Processing flow:
    1. Normalize the category suffix
    2. Try to generate a male-gendered label
    3. If no male label, try female-gendered label
    4. Return the first successful match

    Args:
        cate: Full category name (for logging/context)
        country_prefix: Country identifier for nationality lookup
        category_suffix: Occupation/category identifier
        males: Manual override for male nationality label
        females: Manual override for female nationality label
        save_result: Whether to persist result (legacy parameter)
        find_nats: Whether to look up nationality in dictionaries

    Returns:
        Formatted job label in Arabic, or empty string if no match found

    Examples:
        >>> jobs_with_nat_prefix("", "egypt", "writers", find_nats=True)
        "كتاب مصريون"

        >>> jobs_with_nat_prefix("", "usa", "people", find_nats=True)
        "أمريكيون"
    """
    # Normalize input
    normalized_suffix = _normalize_category_suffix(category_suffix)

    logger.debug(f"<<lightblue>> jobs_with_nat_prefix: {cate=}, {country_prefix=}, {normalized_suffix=}")

    # Try to build male-gendered label
    male_label = _handle_male_label(country_prefix, males, normalized_suffix, find_nats)
    if male_label:
        return male_label

    # Try to build female-gendered label
    female_label = _handle_female_label(country_prefix, females, normalized_suffix, find_nats)
    if female_label:
        return female_label

    # No match found
    return ""


# ============================================================================
# Legacy Function Aliases (for backward compatibility)
# ============================================================================


def fix_expatriates(country_lab: str, country_label: str, nat_lab: str) -> str:
    """Legacy function - use _normalize_expatriate_label instead."""
    return _normalize_expatriate_label(country_label, nat_lab, country_lab)


def create_country_lab(country_label: str, nat_lab: str, category_suffix: str) -> str:
    """Legacy function - use _construct_country_nationality_label instead."""
    return _construct_country_nationality_label(country_label, nat_lab, category_suffix)


def country_lab_mens_womens(
    jender_key: str,
    category_suffix: str,
    nat_lab: str,
    country_label: str,
) -> str:
    """Legacy function - use _build_gender_occupation_label instead."""
    return _build_gender_occupation_label(jender_key, category_suffix, nat_lab, country_label)


MEN_WOMENS_WITH_NATO = GENDER_NATIONALITY_TEMPLATES
