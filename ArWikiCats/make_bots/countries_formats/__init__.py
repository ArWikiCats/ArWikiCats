
from . import p17_bot, p17_bot_sport_new, p17_sport_to_move_under


def resolved_countries_formats_labels(normalized_category) -> str:

    resolved_label = (
        p17_bot.get_p17_main(normalized_category) or

        #  [yemen international soccer players] : "تصنيف:لاعبو منتخب اليمن لكرة القدم",
        # countries_names.resolve_by_countries_names(normalized_category) or

        #  "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال"
        p17_sport_to_move_under.resolve_sport_under_labels(normalized_category) or

        # [yemen international soccer players] : "تصنيف:لاعبو كرة قدم دوليون من اليمن",
        p17_bot_sport_new.get_p17_with_sport_new(normalized_category) or

        ""
    )
    return resolved_label
