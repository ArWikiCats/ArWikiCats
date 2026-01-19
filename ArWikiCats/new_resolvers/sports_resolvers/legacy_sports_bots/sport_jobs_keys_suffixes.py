"""
Helpers for resolving sports teams and language categories.

TODO: compare this file with ArWikiCats/new/handle_suffixes.py
"""
from __future__ import annotations
import functools
from ....helps import logger
from ....translations import SPORTS_KEYS_FOR_JOBS
from ....translations_formats import FormatData


def _load_bot() -> FormatData:
    jobs_formatted_data = {
        "{en_sport} cup playoffs": "تصفيات كأس {sport_jobs}",
        "{en_sport} cup": "كأس {sport_jobs}",

        "{en_sport} broadcasters": "مذيعو {sport_jobs}",
        "{en_sport} commentators": "معلقو {sport_jobs}",
        "{en_sport} commissioners": "مفوضو {sport_jobs}",
        "{en_sport} trainers": "مدربو {sport_jobs}",
        "{en_sport} chairmen and investors": "رؤساء ومسيرو {sport_jobs}",
        "{en_sport} coaches": "مدربو {sport_jobs}",
        "{en_sport} managers": "مدربو {sport_jobs}",
        "{en_sport} manager": "مدربو {sport_jobs}",
        "{en_sport} manager history": "تاريخ مدربو {sport_jobs}",
        "{en_sport} footballers": "لاعبو {sport_jobs}",
        "{en_sport} playerss": "لاعبو {sport_jobs}",
        "{en_sport} players": "لاعبو {sport_jobs}",
        "{en_sport} fan clubs": "أندية معجبي {sport_jobs}",
        "{en_sport} owners and executives": "رؤساء تنفيذيون وملاك {sport_jobs}",
        "{en_sport} personnel": "أفراد {sport_jobs}",
        "{en_sport} owners": "ملاك {sport_jobs}",
        "{en_sport} executives": "مدراء {sport_jobs}",
        "{en_sport} equipment": "معدات {sport_jobs}",
        "{en_sport} culture": "ثقافة {sport_jobs}",
        "{en_sport} logos": "شعارات {sport_jobs}",
        "{en_sport} tactics and skills": "مهارات {sport_jobs}",
        "{en_sport} media": "إعلام {sport_jobs}",
        "{en_sport} people": "أعلام {sport_jobs}",
        "{en_sport} terminology": "مصطلحات {sport_jobs}",
        "{en_sport} variants": "أشكال {sport_jobs}",
        "{en_sport} governing bodies": "هيئات تنظيم {sport_jobs}",
        "{en_sport} bodies": "هيئات {sport_jobs}",
        "{en_sport} video games": "ألعاب فيديو {sport_jobs}",
        "{en_sport} comics": "قصص مصورة {sport_jobs}",
        "{en_sport} cups": "كؤوس {sport_jobs}",
        "{en_sport} records and statistics": "سجلات وإحصائيات {sport_jobs}",
        "{en_sport} leagues": "دوريات {sport_jobs}",
        "{en_sport} leagues seasons": "مواسم دوريات {sport_jobs}",
        "{en_sport} seasons": "مواسم {sport_jobs}",
        "{en_sport} competition": "منافسات {sport_jobs}",
        "{en_sport} competitions": "منافسات {sport_jobs}",
        "{en_sport} world competitions": "منافسات {sport_jobs} عالمية",
        "{en_sport} teams": "فرق {sport_jobs}",
        "{en_sport} television series": "مسلسلات تلفزيونية {sport_jobs}",
        "{en_sport} films": "أفلام {sport_jobs}",
        "{en_sport} championships": "بطولات {sport_jobs}",
        "{en_sport} music": "موسيقى {sport_jobs}",
        "{en_sport} clubs and teams": "أندية وفرق {sport_jobs}",
        "{en_sport} clubs": "أندية {sport_jobs}",
        "{en_sport} referees": "حكام {sport_jobs}",
        "{en_sport} organizations": "منظمات {sport_jobs}",
        "{en_sport} non-profit organizations": "منظمات غير ربحية {sport_jobs}",
        "{en_sport} non-profit publishers": "ناشرون غير ربحيون {sport_jobs}",
        "{en_sport} stadiums": "ملاعب {sport_jobs}",
        "{en_sport} lists": "قوائم {sport_jobs}",
        "{en_sport} awards": "جوائز {sport_jobs}",
        "{en_sport} songs": "أغاني {sport_jobs}",
        "{en_sport} non-playing staff": "طاقم {sport_jobs} غير اللاعبين",
        "{en_sport} umpires": "حكام {sport_jobs}",
        "{en_sport} results": "نتائج {sport_jobs}",
        "{en_sport} matches": "مباريات {sport_jobs}",
        "{en_sport} rivalries": "دربيات {sport_jobs}",
        "{en_sport} champions": "أبطال {sport_jobs}",
    }
    return FormatData(
        formatted_data=jobs_formatted_data,
        data_list=SPORTS_KEYS_FOR_JOBS,
        key_placeholder="{en_sport}",
        value_placeholder="{sport_jobs}",
    )


@functools.lru_cache(maxsize=None)
def resolve_sport_jobs_keys_and_suffix(category: str, default: str = "") -> str:
    """Search for a job-related sports label, returning ``default`` when missing."""
    jobs_bot = _load_bot()
    result = jobs_bot.search(category) or default
    logger.info_if_or_debug(f"<<yellow>> end resolve_sport_jobs_keys_and_suffix: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_sport_jobs_keys_and_suffix",
]
