#!/usr/bin/python3
"""
Bot for translating job-related and nationality-based categories.

This module provides functionality for matching and translating categories
related to jobs, nationalities, and multi-sports topics from English to Arabic.

TODO: planed to be replaced by ArWikiCats.new_resolvers.nationalities_resolvers
"""

import functools
from ..new_resolvers.jobs_resolvers import resolve_jobs_main

from ..helps import logger

multi_sport_for_jobs = {
    "afc asian cup": "كأس آسيا",
    "afc asian cup finals": "نهائيات كأس آسيا",
    "afc asian cup qualification": "تصفيات كأس آسيا",
    "afc challenge league": "دوري التحدي الآسيوي",
    "afc champions league": "دوري أبطال آسيا",
    "afc champions league elite": "دوري نخبة ابطال آسيا",
    "afc champions league two": "دوري أبطال آسيا الثاني",
    "afc cup": "كأس الاتحاد الآسيوي",
    "afc cup participants": "مشاركون في كأس الاتحاد الآسيوي لكرة القدم",
    "afc elite league": "دوري نخبة ابطال آسيا",
    "afc football": "كرة قدم الاتحاد الآسيوي لكرة القدم",
    "afc futsal asian cup": "كأس آسيا لكرة الصالات",
    "afc futsal championship": "بطولة آسيا لكرة الصالات",
    "afc futsal club championship": "بطولة آسيا لكرة الصالات للأندية",
    "afc president's cup": "كأس رئيس الاتحاد الآسيوي",
    "afc solidarity cup": "كأس التضامن الآسيوي",
    "afc u-16 asian cup": "كأس آسيا للناشئين تحت 16 سنة",
    "afc u-16 championship": "بطولة آسيا للناشئين تحت 16 سنة",
    "afc u-16 women's asian cup": "كأس آسيا للسيدات تحت 16 سنة",
    "afc u-16 women's championship": "بطولة آسيا للسيدات تحت 16 سنة",
    "afc u-17 asian cup": "كأس آسيا للناشئين تحت 17 سنة",
    "afc u-17 championship": "بطولة آسيا للناشئين تحت 17 سنة",
    "afc u-17 women's asian cup": "كأس آسيا للسيدات تحت 17 سنة",
    "afc u-17 women's championship": "بطولة آسيا للسيدات تحت 17 سنة",
    "afc u-19 asian cup": "كأس آسيا للناشئين تحت 19 سنة",
    "afc u-19 championship": "بطولة آسيا للناشئين تحت 19 سنة",
    "afc u-19 women's asian cup": "كأس آسيا للسيدات تحت 19 سنة",
    "afc u-19 women's championship": "بطولة آسيا للسيدات تحت 19 سنة",
    "afc u-20 asian cup": "كأس آسيا للناشئين تحت 20 سنة",
    "afc u-20 championship": "بطولة آسيا للناشئين تحت 20 سنة",
    "afc u-20 women's asian cup": "كأس آسيا للسيدات تحت 20 سنة",
    "afc u-20 women's championship": "بطولة آسيا للسيدات تحت 20 سنة",
    "afc u-22 asian cup": "كأس آسيا للناشئين تحت 22 سنة",
    "afc u-22 championship": "بطولة آسيا للناشئين تحت 22 سنة",
    "afc u-22 women's asian cup": "كأس آسيا للسيدات تحت 22 سنة",
    "afc u-22 women's championship": "بطولة آسيا للسيدات تحت 22 سنة",
    "afc u-23 asian cup": "كأس آسيا تحت 23 سنة",
    "afc u-23 championship": "بطولة آسيا تحت 23 سنة",
    "afc u-23 women's asian cup": "كأس آسيا للسيدات تحت 23 سنة",
    "afc u-23 women's championship": "بطولة آسيا للسيدات تحت 23 سنة",
    "afc women's asian cup": "كأس الأمم الآسيوية لكرة القدم للسيدات",
    "afc women's championship": "بطولة آسيا للسيدات",
    "afc women's futsal championship": "بطولة آسيا لكرة الصالات للسيدات",
    "afc youth championship": "بطولة آسيا للشباب",
    "african games": "الألعاب الإفريقية",
    "asian beach games": "دورة الألعاب الآسيوية الشاطئية",
    "asian football confederation": "الاتحاد الآسيوي لكرة القدم",
    "asian games": "الألعاب الآسيوية",
    "asian indoor games": "دورة الألعاب الآسيوية داخل الصالات",
    "asian para games": "الألعاب البارالمبية الآسيوية",
    "asian summer games": "الألعاب الآسيوية الصيفية",
    "asian winter games": "الألعاب الآسيوية الشتوية",
    "association football afc": "كرة القدم في الاتحاد الآسيوي لكرة القدم",
    "association-football afc": "كرة القدم في الاتحاد الآسيوي لكرة القدم",
    "bolivarian games": "الألعاب البوليفارية",
    "central american and caribbean games": "ألعاب أمريكا الوسطى والكاريبي",
    "central american games": "ألعاب أمريكا الوسطى",
    "commonwealth games": "ألعاب الكومنولث",
    "commonwealth youth games": "ألعاب الكومنولث الشبابية",
    "deaflympic games": "ألعاب ديفلمبياد",
    "european games": "الألعاب الأوروبية",
    "european youth olympic": "الألعاب الأولمبية الشبابية الأوروبية",
    "european youth olympic winter": "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "fifa futsal world cup": "كأس العالم لكرة الصالات",
    "fifa futsal world cup qualification": "تصفيات كأس العالم لكرة الصالات",
    "fifa futsal world cup qualification (afc)": "تصفيات كأس العالم لكرة الصالات (آسيا)",
    "fifa futsal world cup qualification (caf)": "تصفيات كأس العالم لكرة الصالات (إفريقيا)",
    "fifa world cup qualification (afc)": "تصفيات كأس العالم لكرة القدم (آسيا)",
    "fifa world cup qualification (caf)": "تصفيات كأس العالم لكرة القدم (إفريقيا)",
    "fis nordic world ski championships": "بطولة العالم للتزلج النوردي على الثلج",
    "friendship games": "ألعاب الصداقة",
    "goodwill games": "ألعاب النوايا الحسنة",
    "islamic solidarity games": "ألعاب التضامن الإسلامي",
    "maccabiah games": "الألعاب المكابيه",
    "mediterranean games": "الألعاب المتوسطية",
    "micronesian games": "الألعاب الميكرونيزية",
    "military world games": "دورة الألعاب العسكرية",
    "pan american games": "دورة الألعاب الأمريكية",
    "pan arab games": "دورة الألعاب العربية",
    "pan asian games": "دورة الألعاب الآسيوية",
    "paralympic": "الألعاب البارالمبية",
    "paralympics": "الألعاب البارالمبية",
    "parapan american games": "ألعاب بارابان الأمريكية",
    "sea games": "ألعاب البحر",
    "south american games": "ألعاب أمريكا الجنوبية",
    "south asian beach games": "دورة ألعاب جنوب أسيا الشاطئية",
    "south asian games": "ألعاب جنوب أسيا",
    "south asian winter games": "ألعاب جنوب آسيا الشتوية",
    "southeast asian games": "ألعاب جنوب شرق آسيا",
    "summer olympics": "الألعاب الأولمبية الصيفية",
    "summer universiade": "الألعاب الجامعية الصيفية",
    "summer world university games": "ألعاب الجامعات العالمية الصيفية",
    "the universiade": "الألعاب الجامعية",
    "universiade": "الألعاب الجامعية",
    "winter olympics": "الألعاب الأولمبية الشتوية",
    "winter universiade": "الألعاب الجامعية الشتوية",
    "winter world university games": "ألعاب الجامعات العالمية الشتوية",
    "world championships": "بطولات العالم",
    "youth olympic": "الألعاب الأولمبية الشبابية",
    "youth olympics": "الألعاب الأولمبية الشبابية",
    "youth olympics games": "الألعاب الأولمبية الشبابية"
}


def _find_sport_prefix_match(category_lower: str) -> tuple[str, str]:
    """Find a matching sport prefix in the category.

    Args:
        category_lower: The lowercase category string.

    Returns:
        A tuple of (job_suffix, sport_label) or ("", "") if no match.
    """
    for sport_prefix, sport_label in multi_sport_for_jobs.items():
        prefix_pattern = f"{sport_prefix} ".lower()
        if category_lower.startswith(prefix_pattern):
            job_suffix = category_lower[len(prefix_pattern) :]
            logger.debug(
                f'jobs_in_multi_sports match: prefix="{prefix_pattern}", ' f'label="{sport_label}", job="{job_suffix}"'
            )
            return job_suffix, sport_label
    return "", ""


@functools.lru_cache(maxsize=None)
def jobs_in_multi_sports(category: str) -> str:
    """Retrieve job information related to multiple sports based on the category.

    Processes categories that combine sports events with job roles and
    returns the Arabic translation.

    Args:
        category: The category string representing the sport or job type.

    Returns:
        A formatted string with the job in the context of the sport event.

    Example:
        >>> jobs_in_multi_sports("african games competitors")
        "منافسون في الألعاب الإفريقية"
    """
    logger.debug(f"<<lightyellow>>>> jobs_in_multi_sports >> category:({category})")

    category_clean = category.replace("_", " ")
    category_lower = category_clean.lower()

    data_find_in_it = {
        # medalists
        "people": "أشخاص",
        "olympic medalists": "فائزون بميداليات أولمبية",
        "olympic gold medalists": "فائزون بميداليات ذهبية أولمبية",
        "olympic silver medalists": "فائزون بميداليات فضية أولمبية",
        "olympic bronze medalists": "فائزون بميداليات برونزية أولمبية",
        "winter olympic medalists": "فائزون بميداليات أولمبية شتوية",
        "summer olympic medalists": "فائزون بميداليات أولمبية صيفية",
        # competitors
        "olympic competitors": "منافسون أولمبيون",
        "winter olympic competitors": "منافسون أولمبيون شتويون",
        "summer olympic competitors": "منافسون أولمبيون صيفيون",
    }

    category_lower_fixed = category_lower.replace("olympics", "olympic")
    if category_lower_fixed in data_find_in_it:
        logger.info(f'end jobs_in_multi_sports "{category_lower_fixed}", direct found')
        return data_find_in_it[category_lower_fixed]

    job_suffix, sport_label = _find_sport_prefix_match(category_lower)

    if not job_suffix or not sport_label:
        return ""

    job_label = resolve_jobs_main(job_suffix)

    if not job_label:
        return ""

    result = f"{job_label} في {sport_label}"
    logger.info(f'end jobs_in_multi_sports "{category_clean}", {result=}')
    return result


__all__ = [
    "jobs_in_multi_sports",
]
