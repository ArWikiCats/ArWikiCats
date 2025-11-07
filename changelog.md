## [Refactor general job label dictionaries] - 2025-11-07

### Added
* None.

### Changed
* Rebuilt `src/ma_lists/jobs/Jobs2.py` around typed helpers, documented constants, and structured logging for gendered job labels.

### Fixed
* None.

### Removed
* Dropped legacy import-time print statements in favour of debug logging.

## [Refactor singer job label utilities] - 2025-11-07

### Added
* Introduced typed helpers for loading singer label JSON configuration and combining category roles.

### Changed
* Rebuilt `src/ma_lists/jobs/jobs_singers.py` around documented constants and reusable builders for gendered label assembly.

### Fixed
* Prevented duplicate whitespace when feminine non-fiction labels are unavailable, matching downstream expectations.

### Removed
* Eliminated the legacy self-import pattern from `jobs_singers` in favour of explicit exports.

## [Refactor player job label utilities] - 2025-11-07

### Added
* Exported structured constants for boxing, skating, and team sport player labels.

### Changed
* Rebuilt `src/ma_lists/jobs/jobs_players_list.py` around typed helper functions and reusable builders.
* Standardized champion, commentator, and coaching label assembly with shared string joining logic.

### Fixed
* Ensured women's sports categories gracefully reuse masculine wording when feminine data is unavailable.

### Removed
* None.

## [Refactor job label definitions for typed helpers] - 2025-11-07

### Added
* None.

### Changed
* Replaced ad-hoc dictionary assembly in `src/ma_lists/jobs/jobs_defs.py` with typed helpers and documented constants for gendered job labels.

### Fixed
* None.

### Removed
* None.

## Pull Request 1

* **New Features:** Added a unified logger and web request utilities, enabling team/player and Wikidata searches through simple command-line tools.
* **Refactor:** Unified JSON and data file loading with expanded public exports; cleaned up old tools and scripts.
* **Documentation:** Removed an outdated diagram from the README and updated the changelog in line with new policies.
* **Tests:** Added tests for external search operations and updated import paths.
* **Maintenance Tasks:** Added ignore rules for files generated during local development.

## Pull Request 2

* Removed the old `ma_lists_bots` module and updated various modules to use the new submodules under `ma_lists`.
* Unified JSON file loading via the `open_json_file` function, reorganized public exports, and adjusted relative imports.
* Added a new logger and HTTP helper utilities, updating dependent modules accordingly.
* Removed old scripts and tools from the `others` directory and reorganized import tests.
* Updated tests and documentation to align with the new module structure.

## #3 - 2025-11-03

### Added
*   New module `src/make2_bots/reg_lines.py` for centralized regular expression definitions.
*   "solar eclipses" added to the country add-ins list.

### Changed
*   Refactored multiple Python files to utilize centralized and precompiled regex patterns.
*   Simplified the event labeling flow in `src/make2_bots/ma_bots/dodo_bots/event2bot_dodo.py` and `src/make2_bots/ma_bots/event2bot.py` by using centralized regex definitions.

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
## #13

* **Refactor**
  * Reorganized package structure with new submodules for improved organization (sports, politics, companies, utilities).
  * Updated import paths across modules for better maintainability.

* **New Features**
  * Added comprehensive localization mappings for sports, companies, buildings, and medical terminology.
  * Expanded translation data for enhanced language support and domain coverage.
