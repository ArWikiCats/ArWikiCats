"""
Module to resolve nationality gender patterns in Arabic categories.

TODO: use format_multi_data_v2

"""

import re
import functools
from ..helps import logger
from ..translations import All_Nat, SPORT_KEY_RECORDS_BASE
from ..translations_formats import FormatDataV2, MultiDataFormatterBaseV2

REGEX_WOMENS = re.compile(r"\b(womens|women)\b", re.I)
REGEX_MENS = re.compile(r"\b(mens|men)\b", re.I)


@functools.lru_cache(maxsize=1)
def _job_bot() -> MultiDataFormatterBaseV2:
    formatted_data = {
        # _build_jobs_data
        "{job_en}": "{job_males} و{job_females}",
        "male {job_en}": "{job_males}",

        # _build_jobs_data
        "{en_nat} {job_en}": "{job_males} و{job_females} {males}",
        "{en_nat} male {job_en}": "{job_males} {males}",

        # _build_jobs_data
        "female {job_en}": "{job_females}",
        "{en_nat} female {job_en}": "{job_females} {females}",
    }

    jobs_data_new = {
        "singers": {"job_males": "مغنون", "job_females": "مغنيات"},
        "actors": {"job_males": "ممثلون", "job_females": "ممثلات"},
        "boxers": {"job_males": "ملاكمون", "job_females": "ملاكمات"},
    }

    nats_data = {
        x: {
            "males": v["males"],
            "females": v["females"],
        }
        for x, v in All_Nat.items()
        if v.get("males")
    }

    country_bot = FormatDataV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
    )

    other_bot = FormatDataV2(
        {},
        jobs_data_new,
        key_placeholder="{job_en}",
    )

    return MultiDataFormatterBaseV2(
        country_bot=country_bot,
        other_bot=other_bot,
    )


@functools.lru_cache(maxsize=1)
def _make_formatted_data_new() -> dict[str, str]:
    formatted_data_new = {
        "actresses": "ممثلات",
        "{en_nat} actresses": "ممثلات {females}",

        # _build_players_data - footballers without nats
        "male footballers": "لاعبو كرة قدم",
        "female footballers": "لاعبات كرة قدم",
        "footballers": "لاعبو ولاعبات كرة قدم",

        # _build_players_data - footballers with nats
        "{en_nat} male footballers": "لاعبو كرة قدم {males}",
        "{en_nat} female footballers": "لاعبات كرة قدم {females}",
        "{en_nat} footballers": "لاعبو ولاعبات كرة قدم {males}",
    }

    formatted_data_females = {
        # _build_players_data - sports without nats
        "female {sport_en} players": "لاعبات {job_ar}",

        # _build_players_data - sports with nats
        "{en_nat} female {sport_en} players": "لاعبات {job_ar} {females}",

    }

    formatted_data_males = {
        # _build_players_data - sports without nats
        "male {sport_en} players": "لاعبو {job_ar}",
        "{sport_en} players": "لاعبو ولاعبات {job_ar}",

        # _build_players_data - sports with nats
        "{en_nat} male {sport_en} players": "لاعبو {job_ar} {males}",
        "{en_nat} {sport_en} players": "لاعبو ولاعبات {job_ar} {males}",
    }

    formatted_data_new.update(formatted_data_females)
    formatted_data_new.update(formatted_data_males)

    players_of_data = {
        "australian rules football": "كرة قدم أسترالية",
        "american-football": "كرة قدم أمريكية",
    }
    for sport, ar in players_of_data.items():
        formatted_data_new.update({
            f"female players of {sport}": f"لاعبات {ar}",
            f"{{en_nat}} female players of {sport}": f"لاعبات {ar} {{females}}",
            f"male players of {sport}": f"لاعبو {ar}",
            f"players of {sport}": f"لاعبو ولاعبات {ar}",
            f"{{en_nat}} male players of {sport}": f"لاعبو {ar} {{males}}",
            f"{{en_nat}} players of {sport}": f"لاعبو ولاعبات {ar} {{males}}",
        })

    return formatted_data_new


@functools.lru_cache(maxsize=1)
def _sport_bot() -> MultiDataFormatterBaseV2:

    sports_data_new = {
        sport: {"job_ar": record.get("jobs", "")}
        for sport, record in SPORT_KEY_RECORDS_BASE.items()
        if record.get("jobs", "")
    }

    sports_data_new.update({
        "softball": {"job_ar": "كرة لينة"},
        "futsal": {"job_ar": "كرة صالات"},
        "badminton": {"job_ar": "تنس ريشة"},
        "australian rules football": {"job_ar": "كرة قدم أسترالية"},
        "american-football": {"job_ar": "كرة قدم أمريكية"},
    })

    nats_data = {
        x: {
            "males": v["males"],
            "females": v["females"],
        }
        for x, v in All_Nat.items()
        if v.get("males")
    }
    formatted_data_new = _make_formatted_data_new()

    country_bot = FormatDataV2(
        formatted_data=formatted_data_new,
        data_list=nats_data,
        key_placeholder="{en_nat}",
    )

    other_bot = FormatDataV2(
        {},
        sports_data_new,
        key_placeholder="{sport_en}",
    )

    return MultiDataFormatterBaseV2(
        country_bot=country_bot,
        other_bot=other_bot,
    )


def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")

    replacements = {
        "expatriates": "expatriate",
        "canadian football": "canadian-football",
        "american football": "american-football",
    }

    category = REGEX_WOMENS.sub("female", category)
    category = REGEX_MENS.sub("male", category)

    for old, new in replacements.items():
        category = category.replace(old, new)

    return category.strip()


@functools.lru_cache(maxsize=10000)
def resolve_nat_genders_pattern_v2(category: str) -> str:
    normalized_category = fix_keys(category)
    logger.debug(f"<<yellow>> start resolve_nat_genders_pattern: {normalized_category=}")

    sport_bot = _sport_bot()
    job_bot = _job_bot()

    result = (
        sport_bot.search_all_other_first(normalized_category) or
        job_bot.search_all_other_first(normalized_category) or
        ""
    )

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result
    logger.debug(f"<<yellow>> end resolve_nat_genders_pattern: {category=}, {result=}")
    return result or ""


__all__=[
    "resolve_nat_genders_pattern_v2",
]
