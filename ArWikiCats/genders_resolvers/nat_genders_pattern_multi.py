"""
Module to resolve nationality gender patterns in Arabic categories.

"""

import functools
import re

from ..helps import logger
from ..translations import SPORT_KEY_RECORDS_BASE, All_Nat, open_json_file
from ..translations_formats import FormatDataV2, MultiDataFormatterBaseV2, format_multi_data_v2

REGEX_WOMENS = re.compile(r"\b(womens|women)\b", re.I)  # replaced by female
REGEX_MENS = re.compile(r"\b(mens|men)\b", re.I)  # replaced by male


def generate_jobs_data_dict():
    """
    Generate jobs data dictionary.
    """
    # "[ا-ي]+ون* و[ا-ي]+ات"
    jobs_data_new = {
        "bobsledders": {
            "job_males": "متزلجون جماعيون",
            "job_females": "متزلجات جماعيات",
            "both_jobs": "متزلجون ومتزلجات جماعيون",
        },
        "models": {"job_males": "عارضو أزياء", "job_females": "عارضات أزياء", "both_jobs": "عارضو وعارضات أزياء"},
        "actors": {"job_males": "ممثلون", "job_females": "ممثلات", "both_jobs": "ممثلون وممثلات"},
        "boxers": {"job_males": "ملاكمون", "job_females": "ملاكمات", "both_jobs": "ملاكمون وملاكمات"},
        "classical composers": {
            "job_males": "ملحنون كلاسيكيون",
            "job_females": "ملحنات كلاسيكيات",
            "both_jobs": "ملحنون وملحنات كلاسيكيون",
        },
        "composers": {"job_males": "ملحنون", "job_females": "ملحنات", "both_jobs": "ملحنون وملحنات"},
        "cyclists": {"job_males": "دراجون", "job_females": "دراجات", "both_jobs": "دراجون ودراجات"},
        "film actors": {"job_males": "ممثلو أفلام", "job_females": "ممثلات أفلام", "both_jobs": "ممثلو وممثلات أفلام"},
        "guitarists": {
            "job_males": "عازفو قيثارة",
            "job_females": "عازفات قيثارة",
            "both_jobs": "عازفو وعازفات قيثارة",
        },
        "singers": {"job_males": "مغنون", "job_females": "مغنيات", "both_jobs": "مغنون ومغنيات"},
        "television actors": {
            "job_males": "ممثلو تلفاز",
            "job_females": "ممثلات تلفاز",
            "both_jobs": "ممثلو وممثلات تلفاز",
        },
    }
    # TODO: Load from jobs_data_multi_one_word.json
    # jobs_data_new.update(open_json_file("jobs_data_multi_one_word.json"))

    return jobs_data_new


def generate_formatted_data():
    formatted_data = {
        "actresses": "ممثلات",
        "{en_nat} actresses": "ممثلات {females}",
        # [guitarists] = "عازفو وعازفات قيثارة"
        "{job_en}": "{both_jobs}",
        # [male guitarists] = "عازفو قيثارة"
        "male {job_en}": "{job_males}",
        # [american guitarists] = "عازفو وعازفات قيثارة أمريكيون"
        "{en_nat} {job_en}": "{both_jobs} {males}",
        # [american male guitarists] = "عازفو قيثارة أمريكيون"
        "{en_nat} male {job_en}": "{job_males} {males}",
        "male {en_nat} {job_en}": "{job_males} {males}",
        # [female guitarists] = "عازفات قيثارة"
        "female {job_en}": "{job_females}",
        # [american female guitarists] = "عازفات قيثارة أمريكيات"
        "{en_nat} female {job_en}": "{job_females} {females}",
        "female {en_nat} {job_en}": "{job_females} {females}",
        # test to add classical
        "classical {job_en}": "{both_jobs} كلاسيكيون",
        "male classical {job_en}": "{job_males} كلاسيكيون",
        "female classical {job_en}": "{job_females} كلاسيكيات",
        "{en_nat} classical {job_en}": "{both_jobs} كلاسيكيون {males}",
        "{en_nat} male classical {job_en}": "{job_males} كلاسيكيون {males}",
        "{en_nat} female classical {job_en}": "{job_females} كلاسيكيات {females}",
    }

    return formatted_data


@functools.lru_cache(maxsize=1)
def _job_bot() -> MultiDataFormatterBaseV2:
    formatted_data = generate_formatted_data()

    jobs_data_new = generate_jobs_data_dict()

    nats_data = {
        x: {
            "males": v["males"],
            "females": v["females"],
        }
        for x, v in All_Nat.items()
        if v.get("males")
    }

    return format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        data_list2=jobs_data_new,
        key2_placeholder="{job_en}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )


@functools.lru_cache(maxsize=1)
def _make_sport_formatted_data() -> dict[str, str]:
    formatted_data_new = {
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
        formatted_data_new.update(
            {
                f"female players of {sport}": f"لاعبات {ar}",
                f"{{en_nat}} female players of {sport}": f"لاعبات {ar} {{females}}",
                f"male players of {sport}": f"لاعبو {ar}",
                f"{{en_nat}} male players of {sport}": f"لاعبو {ar} {{males}}",
                f"players of {sport}": f"لاعبو ولاعبات {ar}",
                f"{{en_nat}} players of {sport}": f"لاعبو ولاعبات {ar} {{males}}",
            }
        )

    return formatted_data_new


@functools.lru_cache(maxsize=1)
def _sport_bot() -> MultiDataFormatterBaseV2:
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

    nats_data = {
        x: {
            "males": v["males"],
            "females": v["females"],
        }
        for x, v in All_Nat.items()
        if v.get("males")
    }
    formatted_data_new = _make_sport_formatted_data()

    return format_multi_data_v2(
        formatted_data=formatted_data_new,
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
def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")

    replacements = {
        "expatriates": "expatriate",
        "canadian football": "canadian-football",
        "american football": "american-football",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    category = REGEX_WOMENS.sub("female", category)
    category = REGEX_MENS.sub("male", category)

    return category.strip()


@functools.lru_cache(maxsize=10000)
def genders_jobs_resolver(category: str) -> str:
    normalized_category = fix_keys(category)
    logger.debug(f"<<yellow>> start genders_jobs_resolver: {normalized_category=}")

    job_bot = _job_bot()

    result = job_bot.search_all_other_first(normalized_category)
    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result
    logger.info_if_or_debug(f"<<yellow>> end genders_jobs_resolver: {category=}, {result=}", result)

    return result


@functools.lru_cache(maxsize=10000)
def genders_sports_resolver(category: str) -> str:
    normalized_category = fix_keys(category)
    logger.debug(f"<<yellow>> start genders_sports_resolver: {normalized_category=}")

    sport_bot = _sport_bot()

    result = sport_bot.search_all_other_first(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result
    logger.info_if_or_debug(f"<<yellow>> end genders_sports_resolver: {category=}, {result=}", result)

    return result


@functools.lru_cache(maxsize=10000)
def resolve_nat_genders_pattern_v2(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_nat_genders_pattern_v2: {category=}")

    result = genders_sports_resolver(category) or genders_jobs_resolver(category) or ""
    logger.info_if_or_debug(f"<<yellow>> end resolve_nat_genders_pattern_v2: {category=}, {result=}", result)

    return result


__all__ = [
    "resolve_nat_genders_pattern_v2",
]
