"""Population and people helpers."""

from __future__ import annotations

import re
from typing import Dict

from ...helps.log import logger
from ...helps.print_bot import print_put
from ...ma_lists import People_key, film_key_women_2, nats_to_add
from ..matables_bots.bot import Pp_Priffix
from .utils import build_cache_key, get_or_set, resolve_suffix_template

WORK_PEOPLES_CACHE: Dict[str, str] = {}


def work_peoples(name: str) -> str:
    """Return the label for ``name`` based on the population prefixes table.

    Args:
        name: The category name that may contain a known population suffix.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """

    cache_key = build_cache_key(name)
    if cache_key in WORK_PEOPLES_CACHE:
        return WORK_PEOPLES_CACHE[cache_key]

    def _resolve() -> str:
        print_put(f"<<lightpurple>> work_peoples lookup for '{name}'")

        def _lookup(prefix: str) -> str:
            return People_key.get(prefix, "")

        label = resolve_suffix_template(name, Pp_Priffix, _lookup)
        if label:
            logger.debug("Resolved work_peoples", extra={"name": name, "label": label})
        else:
            logger.debug("Failed to resolve work_peoples", extra={"name": name})
        return label

    return get_or_set(WORK_PEOPLES_CACHE, cache_key, _resolve)


def make_people_lab(value: str) -> str:
    """Return a label for general ``people`` categories.

    Args:
        value: Category type describing a people group.

    Returns:
        The formatted Arabic label or an empty string if the value is not
        recognised.
    """

    normalized_value = value.strip().lower()
    new_label = nats_to_add.get(normalized_value, "")

    if not new_label:
        base_value = re.sub(r"people$", "", normalized_value)
        film_label = film_key_women_2.get(base_value, "")
        if film_label:
            new_label = f"أعلام {film_label}"

    if new_label:
        logger.debug(
            "Resolved make_people_lab",
            extra={"value": normalized_value, "label": new_label},
        )

    return new_label


# Backwards compatibility ----------------------------------------------------------------------
Work_peoples = work_peoples

__all__ = ["work_peoples", "make_people_lab", "Work_peoples"]
