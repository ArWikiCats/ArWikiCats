"""Population and people helpers."""

from __future__ import annotations

import functools
import re

from ...helps.log import logger
from ...helps.print_bot import print_put
from ...translations import People_key, film_key_women_2, nats_to_add
from ..matables_bots.bot import Pp_Priffix
from .utils import resolve_suffix_template

from pathlib import Path
from ...helps.jsonl_dump import save_data


@save_data(Path(__file__).parent / "work_peoples_old.jsonl", ["name"])
def work_peoples_old(name: str) -> str:
    """Return the label for ``name`` based on the population prefixes table.

    Args:
        name: The category name that may contain a known population suffix.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """

    # ---
    print_put(f"<<lightpurple>> >work_peoples:> len People_key: {len(People_key)} ")
    PpP_lab = ""
    person = ""
    pri = ""
    for pri_ff in Pp_Priffix:
        if not person:
            if name.endswith(pri_ff):
                print_put(f'>>>><<lightblue>> work_peoples :"{name}"')
                pri = pri_ff
                person = name[: -len(pri_ff)]
                break

    personlab = People_key.get(person, "")
    if not personlab:
        print_put(f'>>>><<lightblue>> cant find personlab for:"{person}"')

    if person and personlab:
        print_put(f'>>>><<lightblue>> person :"{person}", personlab : "{personlab}"')
        PpP_lab = Pp_Priffix[pri].format(personlab)
        print_put(f'>>>><<lightblue>> name.endswith pri("{pri}"), PpP_lab:"{PpP_lab}"')
    # ---
    return PpP_lab


@functools.lru_cache(maxsize=None)
@save_data(Path(__file__).parent / "work_peoples.jsonl", ["name"])
def work_peoples(name: str) -> str:
    """Return the label for ``name`` based on the population prefixes table.

    Args:
        name: The category name that may contain a known population suffix.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """

    print_put(f"<<lightpurple>> work_peoples lookup for '{name}'")

    def _lookup(prefix: str) -> str:
        return People_key.get(prefix, "")

    label = resolve_suffix_template(name, Pp_Priffix, _lookup)
    if label:
        logger.debug(f"Resolved work_peoples: name:{name}, label:{label}")
    else:
        logger.debug(f"Failed to resolve work_peoples: name:{name}")
    return label


@save_data(Path(__file__).parent / "make_people_lab.jsonl", ["normalized_value"])
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
        film_label = film_key_women_2.get(base_value, "")
        if film_label:
            new_label = f"أعلام {film_label}"

    if new_label:
        logger.debug(">>>>>>>>>>>>")
        logger.debug(f">> make_people_lab normalized_value: {normalized_value}, new_label: {new_label}")

    return new_label


__all__ = [
    "work_peoples",
    "make_people_lab",
]
