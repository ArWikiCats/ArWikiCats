#!/usr/bin/python3
"""
Resolve country names categories translations
"""
from typing import Dict
import functools
from ...helps import logger
from ...translations_formats import FormatData, MultiDataFormatterBase
from ...translations import countries_from_nat, COUNTRY_LABEL_OVERRIDES

# NOTE: ONLY_COUNTRY_NAMES should not merge to formatted_data_en_ar_only directly

ONLY_COUNTRY_NAMES = {
    "{en} political leader": "قادة {ar} السياسيون",
    "government ministers of {en}": "وزراء {ar}",
    "secretaries of {en}": "وزراء {ar}",
    "state lieutenant governors of {en}": "نواب حكام الولايات في {ar}",
    "state secretaries of state of {en}": "وزراء خارجية الولايات في {ar}",
}

# NOTE: formatted_data_en_ar_only used in other resolver
formatted_data_en_ar_only: Dict[str, str] = {

    "ministries of the government of {en}": "وزارات حكومة {ar}",
    "government ministers of {en}": "وزراء {ar}",
    "secretaries of {en}": "وزراء {ar}",
    "united states secretaries of state": "وزراء خارجية أمريكيون",
    "state cabinet secretaries of {en}": "أعضاء مجلس وزراء {ar}",

    "{en}": "{ar}",
    "{en} women's international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم",

    "police of {en}": "شرطة {ar}",
    "army of {en}": "جيش {ar}",
    "national congress ({en})": "المؤتمر الوطني ({ar})",
    "national council ({en})": "المجلس الوطني ({ar})",
    "national assembly ({en})": "الجمعية الوطنية ({ar})",

    "senate ({en})": "مجلس الشيوخ ({ar})",
    "{en} general assembly": "جمعية {ar} العامة",
    "parliament of {en}": "برلمان {ar}",
    "accidental deaths from falls in {en}": "وفيات عرضية نتيجة السقوط في {ar}",
    "bodies of water of {en}": "مسطحات مائية في {ar}",
    "national university of {en}": "جامعة {ar} الوطنية",
    "national library of {en}": "مكتبة {ar} الوطنية",
    "{en} afc asian cup squad": "تشكيلات {ar} في كأس آسيا",
    "{en} afc women's asian cup squad": "تشكيلات {ar} في كأس آسيا للسيدات",
    "{en} board members": "أعضاء مجلس {ar}",
    "{en} conflict": "نزاع {ar}",
    "{en} cup": "كأس {ar}",
    "{en} elections": "انتخابات {ar}",
    "{en} executive cabinet": "مجلس وزراء {ar} التنفيذي",
    "{en} fifa futsal world cup squad": "تشكيلات {ar} في كأس العالم لكرة الصالات",
    "{en} fifa world cup squad": "تشكيلات {ar} في كأس العالم",
    "{en} government personnel": "موظفي حكومة {ar}",
    "{en} government": "حكومة {ar}",
    "{en} governorate": "محافظة {ar}",
    "{en} olympics squad": "تشكيلات {ar} في الألعاب الأولمبية",
    "{en} presidents": "رؤساء {ar}",
    "{en} responses": "استجابات {ar}",
    "{en} summer olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الصيفية",
    "{en} summer olympics": " {ar} في الألعاب الأولمبية الصيفية",
    "{en} territorial judges": "قضاة أقاليم {ar}",
    "{en} territorial officials": "مسؤولو أقاليم {ar}",
    "{en} war and conflict": "حروب ونزاعات {ar}",
    "{en} war": "حرب {ar}",
    "{en} winter olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الشتوية",
    "{en} winter olympics": " {ar} في الألعاب الأولمبية الشتوية",
}

main_data = {
    "{en} amateur international footballers": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} amateur international soccer players": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} amateur international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم",
    "{en} international rally": "رالي {ar} الدولي",
    "{en} international rules football team": "منتخب {ar} لكرة القدم الدولية",
    "{en} international soccer players": "لاعبو منتخب {ar} لكرة القدم",
    "{en} international soccer playerss": "لاعبو منتخب {ar} لكرة القدم",
    "{en} men's a' international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's a' international soccer players": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's a' international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's b international footballers": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's b international soccer players": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's b international soccer playerss": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's international soccer players": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's youth international footballers": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} men's youth international soccer players": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} men's youth international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} national football team managers": "مدربو منتخب {ar} لكرة القدم",
    "{en} national team": "منتخبات {ar} الوطنية",
    "{en} national teams": "منتخبات {ar} الوطنية",
    "{en} rally championship": "بطولة {ar} للراليات",
    "{en} sports templates": "قوالب {ar} الرياضية",
    "{en} women's international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's international soccer players": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's international soccer playerss": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} women's youth international soccer players": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} women's youth international soccer playerss": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} youth international footballers": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} youth international soccer players": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} youth international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للشباب",
}

formatted_data_en_ar_only.update(main_data)

formatted_data_en_ar_only.update({
    x.replace("secretaries of", "secretaries-of"): y
    for x, y in formatted_data_en_ar_only.items()
    if "secretaries of" in x
})

formatted_data_updated = dict(formatted_data_en_ar_only)
formatted_data_updated.update(ONLY_COUNTRY_NAMES)
countries_from_nat_data: Dict[str, str] = dict(countries_from_nat)

# TODO: update countries_from_nat_data with COUNTRY_LABEL_OVERRIDES after check any issues!


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:

    return FormatData(
        formatted_data_updated,
        countries_from_nat_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        text_before="the ",
        regex_filter=r"[\w-]",
    )


@functools.lru_cache(maxsize=10000)
def resolve_by_countries_names(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_by_countries_names: {category=}")

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)

    logger.debug(f"<<yellow>> end resolve_by_countries_names: {category=}, {result=}")
    return result


__all__ = [
    "resolve_by_countries_names",
]
