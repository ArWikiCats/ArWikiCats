"""

Usage:
from .bot import event # event(tab, **kwargs)

from . import bot # bot.event(tab, **kwargs)

from . import bot as MA_MAIN # MA_MAIN.event(tab, **kwargs)
"""

from typing import Dict, Any, List
from . import main
from .make2_bots.media_bots import films_bot  # test_films

new_func_lab = main.new_func_lab

def event(tab: Dict[str, Any], return_no_labs: bool = False, **kwargs: Any) -> List[str]:
    return main.event(tab, return_no_labs=return_no_labs, **kwargs)


def test_films(cate: str, reference_category: str = "") -> str:
    return films_bot.test_films(cate, reference_category=reference_category)
