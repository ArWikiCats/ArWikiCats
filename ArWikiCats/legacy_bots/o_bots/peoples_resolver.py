"""Population and people helpers."""

from __future__ import annotations

import functools
import re

from ...helps import logger
from ...translations import TELEVISION_BASE_KEYS_FEMALE, People_key

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
    """
    Resolve an Arabic label for a category name by matching its suffix against known population-related templates.
    
    Parameters:
        name (str): Category name that may end with a known population suffix.
    
    Returns:
        str: The resolved Arabic label if a mapping is found, otherwise an empty string.
    """
    logger.info(f"<<lightpurple>> >work_peoples:> len People_key: {len(People_key)} ")
    person_key = ""
    prefix_type = ""

    for name_end_suffix in labelSuffixMappings:
        if name.endswith(name_end_suffix.strip()):
            logger.info(f'>>>><<lightblue>> work_peoples :"{name}"')
            prefix_type = name_end_suffix.strip()
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
    resolved_label = labelSuffixMappings[prefix_type].format(ar=personlab)
    logger.info(f'>>>><<lightblue>> name.endswith pri("{prefix_type}"), {resolved_label=}')

    return resolved_label


def make_people_lab(normalized_value: str) -> str:
    """
    Return an Arabic label for a general "people" category.
    
    Parameters:
        normalized_value (str): Category name (whitespace-trimmed) that may end with the word "people".
    
    Returns:
        The formatted Arabic label (e.g., "أعلام <label>") if a mapping for the base category exists, otherwise an empty string.
    """

    normalized_value = normalized_value.strip()

    new_label = ""

    base_value = re.sub(r"people$", "", normalized_value)
    film_label = TELEVISION_BASE_KEYS_FEMALE.get(base_value, "")

    if film_label:
        new_label = f"أعلام {film_label}"

    logger.info_if_or_debug(f">> make_people_lab {normalized_value=}, {new_label=}", new_label)

    return new_label


__all__ = [
    "work_peoples",
    "make_people_lab",
]