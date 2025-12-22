"""
TODO: merge with translations_resolvers OR translations_resolvers_v2
"""
import functools
import re
from ...helps.log import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    AFTER_KEYS_TEAM,
    countries_from_nat,
    SPORTS_KEYS_FOR_TEAM,
    SPORTS_KEYS_FOR_JOBS,
    match_sport_key,
    apply_pattern_replacements,
)

from ..jobs_bots.get_helps import get_suffix_with_keys


sport_formts_enar_p17_jobs = {
    "international men's xoxo players": "لاعبو xoxo دوليون من {}",
    "international women's xoxo players": "لاعبات xoxo دوليات من {}",
    "international xoxo players": "لاعبو xoxo دوليون من {}",
    "men's international xoxo players": "لاعبو xoxo دوليون من {}",
    "olympics xoxo": "xoxo {} في الألعاب الأولمبية",
    "summer olympics xoxo": "xoxo {} في الألعاب الأولمبية الصيفية",
    "under-13 international xoxo managers": "مدربو xoxo تحت 13 سنة دوليون من {}",
    "under-13 international xoxo players": "لاعبو xoxo تحت 13 سنة دوليون من {}",
    "under-14 international xoxo managers": "مدربو xoxo تحت 14 سنة دوليون من {}",
    "under-14 international xoxo players": "لاعبو xoxo تحت 14 سنة دوليون من {}",
    "under-15 international xoxo managers": "مدربو xoxo تحت 15 سنة دوليون من {}",
    "under-15 international xoxo players": "لاعبو xoxo تحت 15 سنة دوليون من {}",
    "under-16 international xoxo managers": "مدربو xoxo تحت 16 سنة دوليون من {}",
    "under-16 international xoxo players": "لاعبو xoxo تحت 16 سنة دوليون من {}",
    "under-17 international xoxo managers": "مدربو xoxo تحت 17 سنة دوليون من {}",
    "under-17 international xoxo players": "لاعبو xoxo تحت 17 سنة دوليون من {}",
    "under-18 international xoxo managers": "مدربو xoxo تحت 18 سنة دوليون من {}",
    "under-18 international xoxo players": "لاعبو xoxo تحت 18 سنة دوليون من {}",
    "under-19 international xoxo managers": "مدربو xoxo تحت 19 سنة دوليون من {}",
    "under-19 international xoxo players": "لاعبو xoxo تحت 19 سنة دوليون من {}",
    "under-20 international xoxo managers": "مدربو xoxo تحت 20 سنة دوليون من {}",
    "under-20 international xoxo players": "لاعبو xoxo تحت 20 سنة دوليون من {}",
    "under-21 international xoxo managers": "مدربو xoxo تحت 21 سنة دوليون من {}",
    "under-21 international xoxo players": "لاعبو xoxo تحت 21 سنة دوليون من {}",
    "under-23 international xoxo managers": "مدربو xoxo تحت 23 سنة دوليون من {}",
    "under-23 international xoxo players": "لاعبو xoxo تحت 23 سنة دوليون من {}",
    "under-24 international xoxo managers": "مدربو xoxo تحت 24 سنة دوليون من {}",
    "under-24 international xoxo players": "لاعبو xoxo تحت 24 سنة دوليون من {}",
    "winter olympics xoxo": "xoxo {} في الألعاب الأولمبية الشتوية",
    "women's international xoxo players": "لاعبات xoxo دوليات من {}",
    "xoxo manager history": "تاريخ مدربو xoxo {}"
}


SPORT_FORMTS_ENAR_P17_TEAM = {}


def _build_new_tato() -> dict[str, str]:
    data = {}

    national_keys: dict[str, str] = {
        "national": "{}",
        "national youth": "{} للشباب",
        "national amateur": "{} للهواة",
        "national junior men's": "{} للناشئين",
        "national junior women's": "{} للناشئات",
        "national men's": "{} للرجال",
        "national women's": "{} للسيدات",
        "multi-national women's": "{} متعددة الجنسيات للسيدات",
        "national youth women's": "{} للشابات",
    }

    YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]

    for mrr, mrr_lab in national_keys.items():
        data[mrr] = mrr_lab
        for year in YEARS_LIST:
            data[f"{mrr} under-{year}"] = mrr_lab.format(f"{{}} تحت {year} سنة")
    # ---
    data["men's under-23 national"] = "{} تحت 23 سنة للرجال"
    data["men's u23 national"] = "{} تحت 23 سنة للرجال"
    data["men's u23 national"] = "{} تحت 23 سنة للرجال"

    return data


def _build_nat_formats_for_p17() -> dict:
    """Construct nationality placeholders used for P17 sports formats."""
    New_Tato = _build_new_tato()
    data = {}
    NAT_PLACE_HOLDER = "{}"
    data["xoxo league"] = "دوري {} xoxo "
    data["professional xoxo league"] = "دوري {} xoxo للمحترفين"
    data["amateur xoxo cup"] = "كأس {} xoxo للهواة"
    data["youth xoxo cup"] = "كأس {} xoxo للشباب"
    data["men's xoxo cup"] = "كأس {} xoxo للرجال"
    data["women's xoxo cup"] = "كأس {} xoxo للسيدات"
    data["amateur xoxo championships"] = "بطولة {} xoxo للهواة"
    data["youth xoxo championships"] = "بطولة {} xoxo للشباب"
    data["men's xoxo championships"] = "بطولة {} xoxo للرجال"
    data["women's xoxo championships"] = "بطولة {} xoxo للسيدات"
    data["amateur xoxo championship"] = "بطولة {} xoxo للهواة"
    data["youth xoxo championship"] = "بطولة {} xoxo للشباب"
    data["men's xoxo championship"] = "بطولة {} xoxo للرجال"
    data["women's xoxo championship"] = "بطولة {} xoxo للسيدات"
    data["xoxo cup"] = "كأس {} xoxo"
    data["xoxo cup"] = "كأس {} xoxo"

    number_xo = 0
    for tyu, tyu_lab in New_Tato.items():
        logger.debug(" ========= country =========== ")
        K_at_p = tyu_lab.format("xoxo")
        number_xo += 1
        nat_Lab = "منتخب {} " + K_at_p
        for pre, pre_lab in AFTER_KEYS_TEAM.items():
            number_xo += 1
            pre_lab2 = pre_lab.format(nat_Lab)
            Ab = f"{tyu} xoxo {pre}"
            if pre == "team players" and "women's" in Ab:
                pre_lab2 = pre_lab2.replace(r"لاعبو ", "لاعبات ")
            elif "لاعبو " in pre_lab2 and "women's" in Ab:
                pre_lab2 = pre_lab2.replace(r"لاعبو ", "لاعبات ")
            printo = f"nat_Lab: [{Ab}] : " + pre_lab2
            # if team2 == "road cycling"and pre == "team":
            # print("%d: %s" % (number_xo , printo) )
            logger.debug("%d: %s" % (number_xo, printo))
            data[Ab] = pre_lab2
    # ---national youth handball team
    data["xoxo national team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo"
    data["national xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo"
    # Category:Denmark national football team staff
    data["xoxo national team staff"] = f"طاقم منتخب {NAT_PLACE_HOLDER} xoxo"
    # Category:Denmark national football team non-playing staff
    data["xoxo national team non-playing staff"] = f"طاقم منتخب {NAT_PLACE_HOLDER} xoxo غير اللاعبين"
    # Polish men's volleyball national team national junior men's
    data["national junior men's xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للناشئين"
    data["national junior xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للناشئين"
    data["national women's xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للسيدات"
    data["mennnn's national xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال"
    data["men's xoxo national team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال"
    data["national men's xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال"
    # Australian men's U23 national road cycling team
    data["men's u23 national xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo تحت 23 سنة للرجال"
    data["xoxo league"] = f"دوري {NAT_PLACE_HOLDER} xoxo"
    data["professional xoxo league"] = f"دوري {NAT_PLACE_HOLDER} xoxo للمحترفين"
    data["national youth xoxo team"] = f"منتخب {NAT_PLACE_HOLDER} xoxo للشباب"

    data["national women's xoxo team managers"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات"
    data["national xoxo team managers"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo"

    data["national women's xoxo team coaches"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات"
    data["national xoxo team coaches"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo"

    data["national women's xoxo team trainers"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات"
    data["national xoxo team trainers"] = f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo"
    return data


SPORT_FORMTS_ENAR_P17_TEAM = _build_nat_formats_for_p17()


def get_sport_formts_enar_p17_jobs(suffix: str) -> str:  # sport_formts_enar_p17_jobs
    """
    Return a sport label that merges templates with Arabic sport names.

    Example:
        suffix: "winter olympics softball", return: "كرة لينة {} في الألعاب الأولمبية الشتوية"
    """
    sport_key = match_sport_key(suffix)
    if not sport_key:
        return ""

    sport_label = ""

    template_label = ""
    normalized_key = suffix.replace(sport_key, "xoxo")
    normalized_key = re.sub(sport_key, "xoxo", normalized_key, flags=re.IGNORECASE)

    logger.info(f'Get_SFxo_en_ar_is P17: {suffix=}, {sport_key=}, team_xoxo:"{normalized_key}"')

    if normalized_key in sport_formts_enar_p17_jobs:
        sport_label = SPORTS_KEYS_FOR_JOBS.get(sport_key, "")
        template_label = sport_formts_enar_p17_jobs.get(normalized_key, "")

    else:
        logger.info(
            f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in sport_formts_enar_p17_jobs'
        )

    con_3_label = ""

    if template_label and sport_label:
        con_3_label = apply_pattern_replacements(template_label, sport_label, "xoxo")
        logger.info(f'Get_SFxo_en_ar_is P17 blab:"{con_3_label}"')
    else:
        logger.info(f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in sport_formts_enar_p17_jobs')

    logger.info(f'Get_SFxo_en_ar_is P17 {suffix=}, {con_3_label=}')

    return con_3_label


def Get_Sport_Format_xo_en_ar_is_P17(suffix: str) -> str:  # SPORT_FORMTS_ENAR_P17_TEAM
    """
    Return a sport label that merges templates with Arabic sport names.

    Example:
        suffix: "winter olympics softball", return: "كرة لينة {} في الألعاب الأولمبية الشتوية"
    """
    sport_key = match_sport_key(suffix)
    if not sport_key:
        return ""

    sport_label = ""

    template_label = ""
    normalized_key = suffix.replace(sport_key, "xoxo")
    normalized_key = re.sub(sport_key, "xoxo", normalized_key, flags=re.IGNORECASE)

    logger.info(f'Get_SFxo_en_ar_is P17: {suffix=}, {sport_key=}, team_xoxo:"{normalized_key}"')

    if normalized_key in SPORT_FORMTS_ENAR_P17_TEAM:
        sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")
        template_label = SPORT_FORMTS_ENAR_P17_TEAM.get(normalized_key, "")

    else:
        logger.info(
            f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in SPORT_FORMTS_ENAR_P17_TEAM'
        )

    con_3_label = ""

    if template_label and sport_label:
        con_3_label = apply_pattern_replacements(template_label, sport_label, "xoxo")
        logger.info(f'Get_SFxo_en_ar_is P17 blab:"{con_3_label}"')
    else:
        logger.info(f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in SPORT_FORMTS_ENAR_P17_TEAM')

    logger.info(f'Get_SFxo_en_ar_is P17 {suffix=}, {con_3_label=}')

    return con_3_label


@functools.lru_cache(maxsize=10000)
@dump_data(1)
def get_p17_with_sport(category: str) -> str:
    """
    TODO: use FormatData method
    """
    resolved_label = ""
    category = category.lower()

    suffix, country_start = get_suffix_with_keys(category, countries_from_nat)
    country_start_lab = countries_from_nat.get(country_start, "")

    if not suffix or not country_start:
        logger.info(f'<<lightred>>>>>> {suffix=} or {country_start=} == ""')
        return ""

    logger.debug(f'<<lightblue>> {country_start=}, {suffix=}')
    logger.debug(f'<<lightpurple>>>>>> {country_start_lab=}')

    suffix_label = Get_Sport_Format_xo_en_ar_is_P17(suffix.strip()) or get_sport_formts_enar_p17_jobs(suffix.strip())

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return ""

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> Get_P17_with_p17_sport: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label


__all__ = [
    "Get_Sport_Format_xo_en_ar_is_P17",
    "get_sport_formts_enar_p17_jobs",
    "get_p17_with_sport",
]
