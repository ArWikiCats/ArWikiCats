#!/usr/bin/python3
""" """

import functools
import logging

from ...translations import All_Nat, all_country_with_nat, countries_en_as_nationality_keys
from ...translations_formats import FormatDataDoubleV2
from ..nats_as_country_names import nats_keys_as_country_names

logger = logging.getLogger(__name__)

countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]

formatted_data = {
    "{en} relations": "العلاقات {the_female}",
    "{en} border crossings": "معابر الحدود {the_female}",
    "{en} joint economic efforts": "الجهود الاقتصادية المشتركة {the_female}",
    "{en} conflict video games": "ألعاب فيديو الصراع {the_male}",
    "{en} conflict legal issues": "قضايا قانونية في الصراع {the_male}",
    "{en} conflict": "الصراع {the_male}",
    "{en} football rivalry": "التنافس {the_male} في كرة القدم",
    # "jewish persian": "فرس يهود",
    "{en}": "{males}",
    "{en} people": "{males}",
    # north american-jewish culture
    "{en} surnames": "ألقاب {female}",
    "{en} culture": "ثقافة {female}",
    "{en} war video games": "ألعاب فيديو الحرب {the_female}",
    "{en} war films": "أفلام الحرب {the_female}",
    "{en} families": "عائلات {female}",
    "{en} war": "الحرب {the_female}",
    "{en} war of independence": "حرب الاستقلال {the_female}",
    "{en} wars": "الحروب {the_female}",
    "{en} television series": "مسلسلات تلفزيونية {female}",
    "{en} literature": "أدب {male}",
    "{en} history": "تاريخ {male}",
    "{en} cuisine": "مطبخ {male}",
    "{en} descent": "أصل {male}",
    "{en} diaspora": "شتات {male}",
    "{en} law": "قانون {male}",
    "{en} wine": "نبيذ {male}",
    "{en} traditions": "تراث {male}",
    "{en} folklore": "فلكور {male}",
    "{en} television": "تلفاز {male}",
    "{en} rock genres": "أنواع روك {male}",
    "{en} musical groups": "فرق موسيقية {female}",
    "{en} music": "موسيقى {female}",
    "{en} music genres": "أنواع موسيقى {female}",
    "{en} genres": "أنواع {female}",
    "{en} novels": "روايات {female}",
    "{en} architecture": "عمارة {female}",
    "{en} plays": "مسرحيات {female}",
    "{en} gangs": "عصابات {female}",
    # Category:People murdered by Italian-American organized crime
    "{en} organized crime": "جريمة منظمة {female}",
}

nats_data = {x: v for x, v in All_Nat.items()}
nats_data.update({x: v for x, v in nats_keys_as_country_names.items()})
nats_data.update(
    {
        "ireland": {
            "male": "أيرلندي",
            "males": "أيرلنديون",
            "female": "أيرلندية",
            "females": "أيرلنديات",
            "the_male": "الأيرلندي",
            "the_female": "الأيرلندية",
            "en": "ireland",
            "ar": "أيرلندا",
        }
    }
)


@functools.lru_cache(maxsize=1)
def double_bot() -> FormatDataDoubleV2:
    # Template data with both nationality and sport placeholders
    # "german jewish history": "تاريخ يهودي ألماني",

    # Create an instance of the FormatDataDoubleV2 class with the formatted data and data list
    _bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en}",
        splitter=r"[−–\- ]",
        sort_ar_labels=True,
    )

    return _bot


def fix_keys(category: str) -> str:
    """Fix known issues in category keys before searching.

    Args:
        category: The original category key.
    """
    # Fix specific known issues with category keys
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")
    return category.strip()


@functools.lru_cache(maxsize=10000)
def resolve_by_nats_double_v2(category: str) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start {category=}")

    if category in countries_en_as_nationality_keys or category in countries_en_keys:
        logger.info(f"<<yellow>> skip resolve_by_nats_double_v2: {category=}, [result=]")
        return ""

    if category in nats_data:
        # NOTE: only nationality key should be handled by other resolvers
        logger.info(f"<<yellow>> skip resolve_by_nats_double_v2: one nationality key only {category=}, [result=]")
        return ""

    nat_bot = double_bot()
    result = nat_bot.search_all_category(category)
    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "resolve_by_nats_double_v2",
]
