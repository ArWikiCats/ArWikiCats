"""
Module to resolve nationality gender patterns in Arabic categories.

TODO: use format_multi_data_v2

"""

import re
import functools
from ..helps import len_print, logger
from ..translations import All_Nat, SPORT_KEY_RECORDS_BASE
from ..translations_formats import FormatDataV2

REGEX_WOMENS = re.compile(r"\b(womens|women)\b", re.I)
REGEX_MENS = re.compile(r"\b(mens|men)\b", re.I)


@functools.lru_cache(maxsize=1)
def _build_jobs_data() -> dict[str, str]:
    occupation_gender_labels = {
        "singers": {"males": "مغنون", "females": "مغنيات"},
        "actors": {"males": "ممثلون", "females": "ممثلات"},
        "boxers": {"males": "ملاكمون", "females": "ملاكمات"},
    }

    gendered_job_title_replacements = {
        "actors": "actresses",
    }

    data = {
        "{en_nat} actors": "ممثلون وممثلات من {males}",
        "{en_nat} male actors": "ممثلون {males}",
        "{en_nat} actresses": "ممثلات {females}",

        "{en_nat} singers": "مغنون ومغنيات {males}",
        "{en_nat} male singers": "مغنون {males}",
        "{en_nat} female singers": "مغنيات {females}",
        "{en_nat} women singers": "مغنيات {females}",
    }
    for job, job_labels in occupation_gender_labels.items():
        males = job_labels["males"]
        females = job_labels["females"]

        # "irish actors": "ممثلون وممثلات أيرلنديون"
        data[f"{{en_nat}} {job}"] = f"{males} و{females} {{males}}"

        # "irish male actors": "ممثلون أيرلنديون"
        data[f"{{en_nat}} male {job}"] = f"{males} {{males}}"

        female_replacement = gendered_job_title_replacements.get(job)

        if female_replacement:
            # "irish actresses": "ممثلات أيرلنديات"
            data[f"{{en_nat}} {female_replacement}"] = f"{females} {{females}}"
        else:
            # "irish actresses": "ممثلات أيرلنديات"
            data[f"{{en_nat}} female {job}"] = f"{females} {{females}}"
            data[f"{{en_nat}} women {job}"] = f"{females} {{females}}"

    return data


@functools.lru_cache(maxsize=1)
def _build_players_data() -> dict[str, str]:

    sport_labels = {
        "softball players": "كرة لينة",
        "futsal players": "كرة صالات",
        "badminton players": "تنس ريشة",
        "footballers": "كرة قدم",
        "players of australian rules football": "كرة قدم أسترالية",
        "players of american football": "كرة قدم أمريكية",
        "players of american-football": "كرة قدم أمريكية",
    }

    sport_labels.update({
        f"{sport} players": record.get("jobs", "")
        for sport, record in SPORT_KEY_RECORDS_BASE.items()
        if record.get("jobs", "")
    })

    # ------------------------------
    # 1) males data

    data_males = {}

    for job, job_label in sport_labels.items():

        # "yemeni softball players": "لاعبو ولاعبات كرة لينة يمنيون"
        # data[f"{{en_nat}} {job}"] = f"لاعبو ولاعبات {job_label} {{males}}"

        # "softball players": "لاعبو ولاعبات كرة لينة"
        data_males[f"{job}"] = f"لاعبو ولاعبات {job_label}"

        # "Category:Scottish male badminton players": "تصنيف:لاعبو تنس ريشة ذكور إسكتلنديون",
        # data_males[f"{{en_nat}} male {job}"] = f"لاعبو {job_label} {{males}}"

        # "Category:Serbian men's footballers": "تصنيف:لاعبو كرة قدم صرب",
        # "Category:Russian men's futsal players": "تصنيف:لاعبو كرة صالات رجالية روس",
        data_males[f"male {job}"] = f"لاعبو {job_label}"
        # data_males[f"mens {job}"] = f"لاعبو {job_label}"

    males_with_nats = {
        f"{{en_nat}} {key}": f"{value} {{males}}"
        for key, value in data_males.items()
    }
    # ------------------------------
    # 2) females data

    # "yemeni women's softball players": "لاعبات كرة لينة يمنيات"
    # "Category:American women baseball players": "تصنيف:لاعبات كرة قاعدة أمريكيات",
    # data[f"{{en_nat}} female {job}"] = f"لاعبات {job_label} {{females}}"

    data_females = {
        f"female {job}": f"لاعبات {job_label}"
        for job, job_label in sport_labels.items()
    }

    females_with_nats = {
        f"{{en_nat}} female {job}": f"لاعبات {job_label} {{females}}"
        for job, job_label in sport_labels.items()
    }
    # ------------------------------
    # 3) full data
    pre_defined = {
        "{en_nat} footballers": "لاعبو ولاعبات كرة قدم {males}",
        # "{en_nat} mens footballers": "لاعبو كرة قدم {males}",
        "{en_nat} male footballers": "لاعبو كرة قدم {males}",
        "{en_nat} womens footballers": "لاعبات كرة قدم {females}",
        "{en_nat} female footballers": "لاعبات كرة قدم {females}",
    }
    data = pre_defined | data_males | data_females | males_with_nats | females_with_nats

    return data


NAT_DATA_MALES_FEMALES = _build_jobs_data() | _build_players_data()


@functools.lru_cache(maxsize=1)
def _bot_new() -> FormatDataV2:

    formatted_data = NAT_DATA_MALES_FEMALES

    nats_data={
        x: {
            "males": v["males"],
            "females": v["females"],
        }
        for x, v in All_Nat.items()
        if v.get("males")
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        text_after="",
        text_before="the ",
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
def resolve_nat_genders_pattern(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_nat_genders_pattern: {category=}")
    yc_bot = _bot_new()

    normalized_category = fix_keys(category)
    result = yc_bot.create_label(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    logger.debug(f"<<yellow>> end resolve_nat_genders_pattern: {category=}, {result=}")
    return result or ""


len_print.data_len(
    "nat_genders_pattern.py",
    {
        "NAT_DATA_MALES_FEMALES": NAT_DATA_MALES_FEMALES        # 1,868
    },
)

__all__=[
    "resolve_nat_genders_pattern",
]
