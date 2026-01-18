"""
Population and people helpers.
"""

from __future__ import annotations

import functools
import re

from ...helps import dump_data, logger
from ...translations import People_key
from ...translations_formats import FormatData

labelSuffixMappings = {
    "administration cabinet members": "أعضاء مجلس وزراء إدارة {ar}",
    "administration personnel": "موظفو إدارة {ar}",
    "animation albums": "ألبومات رسوم متحركة {ar}",
    "comedy albums": "ألبومات كوميدية {ar}",
    "compilation albums": "ألبومات تجميعية {ar}",
    "concept albums": "ألبومات مفاهيمية {ar}",
    "eps albums": "ألبومات أسطوانة مطولة {ar}",
    "executive office": "مكتب {ar} التنفيذي",
    "folk albums": "ألبومات فولك {ar}",
    "folktronica albums": "ألبومات فولكترونيكا {ar}",
    "jazz albums": "ألبومات جاز {ar}",
    "live albums": "ألبومات مباشرة {ar}",
    "mixtape albums": "ألبومات ميكستايب {ar}",
    "remix albums": "ألبومات ريمكس {ar}",
    "surprise albums": "ألبومات مفاجئة {ar}",
    "video albums": "ألبومات فيديو {ar}",
    "memorials": "نصب {ar} التذكارية",
    "cabinet": "مجلس وزراء {ar}",
    "albums": "ألبومات {ar}",
}

labelSuffixMappings = dict(
    sorted(
        labelSuffixMappings.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)


@functools.lru_cache(maxsize=None)
def work_peoples(name: str) -> str:
    """Return the label for ``name`` based on the population prefixes table.

    Args:
        name: The category name that may contain a known population suffix.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """
    logger.info(f"<<lightpurple>> >work_peoples:> len People_key: {len(People_key)} ")
    person_key = ""
    prefix_type = ""
    prefix_type_label = ""

    for name_end_suffix in labelSuffixMappings:
        if name.endswith(name_end_suffix.strip()):
            logger.info(f'>>>><<lightblue>> work_peoples :"{name}"')
            prefix_type = name_end_suffix.strip()
            prefix_type_label = labelSuffixMappings[prefix_type]
            person_key = name[: -len(name_end_suffix)].strip()
            break

    if not person_key:
        logger.info(f'>>>><<lightblue>> cant find person_key for:"{name}", prefix_type:"{prefix_type}"')
        return ""

    if not prefix_type:
        logger.info(f'>>>><<lightblue>> cant find prefix_type for:"{name}", person_key:"{person_key}"')
        return ""

    personlab = People_key.get(person_key, "")

    if not personlab:
        logger.info(f'>>>><<lightblue>> cant find personlab for:"{person_key}"')
        return ""

    logger.info(f">>>><<lightblue>> {person_key=}, {personlab=}")
    resolved_label = prefix_type_label.format(ar=personlab)
    logger.info(f'>>>><<lightblue>> name.endswith pri("{prefix_type}"), {resolved_label=}')

    return resolved_label


def work_peoples_formatdata_baesed(name: str) -> str:
    """
    Return the label for ``name`` using FormatData.
    """
    formatted_data = {f"{{person_key}} {k}": v.replace("{ar}", "{person_label}") for k, v in labelSuffixMappings.items()}
    bot = FormatData(
        formatted_data=formatted_data,
        data_list=People_key,
        key_placeholder="{person_key}",
        value_placeholder="{person_label}",
    )
    return bot.search(name)


__all__ = [
    "work_peoples",
    "work_peoples_formatdata_baesed",
]
