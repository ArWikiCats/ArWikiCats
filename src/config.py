import os
import sys
from dataclasses import dataclass

argv_lower = [x.lower() for x in sys.argv]


all_params = ["NOKOOORA", "NOWIKIDATA"]


def one_req(name: str) -> bool:
    """Check if the given flag is active via env or command line."""
    all_params.append(name)
    return os.getenv(name.upper(), "false").lower() in ("1", "true", "yes") or name.lower() in argv_lower


@dataclass(frozen=True)
class PrintConfig:
    noprint: bool


@dataclass(frozen=True)
class AppConfig:
    start_yementest: bool
    find_stubs: bool
    makeerr: bool
    load_p17nat: bool
    save_data_path: str


@dataclass(frozen=True)
class Config:
    print: PrintConfig
    app: AppConfig


settings = Config(
    print=PrintConfig(
        noprint=one_req("NOPRINT"),
    ),
    app=AppConfig(
        start_yementest=one_req("YEMENTEST"),
        find_stubs=one_req("-STUBS"),
        makeerr=one_req("MAKEERR"),
        load_p17nat=one_req("LOAD_P17NAT"),
        save_data_path=os.getenv("SAVE_DATA_PATH", ""),
    ),
)
print_settings = settings.print
app_settings = settings.app

__all__ = [
    "settings",
    "print_settings",
    "app_settings",
    "all_params",
]
