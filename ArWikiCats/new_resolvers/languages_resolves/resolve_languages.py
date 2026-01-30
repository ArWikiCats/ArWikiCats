#!/usr/bin/python3
""" """

import functools
import re

from ...helps import getLogger
from ...translations import (
    COMPLEX_LANGUAGE_TRANSLATIONS,
    PRIMARY_LANGUAGE_TRANSLATIONS,
)
from ...translations_formats import FormatDataV2

logger = getLogger(__name__)

new_data = PRIMARY_LANGUAGE_TRANSLATIONS | COMPLEX_LANGUAGE_TRANSLATIONS

formatted_data = {
    # "{en} language": "لغة {ar}",
    "{en} language": "اللغة {al_ar}",
    "{en}-language": "اللغة {al_ar}",
    "{en} languages": "اللغات {al_ar}",
    "{en} language comedy films": "أفلام كوميدية باللغة {al_ar}",
    "{en} language film series": "سلاسل أفلام باللغة {al_ar}",
    "{en} films": "أفلام باللغة {al_ar}",
    "{en} language films": "أفلام باللغة {al_ar}",
    "{en} languages films": "أفلام باللغات {al_ar}",
    "{en} language activists": "ناشطون بلغة {ar}",
    "{en} language non-fiction writers": "كتاب غير روائيين باللغة {al_ar}",
    "{en} language writers": "كتاب باللغة {al_ar}",
    "{en} language singers": "مغنون باللغة {al_ar}",
    "romanization of {en}": "رومنة اللغة {al_ar}",
    "{en} language countries": "بلدان اللغة {al_ar}",
    "{en} language culture": "ثقافة اللغة {al_ar}",
    "{en} language dialects": "لهجات اللغة {al_ar}",
    "{en} language categories": "تصنيفات اللغة {al_ar}",
    "{en} language education": "تعليم اللغة {al_ar}",
    "{en} language given names": "أسماء شخصية باللغة {al_ar}",
    "{en} language grammar": "قواعد اللغة {al_ar}",
    "{en} language literature": "أدب اللغة {al_ar}",
    "{en} language masculine given names": "أسماء ذكور باللغة {al_ar}",
    "{en} language mass media": "إعلام اللغة {al_ar}",
    "{en} language romanization": "رومنة اللغة {al_ar}",
    "{en} language surnames": "ألقاب باللغة {al_ar}",
    "{en} language underground culture": "ثقافة باطنية اللغة {al_ar}",
    "{en} language varieties and styles": "أصناف وأساليب اللغة {al_ar}",
    "{en} language writing system": "نظام كتابة اللغة {al_ar}",
    "{en} newspapers": "صحف باللغة {al_ar}",
    "{en} language newspapers": "صحف باللغة {al_ar}",
    "{en} phonology": "نطقيات {ar}",
    "{en} mythology": "أساطير {ar}",
    "{en} texts": "نصوص {ar}",
    "{en} prose texts": "نصوص نثرية {ar}",
    "{en} languages writing system": "نظام كتابة اللغات {al_ar}",
    "{en} languages dialects": "لهجات اللغات {al_ar}",
    "{en} languages given names": "أسماء شخصية باللغات {al_ar}",
    "{en} languages grammar": "قواعد اللغات {al_ar}",
    "{en} languages surnames": "ألقاب باللغات {al_ar}",
    "{en} language academic journals": "دوريات أكاديمية باللغة {al_ar}",
    "{en} language albums": "ألبومات باللغة {al_ar}",
    "{en} language animation albums": "ألبومات رسوم متحركة باللغة {al_ar}",
    "{en} language books": "كتب باللغة {al_ar}",
    "{en} language comedy albums": "ألبومات كوميدية باللغة {al_ar}",
    "{en} language comic book": "كتب قصص مصورة باللغة {al_ar}",
    "{en} language comic strips": "شرائط كومكس باللغة {al_ar}",
    "{en} language comic": "قصص مصورة باللغة {al_ar}",
    "{en} language comics": "قصص مصورة باللغة {al_ar}",
    "{en} language compilation albums": "ألبومات تجميعية باللغة {al_ar}",
    "{en} language concept albums": "ألبومات مفاهيمية باللغة {al_ar}",
    "{en} language dictionaries": "قواميس باللغة {al_ar}",
    "{en} language encyclopedias": "موسوعات باللغة {al_ar}",
    "{en} language eps albums": "ألبومات أسطوانة مطولة باللغة {al_ar}",
    "{en} language folk albums": "ألبومات فولك باللغة {al_ar}",
    "{en} language folktronica albums": "ألبومات فولكترونيكا باللغة {al_ar}",
    "{en} language graphic novels": "روايات مصورة باللغة {al_ar}",
    "{en} language inscriptions": "نقوش باللغة {al_ar}",
    "{en} language jazz albums": "ألبومات جاز باللغة {al_ar}",
    "{en} language literary awards": "جوائز أدبية باللغة {al_ar}",
    "{en} language live albums": "ألبومات مباشرة باللغة {al_ar}",
    "{en} language magazines": "مجلات باللغة {al_ar}",
    "{en} language manga": "مانغا باللغة {al_ar}",
    "{en} language marvel comics": "مارفال كومكس باللغة {al_ar}",
    "{en} language media": "إعلام باللغة {al_ar}",
    "{en} language medieval literature": "أدب العصور الوسطى باللغة {al_ar}",
    "{en} language mixtape albums": "ألبومات ميكستايب باللغة {al_ar}",
    "{en} language music": "موسيقى باللغة {al_ar}",
    "{en} language musicians": "موسيقيون باللغة {al_ar}",
    "{en} language names": "أسماء باللغة {al_ar}",
    "{en} language novellas": "روايات قصيرة باللغة {al_ar}",
    "{en} language novels": "روايات باللغة {al_ar}",
    "{en} language operas": "أوبيرات باللغة {al_ar}",
    "{en} language people": "أشخاص باللغة {al_ar}",
    "{en} language plays": "مسرحيات باللغة {al_ar}",
    "{en} language poems": "قصائد باللغة {al_ar}",
    "{en} language publications": "منشورات باللغة {al_ar}",
    "{en} language radio stations": "محطات إذاعية باللغة {al_ar}",
    "{en} language remix albums": "ألبومات ريمكس باللغة {al_ar}",
    "{en} language short stories": "قصص قصيرة باللغة {al_ar}",
    "{en} language songs": "أغان باللغة {al_ar}",
    "{en} language surprise albums": "ألبومات مفاجئة باللغة {al_ar}",
    "{en} language telenovelas": "تيلينوفيلا باللغة {al_ar}",
    "{en} language television episodes": "حلقات تلفزيونية باللغة {al_ar}",
    "{en} language television networks": "شبكات تلفزيونية باللغة {al_ar}",
    "{en} language television programmes": "برامج تلفزيونية باللغة {al_ar}",
    "{en} language television programs": "برامج تلفزيونية باللغة {al_ar}",
    "{en} language television seasons": "مواسم تلفزيونية باللغة {al_ar}",
    "{en} language television series": "مسلسلات تلفزيونية باللغة {al_ar}",
    "{en} language television shows": "عروض تلفزيونية باللغة {al_ar}",
    "{en} language television stations": "محطات تلفزيونية باللغة {al_ar}",
    "{en} language television": "تلفاز باللغة {al_ar}",
    "{en} language verbs": "أفعال باللغة {al_ar}",
    "{en} language video albums": "ألبومات فيديو باللغة {al_ar}",
    "{en} language video games": "ألعاب فيديو باللغة {al_ar}",
    "{en} language webcomic": "ويب كومكس باللغة {al_ar}",
    "{en} language webcomics": "ويب كومكس باللغة {al_ar}",
    "{en} language websites": "مواقع ويب باللغة {al_ar}",
    "{en} language words and phrases": "كلمات وجمل باللغة {al_ar}",
    "{en} language works": "أعمال باللغة {al_ar}",
}


def add_definite_article(label: str) -> str:
    """Prefix each word in ``label`` with the Arabic definite article."""
    label = re.sub(r" ال", " ", f" {label} ").strip()
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatDataV2:
    data = {
        x: {
            "ar": v,
            "al_ar": add_definite_article(v),
        }
        for x, v in new_data.items()
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=data,
        key_placeholder="{en}",
        # text_after=" language",
        text_before="",
        # regex_filter=r"[\w-]"
    )


def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "").replace("'", "")
    category = category.replace("-language ", " language ")
    return category


@functools.lru_cache(maxsize=10000)
def _resolve_languages_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start _resolve_languages_labels: {category=}")

    category = fix_keys(category)

    result = _load_bot().search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end _resolve_languages_labels: {category=}, {result=}", result)
    return result


__all__ = [
    "_resolve_languages_labels",
]
