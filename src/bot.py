"""

Usage:
from .bot import event # event(tab, **kwargs)

from . import bot # bot.event(tab, **kwargs)

from . import bot as MA_MAIN # MA_MAIN.event(tab, **kwargs)
"""

from typing import Any, Dict, List

from . import main
from .event_processing import event_result
from .event_processing import new_func_lab as _new_func_lab
from .make2_bots.media_bots import films_bot  # te_films

new_func_lab = _new_func_lab


def event(tab: Dict[str, Any], return_no_labs: bool = False, **kwargs: Any) -> List[str]:
    """Delegate event processing to the main module with optional extras."""
    return main.event(tab, return_no_labs=return_no_labs, **kwargs)


def te_films(cate: str, reference_category: str = "") -> str:
    """Resolve film category labels via the media bot helper."""
    return films_bot.te_films(cate)
