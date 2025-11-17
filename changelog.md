
## [#68](https://github.com/MrIbrahem/make2_new/pull/68) - 2025-11-17

* **Refactor**
  * Reorganized internal module structure for better code maintainability and clarity.
  * Consolidated category labeling logic into streamlined components.
  * Simplified API signatures to improve consistency across bot modules.
  * Improved logging infrastructure for better system monitoring.

* **Bug Fixes**
  * Removed erroneous internal imports that could cause module initialization issues.

## [#65](https://github.com/MrIbrahem/make2_new/pull/65) - 2025-11-16

* **Refactor [Nationality.py](src/translations/nats/Nationality.py)**
  * Reorganized labeling engine and moved label construction into a focused start-with-year/type workflow; simplified mapping usage and renamed a public category mapping for clarity.
  * Overhauled nationality data and normalization to improve country/name lookups and translations.

* **Bug Fixes**
  * Fixed month+year/BC regex in time-to-Arabic conversion.

* **Tests**
  * Updated, added, and relocated tests to cover the new labeling flow and time parsing; removed obsolete test harnesses.

## [#64](https://github.com/MrIbrahem/make2_new/pull/64) - 2025-11-16

* **New Features**
  * Added modular event labeling with improved country and type processing
  * New time-matching utility for first-match retrieval
  * Added century labeling variant support

* **Bug Fixes**
  * Updated regex patterns for consistent dash character handling
  * Improved category normalization logic

* **Refactors [bot_lab.py](src/make2_bots/ma_bots/year_or_typeo/bot_lab.py)**
  * Refactored event labeling into modular helper functions
  * Simplified category normalization
  * Replaced legacy parsing functions with efficient aliases

* **Tests**
  * Added unit tests for event labeling with century-focused coverage
  * Expanded pattern matching test coverage
  * Added slow test markers for performance-intensive tests

## [#62](https://github.com/MrIbrahem/make2_new/pull/62) - 2025-11-15

* **Refactor**
  * Modernized internal caching mechanisms across the application to use Python's built-in caching utilities instead of manual implementations, improving code maintainability and performance consistency.

* **Tests**
  * Added skeleton test files across multiple modules to establish testing infrastructure and improve code coverage foundation.

## [#59](https://github.com/MrIbrahem/make2_new/pull/59) - 2025-11-14
* **Refactor [Sport_key.py](src/translations/sports/Sport_key.py)**
  * Restructured sport key data handling into a modular pipeline with validation and alias expansion for improved maintainability.
  * Standardized constant naming conventions across the codebase for consistency.

* **New Features**
  * Added template rendering utilities for generating sport labels with year-based and formatted variants.

* **Bug Fixes**
  * Removed deprecated method from sports formatting module.
  * Updated test fixtures to reflect current data requirements.

* **Tests**
  * Removed obsolete test file for normalization logic.
  * Updated test coverage to align with refactored APIs and new data structure.

## [#58](https://github.com/MrIbrahem/make2_new/pull/58) - 2025-11-14
* Refactor [fixtitle.py](src/fix/fixtitle.py)
* **New Features**
  * Added comprehensive Arabic text normalization with improved handling of formulas, prepositions, time expressions, and category-specific replacements.

* **Performance Improvements**
  * Implemented function-level caching across multiple modules to enhance response times.

* **API Updates**
  * Standardized naming convention for exported constants to uppercase format for consistency.

## [#54](https://github.com/MrIbrahem/make2_new/pull/54) - 2025-11-13
* **Refactor [all_keys2.py](src/translations/mixed/all_keys2.py)**
  * Restructured internal data mapping generation for improved maintainability and scalability of data definitions.

* **New Features**
  * Expanded available data mappings to include international federations, educational institutions, maritime vessels, religious traditions, and political categories.

* **Chores**
  * Updated naming conventions for consistency across the public API.

## [#53](https://github.com/MrIbrahem/make2_new/pull/53) - 2025-11-13

* **Bug Fixes**
  * Corrected Arabic translations for sports categories, publications, and cultural topics.
  * Improved consistency of multilingual mappings across datasets.

* **Tests**
  * Added comprehensive test coverage for wheelchair sports categories and classifications.
  * Expanded validation for cultural and ethnic category translations.
  * Implemented regression tests for Arabic label accuracy.

* **Chores**
  * Refactored internal data structure organization for improved maintainability.
  * Standardized naming conventions across core mappings.

## [#50](https://github.com/MrIbrahem/make2_new/pull/50) - 2025-11-12

* **Refactor [Jobs.py](src/translations/jobs/Jobs.py)**
  * Updated job data API naming conventions and restructured internal data assembly pipeline for improved maintainability and consistency.
  * Enhanced data normalization for automatic sorting and deduplication of lists and dictionaries.

## [#47](https://github.com/MrIbrahem/make2_new/pull/47) - 2025-11-11

* **New Features**
  * Added support for wheelchair racers and expanded wheelchair sport coverage (rugby, tennis, handball, curling, fencing) with localized labels and metadata.
  * New country title processing aid to improve place/category labeling.

* **Bug Fixes**
  * Updated translations: discus throwers and figure skating on television.
  * Removed an obsolete wheelchair basketball key from the sports index.

* **Tests**
  * Added comprehensive wheelchair labeling tests.

* **Chores**
  * Added changelog entry and general internal string-handling cleanups.

## [#46](https://github.com/MrIbrahem/make2_new/pull/46) - 2025-11-11

* **New Features [format_data.py](src/translations_formats/format_data.py)**
  * Introduces FormatData class with template-based string transformation logic, including regex pattern matching from sport keys, placeholder replacement, category normalization, and a unified search() method orchestrating the lookup pipeline. Includes a sample usage function.

## [#45](https://github.com/MrIbrahem/make2_new/pull/45) - 2025-11-11

* **New Features**
  * Improved organization and categorization of sports team-related data
  * Enhanced support for sports category mappings and labels

* **Chores**
  * Reorganized internal data structures for better sports information management
  * Updated code formatting and test annotations

## [#44](https://github.com/MrIbrahem/make2_new/pull/44) - 2025-11-10
* **Refactor [jobs_players_list.py](src/translations/jobs/jobs_players_list.py)**

## [#42](https://github.com/MrIbrahem/make2_new/pull/42) - 2025-11-10

* **Refactor**
  * Optimized data loading performance through lazy initialization and caching mechanisms.
  * Reorganized internal data structures and standardized naming conventions for consistency.
  * Expanded public API to expose additional utility functions and data resources.

* **Performance Improvements**
  * Enhanced lookup efficiency with memoized function calls and cached data retrieval.

* **Tests**
  * Added slow-test markers for improved test categorization and execution management.

## [#41](https://github.com/MrIbrahem/make2_new/pull/41) - 2025-11-09

* **Refactor [pop_All_2018_bot.py](src/translations/mix_data/pop_All_2018_bot.py)**
  - Reorganized internal data-loading and resolution flows for consistency.
  - Removed deprecated backward-compatibility aliases and an obsolete resolver.
  - Consolidated imports and simplified name-resolution logic to improve maintainability.

## [#37](https://github.com/MrIbrahem/make2_new/pull/37) - 2025-11-09

* **New Features**
  * Centralized runtime configuration controlling printing, Wikidata, Kooora, stubs, and other app flags.
  * New colored text formatting helper for styled output.

* **Refactor**
  * Replaced argv-driven flags with settings-driven behavior across the app.
  * Unified logging via a wrapper and simplified printing API to delegate to the logger.

* **Chores**
  * Updated ignore list (added generated start file).

## [#36](https://github.com/MrIbrahem/make2_new/pull/36) - 2025-11-09

* **Refactor [jobs_singers.py](src/translations/jobs/jobs_singers.py)**
  * Updated public constant names to follow Python naming conventions (MEN_WOMENS_SINGERS, FILMS_TYPE, SINGERS_TAB)
  * Reorganized data generation with modular helper functions
  * Consolidated internal data mappings and improved code organization

* **Tests**
  * Updated tests to align with refactored constant names

## [#35](https://github.com/MrIbrahem/make2_new/pull/35) - 2025-11-09

* **New Features**
  * Expanded job and place name datasets with additional job categories and extensive place-name translations for improved Arabic localization.

* **Refactor  [Cities.py](src/translations/geo/Cities.py), [jobs_defs.py](src/translations/jobs/jobs_defs.py)**
  * Switched to centralized data-driven loading for geographic names and job labels to simplify updates and reduce hardcoded entries.

* **Chores**
  * Added new data assets and updated changelog with two new entries and an expanded existing entry.

## [#34](https://github.com/MrIbrahem/make2_new/pull/34) - 2025-11-09

* **New Features**
  * Expanded and enriched job, player and singer datasets with additional entries and gendered labels, improving localized display.

* **Refactor**
  * Migrated data loading to centralized JSON sources for jobs, singers and players to enable data-driven updates and consistency.

* **Chores**
  * Added new JSON data files to supply the updated datasets and translations.

## [#32](https://github.com/MrIbrahem/make2_new/pull/32) - 2025-11-08

### Changed
* Refactored all modules under `src/make2_bots/o_bots` with comprehensive type hints, PEP 8 naming, and Google-style documentation.
* Centralised shared suffix-matching and caching helpers to eliminate duplicated logic across bots.
* Standardised logging usage and cache handling, adding inline comments to clarify complex resolution flows.
* Updated dependent bots to consume the new PEP 8 interfaces and refreshed formatting across touched files.

### Added
* Introduced `src/make2_bots/o_bots/utils.py` to host reusable helpers for cache keys, suffix resolution, and article handling.

## #31

* **Bug Fixes**
  * Improved template and label resolution with fallbacks
  * Consolidated year-handling logic

* **Tests**
  * Expanded test coverage for locale, year, and historical-period data

* **Improvements**
  * Refined public API with clearer naming conventions
  * Enhanced text normalization pipeline for Arabic label processing

---

## #30

* **Bug Fixes**
  * Improved template/label resolution with additional fallback steps for more accurate mapping.

* **Tests**
  * Reorganized and expanded locale/year and historical-period test data; trimmed other year mappings for focused coverage.

* **Documentation**
  * Standardized and simplified changelog structure and headers.

* **Chores**
  * Removed the automatic type-hint injector module; consolidated dependency imports and removed optional local fallbacks; minor typing and config adjustments.

---

## #13

* **Refactor**
  * Reorganized package structure with new submodules for improved organization (sports, politics, companies, utilities).
  * Updated import paths across modules for better maintainability.

* **New Features**
  * Added comprehensive localization mappings for sports, companies, buildings, and medical terminology.
  * Expanded translation data for enhanced language support and domain coverage.

---

## #5 [Enhance event label processing and test suite reorganization] - 2025-11-05

This update improves label processing accuracy and restructures the test architecture for better maintainability.

### Added

* Introduced new event label processing functionality with enhanced category handling.
* Expanded structured test suites covering various event domains such as culture, entertainment, geography, institutions, people, places, politics, science, sports, and temporal data.

### Changed

* Refactored imports and package-level exports for consistency.
* Updated pytest configuration for broader and more efficient test discovery.
* Improved data consistency and label comparison logic.

### Fixed

* Corrected import paths and unified test result assertions.

### Removed

* Cleaned up deprecated test scripts and legacy helpers replaced by the unified pytest structure.

---

## #3 - 2025-11-03

### Added
*   New module `src/make2_bots/reg_lines.py` for centralized regular expression definitions.
*   "solar eclipses" added to the country add-ins list.

### Changed
*   Refactored multiple Python files to utilize centralized and precompiled regex patterns.
*   Simplified the event labeling flow in `src/make2_bots/ma_bots/year_or_typeo/bot_lab.py` and `src/make2_bots/ma_bots/event2bot.py` by using centralized regex definitions.

---

## Pull Request 2

* Removed the old `ma_lists_bots` module and updated various modules to use the new submodules under `translations`.
* Unified JSON file loading via the `open_json_file` function, reorganized public exports, and adjusted relative imports.
* Added a new logger and HTTP helper utilities, updating dependent modules accordingly.
* Removed old scripts and tools from the `others` directory and reorganized import tests.
* Updated tests and documentation to align with the new module structure.

---

## Pull Request 1

* **New Features:** Added a unified logger and web request utilities, enabling team/player and Wikidata searches through simple command-line tools.
* **Refactor:** Unified JSON and data file loading with expanded public exports; cleaned up old tools and scripts.
* **Documentation:** Removed an outdated diagram from the README and updated the changelog in line with new policies.
* **Tests:** Added tests for external search operations and updated import paths.
* **Maintenance Tasks:** Added ignore rules for files generated during local development.
