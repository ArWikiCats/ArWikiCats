"""
LabsYearsFormat resolver.
"""

import functools

from ..helps import logger
from ..patterns_resolvers.categories_patterns.YEAR_PATTERNS import YEAR_DATA
from ..translations_formats import LabsYearsFormat

from ..time_resolvers.utils_time import fixing


@functools.lru_cache(maxsize=1)
def build_labs_years_object() -> LabsYearsFormat:
    category_templates = dict(YEAR_DATA)
    category_templates.update({
        "{year1}": "{year1}",
        "films in {year1}": "أفلام في {year1}",
        "{year1} films": "أفلام إنتاج {year1}",
    })
    labs_years_bot = LabsYearsFormat(
        category_templates=category_templates,
        year_param_placeholder="{year1}",
        year_param_name="year1",
        fixing_callback=fixing,
    )
    return labs_years_bot


def resolve_lab_from_years_patterns(category: str) -> str:
    """Resolve the label from year using LabsYearsFormat."""
    logger.debug(f"<<yellow>> start resolve_lab_from_years_patterns: {category=}")

    labs_years_bot = build_labs_years_object()
    _, from_year = labs_years_bot.lab_from_year(category)

    logger.info_if_or_debug(f"<<yellow>> end resolve_lab_from_years_patterns: {category=}, {from_year=}", from_year)
    return from_year


__all__ = [
    "build_labs_years_object",
    "resolve_lab_from_years_patterns",
]
