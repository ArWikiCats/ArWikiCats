#!/usr/bin/python3
"""
Bot for generating Arabic Wikipedia category labels for sports formats involving nationalities and sports.
"""

import functools
from ...translations_formats import format_multi_data
from ..nats.Nationality import en_nats_to_ar_label
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM


# Placeholder used for sport key substitution in templates
SPORT_PLACEHOLDER = "{sport_en}"
LABEL_PLACEHOLDER = "{sport_ar}"


NAT_P17_OIOI = {
    "{nat} amateur {sport_en} championship": "بطولة {ar} {sport_ar} للهواة",
    "{nat} amateur {sport_en} championships": "بطولة {ar} {sport_ar} للهواة",
    "{nat} championships ({sport_en})": "بطولة {ar} {sport_ar}",
    "{nat} championships {sport_en}": "بطولة {ar} {sport_ar}",
    "{nat} current {sport_en} seasons": "مواسم {sport_ar} {nat} حالية",
    "{nat} defunct indoor {sport_en} clubs": "أندية {sport_ar} {nat} داخل الصالات سابقة",
    "{nat} defunct indoor {sport_en} coaches": "مدربو {sport_ar} {nat} داخل الصالات سابقة",
    "{nat} defunct indoor {sport_en} competitions": "منافسات {sport_ar} {nat} داخل الصالات سابقة",
    "{nat} defunct indoor {sport_en} cups": "كؤوس {sport_ar} {nat} داخل الصالات سابقة",
    "{nat} defunct indoor {sport_en} leagues": "دوريات {sport_ar} {nat} داخل الصالات سابقة",
    "{nat} defunct {sport_en} clubs": "أندية {sport_ar} {nat} سابقة",
    "{nat} defunct {sport_en} coaches": "مدربو {sport_ar} {nat} سابقة",
    "{nat} defunct {sport_en} competitions": "منافسات {sport_ar} {nat} سابقة",
    "{nat} defunct {sport_en} cup competitions": "منافسات كؤوس {sport_ar} {nat} سابقة",
    "{nat} defunct {sport_en} cups": "كؤوس {sport_ar} {nat} سابقة",
    "{nat} defunct {sport_en} leagues": "دوريات {sport_ar} {nat} سابقة",
    "{nat} defunct outdoor {sport_en} clubs": "أندية {sport_ar} {nat} في الهواء الطلق سابقة",
    "{nat} defunct outdoor {sport_en} coaches": "مدربو {sport_ar} {nat} في الهواء الطلق سابقة",
    "{nat} defunct outdoor {sport_en} competitions": "منافسات {sport_ar} {nat} في الهواء الطلق سابقة",
    "{nat} defunct outdoor {sport_en} cups": "كؤوس {sport_ar} {nat} في الهواء الطلق سابقة",
    "{nat} defunct outdoor {sport_en} leagues": "دوريات {sport_ar} {nat} في الهواء الطلق سابقة",
    "{nat} domestic {sport_en} clubs": "أندية {sport_ar} {nat} محلية",
    "{nat} domestic {sport_en} coaches": "مدربو {sport_ar} {nat} محلية",
    "{nat} domestic {sport_en} competitions": "منافسات {sport_ar} {nat} محلية",
    "{nat} domestic {sport_en} cup": "كؤوس {sport_ar} {nat} محلية",
    "{nat} domestic {sport_en} cups": "كؤوس {sport_ar} {nat} محلية",
    "{nat} domestic {sport_en} leagues": "دوريات {sport_ar} {nat} محلية",
    "{nat} domestic {sport_en}": "{sport_ar} {nat} محلية",
    "{nat} domestic women's {sport_en} clubs": "أندية {sport_ar} محلية {nat} للسيدات",
    "{nat} domestic women's {sport_en} coaches": "مدربو {sport_ar} محلية {nat} للسيدات",
    "{nat} domestic women's {sport_en} competitions": "منافسات {sport_ar} محلية {nat} للسيدات",
    "{nat} domestic women's {sport_en} cups": "كؤوس {sport_ar} محلية {nat} للسيدات",
    "{nat} domestic women's {sport_en} leagues": "دوريات {sport_ar} محلية {nat} للسيدات",
    "{nat} indoor {sport_en} clubs": "أندية {sport_ar} {nat} داخل الصالات",
    "{nat} indoor {sport_en} coaches": "مدربو {sport_ar} {nat} داخل الصالات",
    "{nat} indoor {sport_en} competitions": "منافسات {sport_ar} {nat} داخل الصالات",
    "{nat} indoor {sport_en} cups": "كؤوس {sport_ar} {nat} داخل الصالات",
    "{nat} indoor {sport_en} leagues": "دوريات {sport_ar} {nat} داخل الصالات",
    "{nat} indoor {sport_en}": "{sport_ar} {nat} داخل الصالات",
    "{nat} men's {sport_en} championship": "بطولة {ar} {sport_ar} للرجال",
    "{nat} men's {sport_en} championships": "بطولة {ar} {sport_ar} للرجال",
    "{nat} men's {sport_en} national team": "منتخب {nat} {sport_ar} للرجال",
    "{nat} men's u23 national {sport_en} team": "منتخب {nat} {sport_ar} تحت 23 سنة للرجال",
    "{nat} {sport_en} chairmen and investors": "رؤساء ومسيرو {sport_ar} {nat}",
    "{nat} {sport_en} championship": "بطولة {ar} {sport_ar}",
    "{nat} {sport_en} championships": "بطولة {ar} {sport_ar}",
    "{nat} {sport_en} clubs": "أندية {sport_ar} {nat}",
    "{nat} {sport_en} coaches": "مدربو {sport_ar} {nat}",
    "{nat} {sport_en} competitions": "منافسات {sport_ar} {nat}",
    "{nat} {sport_en} cup competitions": "منافسات كؤوس {sport_ar} {nat}",
    "{nat} {sport_en} cups": "كؤوس {sport_ar} {nat}",
    "{nat} {sport_en} indoor championship": "بطولة {ar} {sport_ar} داخل الصالات",
    "{nat} {sport_en} indoor championships": "بطولة {ar} {sport_ar} داخل الصالات",
    "{nat} {sport_en} junior championships": "بطولة {ar} {sport_ar} للناشئين",
    "{nat} {sport_en} leagues": "دوريات {sport_ar} {nat}",
    "{nat} {sport_en} national team": "منتخب {nat} {sport_ar}",
    "{nat} {sport_en} u-13 championships": "بطولة {ar} {sport_ar} تحت 13 سنة",
    "{nat} {sport_en} u-14 championships": "بطولة {ar} {sport_ar} تحت 14 سنة",
    "{nat} {sport_en} u-15 championships": "بطولة {ar} {sport_ar} تحت 15 سنة",
    "{nat} {sport_en} u-16 championships": "بطولة {ar} {sport_ar} تحت 16 سنة",
    "{nat} {sport_en} u-17 championships": "بطولة {ar} {sport_ar} تحت 17 سنة",
    "{nat} {sport_en} u-18 championships": "بطولة {ar} {sport_ar} تحت 18 سنة",
    "{nat} {sport_en} u-19 championships": "بطولة {ar} {sport_ar} تحت 19 سنة",
    "{nat} {sport_en} u-20 championships": "بطولة {ar} {sport_ar} تحت 20 سنة",
    "{nat} {sport_en} u-21 championships": "بطولة {ar} {sport_ar} تحت 21 سنة",
    "{nat} {sport_en} u-23 championships": "بطولة {ar} {sport_ar} تحت 23 سنة",
    "{nat} {sport_en} u-24 championships": "بطولة {ar} {sport_ar} تحت 24 سنة",
    "{nat} {sport_en} u13 championships": "بطولة {ar} {sport_ar} تحت 13 سنة",
    "{nat} {sport_en} u14 championships": "بطولة {ar} {sport_ar} تحت 14 سنة",
    "{nat} {sport_en} u15 championships": "بطولة {ar} {sport_ar} تحت 15 سنة",
    "{nat} {sport_en} u16 championships": "بطولة {ar} {sport_ar} تحت 16 سنة",
    "{nat} {sport_en} u17 championships": "بطولة {ar} {sport_ar} تحت 17 سنة",
    "{nat} {sport_en} u18 championships": "بطولة {ar} {sport_ar} تحت 18 سنة",
    "{nat} {sport_en} u19 championships": "بطولة {ar} {sport_ar} تحت 19 سنة",
    "{nat} {sport_en} u20 championships": "بطولة {ar} {sport_ar} تحت 20 سنة",
    "{nat} {sport_en} u21 championships": "بطولة {ar} {sport_ar} تحت 21 سنة",
    "{nat} {sport_en} u23 championships": "بطولة {ar} {sport_ar} تحت 23 سنة",
    "{nat} {sport_en} u24 championships": "بطولة {ar} {sport_ar} تحت 24 سنة",
    "{nat} open ({sport_en})": "{nat} المفتوحة {sport_ar}",
    "{nat} open {sport_en}": "{nat} المفتوحة {sport_ar}",
    "{nat} outdoor {sport_en} championship": "بطولة {ar} {sport_ar} في الهواء الطلق",
    "{nat} outdoor {sport_en} championships": "بطولة {ar} {sport_ar} في الهواء الطلق",
    "{nat} outdoor {sport_en} clubs": "أندية {sport_ar} {nat} في الهواء الطلق",
    "{nat} outdoor {sport_en} coaches": "مدربو {sport_ar} {nat} في الهواء الطلق",
    "{nat} outdoor {sport_en} competitions": "منافسات {sport_ar} {nat} في الهواء الطلق",
    "{nat} outdoor {sport_en} cups": "كؤوس {sport_ar} {nat} في الهواء الطلق",
    "{nat} outdoor {sport_en} leagues": "دوريات {sport_ar} {nat} في الهواء الطلق",
    "{nat} outdoor {sport_en}": "{sport_ar} {nat} في الهواء الطلق",
    "{nat} professional {sport_en} clubs": "أندية {sport_ar} {nat} للمحترفين",
    "{nat} professional {sport_en} coaches": "مدربو {sport_ar} {nat} للمحترفين",
    "{nat} professional {sport_en} competitions": "منافسات {sport_ar} {nat} للمحترفين",
    "{nat} professional {sport_en} cups": "كؤوس {sport_ar} {nat} للمحترفين",
    "{nat} professional {sport_en} leagues": "دوريات {sport_ar} {nat} للمحترفين",
    "{nat} women's {sport_en} championship": "بطولة {ar} {sport_ar} للسيدات",
    "{nat} women's {sport_en} championships": "بطولة {ar} {sport_ar} للسيدات",
    "{nat} women's {sport_en}": "{sport_ar} {nat} نسائية",
    "{nat} youth {sport_en} championship": "بطولة {ar} {sport_ar} للشباب",
    "{nat} youth {sport_en} championships": "بطولة {ar} {sport_ar} للشباب",
}

both_bot = format_multi_data(
    NAT_P17_OIOI,
    en_nats_to_ar_label,
    key_placeholder="{nat}",
    value_placeholder="{ar}",
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
]
