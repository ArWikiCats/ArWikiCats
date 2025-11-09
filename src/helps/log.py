
import logging
from typing import Optional, Union, Any

from ..helps.printe_helper import make_str
from ..config import settings


class LoggerWrap:
    def __init__(self, name: str) -> None:
        self._logger = logging.getLogger(name)

        if settings.print.disable_all_printing or settings.print.noprint:
            self._logger.disabled = True

    def logger(self) -> logging.Logger:
        return self._logger

    def debug(self, msg: str) -> None:
        self._logger.debug(make_str(msg))

    def info(self, msg: str) -> None:
        self._logger.info(make_str(msg))

    def output(self, msg: str, *kwargs: Any) -> None:
        self._logger.info(make_str(msg))

    def warning(self, msg: str) -> None:
        self._logger.warning(make_str(msg))

    def error(self, msg: str) -> None:
        self._logger.error(make_str(msg))

    def error_red(self, msg: str) -> None:
        text = f"<<red>> {str(msg)} <<default>>"
        self._logger.error(make_str(text))

    def critical(self, msg: str) -> None:
        self._logger.critical(make_str(msg))

    def exception(self, msg: str) -> None:
        self._logger.exception(make_str(msg))

    def log(self, level: int, msg: str) -> None:
        self._logger.log(level, make_str(msg))


logger = LoggerWrap(__name__)


def config_logger(level: Optional[Union[int, str]] = None) -> None:
    _levels = [
        'CRITICAL',
        'ERROR',
        'WARNING',
        'INFO',
        'DEBUG',
        'NOTSET',
    ]

    if not level:
        level = logging.DEBUG

    logging.basicConfig(
        level=level,
        # format='%(asctime)s - %(levelname)s - %(message)s',
        format='%(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


__all__ = [
    'logger',
    'config_logger',
]
