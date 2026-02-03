"""
Population and people helpers.
"""

from __future__ import annotations

import functools
import logging

from ..translations import People_key
from ..translations_formats import FormatData

logger = logging.getLogger(__name__)

formatted_data = {
    # Category:Relationships_of_Jeffrey_Epstein
    "relationships of {person_key}": "علاقات {person_label}",
    "{person_key} administration cabinet members": "أعضاء مجلس وزراء إدارة {person_label}",
    "{person_key} administration personnel": "موظفو إدارة {person_label}",
    "{person_key} executive office": "مكتب {person_label} التنفيذي",
    "{person_key} memorials": "نصب {person_label} التذكارية",
    "{person_key} cabinet": "مجلس وزراء {person_label}",
    "{person_key} albums": "ألبومات {person_label}",

    "{person_key} animation albums": "ألبومات رسوم متحركة {person_label}",
    "{person_key} comedy albums": "ألبومات كوميدية {person_label}",
    "{person_key} compilation albums": "ألبومات تجميعية {person_label}",
    "{person_key} concept albums": "ألبومات مفاهيمية {person_label}",
    "{person_key} eps albums": "ألبومات أسطوانة مطولة {person_label}",
    "{person_key} folk albums": "ألبومات فولك {person_label}",
    "{person_key} folktronica albums": "ألبومات فولكترونيكا {person_label}",
    "{person_key} jazz albums": "ألبومات جاز {person_label}",
    "{person_key} live albums": "ألبومات مباشرة {person_label}",
    "{person_key} mixtape albums": "ألبومات ميكستايب {person_label}",
    "{person_key} remix albums": "ألبومات ريمكس {person_label}",
    "{person_key} surprise albums": "ألبومات مفاجئة {person_label}",
    "{person_key} video albums": "ألبومات فيديو {person_label}",
}


def _load_bot() -> FormatData:
    _peoples_bot = FormatData(
        formatted_data=formatted_data,
        data_list=People_key,
        key_placeholder="{person_key}",
        value_placeholder="{person_label}",
    )

    return _peoples_bot


@functools.lru_cache(maxsize=2048)
def work_peoples(name: str) -> str:
    """
    Return the label for ``name`` using FormatData.
    """
    logger.debug(f"<<yellow>> {name=}")

    if label := People_key.get(name):
        logger.info(f"<<yellow>> end direct hit {name=}, {label=}")
        return label

    _peoples_bot = _load_bot()

    resolved_label = _peoples_bot.search(name)

    logger.info(f"<<yellow>> end {name=}, {resolved_label=}")
    return resolved_label


__all__ = [
    "work_peoples",
]
