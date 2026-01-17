"""
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

from .jobs_and_genders_resolver import resolve_nat_genders_pattern_v2

__all__ = [
    "resolve_nat_genders_pattern_v2",
]
