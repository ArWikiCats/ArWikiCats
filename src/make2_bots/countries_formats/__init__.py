
from . import p17_bot, p17_bot_sport, p17_bot_2


def resolved_countries_formats_labels(normalized_category):
    resolved_label = p17_bot.Get_P17_main(normalized_category)

    if not resolved_label:
        resolved_label = p17_bot_sport.Get_P17_with_sport(normalized_category)

    if not resolved_label:
        resolved_label = p17_bot_2.Get_P17_2(normalized_category)

    return resolved_label
