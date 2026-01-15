"""Ethnic labelling helpers."""

from __future__ import annotations

import functools
from typing import Dict

from ...helps import logger, dump_data
from ...translations import all_nat_sorted, Nat_men, Nat_mens, Nat_women
from ..jobs_bots.get_helps import get_suffix_with_keys

# NOTE: looks like female_data in nationalities_v2.py
en_is_nat_ar_is_women_2: Dict[str, str] = {
    "airstrikes": "ضربات جوية {}",
    "archipelagoes": "أرخبيلات {}",
    "architecture": "عمارة {}",
    "autobiographies": "ترجمة ذاتية {}",
    "automotive": "سيارات {}",
    "awards": "جوائز {}",
    "awards and decorations": "جوائز وأوسمة {}",
    "ballot measures": "إجراءات اقتراع {}",
    "ballot propositions": "اقتراحات اقتراع {}",
    "border": "حدود {}",
    "border crossings": "معابر حدودية {}",
    "brands": "ماركات {}",
    "budgets": "موازنات {}",
    "buildings": "مباني {}",
    "business culture": "ثقافة مالية {}",
    "businesspeople": "شخصيات أعمال {}",
    "cantons": "كانتونات {}",
    "casualties": "خسائر {}",
    "cathedrals": "كاتدرائيات {}",
    "championships": "بطولات {}",
    "civil awards and decorations": "جوائز وأوسمة مدنية {}",
    "classical albums": "ألبومات كلاسيكية {}",
    "classical music": "موسيقى كلاسيكية {}",
    "clothing": "ملابس {}",
    "clubs": "أندية {}",
    "coats of arms": "شعارات نبالة {}",
    "colonial": "مستعمرات {}",
    "comedy": "كوميديا {}",
    "comedy albums": "ألبومات كوميدية {}",
    "comedy music": "موسيقى كوميدية {}",
    "companies": "شركات {}",
    "competitions": "منافسات {}",
    "compilation albums": "ألبومات تجميعية {}",
    "countries": "بلدان {}",
    "crimes": "جرائم {}",
    "crimes against humanity": "جرائم ضد الإنسانية {}",
    "culture": "ثقافة {}",
    "decorations": "أوسمة {}",
    "diplomatic missions": "بعثات دبلوماسية {}",
    "discoveries": "اكتشافات {}",
    "drink": "مشروبات {}",
    "elections": "انتخابات {}",
    "encyclopedias": "موسوعات {}",
    "executions": "إعدامات {}",
    "explosions": "انفجارات {}",
    "families": "عائلات {}",
    "fauna": "حيوانات {}",
    "festivals": "مهرجانات {}",
    "film series": "سلاسل أفلام {}",
    "folk albums": "ألبومات فلكلورية {}",
    "folk music": "موسيقى فلكلورية {}",
    "folklore characters": "شخصيات فلكلورية {}",
    "football club matches": "مباريات أندية كرة قدم {}",
    "football club seasons": "مواسم أندية كرة قدم {}",
    "forests": "غابات {}",
    "gangs": "عصابات {}",
    "given names": "أسماء شخصية {}",
    "heraldry": "نبالة {}",
    "heritage sites": "موقع تراث عالمي {}",
    "inscriptions": "نقوش {}",
    "introductions": "استحداثات {}",
    "inventions": "اختراعات {}",
    "islands": "جزر {}",
    "issues": "قضايا {}",
    "jewellery": "مجوهرات {}",
    "journalism": "صحافة {}",
    "lakes": "بحيرات {}",
    "learned and professional societies": "جمعيات علمية ومهنية {}",
    "learned societies": "جمعيات علمية {}",
    "literary awards": "جوائز أدبية {}",
    "magazines": "مجلات {}",
    "mascots": "تمائم {}",
    "masculine given names": "أسماء ذكور {}",
    "media": "وسائل إعلام {}",
    "media personalities": "شخصيات إعلامية {}",
    "memoirs": "مذكرات {}",
    "memorials and cemeteries": "نصب تذكارية ومقابر {}",
    "military equipment": "معدات عسكرية {}",
    "military terminology": "مصطلحات عسكرية {}",
    "military-equipment": "معدات عسكرية {}",
    "military-terminology": "مصطلحات عسكرية {}",
    "miniseries": "مسلسلات قصيرة {}",
    "monarchy": "ملكية {}",
    "motorsport": "رياضة محركات {}",
    "mountains": "جبال {}",
    "movies": "أفلام {}",
    "mythology": "أساطير {}",
    "names": "أسماء {}",
    "nationalism": "قومية {}",
    "newspapers": "صحف {}",
    "non profit organizations": "منظمات غير ربحية {}",
    "non-profit organizations": "منظمات غير ربحية {}",
    "novels": "روايات {}",
    "occupations": "مهن {}",
    "online journalism": "صحافة إنترنت {}",
    "operas": "أوبيرات {}",
    "organisations": "منظمات {}",
    "organizations": "منظمات {}",
    "parishes": "أبرشيات {}",
    "parks": "متنزهات {}",
    "peoples": "شعوب {}",
    "philosophy": "فلسفة {}",
    "phonologies": "تصريفات صوتية {}",
    "phonology": "نطقيات {}",
    "plays": "مسرحيات {}",
    "poems": "قصائد {}",
    "political philosophy": "فلسفة سياسية {}",
    "popular culture": "ثقافة شعبية {}",
    "professional societies": "جمعيات مهنية {}",
    "provinces": "مقاطعات {}",
    "publications": "منشورات {}",
    "radio": "راديو {}",
    "radio networks": "شبكات مذياع {}",
    "radio stations": "محطات إذاعية {}",
    "rebellions": "تمردات {}",
    "rectors": "عمدات {}",
    "referendums": "استفتاءات {}",
    "religions": "ديانات {}",
    "religious occupations": "مهن دينية {}",
    "resorts": "منتجعات {}",
    "restaurants": "مطاعم {}",
    "revolutions": "ثورات {}",
    "riots": "أعمال شغب {}",
    "road cycling": "سباقات دراجات على الطريق {}",
    "roads": "طرقات {}",
    "royal families": "عائلات ملكية {}",
    "schools and colleges": "مدارس وكليات {}",
    "sculptures": "منحوتات {}",
    "sea temples": "معابد بحرية {}",
    "short stories": "قصص قصيرة {}",
    "societies": "جمعيات {}",
    "songs": "أغاني {}",
    "sorts events": "أحداث رياضية {}",
    "soundtracks": "موسيقى تصويرية {}",
    "sport": "رياضة {}",
    "sports": "رياضة {}",
    "sports competitions": "منافسات رياضية {}",
    "sports events": "أحداث رياضية {}",
    "sports-events": "أحداث رياضية {}",
    "surnames": "ألقاب {}",
    "swamps": "مستنقعات {}",
    "telenovelas": "تيلينوفيلا {}",
    "television commercials": "إعلانات تجارية تلفزيونية {}",
    "television films": "أفلام تلفزيونية {}",
    "television networks": "شبكات تلفزيونية {}",
    "television news": "أخبار تلفزيونية {}",
    "television personalities": "شخصيات تلفزيونية {}",
    "television programmes": "برامج تلفزيونية {}",
    "television programs": "برامج تلفزيونية {}",
    "television series": "مسلسلات تلفزيونية {}",
    "television series-debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series-endings": "مسلسلات تلفزيونية {} انتهت في",
    "television stations": "محطات تلفزيونية {}",
    "television-seasons": "مواسم تلفزيونية {}",
    "temples": "معابد {}",
    "tennis": "كرة مضرب {}",
    "terminology": "مصطلحات {}",
    "titles": "ألقاب {}",
    "tour": "بطولات {}",
    "towns": "بلدات {}",
    "trains": "قطارات {}",
    "trials": "محاكمات {}",
    "tribes": "قبائل {}",
    "underground culture": "ثقافة باطنية {}",
    "universities": "جامعات {}",
    "verbs": "أفعال {}",
    "video games": "ألعاب فيديو {}",
    "volcanoes": "براكين {}",
    "war crimes": "جرائم حرب {}",
    "wars": "حروب {}",
    "waterfalls": "شلالات {}",
    "webcomic": "ويب كومكس {}",
    "webcomics": "ويب كومكس {}",
    "websites": "مواقع ويب {}",
    "women's sport": "رياضة {} نسائية",
    "works": "أعمال {}",
    "youth competitions": "منافسات شبابية {}",
    "youth music competitions": "منافسات موسيقية شبابية {}",
    "mixtape albums": "ألبومات ميكستايب {}",
    "mixtape music": "موسيقى ميكستايب {}",
    "music": "موسيقى {}",
    "music people": "شخصيات موسيقية {}",
    "music personalities": "شخصيات موسيقية {}",
    "musical duos": "فرق موسيقية ثنائية {}",
    "musical groups": "فرق موسيقية {}",
    "musical instruments": "آلات موسيقية {}",
    "youth sports competitions": "منافسات رياضية شبابية {}"
}

MALE_TOPIC_TABLE: Dict[str, str] = {
    "history": "تاريخ {}",
    "descent": "أصل {}",
    "cuisine": "مطبخ {}",
    "literature": "أدب {}",
    "law": "قانون {}",
    "wine": "نبيذ {}",
    "diaspora": "شتات {}",
    "traditions": "تراث {}",
    "folklore": "فلكور {}",
    "television": "تلفاز {}",
}


@functools.lru_cache(maxsize=None)
def ethnic_culture(category: str, start: str, suffix: str) -> str:
    """Return the cultural label for ``suffix`` relative to ``start``.

    Args:
        category: Full category name (used only for logging).
        start: The base nationality or country.
        suffix: The trailing segment describing the specific topic.

    Returns:
        The resolved label or an empty string.
    """

    if not Nat_women.get(start, "") and not Nat_men.get(start, ""):
        return ""

    logger.debug(f"Resolving ethnic culture, category={category}, start={start}, suffix={suffix}")

    topic_label = ""
    group_label = ""
    start_label = ""

    # Try to resolve using women-centric templates first.
    start_women_label = Nat_women.get(start, "")
    if start_women_label:
        for key, template in en_is_nat_ar_is_women_2.items():
            candidate_suffix = f" {key}"
            if suffix.endswith(candidate_suffix):
                base_key = suffix[: -len(candidate_suffix)].strip()
                group_label = Nat_women.get(base_key, "")
                if group_label:
                    topic_label = template
                    start_label = start_women_label
                    break

    # Fallback to male templates when the women-specific search fails.
    if not topic_label:
        start_men_label = Nat_men.get(start, "")
        if start_men_label:
            for key, template in MALE_TOPIC_TABLE.items():
                candidate_suffix = f" {key}"
                if suffix.endswith(candidate_suffix):
                    base_key = suffix[: -len(candidate_suffix)].strip()
                    group_label = Nat_men.get(base_key, "")
                    if group_label:
                        topic_label = template
                        start_label = start_men_label
                        break

    if topic_label and group_label and start_label:
        combined = f"{group_label} {start_label}"
        resolved = topic_label.format(combined)
        logger.debug(f'<<lightblue>> ethnic_culture resolved label "{resolved}" for "{category}"')
        return resolved

    return ""


@functools.lru_cache(maxsize=None)
def ethnic(category: str, start: str, suffix: str) -> str:
    """Return the ethnic label for ``category``."""

    logger.debug(f"Resolving ethnic label, category={category}, start={start}, suffix={suffix}")

    group_label = Nat_mens.get(suffix, "")
    start_label = Nat_mens.get(start, "")
    if group_label and start_label:
        resolved = f"{group_label} {start_label}"
        logger.debug(f'<<lightblue>> ethnic resolved label "{resolved}" for "{category}"')
        return resolved

    return ""


@functools.lru_cache(maxsize=None)
def ethnic_label(category: str, nat: str = "", suffix: str = "") -> str:
    if not suffix or not nat:
        suffix, nat = get_suffix_with_keys(category, all_nat_sorted, "nat")

    normalized_suffix = suffix
    if suffix.endswith(" people"):
        candidate = suffix[: -len(" people")]
        if Nat_mens.get(candidate, ""):
            normalized_suffix = candidate

    result = ethnic(category, nat, normalized_suffix)

    if not result:
        result = ethnic_culture(category, nat, normalized_suffix)

    return result


@functools.lru_cache(maxsize=None)
@dump_data(1)
def ethnic_label_main(category: str) -> str:
    logger.debug(f"<<lightyellow>>>> ethnic_label_main >> category:({category})")
    # return ""
    normalized_category = category.lower().replace("_", " ").replace("-", " ")
    result = ""
    suffix, nationality_key = get_suffix_with_keys(normalized_category, all_nat_sorted, "nat")

    if suffix:
        result = ethnic_label(normalized_category, nationality_key, suffix)

    logger.debug(f'<<lightblue>> ethnic_label_main :: "{result}"')
    return result


__all__ = [
    "ethnic",
    "ethnic_label",
    "ethnic_label_main",
    "ethnic_culture",
]
