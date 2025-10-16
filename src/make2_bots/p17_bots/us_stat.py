"""
"""

from ...ma_lists import US_State_lower, kk_end_US_State
from ...helps.print_bot import print_put

# ---
Work_US_State_cash = {}


def Work_US_State(SUUS):
    SUUS = SUUS.lower().strip()
    # ---
    if SUUS in Work_US_State_cash:
        return Work_US_State_cash[SUUS]
    # ---
    print_put(f'<<lightpurple>> > Work_US_State:> len US_State_lower: "{len(US_State_lower)}", SUUS : "{SUUS}"')
    lable = ""

    State_key = ""
    pri = ""
    for pri_ff in kk_end_US_State:
        pri_ff_2 = f" state {pri_ff}"
        if not State_key:
            if SUUS.lower().endswith(pri_ff.lower()):
                print_put(f'>>>><<lightblue>> Work_US_State :"{SUUS}"')
                pri = pri_ff
                State_key = SUUS[: -len(pri_ff)]
                break
            elif SUUS.lower().endswith(pri_ff_2.lower()):
                print_put(f'>>>><<lightblue>> Work_US_State :"{SUUS}"')
                pri = pri_ff
                State_key = SUUS[: -len(pri_ff_2)]
                break

    if pri:
        print_put(f'>>>><<lightblue>> Work_US_State pri:"{pri}"')
        Statelabel = US_State_lower.get(State_key, "")
        if State_key and Statelabel == "":
            print_put(f'>>>><<lightblue>> cant find Statelabel for:"{State_key}"')

        if State_key and Statelabel:
            print_put(f'>>>><<lightblue>> State_key :"{State_key}", Statelabel : "{Statelabel}"')

            uuu_lab = kk_end_US_State[pri] % Statelabel
            print_put(f'>>>><<lightblue>> SUUS.endswith pri("{pri}"), uuu_lab:"{uuu_lab}"')
            lable = uuu_lab

    lable = lable.replace("ولاية واشنطن العاصمة", "واشنطن العاصمة")
    lable = lable.replace(" ولاية ولاية ", " ولاية ")
    # ---
    Work_US_State_cash[SUUS] = lable
    # ---
    return lable
