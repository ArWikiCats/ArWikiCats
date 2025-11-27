#!/usr/bin/python3
""" """

from ...translations_resolvers.nats_new import nats_new_create_label
from .sport_lab2 import wrap_team_xo_normal_2025


def get_new_team_xo(team: str) -> str:
    """Resolve team labels with 2026-format templates and fallbacks."""
    team_lab = wrap_team_xo_normal_2025(team)
    if not team_lab:
        team_lab = nats_new_create_label(team)
    return team_lab


__all__ = [
    "get_new_team_xo",
]
