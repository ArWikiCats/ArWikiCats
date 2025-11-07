#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module provides Arabic translations for various job titles and roles.

It includes translations for religious groups, sports player roles, NATO job titles,
and more. The translations are organized into dictionaries with English keys
and Arabic values.

This module is intended to be used as a single source of truth for job-related
translations throughout the application.
"""
from typing import Dict

# ---
ARABIC_TRANSLATIONS: Dict[str, str] = {}
# ---
RELIGIOUS_GROUPS: Dict[str, str] = {
    "Shiites": "شيعة",
    "Jews": "يهود",
    "Christians": "مسيحيون",
    "Sunnis": "سنة",
    "Druze": "دروز",
    "Muslims": "مسلمون",
    "Yazidis": "أيزيديون",
}
# ---
SPORTS_PLAYER_ROLES: Dict[str, str] = {
    "goalkeepers": "حراس مرمى",
    "defenders": "مدافعون",
    "midfielders": "لاعبو وسط",
    "forwards": "مهاجمون",
    "players": "لاعبون",
}
# ---
NATO_JOB_TITLES: Dict[str, str] = {
    "nato commanders": "قادة الناتو",
    "nato generals": "جنرالات الناتو",
    "nato officials": "مسؤولو الناتو",
}
# ---
DISABILITY_RELATED_JOBS: Dict[str, str] = {
    "deaf": "أصم",
    "blind": "أعمى",
}
# ---
EXECUTIVE_ROLES: Dict[str, str] = {
    "vice presidents": "نواب رؤساء",
    "vice presidents of": "نواب رئيس",
    "acting presidents": "رؤساء بالإنابة",
    "honorary presidents": "رؤساء فخريون",
    "presidents": "رؤساء",
}
# ---
NATIONALITY_FIRST_JOBS: Dict[str, str] = {
    "prime ministers": "رؤساء وزراء",
    "prime minister": "رئيس وزراء",
    "politicians": "سياسيون",
    "judges": "قضاة",
    "lawyers": "محامون",
    "mayors": "رؤساء بلديات",
    "governors": "ولاة",
    "chancellors": "مستشارون",
}
# ---
ARABIC_TRANSLATIONS.update(RELIGIOUS_GROUPS)
ARABIC_TRANSLATIONS.update(SPORTS_PLAYER_ROLES)
ARABIC_TRANSLATIONS.update(NATO_JOB_TITLES)
ARABIC_TRANSLATIONS.update(DISABILITY_RELATED_JOBS)
ARABIC_TRANSLATIONS.update(EXECUTIVE_ROLES)
ARABIC_TRANSLATIONS.update(NATIONALITY_FIRST_JOBS)
