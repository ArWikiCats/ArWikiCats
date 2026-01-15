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
    noprint_formats: bool
    noprint: bool


@dataclass(frozen=True)
class AppConfig:
    start_tgc_resolver_first: bool
    find_stubs: bool
    makeerr: bool
    save_data_path: str


@dataclass(frozen=True)
class Config:
    print: PrintConfig
    app: AppConfig


settings = Config(
    print=PrintConfig(
        noprint=one_req("NOPRINT"),
        noprint_formats=one_req("NOPRINT_FORMATS"),
    ),
    app=AppConfig(
        start_tgc_resolver_first=one_req("TGC_RESOLVER_FIRST"),
        find_stubs=one_req("-STUBS"),
        makeerr=one_req("MAKEERR"),
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
