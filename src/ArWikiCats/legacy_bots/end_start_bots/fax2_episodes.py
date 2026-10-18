"""
!
"""

from typing import Tuple


def get_episodes(category3: str, category3_nolower: str = "") -> Tuple[str, str]:
    """
    examples:
    Category:2016 American television episodes
    Category:Game of Thrones (season 1) episodes
    Category:Game of Thrones season 1 episodes
    """

    list_of_cat = ""

    if not category3_nolower:
        category3_nolower = category3

    category3_nolower = category3_nolower.strip()
    category3 = category3.strip()
    # Generate episode patterns for seasons 1–10
    for i in range(1, 11):
        label = f"حلقات {{}} الموسم {i}"

        # Generate both key patterns
        patterns = [
            f" (season {i}) episodes",
            f" season {i} episodes",
        ]

        for key in patterns:
            # Use lower() once for comparison
            if category3.lower().endswith(key.lower()):
                list_of_cat = label
                category3 = category3_nolower[: -len(key)].strip()
                return list_of_cat, category3

    list_of_cat = "حلقات {}"
    if category3.lower().endswith("episodes"):
        category3 = category3_nolower[: -len("episodes")].strip()

    return list_of_cat, category3
