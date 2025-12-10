#!/usr/bin/python3
"""
TODO: use FormatData method
"""

import functools
import re
from typing import Dict, Tuple
from ...helps.log import logger
from ...translations_formats import format_multi_data
from ..nats.Nationality import en_nats_to_ar_label
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM
from ..utils.match_sport_keys import match_sport_key

NAT_P17_OIOI = {
    "{nat} amateur oioioi championship": "بطولة {nat} ixix للهواة",
    "{nat} amateur oioioi championships": "بطولة {nat} ixix للهواة",
    "{nat} championships (oioioi)": "بطولة {nat} ixix",
    "{nat} championships oioioi": "بطولة {nat} ixix",
    "{nat} current oioioi seasons": "مواسم ixix {nat} حالية",
    "{nat} defunct indoor oioioi clubs": "أندية ixix {nat} داخل الصالات سابقة",
    "{nat} defunct indoor oioioi coaches": "مدربو ixix {nat} داخل الصالات سابقة",
    "{nat} defunct indoor oioioi competitions": "منافسات ixix {nat} داخل الصالات سابقة",
    "{nat} defunct indoor oioioi cups": "كؤوس ixix {nat} داخل الصالات سابقة",
    "{nat} defunct indoor oioioi leagues": "دوريات ixix {nat} داخل الصالات سابقة",
    "{nat} defunct oioioi clubs": "أندية ixix {nat} سابقة",
    "{nat} defunct oioioi coaches": "مدربو ixix {nat} سابقة",
    "{nat} defunct oioioi competitions": "منافسات ixix {nat} سابقة",
    "{nat} defunct oioioi cup competitions": "منافسات كؤوس ixix {nat} سابقة",
    "{nat} defunct oioioi cups": "كؤوس ixix {nat} سابقة",
    "{nat} defunct oioioi leagues": "دوريات ixix {nat} سابقة",
    "{nat} defunct outdoor oioioi clubs": "أندية ixix {nat} في الهواء الطلق سابقة",
    "{nat} defunct outdoor oioioi coaches": "مدربو ixix {nat} في الهواء الطلق سابقة",
    "{nat} defunct outdoor oioioi competitions": "منافسات ixix {nat} في الهواء الطلق سابقة",
    "{nat} defunct outdoor oioioi cups": "كؤوس ixix {nat} في الهواء الطلق سابقة",
    "{nat} defunct outdoor oioioi leagues": "دوريات ixix {nat} في الهواء الطلق سابقة",
    "{nat} domestic oioioi clubs": "أندية ixix {nat} محلية",
    "{nat} domestic oioioi coaches": "مدربو ixix {nat} محلية",
    "{nat} domestic oioioi competitions": "منافسات ixix {nat} محلية",
    "{nat} domestic oioioi cup": "كؤوس ixix {nat} محلية",
    "{nat} domestic oioioi cups": "كؤوس ixix {nat} محلية",
    "{nat} domestic oioioi leagues": "دوريات ixix {nat} محلية",
    "{nat} domestic oioioi": "ixix {nat} محلية",
    "{nat} domestic women's oioioi clubs": "أندية ixix محلية {nat} للسيدات",
    "{nat} domestic women's oioioi coaches": "مدربو ixix محلية {nat} للسيدات",
    "{nat} domestic women's oioioi competitions": "منافسات ixix محلية {nat} للسيدات",
    "{nat} domestic women's oioioi cups": "كؤوس ixix محلية {nat} للسيدات",
    "{nat} domestic women's oioioi leagues": "دوريات ixix محلية {nat} للسيدات",
    "{nat} indoor oioioi clubs": "أندية ixix {nat} داخل الصالات",
    "{nat} indoor oioioi coaches": "مدربو ixix {nat} داخل الصالات",
    "{nat} indoor oioioi competitions": "منافسات ixix {nat} داخل الصالات",
    "{nat} indoor oioioi cups": "كؤوس ixix {nat} داخل الصالات",
    "{nat} indoor oioioi leagues": "دوريات ixix {nat} داخل الصالات",
    "{nat} indoor oioioi": "ixix {nat} داخل الصالات",
    "{nat} men's oioioi championship": "بطولة {nat} ixix للرجال",
    "{nat} men's oioioi championships": "بطولة {nat} ixix للرجال",
    "{nat} men's oioioi national team": "منتخب {nat} ixix للرجال",
    "{nat} men's u23 national oioioi team": "منتخب {nat} ixix تحت 23 سنة للرجال",
    "{nat} oioioi chairmen and investors": "رؤساء ومسيرو ixix {nat}",
    "{nat} oioioi championship": "بطولة {nat} ixix",
    "{nat} oioioi championships": "بطولة {nat} ixix",
    "{nat} oioioi clubs": "أندية ixix {nat}",
    "{nat} oioioi coaches": "مدربو ixix {nat}",
    "{nat} oioioi competitions": "منافسات ixix {nat}",
    "{nat} oioioi cup competitions": "منافسات كؤوس ixix {nat}",
    "{nat} oioioi cups": "كؤوس ixix {nat}",
    "{nat} oioioi indoor championship": "بطولة {nat} ixix داخل الصالات",
    "{nat} oioioi indoor championships": "بطولة {nat} ixix داخل الصالات",
    "{nat} oioioi junior championships": "بطولة {nat} ixix للناشئين",
    "{nat} oioioi leagues": "دوريات ixix {nat}",
    "{nat} oioioi national team": "منتخب {nat} ixix",
    "{nat} oioioi u-13 championships": "بطولة {nat} ixix تحت 13 سنة",
    "{nat} oioioi u-14 championships": "بطولة {nat} ixix تحت 14 سنة",
    "{nat} oioioi u-15 championships": "بطولة {nat} ixix تحت 15 سنة",
    "{nat} oioioi u-16 championships": "بطولة {nat} ixix تحت 16 سنة",
    "{nat} oioioi u-17 championships": "بطولة {nat} ixix تحت 17 سنة",
    "{nat} oioioi u-18 championships": "بطولة {nat} ixix تحت 18 سنة",
    "{nat} oioioi u-19 championships": "بطولة {nat} ixix تحت 19 سنة",
    "{nat} oioioi u-20 championships": "بطولة {nat} ixix تحت 20 سنة",
    "{nat} oioioi u-21 championships": "بطولة {nat} ixix تحت 21 سنة",
    "{nat} oioioi u-23 championships": "بطولة {nat} ixix تحت 23 سنة",
    "{nat} oioioi u-24 championships": "بطولة {nat} ixix تحت 24 سنة",
    "{nat} oioioi u13 championships": "بطولة {nat} ixix تحت 13 سنة",
    "{nat} oioioi u14 championships": "بطولة {nat} ixix تحت 14 سنة",
    "{nat} oioioi u15 championships": "بطولة {nat} ixix تحت 15 سنة",
    "{nat} oioioi u16 championships": "بطولة {nat} ixix تحت 16 سنة",
    "{nat} oioioi u17 championships": "بطولة {nat} ixix تحت 17 سنة",
    "{nat} oioioi u18 championships": "بطولة {nat} ixix تحت 18 سنة",
    "{nat} oioioi u19 championships": "بطولة {nat} ixix تحت 19 سنة",
    "{nat} oioioi u20 championships": "بطولة {nat} ixix تحت 20 سنة",
    "{nat} oioioi u21 championships": "بطولة {nat} ixix تحت 21 سنة",
    "{nat} oioioi u23 championships": "بطولة {nat} ixix تحت 23 سنة",
    "{nat} oioioi u24 championships": "بطولة {nat} ixix تحت 24 سنة",
    "{nat} open (oioioi)": "{nat} المفتوحة ixix",
    "{nat} open oioioi": "{nat} المفتوحة ixix",
    "{nat} outdoor oioioi championship": "بطولة {nat} ixix في الهواء الطلق",
    "{nat} outdoor oioioi championships": "بطولة {nat} ixix في الهواء الطلق",
    "{nat} outdoor oioioi clubs": "أندية ixix {nat} في الهواء الطلق",
    "{nat} outdoor oioioi coaches": "مدربو ixix {nat} في الهواء الطلق",
    "{nat} outdoor oioioi competitions": "منافسات ixix {nat} في الهواء الطلق",
    "{nat} outdoor oioioi cups": "كؤوس ixix {nat} في الهواء الطلق",
    "{nat} outdoor oioioi leagues": "دوريات ixix {nat} في الهواء الطلق",
    "{nat} outdoor oioioi": "ixix {nat} في الهواء الطلق",
    "{nat} professional oioioi clubs": "أندية ixix {nat} للمحترفين",
    "{nat} professional oioioi coaches": "مدربو ixix {nat} للمحترفين",
    "{nat} professional oioioi competitions": "منافسات ixix {nat} للمحترفين",
    "{nat} professional oioioi cups": "كؤوس ixix {nat} للمحترفين",
    "{nat} professional oioioi leagues": "دوريات ixix {nat} للمحترفين",
    "{nat} women's oioioi championship": "بطولة {nat} ixix للسيدات",
    "{nat} women's oioioi championships": "بطولة {nat} ixix للسيدات",
    "{nat} women's oioioi": "ixix {nat} نسائية",
    "{nat} youth oioioi championship": "بطولة {nat} ixix للشباب",
    "{nat} youth oioioi championships": "بطولة {nat} ixix للشباب",
}
# ---

# Placeholder used for sport key substitution in templates
SPORT_PLACEHOLDER = "oioioi"
LABEL_PLACEHOLDER = "ixix"

NAT_P17_OIOI_ADD = {
    "{nat} defunct oioioi coaches": "مدربو ixix {nat} سابقة",
    "{nat} defunct oioioi competitions": "منافسات ixix {nat} سابقة",
    "{nat} defunct oioioi cup competitions": "منافسات كؤوس ixix {nat} سابقة",
    "{nat} oioioi championships": "بطولة {nat} ixix",
    "{nat} oioioi clubs": "أندية ixix {nat}",
    "{nat} oioioi coaches": "مدربو ixix {nat}",
    "{nat} oioioi competitions": "منافسات ixix {nat}",
    "{nat} oioioi cup competitions": "منافسات كؤوس ixix {nat}",
    "{nat} oioioi cups": "كؤوس ixix {nat}",
    "{nat} oioioi indoor championship": "بطولة {nat} ixix داخل الصالات",
}

NAT_P17_OIOI.update(NAT_P17_OIOI_ADD)


@functools.lru_cache(maxsize=None)
def _get_start_p17(cate: str, check_the: bool = False) -> Tuple[str, str]:
    """
    Fast and optimized version of _get_start_p17.

    Example:
        cate: "swiss wheelchair curling championship": result: ("{nat} wheelchair curling championship", "swiss"),
    """
    # Pre-lower cate once for speed
    cate_lower = cate.lower()

    category_suffix: str = ""
    country_prefix: str = ""

    cate2 = cate[4:] if cate.startswith("the ") else cate

    cate_lower2 = cate_lower[4:] if cate_lower.startswith("the ") else cate_lower

    for key in en_nats_to_ar_label:
        if category_suffix:
            # A match has already been found; exit early
            break

        # Pre-lower key only once
        key_lower = key.lower().strip()

        # Build minimal prefix options
        # Index meanings are kept exactly as original logic
        candidate_prefixes: Dict[int, str] = {
            1: f"{key_lower} people",
            2: f"{key_lower} ",
        }

        # Add the "the <country>" special case
        if key.startswith("the "):
            candidate_prefixes[3] = key[4:].lower()

        # Try each prefix option in fixed order
        for option_index in (1, 2, 3):
            prefix_candidate = candidate_prefixes.get(option_index)
            if not prefix_candidate:
                continue

            if cate_lower.startswith(prefix_candidate):
                country_prefix = key
                category_suffix = cate[len(prefix_candidate) :].strip()

                logger.debug(f"<<lightyellow>>>>>> {prefix_candidate=}, {category_suffix=}, {country_prefix=}")

                break

            if check_the and cate_lower2.startswith(prefix_candidate):
                country_prefix = key
                category_suffix = cate2[len(prefix_candidate) :].strip()

                logger.debug(f"<<lightyellow>>>>>> {prefix_candidate=}, {category_suffix=}, {country_prefix=}")

                break

    # Logging final result if match found
    if category_suffix and country_prefix:
        logger.debug(
            f'<<lightpurple>>>>>> bot_te_4.py country_start:"{country_prefix}",_get_start_p17 fo_3:"{category_suffix}"'
        )

    if category_suffix and not category_suffix.startswith("{nat}"):
        category_suffix = f"{{nat}} {category_suffix}"

    # TODO: Remove this
    sport_format_label = _make_sport_formats_p17(category_suffix)
    if not sport_format_label:
        return "", ""

    return category_suffix, country_prefix


@functools.lru_cache(maxsize=None)
def _make_sport_formats_p17(category_key: str) -> str:
    """Resolve a sport format label for P17 lookups.

    Args:
        category_key: The category key to resolve

    Returns:
        Resolved sport format label or empty string
    """
    logger.info(f'<<lightblue>>>>>> _make_sport_formats_p17: {category_key=}')

    resolved_label = ""
    sport_key = match_sport_key(category_key)

    if not sport_key:
        return ""

    sport_label = ""

    placeholder_key = category_key.replace(sport_key, SPORT_PLACEHOLDER)
    placeholder_key = re.sub(sport_key, SPORT_PLACEHOLDER, placeholder_key, flags=re.IGNORECASE)
    logger.debug(
        f'_make_sport_formats_p17 {category_key=}, {sport_key=}, {placeholder_key=}'
    )

    placeholder_template = NAT_P17_OIOI.get(placeholder_key, "")

    if not placeholder_template:
        logger.debug(f'_make_sport_formats_p17 {placeholder_key=} not in NAT_P17_OIOI')
        return ""

    sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")
    if not sport_label:
        logger.debug(f' {sport_key=} not in SPORTS_KEYS_FOR_TEAM ')

    if not placeholder_template or not sport_label:
        return ""

    formatted_label = placeholder_template.replace(LABEL_PLACEHOLDER, sport_label)

    if LABEL_PLACEHOLDER not in formatted_label:
        resolved_label = formatted_label

    logger.info(f'_make_sport_formats_p17 {category_key=}, {resolved_label=}')

    return resolved_label


@functools.lru_cache(maxsize=None)
def sport_lab_oioioi_load_new(category: str, check_the: bool = False) -> str:
    """
    Example:
        category:Yemeni under-13 baseball teams", result: "فرق كرة قاعدة يمنية تحت 13 سنة"
    """
    normalized_category = category.lower()

    sport_format_key, country_start = _get_start_p17(normalized_category, check_the=check_the)

    logger.debug(f"sport_lab_oioioi_load {normalized_category=}: {sport_format_key=} {country_start=}")

    if not country_start or not sport_format_key:
        return ""

    country_label = en_nats_to_ar_label.get(country_start, "")

    if not country_label:
        return ""

    sport_format_label = _make_sport_formats_p17(sport_format_key)
    if not sport_format_label:
        return ""

    category_label = sport_format_label.format(nat=country_label)
    logger.debug(f'<<lightblue>>xxx sport_lab_oioioi_load: new {category_label=}')

    return category_label

# ======================
#
# ======================


both_bot = format_multi_data(
    NAT_P17_OIOI,
    en_nats_to_ar_label,
    key_placeholder="{nat}",
    value_placeholder="{nat}",
    data_list2=SPORTS_KEYS_FOR_TEAM,
    key2_placeholder=SPORT_PLACEHOLDER,
    value2_placeholder=LABEL_PLACEHOLDER,
    # text_after=" people",
    # text_before="the ",
)


@functools.lru_cache(maxsize=None)
def sport_lab_oioioi_load(category) -> str:
    return both_bot.create_label(category)


__all__ = [
    "sport_lab_oioioi_load",
    "sport_lab_oioioi_load_new",
]
