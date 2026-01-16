from ...helps import logger
from . import (
    p17_bot_sport,
    p17_sport_to_move_under,
)


def resolved_names_with_sports(normalized_category) -> str:
    logger.debug(f"<><><><><><> <<green>> Trying resolved_names_with_sports for: {normalized_category=}")
    resolved_label = (
        #  [yemen international soccer players] : "تصنيف:لاعبو منتخب اليمن لكرة القدم",
        # countries_names.resolve_by_countries_names(normalized_category) or
        #  "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال"
        p17_sport_to_move_under.resolve_sport_under_labels(normalized_category)
        # [yemen international soccer players] : "تصنيف:لاعبو كرة قدم دوليون من اليمن",
        or p17_bot_sport.get_p17_with_sport_new(normalized_category)
        or ""
    )
    logger.info_if_or_debug(
        f"<<yellow>> end countries_names_resolvers: {normalized_category=}, {resolved_label=}", resolved_label
    )
    return resolved_label
