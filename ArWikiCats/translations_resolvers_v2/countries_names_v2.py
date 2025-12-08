#!/usr/bin/python3
"""
TODO: use this inestead of for_me.py
"""
import functools
from ..translations_formats import FormatDataV2
from ..translations import countries_nat_en_key

en_is_P17_ar_is_P17: dict[str, str] = {
    "national university of {en}": "جامعة {ar} الوطنية",
    "Olympic gold medalists for {en} in alpine skiing": "فائزون بميداليات ذهبية أولمبية من {ar} في التزلج على المنحدرات الثلجية",
    "{en} board members": "أعضاء مجلس {ar}",
    "accidental deaths from falls in {en}": "وفيات عرضية نتيجة السقوط في {ar}",
    "{en} conflict": "نزاع {ar}",
    "{en} cup": "كأس {ar}",
    "{en} elections": "انتخابات {ar}",
    "{en} executive cabinet": "مجلس وزراء {ar} التنفيذي",
    "{en} government personnel": "موظفي حكومة {ar}",
    "{en} government": "حكومة {ar}",
    "{en} governorate": "محافظة {ar}",
    "{en} political leader": "قادة {ar} السياسيون",
    "{en} presidents": "رؤساء {ar}",
    "{en} responses": "استجابات {ar}",
    "{en} territorial judges": "قضاة أقاليم {ar}",
    "{en} territorial officials": "مسؤولو أقاليم {ar}",
    "{en} war and conflict": "حروب ونزاعات {ar}",
    "{en} war": "حرب {ar}",
    "{en} afc women's asian cup squad": "تشكيلات {ar} في كأس آسيا للسيدات",
    "{en} afc asian cup squad": "تشكيلات {ar} في كأس آسيا",
    "{en} fifa world cup squad": "تشكيلات {ar} في كأس العالم",
    "{en} fifa futsal world cup squad": "تشكيلات {ar} في كأس العالم لكرة الصالات",
    "{en} summer olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الصيفية",
    "{en} winter olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الشتوية",
    "{en} olympics squad": "تشكيلات {ar} في الألعاب الأولمبية",
    "{en} summer olympics": " {ar} في الألعاب الأولمبية الصيفية",
    "{en} winter olympics": " {ar} في الألعاب الأولمبية الشتوية",
}


all_data: dict[str, str] = {
    # the_female
    # en_is_P17_ar_is_al_women
    "{en} royal air force": "القوات الجوية الملكية {the_female}",
    "{en} civil war": "الحرب الأهلية {the_female}",
    "{en} air force": "القوات الجوية {the_female}",
    "{en} royal defence force": "قوات الدفاع الملكية {the_female}",
    "{en} navy": "البحرية {the_female}",
    "{en} royal navy": "البحرية الملكية {the_female}",
    "{en} naval force": "البحرية {the_female}",
    "{en} naval forces": "البحرية {the_female}",

    # males

    # en_is_P17_ar_is_mens
    "{en} government officials": "مسؤولون حكوميون {males}",

    # the_male
    "{en} premier division": "الدوري {the_male} الممتاز",
    "{en} coast guard": "خفر السواحل {the_male}",

    # the_male
    # military_format_men
    "{en} congressional delegation": "وفود الكونغرس {the_male}",
    "{en} congressional delegations": "وفود الكونغرس {the_male}",
    "{en} parliament": "البرلمان {the_male}",
    "{en} congress": "الكونغرس {the_male}",
    "{en} house of commons": "مجلس العموم {the_male}",
    "{en} house-of-commons": "مجلس العموم {the_male}",
    "{en} senate election": "انتخابات مجلس الشيوخ {the_male}",
    "{en} senate elections": "انتخابات مجلس الشيوخ {the_male}",
    "{en} fa cup": "كأس الاتحاد {the_male}",  # Category:Iraq FA Cup
    "{en} federation cup": "كأس الاتحاد {the_male}",  # Category:Bangladesh Federation Cup
    "{en} marine corps personnel": "أفراد سلاح مشاة البحرية {the_male}",
    "{en} army personnel": "أفراد الجيش {the_male}",
    "{en} coast guard aviation": "طيران خفر السواحل {the_male}",
    "{en} abortion law": "قانون الإجهاض {the_male}",
    "{en} labour law": "قانون العمل {the_male}",  # Category:French_labour_law
    "{en} professional league": "دوري المحترفين {the_male}",
    "{en} first division league": "الدوري {the_male} الدرجة الأولى",
    "{en} second division": "الدوري {the_male} الدرجة الثانية",
    "{en} second division league": "الدوري {the_male} الدرجة الثانية",
    "{en} third division league": "الدوري {the_male} الدرجة الثالثة",
    "{en} forth division league": "الدوري {the_male} الدرجة الرابعة",
}


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatDataV2:
    nats_data = {
        x: v
        for x, v in countries_nat_en_key.items()
        if v.get("ar")
    }
    formatted_data = en_is_P17_ar_is_P17 | all_data

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en}",
        text_before="the ",
    )


def resolve_by_countries_names(category: str) -> str:
    normalized_category = category.lower().replace("category:", "")
    nat_bot = _load_bot()
    result = nat_bot.search(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    return result


__all__ = [
    "resolve_by_countries_names",
]
