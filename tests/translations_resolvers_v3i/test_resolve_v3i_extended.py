#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_diff_text, dump_same_and_not_same
from ArWikiCats.translations_resolvers_v3i.resolve_v3i import resolve_year_job_from_countries
from ArWikiCats import resolve_label_ar

test_0 = {
    "10th-century people from Ifriqiya": "تونسيون في القرن 10",
    "11th-century people from Ifriqiya": "تونسيون في القرن 11",
    "12th-century people from Ifriqiya": "تونسيون في القرن 12",
    "13th-century people from ifriqiya": "تونسيون في القرن 13",
    "14th-century people from Ifriqiya": "تونسيون في القرن 14",
    "15th-century people from Ifriqiya": "تونسيون في القرن 15",
    "9th-century people from Ifriqiya": "تونسيون في القرن 9",
    "21st-century people from Northern Ireland by occupation": "أشخاص من أيرلندا الشمالية حسب المهنة في القرن 21",
    "21st-century people from Georgia (country) by occupation": "أشخاص من جورجيا في القرن 21 حسب المهنة",
    "20th-century people from Northern Ireland by occupation": "أشخاص من أيرلندا الشمالية حسب المهنة في القرن 20",
    "20th-century people from Georgia (country) by occupation": "أشخاص من جورجيا في القرن 20 حسب المهنة",
    "19th-century people from the Ottoman Empire by conflict": "أشخاص من الدولة العثمانية في القرن 19 حسب النزاع",
    "19th-century people from the Russian Empire by occupation": "روس في القرن 19 حسب المهنة",
    "19th-century people from Ottoman Iraq by occupation": "عراقيون في القرن 19 حسب المهنة",
    "19th-century people from Georgia (country) by occupation": "أشخاص من جورجيا في القرن 19 حسب المهنة",
    "18th-century people from the Polish–Lithuanian Commonwealth by occupation": "أشخاص بولنديون في القرن 18 حسب المهنة",
    "18th-century people from the Russian Empire by occupation": "روس في القرن 18 حسب المهنة",

    "18th-century writers from Safavid Iran": "كتاب القرن 18 من إيران الصفوية",
    "18th-century people from Safavid Iran": "أشخاص من الدولة الصفوية القرن 18",
    "17th-century writers from Safavid Iran": "كتاب القرن 17 من إيران الصفوية",
    "17th-century politicians from the Province of New York": "سياسيو ولاية نيويورك القرن 17",
    "17th-century people from Safavid Iran": "أشخاص من الدولة الصفوية القرن 17",
    "16th-century writers from Safavid Iran": "كتاب القرن 16 من إيران الصفوية",
    "16th-century people from Safavid Iran": "أشخاص من الدولة الصفوية القرن 16",
    "14th-century deaths from plague (disease)": "وفيات القرن 14 بسبب الطاعون",

    "11th-century people from the Savoyard State": "أشخاص من منطقة سافوا في القرن 11",
    "16th-century people from the Colony of Santo Domingo": "دومينيكانيون في القرن 16",
    "17th-century people from the Colony of Santo Domingo": "دومينيكانيون في القرن 17",
    "17th-century people from the Province of New York": "أشخاص من ولاية نيويورك في القرن 17",
    "18th-century people from the Savoyard State": "أشخاص من منطقة سافوا في القرن 18",
    "19th-century poets from Ottoman Iraq": "شعراء عراقيون في القرن 19",
}

test_data_1 = {

}

test_data_2 = {
    "19th-century people from Ottoman Arabia": "عرب سعوديون في القرن 19",
    "19th-century poets from Ottoman Arabia": "شعراء سعوديون في القرن 19",
    "11th-century historians from the Abbasid Caliphate": "مؤرخون من الدولة العباسية القرن 11",
    "10th-century historians from the Fatimid Caliphate": "مؤرخون من الدولة الفاطمية القرن 10",
    "15th-century historians from the Ottoman Empire": "مؤرخو الدولة العثمانية القرن 15",
    "16th-century historians from the Ottoman Empire": "مؤرخو الدولة العثمانية القرن 16",
    "17th-century historians from the Ottoman Empire": "مؤرخو الدولة العثمانية القرن 17",
    "18th-century historians from the Ottoman Empire": "مؤرخو الدولة العثمانية القرن 18",
    "19th-century historians from the Ottoman Empire": "مؤرخو الدولة العثمانية القرن 19",
    "18th-century historians from the Russian Empire": "مؤرخون روس في القرن 18",
    "19th-century historians from the Russian Empire": "مؤرخون روس في القرن 19",

    "19th-century illustrators from the Russian Empire": "رسامون توضيحيون روس في القرن 19",
    "10th-century Jews from al-Andalus": "يهود من الأندلس القرن 10",
    "11th-century Jews from al-Andalus": "يهود من الأندلس القرن 11",
    "12th-century Jews from al-Andalus": "يهود من الأندلس القرن 12",
    "9th-century Jews from al-Andalus": "يهود من الأندلس القرن 9",
    "16th-century Jews from the Ottoman Empire": "يهود من الدولة العثمانية القرن 16",
    "17th-century Jews from the Ottoman Empire": "يهود من الدولة العثمانية القرن 17",
    "19th-century Jews from the Russian Empire": "يهود روس في القرن 19",
    "19th-century journalists from the Ottoman Empire": "صحفيون من الدولة العثمانية القرن 19",
    "20th-century journalists from the Ottoman Empire": "صحفيون من الدولة العثمانية القرن 20",
    "19th-century journalists from the Russian Empire": "صحفيون روس في القرن 19",

    "20th-century LGBTQ people from Northern Ireland": "أعلام إل جي بي تي من أيرلندا الشمالية القرن 20",
    "21st-century LGBTQ people from Northern Ireland": "شخصيات مثلية من أيرلندا الشمالية القرن 21",
    "19th-century LGBTQ people from the Russian Empire": "أعلام إل جي بي تي روسية القرن 19",

    "20th-century male actors from Georgia (country)": "ممثلون ذكور في القرن 20 من جورجيا",
    "21st-century male actors from Georgia (country)": "ممثلون ذكور في القرن 21 من جورجيا",
    "20th-century male actors from Northern Ireland": "ممثلون من أيرلندا الشمالية في القرن 20",
    "21st-century male actors from Northern Ireland": "ممثلون من أيرلندا الشمالية في القرن 21",
    "19th-century male actors from the Russian Empire": "ممثلون روس في القرن 19",
    "19th-century male artists from the Russian Empire": "فنانون ذكور روس في القرن 19",
    "19th-century male writers from the Russian Empire": "كتاب ذكور روس في القرن 19",


    "18th-century mathematicians from the Russian Empire": "رياضياتيون روس في القرن 18",
    "19th-century mathematicians from the Russian Empire": "رياضياتيون روس في القرن 19",

    "18th-century military personnel from the Russian Empire": "عسكريون روس في القرن 18",
    "19th-century military personnel from the Russian Empire": "عسكريون روس في القرن 19",

    "18th-century musicians from Bohemia": "موسيقيون بوهيميون في القرن 18",
    "21st-century musicians from Georgia (country)": "موسيقيون في القرن 21 من جورجيا",
    "19th-century musicians from the Russian Empire": "موسيقيون روس في القرن 19",
    "18th-century musicians from the Russian Empire": "موسيقيون من الإمبراطورية الروسية القرن 18",

    "10th-century nobility from the Kingdom of León": "نبلاء في القرن 10 من مملكة ليون",
    "11th-century nobility from the Kingdom of León": "نبلاء في القرن 11 من مملكة ليون",
    "12th-century nobility from the Kingdom of Navarre": "نبلاء في القرن 12 من مملكة نبرة",
    "13th-century nobility from the Kingdom of Navarre": "نبلاء في القرن 13 من مملكة نبرة",
    "14th-century nobility from the Kingdom of Navarre": "نبلاء في القرن 14 من مملكة نبرة",
    "15th-century nobility from the Kingdom of Navarre": "نبلاء في القرن 15 من مملكة نبرة",

    "20th-century non-fiction writers from Northern Ireland": "كتاب غير روائيون من أيرلندا الشمالية في القرن 20",
    "18th-century non-fiction writers from the Russian Empire": "كتاب غير روائيون من الإمبراطورية الروسية في القرن 18",
    "19th-century non-fiction writers from the Russian Empire": "كتاب غير روائيين روس في القرن 19",

    "18th-century novelists from the Russian Empire": "روائيون روس في القرن 18",
    "19th-century novelists from the Russian Empire": "روائيون روس في القرن 19",
    "18th-century painters from Bohemia": "رسامون من بوهيميا القرن 18",
    "20th-century painters from Georgia (country)": "رسامون في القرن 20 من جورجيا",
    "19th-century painters from the Ottoman Empire": "رسامون أتراك في القرن 19",
    "20th-century painters from the Ottoman Empire": "رسامون من الدولة العثمانية القرن 20",
    "18th-century painters from the Russian Empire": "رسامون روس في القرن 18",
    "19th-century painters from the Russian Empire": "رسامون روس في القرن 19",

    "10th-century people from al-Andalus": "أندلسيون في القرن 10",
    "11th-century people from al-Andalus": "أندلسيون في القرن 11",
    "12th-century people from al-Andalus": "أندلسيون في القرن 12",
    "13th-century people from al-Andalus": "أندلسيون في القرن 13",
    "14th-century people from al-Andalus": "أندلسيون في القرن 14",
    "15th-century people from al-Andalus": "أندلسيون في القرن 15",
    "8th-century people from al-Andalus": "أندلسيون في القرن 8",
    "9th-century people from al-Andalus": "أندلسيون في القرن 9",
    "13th-century people from bohemia": "بوهيميون في القرن 13",
    "14th-century people from Bohemia": "بوهيميون في القرن 14",
    "15th-century people from Bohemia": "بوهيميون في القرن 15",
    "16th-century people from Bohemia": "بوهيميون في القرن 16",
    "17th-century people from Bohemia": "بوهيميون في القرن 17",
    "18th-century people from Bohemia": "بوهيميون في القرن 18",
    "14th-century people from Georgia (country)": "أشخاص في القرن 14 من جورجيا",
    "16th-century people from Georgia (country)": "أشخاص في القرن 16 من جورجيا",
    "17th-century people from Georgia (country)": "أشخاص في القرن 17 من جورجيا",
    "18th-century people from Georgia (country)": "أشخاص في القرن 18 من جورجيا",
    "20th-century people from Georgia (country)": "جورجيون في القرن 20",
    "21st-century people from Nevada": "أشخاص من نيفادا القرن 21",
    "21st-century people from New York (state)": "أشخاص من ولاية نيويورك القرن 21",
    "19th-century people from North Dakota": "أشخاص من داكوتا الشمالية القرن 19",
    "21st-century people from North Dakota": "أشخاص من داكوتا الشمالية القرن 21",
    "19th-century people from Ottoman Iraq": "عراقيون في القرن 19",
    "13th-century people from the Abbasid Caliphate": "أشخاص من الدولة العباسية القرن 13",
    "11th-century people from the Abbasid Caliphate": "عراقيون في القرن 11",
    "12th-century people from the Abbasid Caliphate": "عراقيون في القرن 12",
    "10th-century people from the County of Barcelona": "أشخاص في القرن 10 من كونتية برشلونة",
    "11th-century people from the County of Barcelona": "أشخاص في القرن 11 من كونتية برشلونة",
    "12th-century people from the County of Barcelona": "أشخاص في القرن 12 من كونتية برشلونة",
    "9th-century people from the County of Barcelona": "أشخاص في القرن 9 من كونتية برشلونة",
    "10th-century people from the Fatimid Caliphate": "أشخاص من الدولة الفاطمية القرن 10",
    "11th-century people from the Fatimid Caliphate": "أشخاص من الدولة الفاطمية القرن 11",
    "12th-century people from the Fatimid Caliphate": "أشخاص من الدولة الفاطمية القرن 12",
    "11th-century people from the Kingdom of Jerusalem": "أشخاص من مملكة بيت المقدس القرن 11",
    "12th-century people from the Kingdom of Jerusalem": "أشخاص من مملكة بيت المقدس القرن 12",
    "13th-century people from the Kingdom of Jerusalem": "أشخاص من مملكة بيت المقدس القرن 13",
    "10th-century people from the Kingdom of León": "أشخاص في القرن 10 من مملكة ليون",
    "11th-century people from the Kingdom of León": "أشخاص في القرن 11 من مملكة ليون",
    "13th-century people from the kingdom of león": "أشخاص في القرن 13 من مملكة ليون",
    "12th-century people from the Kingdom of Navarre": "أشخاص في القرن 12 من مملكة نبرة",
    "13th-century people from the Kingdom of Navarre": "أشخاص في القرن 13 من مملكة نبرة",
    "14th-century people from the Kingdom of Navarre": "أشخاص في القرن 14 من مملكة نبرة",
    "15th-century people from the Kingdom of Navarre": "أشخاص في القرن 15 من مملكة نبرة",
    "16th-century people from the Kingdom of Navarre": "أشخاص في القرن 16 من مملكة نبرة",
    "10th-century people from the Kingdom of Pamplona": "أشخاص في القرن 10 من مملكة نبرة",
    "11th-century people from the Kingdom of Pamplona": "أشخاص في القرن 11 من مملكة نبرة",
    "9th-century people from the Kingdom of Pamplona": "أشخاص في القرن 9 من مملكة نبرة",
    "13th-century people from the Mamluk Sultanate": "أشخاص من مماليك مصر القرن 13",
    "14th-century people from the Mamluk Sultanate": "أشخاص من مماليك مصر القرن 14",
    "15th-century people from the Mamluk Sultanate": "أشخاص من مماليك مصر القرن 15",
    "16th-century people from the Mamluk Sultanate": "أشخاص من مماليك مصر القرن 16",
    "13th-century people from the Ottoman Empire": "عثمانيون في القرن 13",
    "14th-century people from the Ottoman Empire": "عثمانيون في القرن 14",
    "15th-century people from the Ottoman Empire": "عثمانيون في القرن 15",
    "16th-century people from the Ottoman Empire": "عثمانيون في القرن 16",
    "17th-century people from the Ottoman Empire": "عثمانيون في القرن 17",
    "18th-century people from the Ottoman Empire": "عثمانيون في القرن 18",
    "19th-century people from the Ottoman Empire": "عثمانيون في القرن 19",
    "20th-century people from the Ottoman Empire": "عثمانيون في القرن 20",
    "16th-century people from the Polish–Lithuanian Commonwealth": "أشخاص من الكومنولث البولندي الليتواني القرن 16",
    "13th-century people from the Republic of Florence": "أشخاص من جمهورية فلورنسا القرن 13",
    "14th-century people from the Republic of Florence": "أشخاص من جمهورية فلورنسا القرن 14",
    "15th-century people from the Republic of Florence": "أشخاص من جمهورية فلورنسا القرن 15",
    "16th-century people from the Republic of Florence": "أشخاص من جمهورية فلورنسا القرن 16",
    "16th-century people from the Republic of Geneva": "أشخاص في جنيف القرن 16",
    "17th-century people from the Republic of Geneva": "أشخاص في جنيف القرن 17",
    "18th-century people from the Republic of Geneva": "أشخاص في جنيف القرن 18",
    "20th-century people from the Russian Empire": "أشخاص من الإمبراطورية الروسية القرن 20",
    "8th-century people from the Umayyad Caliphate": "أمويون في القرن 8",
    "7th-century people from the Umayyad Caliphate": "عراقيون في القرن 7",
    "6th-century people from the Visigothic Kingdom": "أشخاص من مملكة القوط القرن 6",
    "7th-century people from the Visigothic Kingdom": "أشخاص من مملكة القوط القرن 7",
    "19th-century people from West Virginia": "أشخاص من فيرجينيا الغربية القرن 19",

}

test_data_holy_roman_empire = {
    "17th-century philosophers from the Holy Roman Empire": "فلاسفة من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century philosophers from the Holy Roman Empire": "فلاسفة من الإمبراطورية الرومانية المقدسة في القرن 18",
    "15th-century physicians from the Holy Roman Empire": "أطباء من الإمبراطورية الرومانية المقدسة في القرن 15",
    "16th-century physicians from the Holy Roman Empire": "أطباء من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century physicians from the Holy Roman Empire": "أطباء من الإمبراطورية الرومانية المقدسة في القرن 17",
    "10th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 10",
    "11th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 11",
    "12th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 12",
    "13th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 13",
    "14th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 14",
    "15th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 15",
    "16th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century people from the Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 18",
    "15th-century painters from the Holy Roman Empire": "رسامون من الإمبراطورية الرومانية المقدسة في القرن 15",
    "16th-century painters from the Holy Roman Empire": "رسامون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century painters from the Holy Roman Empire": "رسامون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century painters from the Holy Roman Empire": "رسامون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "13th-century nobility from the Holy Roman Empire": "نبلاء من الإمبراطورية الرومانية المقدسة في القرن 13",
    "14th-century nobility from the Holy Roman Empire": "نبلاء من الإمبراطورية الرومانية المقدسة في القرن 14",
    "17th-century nobility from the Holy Roman Empire": "نبلاء من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century nobility from the Holy Roman Empire": "نبلاء من الإمبراطورية الرومانية المقدسة في القرن 18",
    "16th-century musicians from the Holy Roman Empire": "موسيقيون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century musicians from the Holy Roman Empire": "موسيقيون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century musicians from the Holy Roman Empire": "موسيقيون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century male actors from the Holy Roman Empire": "ممثلون ذكور من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century male singers from the Holy Roman Empire": "مغنون ذكور من الإمبراطورية الرومانية المقدسة في القرن 18",
    "15th-century mathematicians from the Holy Roman Empire": "رياضياتيون من الإمبراطورية الرومانية المقدسة في القرن 15",
    "16th-century mathematicians from the Holy Roman Empire": "رياضياتيون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century mathematicians from the Holy Roman Empire": "رياضياتيون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century mathematicians from the Holy Roman Empire": "رياضياتيون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "15th-century jurists from the Holy Roman Empire": "حقوقيون من الإمبراطورية الرومانية المقدسة في القرن 15",
    "16th-century jurists from the Holy Roman Empire": "حقوقيون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century jurists from the Holy Roman Empire": "حقوقيون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century jurists from the Holy Roman Empire": "حقوقيون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "16th-century historians from the Holy Roman Empire": "مؤرخون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century historians from the Holy Roman Empire": "مؤرخون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "11th-century historians from the Holy Roman Empire": "مؤرخون من الإمبراطورية الرومانية المقدسة في القرن 11",
    "12th-century historians from the Holy Roman Empire": "مؤرخون من الإمبراطورية الرومانية المقدسة في القرن 12",
    "14th-century historians from the Holy Roman Empire": "مؤرخون من الإمبراطورية الرومانية المقدسة في القرن 14",
    "15th-century historians from the Holy Roman Empire": "مؤرخون من الإمبراطورية الرومانية المقدسة في القرن 15",
    "12th-century poets from the Holy Roman Empire": "شعراء من الإمبراطورية الرومانية المقدسة في القرن 12",
    "13th-century poets from the Holy Roman Empire": "شعراء من الإمبراطورية الرومانية المقدسة في القرن 13",
    "14th-century poets from the Holy Roman Empire": "شعراء من الإمبراطورية الرومانية المقدسة في القرن 14",
    "15th-century poets from the Holy Roman Empire": "شعراء من الإمبراطورية الرومانية المقدسة في القرن 15",
    "16th-century poets from the Holy Roman Empire": "شعراء من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century poets from the Holy Roman Empire": "شعراء من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century poets from the Holy Roman Empire": "شعراء من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century violinists from the Holy Roman Empire": "عازفو كمان من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century women singers from the Holy Roman Empire": "مغنيات من الإمبراطورية الرومانية المقدسة في القرن 18",
    "17th-century singers from the Holy Roman Empire": "مغنون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century singers from the Holy Roman Empire": "مغنون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "13th-century scientists from the Holy Roman Empire": "علماء من الإمبراطورية الرومانية المقدسة في القرن 13",
    "14th-century scientists from the Holy Roman Empire": "علماء من الإمبراطورية الرومانية المقدسة في القرن 14",
    "15th-century scientists from the Holy Roman Empire": "علماء من الإمبراطورية الرومانية المقدسة في القرن 15",
    "16th-century scientists from the Holy Roman Empire": "علماء من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century scientists from the Holy Roman Empire": "علماء من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century scientists from the Holy Roman Empire": "علماء من الإمبراطورية الرومانية المقدسة في القرن 18",
    "16th-century sculptors from the Holy Roman Empire": "نحاتون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "18th-century sculptors from the Holy Roman Empire": "نحاتون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "16th-century scholars from the Holy Roman Empire": "دارسون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century scholars from the Holy Roman Empire": "دارسون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century scholars from the Holy Roman Empire": "دارسون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "17th-century politicians from the Holy Roman Empire": "سياسيون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century politicians from the Holy Roman Empire": "سياسيون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "17th-century publishers (people) from the Holy Roman Empire": "ناشرون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century publishers (people) from the Holy Roman Empire": "ناشرون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "10th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 10",
    "11th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 11",
    "12th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 12",
    "13th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 13",
    "14th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 14",
    "15th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 15",
    "16th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 16",
    "17th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century writers from the Holy Roman Empire": "كتاب من الإمبراطورية الرومانية المقدسة في القرن 18"
}

test_data_3 = {
    "19th-century philosophers from the Russian Empire": "فلاسفة روس في القرن 19",
    "19th-century photographers from the Russian Empire": "مصورون روس في القرن 19",

    "17th-century physicians from Bohemia": "أطباء تشيكيون في القرن 17",
    "15th-century physicians from the Ottoman Empire": "أطباء عثمانيون في القرن 15",
    "16th-century physicians from the Ottoman Empire": "أطباء عثمانيون في القرن 16",
    "18th-century physicians from the Ottoman Empire": "أطباء عثمانيون في القرن 18",
    "19th-century physicians from the Ottoman Empire": "أطباء عثمانيون في القرن 19",
    "20th-century physicians from the Ottoman Empire": "أطباء عثمانيون في القرن 20",
    "17th-century physicians from the Ottoman Empire": "أطباء من الدولة العثمانية القرن 17",
    "18th-century physicians from the Russian Empire": "أطباء روس في القرن 18",
    "19th-century physicians from the Russian Empire": "أطباء روس في القرن 19",

    "19th-century pianists from the Russian Empire": "عازفو بيانو روس في القرن 19",

    "19th-century poets from Georgia (country)": "شعراء جورجيون في القرن 19",
    "14th-century poets from the Ottoman Empire": "شعراء عثمانيون في القرن 14",
    "15th-century poets from the Ottoman Empire": "شعراء عثمانيون في القرن 15",
    "16th-century poets from the Ottoman Empire": "شعراء عثمانيون في القرن 16",
    "17th-century poets from the Ottoman Empire": "شعراء عثمانيون في القرن 17",
    "18th-century poets from the Ottoman Empire": "شعراء عثمانيون في القرن 18",
    "19th-century poets from the Ottoman Empire": "شعراء عثمانيون في القرن 19",
    "20th-century poets from the Ottoman Empire": "شعراء عثمانيون في القرن 20",
    "18th-century poets from the Russian Empire": "شعراء روس في القرن 18",
    "19th-century poets from the Russian Empire": "شعراء روس في القرن 19",

    "21st-century politicians from Georgia (country)": "سياسيون في القرن 21 من جورجيا",
    "18th-century politicians from the Russian Empire": "سياسيون روس في القرن 18",
    "19th-century politicians from the Russian Empire": "سياسيون روس في القرن 19",

    "10th-century princes from Kievan Rus'": "أمراء في خقانات روس القرن 10",
    "11th-century princes from Kievan Rus'": "أمراء في كييف روس القرن 11",
    "12th-century princes from Kievan Rus'": "أمراء في كييف روس القرن 12",
    "13th-century princes from Kievan Rus'": "أمراء في كييف روس القرن 13",

    "15th-century rabbis from the Ottoman Empire": "حاخامات من الدولة العثمانية القرن 15",
    "16th-century rabbis from the Ottoman Empire": "حاخامات من الدولة العثمانية القرن 16",
    "17th-century rabbis from the Ottoman Empire": "حاخامات من الدولة العثمانية القرن 17",
    "18th-century rabbis from the Ottoman Empire": "حاخامات من الدولة العثمانية القرن 18",
    "19th-century rabbis from the Ottoman Empire": "حاخامات من الدولة العثمانية القرن 19",
    "19th-century rabbis from the Russian Empire": "حاخامات من الإمبراطورية الروسية القرن 19",
    "20th-century rabbis from the Russian Empire": "حاخامات من الإمبراطورية الروسية القرن 20",
    "18th-century scholars from the Ottoman Empire": "دارسون من الدولة العثمانية القرن 18",
    "19th-century scholars from the Ottoman Empire": "دارسون من الدولة العثمانية القرن 19",
    "20th-century scholars from the Ottoman Empire": "دارسون من الدولة العثمانية القرن 20",

    "16th-century scientists from the Ottoman Empire": "علماء من الدولة العثمانية القرن 16",
    "17th-century scientists from the Ottoman Empire": "علماء من الدولة العثمانية القرن 17",
    "18th-century scientists from the Ottoman Empire": "علماء من الدولة العثمانية القرن 18",
    "19th-century scientists from the Ottoman Empire": "علماء من الدولة العثمانية القرن 19",
    "20th-century scientists from the Ottoman Empire": "علماء من الدولة العثمانية القرن 20",
    "18th-century scientists from the Russian Empire": "علماء روس في القرن 18",
    "19th-century scientists from the Russian Empire": "علماء روس في القرن 19",

    "18th-century sculptors from the Russian Empire": "نحاتون روس في القرن 18",
    "19th-century sculptors from the Russian Empire": "نحاتون روس في القرن 19",

    "19th-century short story writers from the Russian Empire": "كتاب قصة قصيرة روس في القرن 19",
    "21st-century singers from Georgia (country)": "مغنون في القرن 21 من جورجيا",
    "18th-century singers from the Russian Empire": "مغنون من الإمبراطورية الروسية القرن 18",
    "21st-century sportspeople from Georgia (country)": "رياضيون من جورجيا في القرن 21",
    "20th-century sportspeople from Northern Ireland": "رياضيون من أيرلندا الشمالية في القرن 20",
    "21st-century sportspeople from Northern Ireland": "رياضيون من أيرلندا الشمالية في القرن 21",
    "18th-century translators from the Russian Empire": "مترجمون روس في القرن 18",
    "19th-century translators from the Russian Empire": "مترجمون روس في القرن 19",

    "19th-century women artists from the Russian Empire": "فنانات روسيات في القرن 19",
    "21st-century women musicians from Northern Ireland": "موسيقيات من أيرلندا الشمالية القرن 21",
    "19th-century women scientists from the Russian Empire": "عالمات روسيات في القرن 19",
    "21st-century women singers from Northern Ireland": "مغنيات من أيرلندا الشمالية القرن 21",
    "15th-century women writers from the Ottoman Empire": "كاتبات في الدولة العثمانية القرن 15",
    "16th-century women writers from the Ottoman Empire": "كاتبات في الدولة العثمانية القرن 16",
    "18th-century women writers from the Ottoman Empire": "كاتبات في الدولة العثمانية القرن 18",
    "20th-century women writers from the Ottoman Empire": "كاتبات في الدولة العثمانية القرن 20",
    "19th-century women writers from the Ottoman Empire": "كاتبات من الدولة العثمانية القرن 19",
    "19th-century women writers from the Russian Empire": "كاتبات روسيات في القرن 19",

    "10th-century writers from al-Andalus": "كتاب من الأندلس القرن 10",
    "11th-century writers from al-Andalus": "كتاب من الأندلس القرن 11",
    "12th-century writers from al-Andalus": "كتاب من الأندلس القرن 12",
    "13th-century writers from al-Andalus": "كتاب من الأندلس القرن 13",
    "14th-century writers from Bohemia": "كتاب بوهيميون في القرن 14",
    "15th-century writers from Bohemia": "كتاب بوهيميون في القرن 15",
    "16th-century writers from Bohemia": "كتاب بوهيميون في القرن 16",
    "17th-century writers from Bohemia": "كتاب بوهيميون في القرن 17",
    "18th-century writers from Bohemia": "كتاب بوهيميون في القرن 18",
    "13th-century writers from Georgia (country)": "كتاب من جورجيا القرن 13",
    "19th-century writers from Ottoman Iraq": "كتاب عراقيون في القرن 19",
    "18th-century writers from the Ottoman Empire": "كتاب الدولة العثمانية في القرن 18",
    "20th-century writers from the Ottoman Empire": "كتاب الدولة العثمانية في القرن 20",
    "15th-century writers from the Ottoman Empire": "كتاب عثمانيون في القرن 15",
    "16th-century writers from the Ottoman Empire": "كتاب عثمانيون في القرن 16",
    "17th-century writers from the Ottoman Empire": "كتاب عثمانيون في القرن 17",
    "19th-century writers from the Ottoman Empire": "كتاب عثمانيون في القرن 19",
    "14th-century writers from the Ottoman Empire": "كتاب من الدولة العثمانية القرن 14",
    "18th-century writers from the Republic of Geneva": "كتاب من جمهورية جنيف القرن 18",

    "19th-century zoologists from the Russian Empire": "علماء حيوانات روس في القرن 19",

}


@pytest.mark.parametrize("category,expected", test_data_1.items(), ids=test_data_1.keys())
@pytest.mark.skip2
def test_resolve_v3i_extended_1(category: str, expected: str) -> None:
    """
    Test
    """
    result = resolve_year_job_from_countries(category)
    assert result == expected


@pytest.mark.parametrize("category,expected", test_data_2.items(), ids=test_data_2.keys())
@pytest.mark.skip2
def test_resolve_v3i_extended_2(category: str, expected: str) -> None:
    """
    Test
    """
    result = resolve_year_job_from_countries(category)
    assert result == expected


to_test = [
    # ("test_resolve_v3i_extended_0", test_0),
    ("test_resolve_v3i_extended_1", test_data_1),
    ("test_resolve_v3i_extended_2", test_data_2),
    ("test_resolve_v3i_extended_3", test_data_3),
    ("test_data_holy_roman_empire", test_data_holy_roman_empire),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_year_job_from_countries)

    dump_diff(diff_result, name)
    dump_diff_text(expected, diff_result, name)

    # dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
