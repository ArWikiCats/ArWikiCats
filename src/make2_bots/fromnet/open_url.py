
import importlib.util
from typing import Any, Mapping

if importlib.util.find_spec("requests") is not None:
    import requests  # type: ignore
    session = requests.Session()
else:

    class _OfflineSession:
        def __init__(self) -> None:
            self.headers = {}

        def get(self, *args: Any, **kwargs: Any) -> None:
            raise RuntimeError("requests library is unavailable")

    session = _OfflineSession()

from ...helps.log import logger

session.headers.update({
    "User-Agent": "WikiMedBot/1.0 (https://meta.wikimedia.org/wiki/User:Mr.Ibrahem; mailto:example@example.org)"
})


def open_url_json(
    url: str,
    params: Mapping[str, Any] | None=None,
    timeout: int=5,
) -> dict[str, Any] | list[Any]:
    try:
        request_params = params or {}
        response = session.get(url, params=request_params, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        logger.error(f"open_url_json : {e}")

    return {}


def open_url_text(url: str, timeout: int=5) -> str:
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.error(f"open_url_text : {e}")

    return ""
