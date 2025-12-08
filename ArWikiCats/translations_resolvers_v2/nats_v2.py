#!/usr/bin/python3
"""
TODO: use this inestead of for_me.py
"""
import functools
from ..translations_formats import FormatDataV2
from ..translations import all_country_with_nat_ar

all_data: dict[str, str] = {
    # en_is_nat_ar_is_mens
    "{en} non profit publishers": "ناشرون غير ربحيون {males}",
    "{en} non-profit publishers": "ناشرون غير ربحيون {males}",
    "{en} government officials": "مسؤولون حكوميون {males}",

    # ar
    # en_is_nat_ar_is_P17
    "{en} grand prix": "جائزة {ar} الكبرى",
    "{en} king's cup": "كأس ملك {ar}",  # Bahraini King's Cup
    "{en} cup": "كأس {ar}",
    "{en} independence": "استقلال {ar}",
    "{en} open": "{ar} المفتوحة",
    "{en} ladies open": "{ar} المفتوحة للسيدات",
    "{en} national university": "جامعة {ar} الوطنية",
    "{en} national university alumni": "خريجو جامعة {ar} الوطنية",
    "{en} national women's motorsports racing team": "منتخب {ar} لسباق رياضة المحركات للسيدات",

    # the_male
    # en_is_nat_ar_is_al_mens
    "{en} president cup": "كأس الرئيس {the_male}",
    "{en} federation cup": "كأس الاتحاد {the_male}",
    "{en} fa cup": "كأس الاتحاد {the_male}",
    "{en} occupation": "الاحتلال {the_male}",
    "{en} super cup": "كأس السوبر {the_male}",
    "{en} elite cup": "كأس النخبة {the_male}",
    "{en} referendum": "الاستفتاء {the_male}",
    "{en} involvement": "التدخل {the_male}",
    "{en} census": "التعداد {the_male}",

    "{en} professional football league": "دوري كرة القدم {the_male} للمحترفين",
    "{en} premier football league": "الدوري {the_male} الممتاز لكرة القدم",
    "{en} national super league": "دوري السوبر {the_male}",
    "{en} super league": "دوري السوبر {the_male}",
    "{en} premier league": "الدوري {the_male} الممتاز",
    "{en} premier division": "الدوري {the_male} الممتاز",
    "{en} amateur football league": "الدوري {the_male} لكرة القدم للهواة",
    "{en} football league": "الدوري {the_male} لكرة القدم",
    "{en} population census": "التعداد السكاني {the_male}",
    "{en} population and housing census": "التعداد {the_male} للسكان والمساكن",
    "{en} national party": "الحزب الوطني {the_male}",
    "{en} criminal law": "القانون الجنائي {the_male}",
    "{en} family law": "قانون الأسرة {the_male}",
    "{en} labour law": "قانون العمل {the_male}",
    "{en} abortion law": "قانون الإجهاض {the_male}",
    "{en} rugby union leagues": "اتحاد دوري الرجبي {the_male}",
    "{en} women's rugby union": "اتحاد الرجبي {the_male} للنساء",
    "{en} rugby union": "اتحاد الرجبي {the_male}",
    "{en} presidential pardons": "العفو الرئاسي {the_male}",
    "{en} pardons": "العفو {the_male}",
}


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatDataV2:
    nats_data = {
        x: v
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar")
    }

    return FormatDataV2(
        formatted_data=all_data,
        data_list=nats_data,
        key_placeholder="{en}",
        text_before="the ",
    )


def resolve_by_nats(category: str) -> str:
    normalized_category = category.lower().replace("category:", "")
    nat_bot = _load_bot()
    result = nat_bot.search(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    return result


__all__ = [
    "resolve_by_nats",
]
