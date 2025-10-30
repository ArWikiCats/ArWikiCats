
import requests

from ...helps.log import logger

session = requests.Session()
session.headers.update({
    "User-Agent": "WikiMedBot/1.0 (https://meta.wikimedia.org/wiki/User:Mr.Ibrahem; mailto:example@example.org)"
})


def open_url_json(url, params={}, timeout=5):

    try:
        response = session.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        logger.error("open_url_json :", e)

    return {}


def open_url_text(url, timeout=5):
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()
        data = response.text
        return data
    except Exception as e:
        logger.error("open_url_text :", e)

    return ""
