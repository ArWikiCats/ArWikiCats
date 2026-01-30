"""
Time pattern resolver using LabsYearsFormat.
This module provides functionality to resolve category labels that follow
complex temporal patterns (years, decades, centuries) using predefined templates.
"""

import functools

import logging
from ..time_formats.utils_time import standardize_time_phrases
from ..translations_formats import LabsYearsFormat
from .categories_patterns.YEAR_PATTERNS import YEAR_DATA

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=1)
def build_labs_years_object() -> LabsYearsFormat:
    category_templates = dict(YEAR_DATA)
    category_templates.update(
        {
            "{year1}": "{year1}",
            "films in {year1}": "أفلام في {year1}",
            "{year1} films": "أفلام إنتاج {year1}",
        }
    )
    labs_years_bot = LabsYearsFormat(
        category_templates=category_templates,
        key_param_placeholder="{year1}",
        year_param_name="year1",
        fixing_callback=standardize_time_phrases,
    )
    return labs_years_bot


def resolve_lab_from_years_patterns(category: str) -> str:
    """
    Resolve a category label that encodes a year, decade, or century pattern into its standardized label.

    Parameters:
        category (str): The input category string that may contain a year-based temporal pattern.

    Returns:
        resolved_label (str): The standardized category label for the detected year/decade/century pattern, or an empty string if no year-based pattern could be resolved.
    """
    logger.debug(f"<<yellow>> start {category=}")

    labs_years_bot = build_labs_years_object()
    _cat_year, from_year = labs_years_bot.lab_from_year(category)

    # NOTE: causing some issues with years and decades
    # [Category:1930s Japanese novels] : "تصنيف:روايات يابانية في عقد 1930",
    # [Category:1930s Japanese novels] : "تصنيف:روايات يابانية في عقد 1930",

    # if not from_year and _cat_year:
    # labs_years_bot.lab_from_year_add(category, from_year, en_year=_cat_year)

    logger.info(f"<<yellow>> end {category=}, {from_year=}")
    return from_year


__all__ = [
    "build_labs_years_object",
    "resolve_lab_from_years_patterns",
]
