import functools
import logging

from ..worker import run_resolvers
from . import (
    p17_bot_sport,
    p17_sport_to_move_under,
)

logger = logging.getLogger(__name__)


@functools.lru_cache(maxsize=10000)
def main_countries_names_with_sports_resolvers(category) -> str:
    """
    Resolve a target label for a normalized category using sport-related resolver fallbacks.

    Attempts sport-specific resolvers in a defined fallback order and returns the first non-empty label found.

    Parameters:
        category (str): Normalized category identifier to resolve.

    Returns:
        str: Resolved label for the category, or an empty string if no resolver produces a value.
    """
    #  [yemen international soccer players] : "تصنيف:لاعبو منتخب اليمن لكرة القدم",
    # countries_names.resolve_by_countries_names(normalized_category) or
    #  "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال"
    result = run_resolvers(
        category,
        [
            p17_sport_to_move_under.resolve_sport_under_labels,
            # [yemen international soccer players] : "تصنيف:لاعبو كرة قدم دوليون من اليمن",
            p17_bot_sport.get_p17_with_sport_new,
        ],
    )
    logger.log(20 if result else 10, f"<<yellow>> end {category=}, {result=}")
    return result
