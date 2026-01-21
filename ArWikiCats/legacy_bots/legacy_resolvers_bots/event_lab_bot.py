"""EventLab Bot (Legacy Wrapper)"""

from __future__ import annotations

def event_label_work(country: str) -> str:
    from .. import _resolver
    return _resolver._event_label_work(country)

def event_Lab(cate_r: str) -> str:
    from .. import _resolver
    return _resolver._resolve_event_lab(cate_r)
