#!/usr/bin/python3
"""

TODO:
    - use this file instead of film_keys_bot.py
    - add formated_data from ArWikiCats/translations/tv/films_mslslat.py

"""

import functools
from typing import Dict

from ...helps import getLogger
from ...translations import (
    Nat_women,
    film_keys_for_female,
)
from ...translations_formats import (
    MultiDataFormatterBase,
    format_films_country_data,
    format_multi_data,
)

logger = getLogger(__name__)


def _build_television_cao() -> tuple[Dict[str, str], Dict[str, str]]:
    """
    Construct two translation mapping dictionaries for television and film category keys: one that includes nationality placeholders and one without.

    The first dictionary maps English pattern keys (which may include `{nat_en}` and `{film_key}`) to Arabic translation templates (which may include `{nat_ar}` and `{film_ar}`). The second dictionary provides equivalent mappings that omit nationality placeholders and may include `{film_ar}` in templates.

    Returns:
        films_key_cao (Dict[str, str]): Mapping of English pattern keys with optional `{nat_en}`/`{film_key}` to Arabic templates containing optional `{nat_ar}`/`{film_ar}`.
        data_no_nats (Dict[str, str]): Mapping of English pattern keys without nationality placeholders to Arabic templates that may include `{film_ar}`.
    """
    data = {}
    data_no_nats = {}

    # Base TV keys with common suffixes
    for suffix, arabic_suffix in [
        ("characters", "شخصيات"),
        ("title cards", "بطاقات عنوان"),
        ("video covers", "أغلفة فيديو"),
        ("posters", "ملصقات"),
        ("images", "صور"),
    ]:
        data_no_nats.update(
            {
                f"{{film_key}} {suffix}": f"{arabic_suffix} {{film_ar}}",
            }
        )
        data.update(
            {
                f"{{nat_en}} {suffix}": f"{arabic_suffix} {{nat_ar}}",
                f"{{nat_en}} {{film_key}} {suffix}": f"{arabic_suffix} {{film_ar}} {{nat_ar}}",
            }
        )

    # Genre-based categories
    # ArWikiCats/jsons/media/Films_key_For_nat.json
    genre_categories = {
        # "fiction": "خيال",
        "film series": "سلاسل أفلام",
        "webcomics": "ويب كومكس",
        "anime and manga": "أنمي ومانغا",
        "compilation albums": "ألبومات تجميعية",
        "folk albums": "ألبومات فلكلورية",
        "classical albums": "ألبومات كلاسيكية",
        "comedy albums": "ألبومات كوميدية",
        "mixtape albums": "ألبومات ميكستايب",
        "soundtracks": "موسيقى تصويرية",
        "terminology": "مصطلحات",
        "series": "مسلسلات",
        "television series": "مسلسلات تلفزيونية",
        "television episodes": "حلقات تلفزيونية",
        "television programs": "برامج تلفزيونية",
        "television programmes": "برامج تلفزيونية",
        "groups": "مجموعات",
        "novellas": "روايات قصيرة",
        "novels": "روايات",
        "films": "أفلام",
        "comic strips": "شرائط كومكس",
        "comics": "قصص مصورة",
        "television shows": "عروض تلفزيونية",
        "television films": "أفلام تلفزيونية",
        "teams": "فرق",
        "television characters": "شخصيات تلفزيونية",
        "video games": "ألعاب فيديو",
        "web series": "مسلسلات ويب",
        "film characters": "شخصيات أفلام",
        "games": "ألعاب",
        "soap opera": "مسلسلات طويلة",
        "television news": "أخبار تلفزيونية",
        "miniseries": "مسلسلات قصيرة",
        "television miniseries": "مسلسلات قصيرة تلفزيونية",
    }

    genre_categories_skip_it = {
        "film characters",
        "series",
        "games",
    }

    # Standard categories
    for suffix, arabic_base in genre_categories.items():
        # Base TV keys with common suffixes
        for sub_suffix, arabic_sub_suffix in [
            ("characters", "شخصيات"),
            ("title cards", "بطاقات عنوان"),
            ("video covers", "أغلفة فيديو"),
            ("posters", "ملصقات"),
            ("images", "صور"),
        ]:
            data_no_nats.update(
                {
                    f"{suffix} {sub_suffix}": f"{arabic_sub_suffix} {arabic_base}",
                    f"{{film_key}} {suffix} {sub_suffix}": f"{arabic_sub_suffix} {arabic_base} {{film_ar}}",
                }
            )
            data.update(
                {
                    f"{{nat_en}} {suffix} {sub_suffix}": f"{arabic_sub_suffix} {arabic_base} {{nat_ar}}",
                    f"{{nat_en}} {{film_key}} {suffix} {sub_suffix}": f"{arabic_sub_suffix} {arabic_base} {{film_ar}} {{nat_ar}}",
                }
            )

        data_no_nats.update(
            {
                f"{suffix}": f"{arabic_base}",
                f"television {suffix}": f"{arabic_base} تلفزيونية",
                f"{{film_key}} {suffix}": f"{arabic_base} {{film_ar}}",
                f"children's-animated-superhero {suffix}": f"{arabic_base} رسوم متحركة أبطال خارقين للأطفال",
                f"children's-animated-adventure-television {suffix}": f"{arabic_base} مغامرات رسوم متحركة تلفزيونية للأطفال",
            }
        )

        # NOTE: we use genre_categories_skip_it because next line makes errors like:
        # "Category:Golf at 2022 Asian Games": "تصنيف:الغولف في ألعاب آسيوية في 2022",
        if suffix not in genre_categories_skip_it:
            data[f"{{nat_en}} {suffix}"] = f"{arabic_base} {{nat_ar}}"

        data.update(
            {
                f"{{nat_en}} {{film_key}} {suffix}": f"{arabic_base} {{film_ar}} {{nat_ar}}",
                f"{{nat_en}} children's-animated-superhero {suffix}": f"{arabic_base} رسوم متحركة أبطال خارقين {{nat_ar}} للأطفال",
                f"{{nat_en}} children's-animated-adventure-television {suffix}": f"{arabic_base} مغامرات رسوم متحركة تلفزيونية {{nat_ar}} للأطفال",
            }
        )

    return data, data_no_nats


@functools.lru_cache(maxsize=1)
def _make_bot() -> MultiDataFormatterBase:
    # NOTE: keys with non-patterns should be added to populate_film_patterns()
    # Template data with both nationality and sport placeholders
    """
    Create and configure formatter bots for film and television category translations.

    Builds and merges formatted pattern data (including television CAO entries and film-key mappings),
    prepares nationality and film-key lookup lists, and generates two formatter instances:
    - `double_bot`: a combined formatter populated with country+film patterns and additional adjustments.
    - `bot`: a multi-data formatter built from the same inputs.

    This function also updates `double_bot.other_bot` to set the `put_label_last` label ordering.

    Returns:
        tuple: `(double_bot, bot)` where `double_bot` is the combined MultiDataFormatterBase with populated film-country patterns and `bot` is an additional MultiDataFormatterBase built from the same formatted data.
    """
    formatted_data = {
        # "{nat_en} films": "أفلام {nat_ar}", #  [2000s American films] : "تصنيف:أفلام أمريكية في عقد 2000",
        "{nat_en} films": "أفلام {nat_ar}",
        "remakes of {nat_en} films": "أفلام {nat_ar} معاد إنتاجها",
        # "Category:yemeni action Teen superhero films" : "تصنيف:أفلام حركة مراهقة يمنية أبطال خارقين",
        "{nat_en} television episodes": "حلقات تلفزيونية {nat_ar}",
        "{nat_en} television series": "مسلسلات تلفزيونية {nat_ar}",
        "remakes of {nat_en} television series": "مسلسلات تلفزيونية {nat_ar} معاد إنتاجها",
        "{nat_en} television-seasons": "مواسم تلفزيونية {nat_ar}",
        "{nat_en} television seasons": "مواسم تلفزيونية {nat_ar}",
        "{nat_en} {film_key} television-seasons": "مواسم تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} television seasons": "مواسم تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} television series": "مسلسلات تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} filmszz": "أفلام {film_ar} {nat_ar}",
        "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
        "remakes of {nat_en} {film_key} films": "أفلام {film_ar} {nat_ar} معاد إنتاجها",
        "{nat_en} {film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar} {nat_ar}",
        # TODO: move this to jobs bot?
        # "{nat_en} sports coaches": "مدربو رياضة {nat_ar}",
        "{nat_en} animated television films": "أفلام رسوم متحركة تلفزيونية {nat_ar}",
        "{nat_en} animated television series": "مسلسلات رسوم متحركة تلفزيونية {nat_ar}",
    }

    _data, data_no_nats = _build_television_cao()

    formatted_data.update(_data)

    other_formatted_data = {
        "{film_key} films": "أفلام {film_ar}",
        "remakes of {film_key} films": "أفلام {film_ar} معاد إنتاجها",
        # "Category:action Teen superhero films" : "تصنيف:أفلام حركة مراهقة أبطال خارقين",
        "{film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar}",
        "animated television films": "أفلام رسوم متحركة تلفزيونية",
        "animated television series": "مسلسلات رسوم متحركة تلفزيونية",
    }
    other_formatted_data.update(data_no_nats)

    # film_keys_for_female
    data_list2 = {
        "action comedy": "حركة كوميدية",
        "action thriller": "إثارة حركة",
        "action": "حركة",
        "drama": "درامية",
        "upcoming": "قادمة",
        "horror": "رعب",
        "black-and-white": "أبيض وأسود",
        "psychological horror": "رعب نفسي",
    }

    put_label_last = {
        "low-budget",
        "supernatural",
        "christmas",
        "lgbtq-related",
        "upcoming",
    }

    data_list2 = dict(film_keys_for_female)
    data_list2.pop("television", None)

    # data_list2.pop("superhero", None)
    data_list2["superhero"] = "أبطال خارقين"

    double_bot = format_films_country_data(
        formatted_data=formatted_data,
        data_list=Nat_women,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        data_list2=data_list2,
        key2_placeholder="{film_key}",
        value2_placeholder="{film_ar}",
        text_after="",
        text_before="",
        other_formatted_data=other_formatted_data,
    )

    double_bot.other_bot.update_put_label_last(put_label_last)
    bot = format_multi_data(
        formatted_data=formatted_data,
        data_list=Nat_women,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        data_list2=data_list2,
        key2_placeholder="{film_key}",
        value2_placeholder="{film_ar}",
        text_after="",
        text_before="",
        other_formatted_data=other_formatted_data,
    )
    return double_bot, bot


def fix_keys(category: str) -> str:
    """
    Normalize a category key and apply specific known corrections.

    Parameters:
        category (str): Original category key string (may include a leading "category:" prefix).

    Returns:
        str: Normalized category key in lowercase with the "category:" prefix removed and specific fixes applied
        (e.g., "saudi arabian" -> "saudiarabian", "children's animated adventure television" ->
        "children's-animated-adventure-television").
    """
    normalized_text = category.lower().replace("category:", " ").strip()
    fixes = {
        "saudi arabian": "saudiarabian",
        # "animated television": "animated-television",
        "children's animated adventure television": "children's-animated-adventure-television",
        "children's animated superhero": "children's-animated-superhero",
    }
    category = category.lower().strip()

    for old, new in fixes.items():
        category = category.replace(old, new)

    return category


@functools.lru_cache(maxsize=10000)
def _get_films_key_tyty_new(text: str) -> str:
    """
    Resolve a films category key from free-form category text.

    Parameters:
        text (str): Free-form category or country identifier text to match against known film/television keys.

    Returns:
        resolved_key (str): The matched films key, or an empty string if no match is found.
    """
    normalized_text = fix_keys(text)
    logger.debug(f"<<yellow>> start get_films_key_tyty_new: {normalized_text=}")
    double_bot, bot = _make_bot()

    result = bot.search_all(normalized_text) or double_bot.search_all(normalized_text)
    logger.info_if_or_debug(f"<<yellow>> end get_films_key_tyty_new: {normalized_text=}, {result=}", result)
    return result


@functools.lru_cache(maxsize=10000)
def get_films_key_tyty_new(text: str) -> str:
    """
    Resolve a films/television category key from an input text.

    Parameters:
        text (str): Category or country identifier text to analyze.

    Returns:
        str: Resolved category key, or an empty string if no match is found.
    """
    # return ""
    return _get_films_key_tyty_new(text)
