"""
Labs Years processing module.
"""

import functools

from ..helps import logger
from .labs_years import LabsYears

YEAR_PARAM = "{year1}"


@functools.lru_cache(maxsize=1)
def build_labs_years_object() -> LabsYears:
    labs_years_bot = LabsYears()
    return labs_years_bot


def resolve_lab_from_years_patterns(category: str) -> str:
    """Resolve the label from year using LabsYears."""
    logger.debug(f"<<yellow>> start resolve_lab_from_years_patterns: {category=}")

    labs_years_bot = build_labs_years_object()
    _, from_year = labs_years_bot.lab_from_year(category)

    logger.info_if_or_debug(f"<<yellow>> end resolve_lab_from_years_patterns: {category=}, {from_year=}", from_year)
    return from_year
