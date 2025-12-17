#!/usr/bin/python3
"""
TODO: use this code in flowworks

Examples:
    - en: 18th-century nobility from the Holy Roman Empire
    - bad arabic: (نبلاء من الإمبراطورية الرومانية المقدسة القرن 18)
    - good arabic: (نبلاء من الإمبراطورية الرومانية المقدسة في القرن 18)

"""
import re
import functools

from ..translations.mixed.keys2 import medical_keys

from ..translations import get_from_new_p17_final, get_from_pf_keys2

from ..make_bots.matables_bots.table1_bot import get_KAKO
# from ..make_bots.ma_bots.country2_lab import get_lab_for_country2
from ..helps import logger
from ..translations_formats import FormatDataFrom, MultiDataFormatterYearAndFrom
from ..translations_resolvers.new_jobs_resolver import new_jobs_resolver_label

from ..new.time_to_arabic import convert_time_to_arabic, match_time_en_first

FROM_REGEX = re.compile(r"^(.*?) from (.*?)$", re.I)

label_new_keys = {
    "crown-of aragon": "تاج أرغون",
}

jobs_part_labels = {
    "lgbtq people": "أعلام إل جي بي تي كيو",
    "princes": "أمراء",
    "deaths": "وفيات",
    "people": "أشخاص",
    "women": "نساء",
    "womens": "نساء",
    "women's": "نساء",
    "female": "نساء",
}

formatted_data = {
    # "{year1} deaths from {country1}": "وفيات بسبب {country1} في {year1}",
    "{year1} {country1}": "{country1} في {year1}",
}


def get_job_label(text: str) -> str:
    text = normalize_text(text)
    result = (
        jobs_part_labels.get(text) or
        new_jobs_resolver_label(text) or
        # get_lab_for_country2(text) or
        ""
    )

    return result


def normalize_text(text):
    text = text.lower()
    text = text.replace("sportspeople", "sports-people")
    text = text.replace(" the ", " ")
    if text.startswith("the "):
        text = text[4:]
    return text.strip()


def get_label_new(text: str) -> str:
    """Get the Arabic label for a 'job from country' category."""
    text = normalize_text(text)
    match = FROM_REGEX.match(text)
    logger.debug(f"get_label_new: {text=}")

    if not match:
        logger.debug(f"get_label_new: no match: {text=}")
        return ""

    job_part = match.group(1)
    from_part = match.group(2)
    logger.debug(f"get_label_new: {job_part=}, {from_part=}")

    job_label = get_job_label(job_part)
    logger.debug(f"get_label_new: {job_part=}, {job_label=}")

    # from_label = get_lab_for_country2(from_part)
    from_label = (
        medical_keys.get(from_part) or
        label_new_keys.get(from_part) or
        get_KAKO(from_part) or
        get_from_pf_keys2(from_part) or
        get_from_new_p17_final(from_part) or
        ""
    )

    logger.debug(f"get_label_new: {from_part=}, {from_label=}")
    min_word = "من" if job_label != "وفيات" else "بسبب"
    if job_label and from_label:
        return f"{job_label} {min_word} {from_label}"

    return ""


def match_key_callback(text: str) -> str:
    """Match the country part from 'job from country'."""
    # replace all formatted_data keys from text
    # text = text.replace("{year1} deaths from", "").replace("{year1}", "")

    keys_to_replace = [x.replace("{country1}", "").strip() for x in formatted_data.keys() if x.replace("{country1}", "").strip()]
    # sort by len
    keys_to_replace = sorted(
        keys_to_replace,
        key=lambda k: (-k.count(" "), -len(k)),
    )
    for key in keys_to_replace:
        if key in text:
            return text.replace(key, "").strip()
    return text.strip()


@functools.lru_cache(maxsize=1)
def multi_bot_v4() -> MultiDataFormatterYearAndFrom:

    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        search_callback=get_label_new,
        match_key_callback=match_key_callback,
    )
    year_bot = FormatDataFrom(
        formatted_data={},
        key_placeholder="{year1}",
        value_placeholder="{year1}",
        search_callback=convert_time_to_arabic,
        match_key_callback=match_time_en_first,
    )
    return MultiDataFormatterYearAndFrom(
        country_bot=country_bot,
        year_bot=year_bot,
        other_key_first=True,
    )


def resolve_year_job_from_countries(category: str) -> str:
    """Resolve year and job from countries using multi_bot_v4."""
    if not FROM_REGEX.match(category):
        return ""

    category = normalize_text(category)

    _bot = multi_bot_v4()
    # NOTE: search_all creates labels like:
    #  [Category:Non-fiction writers from Northern Ireland by century]:
    #  "تصنيف:كتاب غير روائيين من أيرلنديون شماليون حسب القرن"
    return _bot.create_label(category)
