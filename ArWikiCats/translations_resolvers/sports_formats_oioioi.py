#!/usr/bin/python3
"""
Bot for generating Arabic Wikipedia category labels for sports formats involving nationalities and sports.

TODO: replace this file by nats_sport_multi_v2.py

"""

import functools
from ..translations_formats import format_multi_data
from ..translations.nats.Nationality import en_nats_to_ar_label
from ..translations.sports.Sport_key import SPORTS_KEYS_FOR_TEAM

NAT_P17_OIOI = {
    "{en_nat} {en_sport} chairmen and investors": "رؤساء ومسيرو {sport_team} {ar}",
    "{en_nat} defunct indoor {en_sport} clubs": "أندية {sport_team} {ar} داخل الصالات سابقة",
    "{en_nat} defunct {en_sport} clubs": "أندية {sport_team} {ar} سابقة",
    "{en_nat} defunct outdoor {en_sport} clubs": "أندية {sport_team} {ar} في الهواء الطلق سابقة",
    "{en_nat} domestic {en_sport} clubs": "أندية {sport_team} {ar} محلية",
    "{en_nat} domestic women's {en_sport} clubs": "أندية {sport_team} محلية {ar} للسيدات",
    "{en_nat} indoor {en_sport} clubs": "أندية {sport_team} {ar} داخل الصالات",
    "{en_nat} {en_sport} clubs": "أندية {sport_team} {ar}",
    "{en_nat} outdoor {en_sport} clubs": "أندية {sport_team} {ar} في الهواء الطلق",
    "{en_nat} professional {en_sport} clubs": "أندية {sport_team} {ar} للمحترفين",
    "{en_nat} current {en_sport} seasons": "مواسم {sport_team} {ar} حالية",

    "{en_nat} amateur {en_sport} championship": "بطولة {ar} {sport_team} للهواة",
    "{en_nat} amateur {en_sport} championships": "بطولة {ar} {sport_team} للهواة",
    "{en_nat} championships ({en_sport})": "بطولة {ar} {sport_team}",
    "{en_nat} championships {en_sport}": "بطولة {ar} {sport_team}",
    "{en_nat} defunct indoor {en_sport} coaches": "مدربو {sport_team} {ar} داخل الصالات سابقة",
    "{en_nat} defunct indoor {en_sport} competitions": "منافسات {sport_team} {ar} داخل الصالات سابقة",
    "{en_nat} defunct indoor {en_sport} cups": "كؤوس {sport_team} {ar} داخل الصالات سابقة",
    "{en_nat} defunct indoor {en_sport} leagues": "دوريات {sport_team} {ar} داخل الصالات سابقة",
    "{en_nat} defunct {en_sport} coaches": "مدربو {sport_team} {ar} سابقة",
    "{en_nat} defunct {en_sport} competitions": "منافسات {sport_team} {ar} سابقة",
    "{en_nat} defunct {en_sport} cup competitions": "منافسات كؤوس {sport_team} {ar} سابقة",
    "{en_nat} defunct {en_sport} cups": "كؤوس {sport_team} {ar} سابقة",
    "{en_nat} defunct {en_sport} leagues": "دوريات {sport_team} {ar} سابقة",
    "{en_nat} defunct outdoor {en_sport} coaches": "مدربو {sport_team} {ar} في الهواء الطلق سابقة",
    "{en_nat} defunct outdoor {en_sport} competitions": "منافسات {sport_team} {ar} في الهواء الطلق سابقة",
    "{en_nat} defunct outdoor {en_sport} cups": "كؤوس {sport_team} {ar} في الهواء الطلق سابقة",
    "{en_nat} defunct outdoor {en_sport} leagues": "دوريات {sport_team} {ar} في الهواء الطلق سابقة",
    "{en_nat} domestic {en_sport} coaches": "مدربو {sport_team} {ar} محلية",
    "{en_nat} domestic {en_sport} competitions": "منافسات {sport_team} {ar} محلية",
    "{en_nat} domestic {en_sport} cup": "كؤوس {sport_team} {ar} محلية",
    "{en_nat} domestic {en_sport} cups": "كؤوس {sport_team} {ar} محلية",
    "{en_nat} domestic {en_sport} leagues": "دوريات {sport_team} {ar} محلية",
    "{en_nat} domestic {en_sport}": "{sport_team} {ar} محلية",
    "{en_nat} domestic women's {en_sport} coaches": "مدربو {sport_team} محلية {ar} للسيدات",
    "{en_nat} domestic women's {en_sport} competitions": "منافسات {sport_team} محلية {ar} للسيدات",
    "{en_nat} domestic women's {en_sport} cups": "كؤوس {sport_team} محلية {ar} للسيدات",
    "{en_nat} domestic women's {en_sport} leagues": "دوريات {sport_team} محلية {ar} للسيدات",
    "{en_nat} indoor {en_sport} coaches": "مدربو {sport_team} {ar} داخل الصالات",
    "{en_nat} indoor {en_sport} competitions": "منافسات {sport_team} {ar} داخل الصالات",
    "{en_nat} indoor {en_sport} cups": "كؤوس {sport_team} {ar} داخل الصالات",
    "{en_nat} indoor {en_sport} leagues": "دوريات {sport_team} {ar} داخل الصالات",
    "{en_nat} indoor {en_sport}": "{sport_team} {ar} داخل الصالات",
    "{en_nat} men's {en_sport} championship": "بطولة {ar} {sport_team} للرجال",
    "{en_nat} men's {en_sport} championships": "بطولة {ar} {sport_team} للرجال",
    "{en_nat} men's {en_sport} national team": "منتخب {ar} {sport_team} للرجال",
    "{en_nat} men's u23 national {en_sport} team": "منتخب {ar} {sport_team} تحت 23 سنة للرجال",
    "{en_nat} {en_sport} championship": "بطولة {ar} {sport_team}",
    "{en_nat} {en_sport} championships": "بطولة {ar} {sport_team}",
    "{en_nat} {en_sport} coaches": "مدربو {sport_team} {ar}",
    "{en_nat} {en_sport} competitions": "منافسات {sport_team} {ar}",
    "{en_nat} {en_sport} cup competitions": "منافسات كؤوس {sport_team} {ar}",
    "{en_nat} {en_sport} cups": "كؤوس {sport_team} {ar}",
    "{en_nat} {en_sport} indoor championship": "بطولة {ar} {sport_team} داخل الصالات",
    "{en_nat} {en_sport} indoor championships": "بطولة {ar} {sport_team} داخل الصالات",
    "{en_nat} {en_sport} junior championships": "بطولة {ar} {sport_team} للناشئين",
    "{en_nat} {en_sport} leagues": "دوريات {sport_team} {ar}",
    "{en_nat} {en_sport} national team": "منتخب {ar} {sport_team}",
    "{en_nat} {en_sport} u-13 championships": "بطولة {ar} {sport_team} تحت 13 سنة",
    "{en_nat} {en_sport} u-14 championships": "بطولة {ar} {sport_team} تحت 14 سنة",
    "{en_nat} {en_sport} u-15 championships": "بطولة {ar} {sport_team} تحت 15 سنة",
    "{en_nat} {en_sport} u-16 championships": "بطولة {ar} {sport_team} تحت 16 سنة",
    "{en_nat} {en_sport} u-17 championships": "بطولة {ar} {sport_team} تحت 17 سنة",
    "{en_nat} {en_sport} u-18 championships": "بطولة {ar} {sport_team} تحت 18 سنة",
    "{en_nat} {en_sport} u-19 championships": "بطولة {ar} {sport_team} تحت 19 سنة",
    "{en_nat} {en_sport} u-20 championships": "بطولة {ar} {sport_team} تحت 20 سنة",
    "{en_nat} {en_sport} u-21 championships": "بطولة {ar} {sport_team} تحت 21 سنة",
    "{en_nat} {en_sport} u-23 championships": "بطولة {ar} {sport_team} تحت 23 سنة",
    "{en_nat} {en_sport} u-24 championships": "بطولة {ar} {sport_team} تحت 24 سنة",
    "{en_nat} {en_sport} u13 championships": "بطولة {ar} {sport_team} تحت 13 سنة",
    "{en_nat} {en_sport} u14 championships": "بطولة {ar} {sport_team} تحت 14 سنة",
    "{en_nat} {en_sport} u15 championships": "بطولة {ar} {sport_team} تحت 15 سنة",
    "{en_nat} {en_sport} u16 championships": "بطولة {ar} {sport_team} تحت 16 سنة",
    "{en_nat} {en_sport} u17 championships": "بطولة {ar} {sport_team} تحت 17 سنة",
    "{en_nat} {en_sport} u18 championships": "بطولة {ar} {sport_team} تحت 18 سنة",
    "{en_nat} {en_sport} u19 championships": "بطولة {ar} {sport_team} تحت 19 سنة",
    "{en_nat} {en_sport} u20 championships": "بطولة {ar} {sport_team} تحت 20 سنة",
    "{en_nat} {en_sport} u21 championships": "بطولة {ar} {sport_team} تحت 21 سنة",
    "{en_nat} {en_sport} u23 championships": "بطولة {ar} {sport_team} تحت 23 سنة",
    "{en_nat} {en_sport} u24 championships": "بطولة {ar} {sport_team} تحت 24 سنة",
    "{en_nat} open ({en_sport})": "{ar} المفتوحة {sport_team}",
    "{en_nat} open {en_sport}": "{ar} المفتوحة {sport_team}",
    "{en_nat} outdoor {en_sport} championship": "بطولة {ar} {sport_team} في الهواء الطلق",
    "{en_nat} outdoor {en_sport} championships": "بطولة {ar} {sport_team} في الهواء الطلق",
    "{en_nat} outdoor {en_sport} coaches": "مدربو {sport_team} {ar} في الهواء الطلق",
    "{en_nat} outdoor {en_sport} competitions": "منافسات {sport_team} {ar} في الهواء الطلق",
    "{en_nat} outdoor {en_sport} cups": "كؤوس {sport_team} {ar} في الهواء الطلق",
    "{en_nat} outdoor {en_sport} leagues": "دوريات {sport_team} {ar} في الهواء الطلق",
    "{en_nat} outdoor {en_sport}": "{sport_team} {ar} في الهواء الطلق",
    "{en_nat} professional {en_sport} coaches": "مدربو {sport_team} {ar} للمحترفين",
    "{en_nat} professional {en_sport} competitions": "منافسات {sport_team} {ar} للمحترفين",
    "{en_nat} professional {en_sport} cups": "كؤوس {sport_team} {ar} للمحترفين",
    "{en_nat} professional {en_sport} leagues": "دوريات {sport_team} {ar} للمحترفين",
    "{en_nat} women's {en_sport} championship": "بطولة {ar} {sport_team} للسيدات",
    "{en_nat} women's {en_sport} championships": "بطولة {ar} {sport_team} للسيدات",
    "{en_nat} women's {en_sport}": "{sport_team} {ar} نسائية",
    "{en_nat} youth {en_sport} championship": "بطولة {ar} {sport_team} للشباب",
    "{en_nat} youth {en_sport} championships": "بطولة {ar} {sport_team} للشباب",
}

both_bot = format_multi_data(
    NAT_P17_OIOI,
    en_nats_to_ar_label,
    key_placeholder="{en_nat}",
    value_placeholder="{ar}",
    data_list2=SPORTS_KEYS_FOR_TEAM,
    key2_placeholder="{en_sport}",
    value2_placeholder="{sport_team}",
    # text_after=" people",
    # text_before="the ",
)


@functools.lru_cache(maxsize=None)
def sport_lab_oioioi_load(category) -> str:
    return both_bot.create_label(category)


__all__ = [
    "sport_lab_oioioi_load",
]
