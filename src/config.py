import os
import sys
from dataclasses import dataclass

argv_lower = [x.lower() for x in sys.argv]


all_params = []


def one_req(name: str) -> bool:
    """Check if the given flag is active via env or command line."""
    all_params.append(name)
    return os.getenv(name.upper(), "0") == "1" or name.lower() in argv_lower


@dataclass(frozen=True)
class PrintConfig:
    disable_all_printing: bool
    force_all_printing: bool
    headline_only_preferences: bool
    enable_print_put: bool
    print_memory_usage: bool
    noprint: bool


@dataclass(frozen=True)
class AppConfig:
    enable_wikidata: bool
    enable_kooora: bool
    start_yementest: bool
    find_stubs: bool
    makeerr: bool
    load_p17nat: bool


@dataclass(frozen=True)
class Config:
    print: PrintConfig
    app: AppConfig


noprint_flag = one_req("NOPRINT")

settings = Config(
    print=PrintConfig(
        disable_all_printing=one_req("ALL_PRINT_OFF") or noprint_flag,
        force_all_printing=one_req("PRINTALL"),
        headline_only_preferences=one_req("PRINTHEAD"),
        enable_print_put=one_req("PRINT_PUT"),
        print_memory_usage=one_req("PRINT_MEMORY_USAGE"),
        noprint=noprint_flag,
    ),
    app=AppConfig(
        enable_wikidata=not one_req("NOWIKIDATA"),
        enable_kooora=not one_req("NOKOOORA"),
        start_yementest=one_req("YEMENTEST"),
        find_stubs=one_req("-STUBS"),
        makeerr=one_req("MAKEERR"),
        load_p17nat=one_req("LOAD_P17NAT"),
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
