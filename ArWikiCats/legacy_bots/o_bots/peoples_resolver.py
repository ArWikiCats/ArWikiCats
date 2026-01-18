"""Population and people helpers."""

from __future__ import annotations

import functools
import re

from ...helps import logger
from ...translations import TELEVISION_BASE_KEYS_FEMALE, People_key, nats_to_add


albumTypePrefixes = {
    " administration cabinet members": "أعضاء مجلس وزراء إدارة {}",
    " administration personnel": "موظفو إدارة {}",
    " albums": "ألبومات {}",
    " cabinet": "مجلس وزراء {}",
    " executive office": "مكتب {} التنفيذي",
    " memorials": "نصب {} التذكارية",
    " video albums": "ألبومات فيديو {}",
    "animation albums": "ألبومات رسوم متحركة {}",
    "comedy albums": "ألبومات كوميدية {}",
    "compilation albums": "ألبومات تجميعية {}",
    "concept albums": "ألبومات مفاهيمية {}",
    "eps albums": "ألبومات أسطوانة مطولة {}",
    "folk albums": "ألبومات فولك {}",
    "folktronica albums": "ألبومات فولكترونيكا {}",
    "jazz albums": "ألبومات جاز {}",
    "live albums": "ألبومات مباشرة {}",
    "mixtape albums": "ألبومات ميكستايب {}",
    "remix albums": "ألبومات ريمكس {}",
    "surprise albums": "ألبومات مفاجئة {}",
    "video albums": "ألبومات فيديو {}"
}


@functools.lru_cache(maxsize=None)
def work_peoples(name: str) -> str:
    """Return the label for ``name`` based on the population prefixes table.

    Args:
        name: The category name that may contain a known population suffix.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """
    logger.info(f"<<lightpurple>> >work_peoples:> len People_key: {len(People_key)} ")
    PpP_lab = ""
    person = ""
    pri = ""
    for pri_ff in albumTypePrefixes:
        if not person:
            if name.endswith(pri_ff):
                logger.info(f'>>>><<lightblue>> work_peoples :"{name}"')
                pri = pri_ff
                person = name[: -len(pri_ff)]
                break

    personlab = People_key.get(person, "")
    if not personlab:
        logger.info(f'>>>><<lightblue>> cant find personlab for:"{person}"')

    if person and personlab:
        logger.info(f">>>><<lightblue>> {person=}, {personlab=}")
        PpP_lab = albumTypePrefixes[pri].format(personlab)
        logger.info(f'>>>><<lightblue>> name.endswith pri("{pri}"), {PpP_lab=}')
    return PpP_lab


def make_people_lab(normalized_value: str) -> str:
    """Return a label for general ``people`` categories.

    Args:
        value: Category type describing a people group.

    Returns:
        The formatted Arabic label or an empty string if the value is not
        recognised.
    """

    normalized_value = normalized_value.strip()

    new_label = nats_to_add.get(normalized_value, "")

    if not new_label:
        base_value = re.sub(r"people$", "", normalized_value)
        film_label = TELEVISION_BASE_KEYS_FEMALE.get(base_value, "")
        if film_label:
            new_label = f"أعلام {film_label}"

    if new_label:
        logger.debug(">>>>>>>>>>>>")
        logger.debug(f">> make_people_lab {normalized_value=}, {new_label=}")

    return new_label


__all__ = [
    "work_peoples",
    "make_people_lab",
]
