"""
Resolver for sports-related category labels with gender-specific logic.
This module provides functions to translate categories combining sports roles,
nationalities, and genders into idiomatic Arabic.
"""

import functools
import re

import logging
from ...translations import SPORT_KEY_RECORDS_BASE, All_Nat
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from .utils import fix_keys

logger = logging.getLogger(__name__)


def generate_sports_data_dict() -> dict[str, dict[str, str]]:
    """
    Build a mapping of sport keys to their Arabic role labels.

    Includes entries from SPORT_KEY_RECORDS_BASE where the record provides a non-empty "jobs" value (stored under the "sport_ar" key) and adds explicit Arabic mappings for several sports that are not present or need overrides.

    Returns:
        dict[str, dict[str, str]]: A dictionary where each English sport key maps to a dictionary with the key "sport_ar" containing the Arabic translation.
    """
    sports_data_new = {
        sport: {"sport_ar": record.get("jobs", "")}
        for sport, record in SPORT_KEY_RECORDS_BASE.items()
        if record.get("jobs", "")
    }

    sports_data_new.update(
        {
            "softball": {"sport_ar": "كرة لينة"},
            "futsal": {"sport_ar": "كرة صالات"},
            "badminton": {"sport_ar": "تنس ريشة"},
            "australian rules football": {"sport_ar": "كرة قدم أسترالية"},
            "american-football": {"sport_ar": "كرة قدم أمريكية"},
            "canadian-football": {"sport_ar": "كرة قدم كندية"},
        }
    )

    return sports_data_new


@functools.lru_cache(maxsize=1)
def _make_sport_formatted_data() -> dict[str, str]:
    formatted_data = {
        # _build_players_data - footballers without nats
        "male footballers": "لاعبو كرة قدم",
        "female footballers": "لاعبات كرة قدم",
        "footballers": "لاعبو ولاعبات كرة قدم",
        # _build_players_data - footballers with nats
        "{en_nat} male footballers": "لاعبو كرة قدم {males}",
        "{en_nat} female footballers": "لاعبات كرة قدم {females}",
        "{en_nat} footballers": "لاعبو ولاعبات كرة قدم {males}",
        # _build_players_data - sports without nats
        "female {en_sport} players": "لاعبات {sport_ar}",
        # _build_players_data - sports with nats
        "{en_nat} female {en_sport} players": "لاعبات {sport_ar} {females}",
        # _build_players_data - sports without nats
        "male {en_sport} players": "لاعبو {sport_ar}",
        "{en_sport} players": "لاعبو ولاعبات {sport_ar}",
        # _build_players_data - sports with nats
        "{en_nat} male {en_sport} players": "لاعبو {sport_ar} {males}",
        "{en_nat} {en_sport} players": "لاعبو ولاعبات {sport_ar} {males}",
    }

    players_of_data = {
        "australian rules football": "كرة قدم أسترالية",
        "american-football": "كرة قدم أمريكية",
    }
    for sport, ar in players_of_data.items():
        formatted_data.update(
            {
                f"female players of {sport}": f"لاعبات {ar}",
                f"{{en_nat}} female players of {sport}": f"لاعبات {ar} {{females}}",
                f"male players of {sport}": f"لاعبو {ar}",
                f"{{en_nat}} male players of {sport}": f"لاعبو {ar} {{males}}",
                f"players of {sport}": f"لاعبو ولاعبات {ar}",
                f"{{en_nat}} players of {sport}": f"لاعبو ولاعبات {ar} {{males}}",
            }
        )

    return formatted_data


@functools.lru_cache(maxsize=1)
def _sport_bot() -> MultiDataFormatterBaseV2:
    sports_data_new = generate_sports_data_dict()

    nats_data = {
        x: {
            "males": v["males"],
            "females": v["females"],
        }
        for x, v in All_Nat.items()
        if v.get("males")
    }
    formatted_data = _make_sport_formatted_data()

    return format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        data_list2=sports_data_new,
        key2_placeholder="{en_sport}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )


@functools.lru_cache(maxsize=10000)
def genders_sports_resolver(category: str) -> str:
    normalized_category = fix_keys(category)
    logger.debug(f"<<yellow>> start {normalized_category=}")

    sport_bot = _sport_bot()
    result = sport_bot.search_all_other_first(normalized_category)
    result = sport_bot.prepend_arabic_category_prefix(category, result)

    logger.info(f"<<yellow>> end {category=}, {result=}")

    return result


__all__ = [
    "genders_sports_resolver",
]
