
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

* **Refactor [pop_All_2018_bot.py](src/ma_lists/mix_data/pop_All_2018_bot.py)**
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

* **Refactor [jobs_singers.py](src/ma_lists/jobs/jobs_singers.py)**
  * Updated public constant names to follow Python naming conventions (MEN_WOMENS_SINGERS, FILMS_TYPE, SINGERS_TAB)
  * Reorganized data generation with modular helper functions
  * Consolidated internal data mappings and improved code organization

* **Tests**
  * Updated tests to align with refactored constant names

## [#35](https://github.com/MrIbrahem/make2_new/pull/35) - 2025-11-09

* **New Features**
  * Expanded job and place name datasets with additional job categories and extensive place-name translations for improved Arabic localization.

* **Refactor  [Cities.py](src/ma_lists/geo/Cities.py), [jobs_defs.py](src/ma_lists/jobs/jobs_defs.py)**
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
*   Simplified the event labeling flow in `src/make2_bots/ma_bots/dodo_bots/event2bot_dodo.py` and `src/make2_bots/ma_bots/event2bot.py` by using centralized regex definitions.

---

## Pull Request 2

* Removed the old `ma_lists_bots` module and updated various modules to use the new submodules under `ma_lists`.
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
