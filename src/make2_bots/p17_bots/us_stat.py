"""
"""

import functools
from ...translations import US_State_lower, kk_end_US_State
from ...helps.print_bot import print_put

from pathlib import Path
from ...helps.jsonl_dump import save_data

# @functools.lru_cache(maxsize=None)


@save_data(Path(__file__).parent / "Work_US_State.jsonl", ["state_identifier"])
def Work_US_State(state_identifier: str) -> str:
    normalized_state = state_identifier.lower().strip()
    # ---
    print_put(
        f'<<lightpurple>> > Work_US_State:> len US_State_lower: "{len(US_State_lower)}", '
        f'SUUS : "{normalized_state}"'
    )
    label = ""

    state_key = ""
    suffix_key = ""
    for suffix in kk_end_US_State:
        state_suffix_variant = f" state {suffix}"
        if not state_key:
            if normalized_state.endswith(suffix.lower()):
                print_put(f'>>>><<lightblue>> Work_US_State :"{normalized_state}"')
                suffix_key = suffix
                state_key = normalized_state[: -len(suffix)]
                break
            if normalized_state.endswith(state_suffix_variant.lower()):
                print_put(f'>>>><<lightblue>> Work_US_State :"{normalized_state}"')
                suffix_key = suffix
                state_key = normalized_state[: -len(state_suffix_variant)]
                break

    if suffix_key:
        print_put(f'>>>><<lightblue>> Work_US_State pri:"{suffix_key}"')
        state_label = US_State_lower.get(state_key, "")
        if state_key and state_label == "":
            print_put(f'>>>><<lightblue>> cant find Statelabel for:"{state_key}"')

        if state_key and state_label:
            print_put(f'>>>><<lightblue>> State_key :"{state_key}", Statelabel : "{state_label}"')

            resolved_label = kk_end_US_State[suffix_key] % state_label
            print_put(
                f'>>>><<lightblue>> SUUS.endswith pri("{suffix_key}"), uuu_lab:"{resolved_label}"'
            )
            label = resolved_label

    label = label.replace("ولاية واشنطن العاصمة", "واشنطن العاصمة")
    label = label.replace(" ولاية ولاية ", " ولاية ")
    # ---
    return label
