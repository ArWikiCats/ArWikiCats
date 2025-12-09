#!/usr/bin/python3
"""
TODO: use this instead of :
- for_me.py
- countries_names.py

"""
import functools
from ..translations_formats import FormatDataV2
from ..translations import countries_nat_en_key
from ..translations_resolvers.countries_names import formatted_data_en_ar_only
countries_nat_en_key_example = {
    "yemen": {
        "ar": "اليمن",
        "en": "Yemen",
        "male": "يمني",
        "female": "يمنية",
        "the_male": "اليمني",
        "the_female": "اليمنية",
    }
}

new_data: dict[str, str] = {
    # ar new
    "national library of {en}": "مكتبة {ar} الوطنية",
    "dependent territories of {en}": "أقاليم ما وراء البحار {the_female}",
    "bodies of water of {en}": "مسطحات مائية في {ar}",
}

# NOTE: patterns with only en-ar should be in formatted_data_en_ar_only countries_names.py to handle countries without gender details

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

all_data |= formatted_data_en_ar_only


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatDataV2:
    nats_data = {
        x: v
        for x, v in countries_nat_en_key.items()
        if v.get("ar")
    }
    formatted_data = all_data | new_data

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en}",
        text_before="the ",
    )


def resolve_by_countries_names_v2(category: str) -> str:
    normalized_category = category.lower().replace("category:", "")
    nat_bot = _load_bot()
    result = nat_bot.search(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    return result


__all__ = [
    "resolve_by_countries_names_v2",
]
