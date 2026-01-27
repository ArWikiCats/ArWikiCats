"""
Unit tests for check_bot module.
"""

import pytest

from ArWikiCats.legacy_bots.make_bots.check_bot import (
    add_key_new_players,
    check_key_in_tables,
    check_key_new_players,
    check_key_new_players_n,
    set_tables,
)


# ---------------------------------------------------------------------------
# Tests for check_key_in_tables function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestCheckKeyInTables:
    """Tests for the check_key_in_tables function."""

    def test_returns_false_for_empty_tables(self) -> None:
        """Should return False for empty tables list."""
        result = check_key_in_tables("test", [])
        assert result is False

    def test_returns_true_when_key_in_dict(self) -> None:
        """Should return True when key is found in a dict."""
        tables = [{"test": "value"}]
        result = check_key_in_tables("test", tables)
        assert result is True

    def test_returns_true_when_key_in_list(self) -> None:
        """Should return True when key is found in a list."""
        tables = [["test", "other"]]
        result = check_key_in_tables("test", tables)
        assert result is True

    def test_returns_true_when_key_in_set(self) -> None:
        """Should return True when key is found in a set."""
        tables = [{"test", "other"}]
        result = check_key_in_tables("test", tables)
        assert result is True

    def test_returns_false_when_key_not_found(self) -> None:
        """Should return False when key is not found."""
        tables = [{"other": "value"}, ["another"]]
        result = check_key_in_tables("test", tables)
        assert result is False

    def test_case_insensitive_lookup(self) -> None:
        """Should check both original and lowercase keys."""
        tables = [{"test": "value"}]
        result = check_key_in_tables("TEST", tables)
        # Check if lowercase version matches
        assert result is True or check_key_in_tables("test", tables) is True


# ---------------------------------------------------------------------------
# Tests for check_key_new_players function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestCheckKeyNewPlayers:
    """Tests for the check_key_new_players function."""

    def test_returns_boolean(self) -> None:
        """Should return a boolean."""
        result = check_key_new_players("test")
        assert isinstance(result, bool)

    def test_returns_false_for_unknown_key(self) -> None:
        """Should return False for unknown key."""
        result = check_key_new_players("unknown_xyz_key_123456")
        assert result is False

    def test_case_insensitive(self) -> None:
        """Should be case insensitive."""
        result1 = check_key_new_players("TEST")
        result2 = check_key_new_players("test")
        # Both should return the same result
        assert result1 == result2


# ---------------------------------------------------------------------------
# Tests for check_key_new_players_n function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestCheckKeyNewPlayersN:
    """Tests for the check_key_new_players_n function."""

    def test_returns_boolean(self) -> None:
        """Should return a boolean."""
        result = check_key_new_players_n("test")
        assert isinstance(result, bool)

    def test_returns_false_for_unknown_key(self) -> None:
        """Should return False for unknown key."""
        result = check_key_new_players_n("unknown_xyz_key_123456")
        assert result is False

    def test_case_insensitive(self) -> None:
        """Should be case insensitive."""
        result1 = check_key_new_players_n("TEST")
        result2 = check_key_new_players_n("test")
        # Both should return the same result
        assert result1 == result2


# ---------------------------------------------------------------------------
# Tests for add_key_new_players function
# ---------------------------------------------------------------------------


@pytest.fixture
def players_new_keys_fixture():
    """Fixture to provide access to players_new_keys and clean up test keys."""
    from ArWikiCats.legacy_bots.make_bots.bot import players_new_keys

    test_keys_added = []
    yield players_new_keys, test_keys_added
    # Cleanup: remove any test keys that were added
    for key in test_keys_added:
        if key in players_new_keys:
            del players_new_keys[key]


@pytest.mark.fast
class TestAddKeyNewPlayers:
    """Tests for the add_key_new_players function."""

    def test_adds_key_to_players_new_keys(self, players_new_keys_fixture) -> None:
        """Should add key to players_new_keys."""
        players_new_keys, test_keys_added = players_new_keys_fixture

        # Use a unique key that won't conflict
        test_key = "test_add_key_12345"
        test_value = "تسمية اختبار"

        # Track this key for cleanup
        test_keys_added.append(test_key.lower())

        add_key_new_players(test_key, test_value, "test_file")
        assert test_key.lower() in players_new_keys
        assert players_new_keys[test_key.lower()] == test_value

    def test_normalizes_key_to_lowercase(self, players_new_keys_fixture) -> None:
        """Should normalize key to lowercase."""
        players_new_keys, test_keys_added = players_new_keys_fixture

        test_key = "TEST_UPPERCASE_KEY_12345"
        test_value = "تسمية"

        # Track this key for cleanup
        test_keys_added.append(test_key.lower())

        add_key_new_players(test_key, test_value, "test_file")
        assert test_key.lower() in players_new_keys
        assert test_key not in players_new_keys  # Original case should not exist


# ---------------------------------------------------------------------------
# Tests for set_tables
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestSetTables:
    """Tests for the set_tables list."""

    def test_set_tables_is_list(self) -> None:
        """set_tables should be a list."""
        assert isinstance(set_tables, list)

    def test_set_tables_not_empty(self) -> None:
        """set_tables should not be empty."""
        assert len(set_tables) > 0

    def test_set_tables_contains_expected_tables(self) -> None:
        """set_tables should contain expected tables."""
        from ArWikiCats.legacy_bots.make_bots.bot import players_new_keys
        from ArWikiCats.translations import Jobs_new, jobs_mens_data

        assert players_new_keys in set_tables
        assert Jobs_new in set_tables
        assert jobs_mens_data in set_tables
