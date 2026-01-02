""""""

from typing import Dict, Any


def sort_by_empty_space(data: Dict[str, Any]) -> dict:
    return dict(
        sorted(
            data.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    )
