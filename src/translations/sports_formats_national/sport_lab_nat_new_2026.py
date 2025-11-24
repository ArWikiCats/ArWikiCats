#!/usr/bin/python3
"""

"""

import functools
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from .te2 import New_For_nat_female_xo_team

from ...translations import Nat_women
from ...translations_formats.format_2_data import FormatMultiData

New_For_nat_female_xo_team_2 = {
    "{nat} xzxz": "xzxz {nat}",  # Category:American_basketball
    "{nat} xzxz championships": "بطولات xzxz {nat}",
    "{nat} national xzxz championships": "بطولات xzxz وطنية {nat}",
    "{nat} national xzxz champions": "أبطال بطولات xzxz وطنية {nat}",
    "{nat} amateur xzxz cup": "كأس {nat} xzxz للهواة",
    "{nat} youth xzxz cup": "كأس {nat} xzxz للشباب",
    "{nat} men's xzxz cup": "كأس {nat} xzxz للرجال",
    "{nat} women's xzxz cup": "كأس {nat} xzxz للسيدات",
    "{nat} xzxz super leagues": "دوريات سوبر xzxz {nat}",
}

New_For_nat_female_xo_team_2.update({
    f"{{nat}} {x}" : v for x, v in New_For_nat_female_xo_team.items()
})

# remove "the " from the start of all Nat_women_2 keys
Nat_women_2 = {k[4:] if k.startswith("the ") else k: v for k, v in Nat_women.items()}

both_bot = FormatMultiData(
    New_For_nat_female_xo_team_2,
    Nat_women_2,
    key_placeholder="{nat}",
    value_placeholder="{nat}",
    data_list2=SPORTS_KEYS_FOR_JOBS,
    key2_placeholder="xzxz",
    value2_placeholder="xzxz",
    text_after=" people",
    text_before="the ",
)


@functools.lru_cache(maxsize=None)
def sport_lab_nat_load_new(category):
    return both_bot.create_label(category)


__all__ = [
    "sport_lab_nat_load_new",
]
