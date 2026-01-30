#!/usr/bin/python3
"""
Sports team and club category processing.
"""

import functools

import logging
from ..translations import INTER_FEDS_LOWER, Clubs_key_2, clubs_teams_leagues
from ..translations_formats import FormatData

logger = logging.getLogger(__name__)

Teams_new_end_keys = {
    "{team_key} broadcasters": "مذيعو {team_label}",
    "{team_key} commentators": "معلقو {team_label}",
    "{team_key} commissioners": "مفوضو {team_label}",
    "{team_key} trainers": "مدربو {team_label}",
    "{team_key} chairmen and investors": "رؤساء ومسيرو {team_label}",
    "{team_key} coaches": "مدربو {team_label}",
    "{team_key} managers": "مدربو {team_label}",  # "مدراء {team_label}"
    "{team_key} manager": "مدربو {team_label}",
    "{team_key} manager history": "تاريخ مدربو {team_label}",
    "{team_key} footballers": "لاعبو {team_label}",
    "{team_key} playerss": "لاعبو {team_label}",
    "{team_key} players": "لاعبو {team_label}",
    "{team_key} fan clubs": "أندية معجبي {team_label}",
    "{team_key} owners and executives": "رؤساء تنفيذيون وملاك {team_label}",
    "{team_key} personnel": "أفراد {team_label}",
    "{team_key} owners": "ملاك {team_label}",
    "{team_key} executives": "مدراء {team_label}",
    "{team_key} equipment": "معدات {team_label}",
    "{team_key} culture": "ثقافة {team_label}",
    "{team_key} logos": "شعارات {team_label}",
    "{team_key} tactics and skills": "مهارات {team_label}",
    "{team_key} media": "إعلام {team_label}",
    "{team_key} people": "أعلام {team_label}",
    "{team_key} terminology": "مصطلحات {team_label}",
    # "{team_key} religious occupations": "مهن دينية {team_label}",
    # "{team_key} occupations": "مهن {team_label}",
    "{team_key} variants": "أشكال {team_label}",
    "{team_key} governing bodies": "هيئات تنظيم {team_label}",
    "{team_key} bodies": "هيئات {team_label}",
    "{team_key} video games": "ألعاب فيديو {team_label}",
    "{team_key} comics": "قصص مصورة {team_label}",
    "{team_key} cups": "كؤوس {team_label}",
    "{team_key} records and statistics": "سجلات وإحصائيات {team_label}",
    "{team_key} leagues": "دوريات {team_label}",
    "{team_key} leagues seasons": "مواسم دوريات {team_label}",
    "{team_key} seasons": "مواسم {team_label}",
    "{team_key} competition": "منافسات {team_label}",
    "{team_key} competitions": "منافسات {team_label}",
    "{team_key} world competitions": "منافسات {team_label} عالمية",
    "{team_key} teams": "فرق {team_label}",
    "{team_key} television series": "مسلسلات تلفزيونية {team_label}",
    "{team_key} films": "أفلام {team_label}",
    "{team_key} championships": "بطولات {team_label}",
    "{team_key} music": "موسيقى {team_label}",
    "{team_key} clubs and teams": "أندية وفرق {team_label}",
    "{team_key} clubs": "أندية {team_label}",
    "{team_key} referees": "حكام {team_label}",
    "{team_key} organizations": "منظمات {team_label}",
    "{team_key} non-profit organizations": "منظمات غير ربحية {team_label}",
    "{team_key} non-profit publishers": "ناشرون غير ربحيون {team_label}",
    "{team_key} stadiums": "ملاعب {team_label}",
    "{team_key} lists": "قوائم {team_label}",
    "{team_key} awards": "جوائز {team_label}",
    "{team_key} songs": "أغاني {team_label}",
    "{team_key} non-playing staff": "طاقم {team_label} غير اللاعبين",
    "{team_key} umpires": "حكام {team_label}",
    "{team_key} cup playoffs": "تصفيات كأس {team_label}",
    "{team_key} cup": "كأس {team_label}",
    "{team_key} results": "نتائج {team_label}",
    "{team_key} matches": "مباريات {team_label}",
    "{team_key} rivalries": "دربيات {team_label}",
    "{team_key} champions": "أبطال {team_label}",
}


def _load_bot() -> FormatData:
    data_list = Clubs_key_2 | clubs_teams_leagues | INTER_FEDS_LOWER
    _peoples_bot = FormatData(
        formatted_data=Teams_new_end_keys,
        data_list=data_list,
        key_placeholder="{team_key}",
        value_placeholder="{team_label}",
    )

    return _peoples_bot


@functools.lru_cache(maxsize=2048)
def resolve_clubs_teams_leagues(name: str) -> str:
    logger.debug(f"<<yellow>> resolve_clubs_teams_leagues {name=}")

    _peoples_bot = _load_bot()

    resolved_label = _peoples_bot.search(name)

    logger.info(f"<<yellow>> end: {name=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "resolve_clubs_teams_leagues",
]
