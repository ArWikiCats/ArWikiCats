
from . import p17_bot, p17_bot_sport, p17_bot_2, not_sports_bot


def resolved_countries_formats_labels(normalized_category):
    resolved_label = p17_bot.Get_P17_main(normalized_category)

    if not resolved_label:
        resolved_label = p17_bot_sport.get_p17_with_sport(normalized_category)

    if not resolved_label:
        resolved_label = p17_bot_2.Get_P17_2(normalized_category)

    if not resolved_label:
        resolved_label = not_sports_bot.resolve_en_is_P17_ar_is_P17(normalized_category)

    return resolved_label
