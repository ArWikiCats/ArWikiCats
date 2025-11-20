""" """

import functools

from ...helps.log import logger
from ...translations import US_State_lower, kk_end_US_State


@functools.lru_cache(maxsize=None)
def Work_US_State(state_identifier: str) -> str:
    """Return the Arabic label for a U.S. state-related category."""
    normalized_state = state_identifier.lower().strip()
    logger.info(f'<<lightpurple>> > Work_US_State:> len US_State_lower: "{len(US_State_lower)}", SUUS : "{normalized_state}"')
    label = ""
    state_key = ""
    suffix_key = ""

    for suffix in kk_end_US_State:
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
            logger.info(f'>>>><<lightblue>> Work_US_State :"{normalized_state}" (matched suffix variant: "{state_suffix_variant}")')
            break

    if suffix_key and state_key:
        logger.info(f'>>>><<lightblue>> Work_US_State pri:"{suffix_key}"')
        state_label = US_State_lower.get(state_key)

        if state_label:
            logger.info(f'>>>><<lightblue>> State_key :"{state_key}", Statelabel : "{state_label}"')
            resolved_label = kk_end_US_State[suffix_key] % state_label
            logger.info(f'>>>><<lightblue>> SUUS.endswith pri("{suffix_key}"), uuu_lab:"{resolved_label}"')
            label = resolved_label
        else:
            logger.info(f'>>>><<lightblue>> cant find Statelabel for:"{state_key}"')

    label = label.replace("ولاية واشنطن العاصمة", "واشنطن العاصمة")
    label = label.replace(" ولاية ولاية ", " ولاية ")
    return label
