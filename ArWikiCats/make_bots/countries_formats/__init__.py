
from ...translations_resolvers import countries_names
from . import p17_bot, p17_bot_sport, p17_sport_to_move_under  # , p17_bot_2


def resolved_countries_formats_labels(normalized_category) -> str:

    resolved_label = p17_bot.get_p17_main(normalized_category)

    if not resolved_label:
        #  [yemen international soccer players] : "تصنيف:لاعبو منتخب اليمن لكرة القدم",
        resolved_label = countries_names.resolve_by_countries_names(normalized_category)

    if not resolved_label:
        #  "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال"
        resolved_label = p17_sport_to_move_under.get_en_ar_is_p17_label_multi(normalized_category)

    if not resolved_label:
        # [yemen international soccer players] : "تصنيف:لاعبو كرة قدم دوليون من اليمن",
        resolved_label = p17_bot_sport.get_p17_with_sport(normalized_category)

    return resolved_label
