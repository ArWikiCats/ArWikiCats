"""
TODO: merge with translations_resolvers OR translations_resolvers_v2
"""
import functools
import re
from ...helps import dump_data, logger, len_print
from ...translations import (
    AFTER_KEYS_TEAM,
    countries_from_nat,
    SPORTS_KEYS_FOR_TEAM,
    match_sport_key,
    apply_pattern_replacements,
)

from ..jobs_bots.get_helps import get_suffix_with_keys


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
    NAT_PLACE_HOLDER = "{}"
    data = {
        "xoxo league": "دوري {} xoxo ",
        "professional xoxo league": "دوري {} xoxo للمحترفين",
        "amateur xoxo cup": "كأس {} xoxo للهواة",
        "youth xoxo cup": "كأس {} xoxo للشباب",
        "men's xoxo cup": "كأس {} xoxo للرجال",
        "women's xoxo cup": "كأس {} xoxo للسيدات",
        "amateur xoxo championships": "بطولة {} xoxo للهواة",
        "youth xoxo championships": "بطولة {} xoxo للشباب",
        "men's xoxo championships": "بطولة {} xoxo للرجال",
        "women's xoxo championships": "بطولة {} xoxo للسيدات",
        "amateur xoxo championship": "بطولة {} xoxo للهواة",
        "youth xoxo championship": "بطولة {} xoxo للشباب",
        "men's xoxo championship": "بطولة {} xoxo للرجال",
        "women's xoxo championship": "بطولة {} xoxo للسيدات",
        "xoxo cup": "كأس {} xoxo",
        # ---national youth handball team
        "xoxo national team": f"منتخب {NAT_PLACE_HOLDER} xoxo",
        "national xoxo team": f"منتخب {NAT_PLACE_HOLDER} xoxo",

        # Category:Denmark national football team staff
        "xoxo national team staff": f"طاقم منتخب {NAT_PLACE_HOLDER} xoxo",

        # Category:Denmark national football team non-playing staff
        "xoxo national team non-playing staff": f"طاقم منتخب {NAT_PLACE_HOLDER} xoxo غير اللاعبين",

        # Polish men's volleyball national team national junior men's
        "national junior men's xoxo team": f"منتخب {NAT_PLACE_HOLDER} xoxo للناشئين",
        "national junior xoxo team": f"منتخب {NAT_PLACE_HOLDER} xoxo للناشئين",
        "national women's xoxo team": f"منتخب {NAT_PLACE_HOLDER} xoxo للسيدات",
        "mennnn's national xoxo team": f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال",
        "men's xoxo national team": f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال",
        "national men's xoxo team": f"منتخب {NAT_PLACE_HOLDER} xoxo للرجال",

        # Australian men's U23 national road cycling team
        "men's u23 national xoxo team": f"منتخب {NAT_PLACE_HOLDER} xoxo تحت 23 سنة للرجال",
        "national youth xoxo team": f"منتخب {NAT_PLACE_HOLDER} xoxo للشباب",

        "national women's xoxo team managers": f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات",
        "national xoxo team managers": f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo",

        "national women's xoxo team coaches": f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات",
        "national xoxo team coaches": f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo",

        "national women's xoxo team trainers": f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo للسيدات",
        "national xoxo team trainers": f"مدربو منتخب {NAT_PLACE_HOLDER} xoxo",
    }

    return data


def generate_team_data(New_Tato) -> dict:
    data = {}
    for tyu, tyu_lab in New_Tato.items():
        logger.debug(" ========= country =========== ")
        K_at_p = tyu_lab.format("xoxo")
        nat_Lab = "منتخب {} " + K_at_p

        for pre, pre_lab in AFTER_KEYS_TEAM.items():    # 35
            pre_lab2 = pre_lab.format(nat_Lab)
            Ab = f"{tyu} xoxo {pre}"

            if pre == "team players" and "women's" in Ab:
                pre_lab2 = pre_lab2.replace(r"لاعبو ", "لاعبات ")

            elif "لاعبو " in pre_lab2 and "women's" in Ab:
                pre_lab2 = pre_lab2.replace(r"لاعبو ", "لاعبات ")

            data[Ab] = pre_lab2
    return data


NEW_TATO = _build_new_tato()                    # 110
TEAM_DATA = generate_team_data(NEW_TATO)        # 3850

SPORT_FORMTS_ENAR_P17_TEAM = _build_nat_formats_for_p17()  # 33


def Get_Sport_Format_xo_en_ar_is_P17(suffix: str) -> str:
    """
    Return a sport label that merges templates with Arabic sport names.

    Example:
        suffix: "winter olympics softball", return: "كرة لينة {} في الألعاب الأولمبية الشتوية"
    """
    sport_key = match_sport_key(suffix)
    if not sport_key:
        return ""

    sport_label = ""

    normalized_key = suffix.replace(sport_key, "xoxo")
    normalized_key = re.sub(sport_key, "xoxo", normalized_key, flags=re.IGNORECASE)

    logger.info(f'Get_SFxo_en_ar_is P17: {suffix=}, {sport_key=}, team_xoxo:"{normalized_key}"')

    template_label = SPORT_FORMTS_ENAR_P17_TEAM.get(normalized_key, "") or TEAM_DATA.get(normalized_key, "")
    if template_label:
        sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")

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

    suffix_label = Get_Sport_Format_xo_en_ar_is_P17(suffix.strip())

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return ""

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> Get_P17_with_p17_sport: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label


len_print.data_len(
    "p17_bot_sport.py",
    {
        "NEW_TATO": NEW_TATO,
        "TEAM_DATA": TEAM_DATA,
        "SPORT_FORMTS_ENAR_P17_TEAM": SPORT_FORMTS_ENAR_P17_TEAM,
    },
)

__all__ = [
    "get_p17_with_sport",
]
