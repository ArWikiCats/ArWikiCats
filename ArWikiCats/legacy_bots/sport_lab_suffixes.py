"""
Helpers for resolving sports teams and language categories.

TODO: compare this file with ArWikiCats/new/handle_suffixes.py
"""
from __future__ import annotations
import functools
from ..helps import logger
from ..translations import SPORTS_KEYS_FOR_JOBS
from ..translations_formats import FormatData

Teams_new_end_keys = {
    "broadcasters": "مذيعو {}",
    "commentators": "معلقو {}",
    "commissioners": "مفوضو {}",
    "trainers": "مدربو {}",
    "chairmen and investors": "رؤساء ومسيرو {}",
    "coaches": "مدربو {}",
    "managers": "مدربو {}",
    "manager": "مدربو {}",
    "manager history": "تاريخ مدربو {}",
    "footballers": "لاعبو {}",
    "playerss": "لاعبو {}",
    "players": "لاعبو {}",
    "fan clubs": "أندية معجبي {}",
    "owners and executives": "رؤساء تنفيذيون وملاك {}",
    "personnel": "أفراد {}",
    "owners": "ملاك {}",
    "executives": "مدراء {}",
    "equipment": "معدات {}",
    "culture": "ثقافة {}",
    "logos": "شعارات {}",
    "tactics and skills": "مهارات {}",
    "media": "إعلام {}",
    "people": "أعلام {}",
    "terminology": "مصطلحات {}",
    "variants": "أشكال {}",
    "governing bodies": "هيئات تنظيم {}",
    "bodies": "هيئات {}",
    "video games": "ألعاب فيديو {}",
    "comics": "قصص مصورة {}",
    "cups": "كؤوس {}",
    "records and statistics": "سجلات وإحصائيات {}",
    "leagues": "دوريات {}",
    "leagues seasons": "مواسم دوريات {}",
    "seasons": "مواسم {}",
    "competition": "منافسات {}",
    "competitions": "منافسات {}",
    "world competitions": "منافسات {} عالمية",
    "teams": "فرق {}",
    "television series": "مسلسلات تلفزيونية {}",
    "films": "أفلام {}",
    "championships": "بطولات {}",
    "music": "موسيقى {}",
    "clubs and teams": "أندية وفرق {}",
    "clubs": "أندية {}",
    "referees": "حكام {}",
    "organizations": "منظمات {}",
    "non-profit organizations": "منظمات غير ربحية {}",
    "non-profit publishers": "ناشرون غير ربحيون {}",
    "stadiums": "ملاعب {}",
    "lists": "قوائم {}",
    "awards": "جوائز {}",
    "songs": "أغاني {}",
    "non-playing staff": "طاقم {} غير اللاعبين",
    "umpires": "حكام {}",
    "cup playoffs": "تصفيات كأس {}",
    "cup": "كأس {}",
    "results": "نتائج {}",
    "matches": "مباريات {}",
    "rivalries": "دربيات {}",
    "champions": "أبطال {}",
}

Teams_new_end_keys = dict(sorted(
    Teams_new_end_keys.items(),
    key=lambda k: (-k[0].count(" "), -len(k[0])),
))


def match_suffix_template(name: str, suffixes: dict[str, str]):
    """
    Find the first suffix template that matches ``name``.

    input: 'football governing bodies'
    output: prefix='football governing' -> template='هيئات {}'
    """

    stripped = name.strip()
    for suffix, template in suffixes.items():
        candidates = [suffix]
        if not suffix.startswith(" "):
            candidates.append(f" {suffix}")

        for candidate in candidates:
            if stripped.endswith(candidate):
                prefix = stripped[: -len(candidate)].strip()
                logger.debug(f"match_suffix_template: {name=} -> {candidate=} -> {prefix=}")
                return prefix, template
    return None


def resolve_team_suffix(normalized_team: str) -> str:
    """Resolve team suffix for sports categories.

    Args:
        normalized_team (str): The normalized team name.

    Returns:
        str: The resolved team suffix.
    """

    match = match_suffix_template(normalized_team, Teams_new_end_keys)
    if not match:
        return ""

    prefix, template = match

    lookup_value = SPORTS_KEYS_FOR_JOBS.get(prefix, "")
    logger.debug(f"resolve_suffix_template: {prefix=} -> {lookup_value=}")

    if not lookup_value:
        return ""

    result = template.format(lookup_value)
    logger.debug(f"resolve_suffix_template: {result=}")

    return result


def _load_bot() -> FormatData:
    jobs_formatted_data = {
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
        "{en_sport} cup playoffs": "تصفيات كأس {sport_jobs}",
        "{en_sport} cup": "كأس {sport_jobs}",
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
def resolve_team_jobs_bot(category: str, default: str = "") -> str:
    """Search for a job-related sports label, returning ``default`` when missing."""
    jobs_bot = _load_bot()
    result = jobs_bot.search(category) or default
    logger.info_if_or_debug(f"<<yellow>> end resolve_team_jobs_bot: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_team_suffix",
    "resolve_team_jobs_bot",
]
