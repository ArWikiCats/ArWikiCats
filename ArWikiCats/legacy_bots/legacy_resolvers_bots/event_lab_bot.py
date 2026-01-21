"""EventLab Bot (Legacy Wrapper)"""

from __future__ import annotations
from .. import _resolver


def event_label_work(country: str) -> str:

    return _resolver._event_label_work(country)


def event_Lab(cate_r: str) -> str:

    return _resolver._resolve_event_lab(cate_r)
