"""Utilities for loading localized city label datasets.

This module consolidates Arabic translations for city names from several JSON
sources, applies manual overrides for edge cases, and exposes the resulting
datasets with compatibility aliases matching the legacy API.
"""

from __future__ import annotations

import logging
import sys
from collections.abc import Mapping
from dataclasses import dataclass
from time import perf_counter
from typing import Any, Final, TypeAlias

from ...helps import len_print
from ..utils.json_dir import open_json_file

LOGGER = logging.getLogger(__name__)

CityLabelMap: TypeAlias = dict[str, str]

DEFAULT_TRANSLATION_FILE: Final[str] = "all_cities"
SUPPLEMENTAL_TRANSLATION_FILE: Final[str] = "Cities_tab2"
PATCH_TRANSLATION_FILE: Final[str] = "yy2"

@dataclass(frozen=True)
class CityTranslationDataset:
    """Container for localized city label datasets.

    Attributes:
        translations: Canonical mapping of English city names to their Arabic
            labels.
        patches: Supplemental lowercase mapping used for fallbacks and
            lightweight overrides.
        lowercase_translations: Case-insensitive view of :attr:`translations`.
    """

    translations: CityLabelMap
    patches: CityLabelMap
    lowercase_translations: CityLabelMap

CITY_OVERRIDES: Final[CityLabelMap] = {
    'Tubas': 'طوباس',
    'Tulkarm': 'طولكرم',
    'Nablus': 'نابلس',
    'Zion': 'صهيون',
    "Ya'bad": 'يعبد',
    'Tarqumiyah': 'ترقوميا',
    'Shechem': 'شكيم',
    'Salfit': 'سلفيت',
    "Sa'ir": 'سعير',
    'Rawabi': 'روابي',
    'Ramallah': 'رام الله',
    'Rafah': 'رفح',
    'Qalqilya': 'قلقيلية',
    'Qabatiya': 'قباطية',
    'Melchizedek': 'ملكي صادق',
    'Knesset': 'كنيست',
    'Jerusalem': 'القدس',
    'Jericho': 'أريحا',
    'Jenin': 'جنين',
    'Antioch': 'أنطاكية',
    'Jebusites': 'يبوسيون',
    'Zoharei Chama Synagogue': 'كنيس زوهري شامة',
    'Zion Square': 'ميدان صهيون',
    'Zeev Sternhell': 'زئيف ستيرنهيل',
    'Zaki Nusseibeh': 'زكي نسيبة',
    'Yossi Harel': 'يوسي هاريل',
    'Yossi Cohen': 'يوسي كوهين',
    'Yosef Ba-Gad': 'يوسف با-غاد',
    'Yehuda Liebes': 'يهودا ليبيس',
    'Yehuda Burla': 'يهودا بورلا',
    'Yatta, Hebron': 'يطا',
    'Yahya Hammuda': 'يحيى حمودة',
    'Yad Kennedy': 'ياد كينيدي',
    'World Central Kitchen aid convoy': 'المطبخ المركزي العالمي',
    'West Jerusalem': 'القدس الغربية',
    'Walls of Jerusalem': 'أسوار القدس',
    'Walid Muhammed Sadi': 'وليد محمد السعدي',
    'Uzzi Ornan': 'عوزي أورنان',
    'Umm al-Nasr Mosque': 'مسجد أم النصر',
    'Tsvi Misinai': 'تسفي ميسيناي',
    'Tower of David': 'برج القلعة',
    'Tombs of the Kings': 'قبور السلاطين',
    'The Jerusalem Post': 'جيروزاليم بوست',
    'Temple Mount Faithful': 'أمناء جبل الهيكل',
    'Tell Balata': 'تل بلاطة',
    'Tel Aviv–Jerusalem railway': 'سكة حديد القدس - غانوت',
    'Talitha Kumi School': 'مدرسة طاليثا قومي',
    'Suha Arafat': 'سهى عرفات',
    'Strings of Freedom': 'سلاسل الحرية',
    'Stern House': 'بيت ستيرن',
    'Star Street': 'شارع النجمة',
    'Sirhan Sirhan': 'سرحان سرحان',
    'Shuhada al-Aqsa Hospital': 'مستشفى شهداء الأقصى الحكومي',
    'Shabab Rafah': 'شباب رفح',
    'Schwester Selma': 'سلمى مائير',
    'Sara Hestrin-Lerner': 'سارة هيسترين ليرنر',
    'Samer Tariq Issawi': 'سامر العيساوي',
    'Salwa Abu Libdeh': 'سلوى أبو لبدة',
    'Safra Square': 'ميدان صفرا',
    'Tell el-Ful': 'تل الفول',
    'Royal Palace, Tell el-Ful': 'قصر تل الفول',
    'Roni Alsheikh': 'روني الشيخ',
    'Ribhi Kamal': 'ربحي كمال',
    'Rhetorical school of Gaza': 'المدرسة البلاغية بغزة',
    'Ramat Rachel': 'رمات راحيل',
    'Rafah Elementary Co-Ed B School': 'مدرسة رفح الابتدائية كو-إد بي',
    'Rafah Border Crossing': 'معبر رفح',
    'Palestinian National Theatre': 'مسرح الحكواتي',
    'Palestinian National Library': 'المكتبة الوطنية الفلسطينية',
    'Palestinian Child Arts Center': 'مركز فنون الطفل الفلسطيني',
    'Orient House': 'بيت الشرق',
    'Olive wood carving': 'نحت خشب الزيتون',
    'Off the Wall Comedy Empire': 'ملهى العروض الكوميدية',
    "Nefesh B'Nefesh": 'نيفيش بنيفيش',
    'Nabulsi soap': 'صابون نابلسي',
    'Nabulsi cheese': 'جبن نابلسي',
    'Nablus Sanjak': 'سنجق نابلس',
    'Mujir al-Din': 'مجير الدين الحنبلي',
    'Mubarak Awad': 'مبارك عواد',
    'Mount of Olives': 'جبل الزيتون',
    'Mount Zion': 'جبل صهيون',
    'Mount Scopus': 'جبل المشارف',
    'Moses Montefiore': 'موشيه مونتيفيوري',
    'Mordechai Zaken': 'مردخاي زاكين',
    'Montefiore Windmill': 'طاحونة باب الخليل',
    'Mohammed Yousef El-Najar Hospital': 'مستشفى الشهيد أبو يوسف النجار الحكومي',
    'Mohammad Zuhdi Nashashibi': 'محمد زهدي النشاشيبي',
    "Modi'in Illit": 'موديعين عيليت',
    'Miriam Eshkol': 'مريام أشكول',
    "Mevo'ot Yeriho": 'ميفوت يريحو',
    'Menahem Yaari': 'مناحيم ياري',
    'Melkite Catholic Patriarchate': 'بطريركية الروم الملكيين الكاثوليك',
    'Marie-Alphonsine Danil Ghattas': 'ماري ألفونسين',
    'Manger Square': 'ساحة المهد',
    'Mandelbaum Gate': 'بوابة ماندلباوم',
    'Mamilla Pool': 'بركة مأمن الله',
    'Mamilla Mall': 'مول مأمن الله',
    'Malha Mall': 'مول المالحة',
    'Mahmoud al-Zahar': 'محمود الزهار',
    "Ma'ale Adumim": 'معاليه أدوميم',
    'Lina Abu Akleh': 'لينا أبو عاقلة',
    'Lily Serna': 'ليلي سيرنا',
    'Lara Khaldi': 'لارا الخالدي',
    'Kohelet Policy Forum': 'منتدى كوهيليت للسياسات',
    'Knesset Yisrael': 'كنيست يسرائيل',
    'Knesset Menorah': 'شمعدان الكنيست',
    'Kiryat Menachem Begin': 'كريات مناحيم بيغن',
    'Kiryat HaLeom': 'كريات هالوم',
    'Kidron Valley': 'وادي النار',
    'Khan Yunis': 'خان يونس',
    'Kenny Young': 'كيني يونغ',
    'Kamal Boullata': 'كمال بلاطة',
    'Kamal Adwan Hospital siege': 'حصار مستشفى كمال عدوان',
    "Joseph's Tomb": 'قبر يوسف',
    'Jonathan Apphus': 'يوناثان المكابي',
    'Jewish Agency for Israel': 'الوكالة اليهودية',
    'Jessica Cohen': 'جيسيكا كوهن',
    'Jerusalem syndrome': 'متلازمة القدس',
    'Jerusalem stone': 'حجر القدس',
    'Jerusalem mixed grill': 'مشاوي القدس المشكلة',
    'Latin Patriarchate of Jerusalem': 'بطريركية القدس للاتين',
    'Jerusalem Technology Park': 'حديقة القدس للتكنولوجيا',
    'Jerusalem Old Town Hall': 'مبنى بلدية القدس التاريخي',
    'Jerusalem Municipality': 'بلدية القدس',
    'Jerusalem Light Rail': 'قطار القدس الخفيف',
    'Jerusalem International YMCA': 'جمعية الشبان المسيحيين – القدس',
    'Jerusalem International Airport': 'مطار القدس الدولي',
    'Jerusalem Foundation': 'مؤسسة القدس',
    'Jerusalem Forest': 'غابة القدس',
    'Jerusalem Film Festival': 'مهرجان القدس السينمائي',
    'Jerusalem District': 'منطقة القدس',
    'Jerusalem Development Authority': 'هيئة تنمية القدس',
    'Jerusalem 24': 'القدس 24',
    'Jaffa–Jerusalem railway': 'خط سكك حديد يافا-القدس',
    'Jabal Al-Mukaber Club': 'نادي جبل المكبر',
    'Issaf Nashashibi Center for Culture and Literature': 'مكتبة دار إسعاف النشاشيبي',
    'Issa Kassissieh': 'عيسى قسيسية',
    'Issa Bandak': 'عيسى البندك',
    'Israeli Public Broadcasting Corporation': 'شركة البث العام الإسرائيلية',
    'Israel Postal Company': 'شركة البريد الإسرائيلي',
    'Israel Democracy Institute': 'المعهد الإسرائيلي للديمقراطية',
    'Israel Antiquities Authority': 'هيئة آثار إسرائيل',
    'Israel Academy of Sciences and Humanities': 'أكاديمية إسرائيل للعلوم والإنسانيات',
    'International Convention Center': 'مباني الأمة',
    'Institute for Zionist Strategies': 'معهد الإستراتيجيات الصهيونية',
    'Indonesia Hospital': 'المستشفى الإندونيسي',
    'Illés Relief': 'نموذج القدس لشتيفان إيلش',
    'Ibtisam Barakat': 'ابتسام بركات',
    'Ibrahim al-Maqadma Mosque missile strike': 'مجزرة مسجد إبراهيم المقادمة',
    'Huda Abuarquob': 'هدى أبو عرقوب',
    'Hitteen SC': 'نادي حطين',
    'Hilal Al-Quds Club': 'هلال القدس',
    'Henry Cattan': 'هنري قطان',
    'Hebron glass': 'زجاج الخليل',
    'Haseki Sultan Imaret': 'تكية خاصكي سلطان',
    'Har HaMenuchot': 'مقبرة هار همنوحوت',
    'Hanna Batatu': 'حنا بطاطو',
    'Haim Koren': 'حاييم كورين',
    'Gihon Spring': 'عين سلوان',
    'Generali Building': 'مبنى جنرالي',
    'mass graves': 'مقابر جماعية',
    'Gaza Sky Geeks': 'غزة سكاي جيكس',
    'Gaza City': 'غزة',
    'Gad Horowitz': 'غاد هوروويتز',
    'Fatima Bernawi': 'فاطمة برناوي',
    'Emi Palmor': 'إيمي بالمور',
    'Ein Lavan': 'عين لافان',
    'East Jerusalem': 'القدس الشرقية',
    'Dura, Hebron': 'دورا',
    'Dimitri Baramki': 'ديمتري برامكي',
    'Deir al-Balah': 'دير البلح',
    'Deir al-Balah Camp': 'مخيم دير البلح',
    'Damascus Gate': 'باب العامود',
    'Cremisan Valley': 'وادي كريمزان',
    "Cotton Merchants' Gate": 'باب القطانين',
    'Clal Center': 'مركز كلال',
    'Chords Bridge': 'جسر القدس الصاري المعلق',
    'Charles Warren': 'تشارلز وارن',
    'Burj al Luq Luq Community Centre and Society': 'جمعية مركز برج اللقلق المجتمعية',
    'Bethlehem Association': 'منظمة بيت لحم',
    'Benny Morris': 'بيني موريس',
    'Beitar Jerusalem F.C.': 'بيتار القدس',
    'Beitar Illit': 'بيتار عيليت',
    'Beit Yonatan': 'بيت يوناتان',
    'Beit Sahour': 'بيت ساحور',
    'Beit Lahia': 'بيت لاهيا',
    'Beit Jala': 'بيت جالا',
    'Beit Jala Lions': 'ليونز بيت جالا',
    'Beit Hanoun': 'بيت حانون',
    'Beit HaNassi': 'بيت هاناسى',
    'Beit Aghion': 'بيت أغيون',
    'Bani Suheila': 'بني سهيلا',
    "Bani Na'im": 'بني نعيم',
    "Arson attack at Joseph's Tomb": 'قبر يوسف',
    'Arab Orthodox Society': 'جمعية حاملات الطيب الأرثوذكسية',
    'Anat Berko': 'عنات بيركو',
    'An-Najah National University': 'جامعة النجاح الوطنية',
    'Amnon Ben-Tor': 'أمنون بن تور',
    'Amin al-Husseini': 'أمين الحسيني',
    'All Nations Café': 'مقهى كل الأمم',
    'Albert Aghazarian': 'ألبرت أغازريان',
    'Al-Shati refugee camp': 'مخيم الشاطئ',
    'Al-Quds University': 'جامعة القدس',
    'Al-Nimr Palace': 'قصر النمر',
    'Al-Najah Secondary School': 'مدرسة النجاح الثانوية',
    'Al-Mashrabiya Building': 'بيت المشربية',
    'Al-Manara Square': 'ميدان المنارة',
    'Al-Aqsa University': 'جامعة الأقصى',
    'Ahli Qalqilyah': 'أهلي قلقيلية',
    'Agron House': 'بيت أغرون',
    'Abu Dis': 'أبو ديس',
    'Abu Daoud': 'محمد داود عودة',
    'Abd al-Qadir al-Husayni': 'عبد القادر الحسيني',
    'Abasan al-Kabira': 'عبسان الكبيرة',
    'Janzouri': 'جنزوري',
    'Jabalia': 'جباليا',
    'Idna': 'إذنا',
    'Hebron': 'الخليل',
    'Hanunu': 'هانونو',
    'Halhul': 'حلحول',
    'Gethsemane': 'جثسيماني',
    'Caphar': 'كفر',
    'Bethlehem': 'بيت لحم',
    'Bethany': 'بيت عبرة',
    'Beitunia': 'بيتونيا',
    'Az-Zawayda': 'الزوايدة',
    'As-Samu': 'السموع',
    "Ar-Rifa'iyya": 'الرفاعية',
    'Al-Yamun': 'اليامون',
    'Al-Ram': 'الرام',
    'Al-Mawazin': 'بائكة',
    'Al-Masyoun': 'الماصيون',
    'Al-Bireh': 'البيرة',
    'Ad-Dhahiriya': 'الظاهرية',
    'Ad-Deirat': 'الديرات'
}

def _ensure_label_map(map_name: str, data: Any) -> CityLabelMap:
    """Return a sanitized mapping of string keys to string values."""

    if not isinstance(data, Mapping):
        if data:
            LOGGER.warning(
                "Expected mapping for %s but received %s", map_name, type(data).__name__
            )
        return {}
    sanitized: CityLabelMap = {}
    for raw_key, raw_value in data.items():
        if isinstance(raw_key, str) and isinstance(raw_value, str):
            sanitized[raw_key] = raw_value
        else:
            LOGGER.debug(
                "Skipping invalid entry in %s: %r -> %r", map_name, raw_key, raw_value
            )
    return sanitized

def _load_json_labels(file_name: str) -> CityLabelMap:
    """Load and sanitize a translation map from a JSON file."""

    raw_data = open_json_file(file_name)
    return _ensure_label_map(file_name, raw_data)

def _create_lowercase_map(translations: Mapping[str, str]) -> CityLabelMap:
    """Create a lowercase-keyed version of *translations* for case-insensitive lookups."""

    return {key.lower(): value for key, value in translations.items()}

def _calculate_memory_usage(dataset: CityTranslationDataset) -> dict[str, int]:
    """Return the approximate memory usage for each dataset component."""

    return {
        "CITY_TRANSLATIONS": sys.getsizeof(dataset.translations),
        "CITY_LABEL_PATCHES": sys.getsizeof(dataset.patches),
        "CITY_TRANSLATIONS_LOWER": sys.getsizeof(dataset.lowercase_translations),
    }

def _log_dataset_statistics(dataset: CityTranslationDataset, duration: float) -> None:
    """Emit debug information about the loaded datasets."""

    LOGGER.info(
        "Loaded %d city translations and %d patches in %.3f seconds",
        len(dataset.translations),
        len(dataset.patches),
        duration,
    )
    memory_usage = _calculate_memory_usage(dataset)
    len_print.lenth_pri("Cities.py", memory_usage, Max=100)

def build_city_translation_dataset(
    *,
    base_file: str = DEFAULT_TRANSLATION_FILE,
    supplement_file: str = SUPPLEMENTAL_TRANSLATION_FILE,
    patch_file: str = PATCH_TRANSLATION_FILE,
) -> CityTranslationDataset:
    """Load, merge, and normalize the city translation datasets.

    Args:
        base_file: Name of the JSON file containing the primary translation
            dataset.
        supplement_file: Name of the supplemental JSON file whose entries are
            merged into the primary dataset.
        patch_file: Name of the JSON file containing lowercase patch entries
            used for fallback lookups.

    Returns:
        A :class:`CityTranslationDataset` instance containing the normalized
        translations, lowercase mappings, and patch datasets.
    """

    start_time = perf_counter()
    base_translations = _load_json_labels(base_file)
    supplemental_translations = _load_json_labels(supplement_file)
    translations: CityLabelMap = {**base_translations, **supplemental_translations}
    translations.update(CITY_OVERRIDES)  # Ensure manual overrides win over JSON data.
    patches = _load_json_labels(patch_file)
    lowercase_translations = _create_lowercase_map(translations)
    dataset = CityTranslationDataset(
        translations=translations,
        patches=patches,
        lowercase_translations=lowercase_translations,
    )
    duration = perf_counter() - start_time
    _log_dataset_statistics(dataset, duration)
    return dataset

_CITY_DATASET = build_city_translation_dataset()

CITY_TRANSLATIONS: CityLabelMap = _CITY_DATASET.translations
CITY_LABEL_PATCHES: CityLabelMap = _CITY_DATASET.patches
CITY_TRANSLATIONS_LOWER: CityLabelMap = _CITY_DATASET.lowercase_translations

N_cit_ies_s = CITY_TRANSLATIONS
tabe_lab_yy2 = CITY_LABEL_PATCHES
N_cit_ies_s_lower = CITY_TRANSLATIONS_LOWER

__all__ = [
    "CityTranslationDataset",
    "CITY_TRANSLATIONS",
    "CITY_LABEL_PATCHES",
    "CITY_TRANSLATIONS_LOWER",
    "N_cit_ies_s",
    "N_cit_ies_s_lower",
    "build_city_translation_dataset",
    "tabe_lab_yy2",
]
