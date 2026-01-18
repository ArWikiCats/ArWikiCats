"""
# isort:skip_file
"""
from __future__ import annotations
import functools

from . import with_years_bot
from .o_bots import univer
from .ma_bots.country_bot import event2_d2
from . import event_lab_bot
from .ma_bots2.year_or_typeo import label_for_startwith_year_or_typeo
from .ma_bots import ye_ts_bot


@functools.lru_cache(maxsize=None)
def legacy_resolvers(changed_cat) -> str:
    category_lab = (
        univer.te_universities(changed_cat)
        or event2_d2(changed_cat)
        or with_years_bot.Try_With_Years2(changed_cat)
        or label_for_startwith_year_or_typeo(changed_cat)
        or ""
    )

    if not category_lab:
        category_lab = event_lab_bot.event_Lab(changed_cat)

    if not category_lab:
        category_lab = ye_ts_bot.translate_general_category(changed_cat)
    return category_lab


__all__ = [
    "legacy_resolvers",
]
