"""
Package for resolving gender-specific category labels.
This package provides specialized resolvers to handle masculine and feminine
forms of job titles and sports roles, ensuring idiomatic Arabic translations.

Translation strategy for category labels (current vs. target with `genders_resolvers`)

Goal:
Improve Arabic category labels by removing weak/redundant gender markers (e.g., "رجال", "ذكور", "السيدات")
and enforcing consistent, idiomatic gender handling using `genders_resolvers`.

Current approach (problematic examples):
- "yemeni softball players"         -> "لاعبو كرة لينة يمنيون"
- "men's softball players"          -> "لاعبو كرة لينة رجال"          # weak label
- "yemeni male softball players"    -> "لاعبو كرة لينة يمنيون ذكور"    # weak label
- "yemeni women's softball players" -> "لاعبات كرة لينة السيدات يمنيات" # weak label
- "women's softball players"        -> "لاعبات كرة لينة للسيدات"       # weak label

Target approach (using `genders_resolvers`):
- Non-gendered categories -> inclusive wording (men + women).
- Men's categories        -> masculine form only, without extra markers.
- Women's categories      -> feminine form only, without "السيدات".

Target examples:
- "yemeni softball players"         -> "لاعبو ولاعبات كرة لينة يمنيون"
- "men's softball players"          -> "لاعبو كرة لينة"
- "yemeni male softball players"    -> "لاعبو كرة لينة يمنيون"
- "yemeni women's softball players" -> "لاعبات كرة لينة يمنيات"
- "women's softball players"        -> "لاعبات كرة لينة"
"""

import functools

from ...helps import getLogger
from .jobs_and_genders_resolver import genders_jobs_resolver
from .sports_and_genders_resolver import genders_sports_resolver

logger = getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def resolve_nat_genders_pattern_v2(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_nat_genders_pattern_v2: {category=}")

    result = genders_sports_resolver(category) or genders_jobs_resolver(category) or ""
    logger.info_if_or_debug(f"<<yellow>> end resolve_nat_genders_pattern_v2: {category=}, {result=}", result)

    return result


__all__ = [
    "resolve_nat_genders_pattern_v2",
]
