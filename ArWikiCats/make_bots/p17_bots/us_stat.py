"""
TODO: replaced by ArWikiCats/translations_resolvers/us_counties_new.py
"""

import functools

from ...helps.log import logger
from ...translations import US_STATE_NAMES_LOWER, STATE_SUFFIX_TEMPLATES


def normalize_state(ar_name: str) -> str:
    if "ولاية ولاية" in ar_name:
        ar_name = ar_name.replace("ولاية ولاية", "ولاية")

    if "ولاية واشنطن العاصمة" in ar_name:
        ar_name = ar_name.replace("ولاية واشنطن العاصمة", "واشنطن العاصمة")

    return ar_name


@functools.lru_cache(maxsize=None)
def Work_US_State(state_identifier: str) -> str:
    """Return the Arabic label for a U.S. state-related category."""
    normalized_state = state_identifier.lower().strip()
    logger.info(
        f'<<lightpurple>> > Work_US_State:> len US_STATE_NAMES_LOWER: "{len(US_STATE_NAMES_LOWER)}", SUUS : "{normalized_state}"'
    )
    label = ""
    state_key = ""
    suffix_key = ""

    keys_sorted = sorted(STATE_SUFFIX_TEMPLATES.keys(), key=lambda x: -x.count(" "))

    for suffix in keys_sorted:
        lower_suffix = suffix.lower()
        state_suffix_variant = f" state {lower_suffix}"

        if normalized_state.endswith(lower_suffix):
            suffix_key = suffix
            state_key = normalized_state[: -len(lower_suffix)]
            logger.info(f'>>>><<lightblue>> Work_US_State :"{normalized_state}" (matched suffix: "{lower_suffix}")')
            break
        elif normalized_state.endswith(state_suffix_variant):
            suffix_key = suffix
            state_key = normalized_state[: -len(state_suffix_variant)]
            logger.info(
                f'>>>><<lightblue>> Work_US_State :"{normalized_state}" (matched suffix variant: "{state_suffix_variant}")'
            )
            break

    if suffix_key and state_key:
        logger.info(f'>>>><<lightblue>> Work_US_State pri:"{suffix_key}"')
        state_label = US_STATE_NAMES_LOWER.get(state_key)

        if state_label:
            logger.info(f'>>>><<lightblue>> State_key :"{state_key}", Statelabel : "{state_label}"')
            resolved_label = STATE_SUFFIX_TEMPLATES[suffix_key] % state_label
            logger.info(f'>>>><<lightblue>> SUUS.endswith pri("{suffix_key}"), uuu_lab:"{resolved_label}"')
            label = resolved_label
        else:
            logger.info(f'>>>><<lightblue>> cant find Statelabel for:"{state_key}"')

    label = normalize_state(label)

    return label
