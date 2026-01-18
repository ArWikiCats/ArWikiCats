"""

"""

from __future__ import annotations

import functools

from . import event_lab_bot, with_years_bot
from .ma_bots import ye_ts_bot
from .ma_bots2.year_or_typeo import label_for_startwith_year_or_typeo
from .ma_bots.country_bot import event2_d2
from .o_bots import univer


@functools.lru_cache(maxsize=None)
def legacy_resolvers(changed_cat) -> str:
    """Wrap legacy resolvers to get category label."""
    category_lab = (
        univer.te_universities(changed_cat)
        or event2_d2(changed_cat)
        or with_years_bot.Try_With_Years2(changed_cat)
        or label_for_startwith_year_or_typeo(changed_cat)
        or event_lab_bot.event_Lab(changed_cat)
        or ye_ts_bot.translate_general_category(changed_cat)
        or ""
    )

    return category_lab


__all__ = [
    "legacy_resolvers",
]
