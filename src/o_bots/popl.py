"""

from ..bots.popl import Work_peoples, make_people_lab

"""

import re
from ..ma_lists_bots import film_key_women_2
from ..ma_lists_bots import nats_to_add
from ..helps.print_bot import print_put
from ..matables_bots.bot import Pp_Priffix
from ..ma_lists_bots import People_key

# ---
Work_peoples_cash = {}


def Work_peoples(SUUS):
    # ---
    cash_key = SUUS.lower().strip()
    # ---
    if cash_key in Work_peoples_cash:
        return Work_peoples_cash[cash_key]
    # ---
    print_put(f"<<lightpurple>> >Work_peoples:> len People_key: {len(People_key)} ")
    PpP_lab = ""
    person = ""
    pri = ""
    for pri_ff in Pp_Priffix:
        if not person:
            if SUUS.endswith(pri_ff):
                print_put(f'>>>><<lightblue>> Work_peoples :"{SUUS}"')
                pri = pri_ff
                person = SUUS[: -len(pri_ff)]
                break

    personlab = People_key.get(person, "")
    if not personlab:
        print_put(f'>>>><<lightblue>> cant find personlab for:"{person}"')

    if person and personlab:
        print_put(f'>>>><<lightblue>> person :"{person}", personlab : "{personlab}"')
        PpP_lab = Pp_Priffix[pri].format(personlab)
        print_put(f'>>>><<lightblue>> SUUS.endswith pri("{pri}"), PpP_lab:"{PpP_lab}"')
    # ---
    Work_peoples_cash[cash_key] = PpP_lab
    # ---
    return PpP_lab


def make_people_lab(type_lower):
    type_lower = type_lower.strip()

    newlab = nats_to_add.get(type_lower, "")

    if not newlab:
        ty2 = re.sub(r"people$", "", type_lower)

        lab2 = film_key_women_2.get(ty2, "")

        if lab2:
            newlab = f"أعلام {lab2}"

    if newlab:
        print(">>>>>>>>>>>>")
        print(">>>>>>>>>>>>")
        print(">>>>>>>>>>>>")
        print(">>>>>>>>>>>>")
        print(">>>>>>>>>>>>")
        print(">>>>>>>>>>>>")
        print(">>>>>>>>>>>>")
        print(f">> make_people_lab type_lower: {type_lower}, newlab: {newlab}")

    return newlab
