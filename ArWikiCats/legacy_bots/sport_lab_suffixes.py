"""
Helpers for resolving sports teams and language categories.

TODO: compare this file with ArWikiCats/new/handle_suffixes.py
"""
from __future__ import annotations
import functools
from ..helps import logger
from ..translations_formats import FormatData
from ..translations import SPORTS_KEYS_FOR_JOBS

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


@functools.lru_cache(maxsize=None)
def resolve_team_jobs_bot(category: str, default: str = "") -> str:
    """Search for a job-related sports label, returning ``default`` when missing."""
    result = resolve_team_suffix(category) or default
    return result


__all__ = [
    "resolve_team_suffix",
    "resolve_team_jobs_bot",
]
