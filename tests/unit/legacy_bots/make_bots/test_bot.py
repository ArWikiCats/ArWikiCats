"""
Tests for matables_bots.bot module functions.
"""

import pytest

from src.ArWikiCats.legacy_bots.make_bots.bot import Films_O_TT, add_to_films_o_tt, add_to_new_players, players_new_keys


@pytest.mark.fast
def test_add_to_new_players() -> None:
    """Test add_to_new_players function with various inputs."""
    # Test with valid inputs
    test_key = "test_player_key"
    test_value = "قيمة الاختبار"

    # Add a test entry
    add_to_new_players(test_key, test_value)

    # Verify it was added
    assert test_key in players_new_keys
    assert players_new_keys[test_key] == test_value

    # Test with empty strings (should not add anything)
    initial_count = len(players_new_keys)
    add_to_new_players("", "arabic")
    assert len(players_new_keys) == initial_count

    add_to_new_players("english", "")
    assert len(players_new_keys) == initial_count

    # Test with both empty (should not add anything)
    add_to_new_players("", "")
    assert len(players_new_keys) == initial_count


@pytest.mark.fast
def test_add_to_new_players_invalid_types() -> None:
    """Test add_to_new_players with invalid types."""
    initial_count = len(players_new_keys)

    # Test with None values (should not add)
    add_to_new_players(None, "arabic")
    assert len(players_new_keys) == initial_count

    add_to_new_players("english", None)
    assert len(players_new_keys) == initial_count

    # Test with non-string types
    add_to_new_players(123, "arabic")
    assert len(players_new_keys) == initial_count

    add_to_new_players("english", 456)
    assert len(players_new_keys) == initial_count


@pytest.mark.fast
def test_add_to_films_o_tt() -> None:
    """Test add_to_films_o_tt function with various inputs."""
    # Test with valid inputs
    test_key = "test_film_key"
    test_value = "قيمة فيلم الاختبار"

    # Add a test entry
    add_to_films_o_tt(test_key, test_value)

    # Verify it was added
    assert test_key in Films_O_TT
    assert Films_O_TT[test_key] == test_value

    # Test with empty strings (should not add anything)
    initial_count = len(Films_O_TT)
    add_to_films_o_tt("", "arabic")
    assert len(Films_O_TT) == initial_count

    add_to_films_o_tt("english", "")
    assert len(Films_O_TT) == initial_count

    # Test with both empty (should not add anything)
    add_to_films_o_tt("", "")
    assert len(Films_O_TT) == initial_count


@pytest.mark.fast
def test_add_to_films_o_tt_invalid_types() -> None:
    """Test add_to_films_o_tt with invalid types."""
    initial_count = len(Films_O_TT)

    # Test with None values (should not add)
    add_to_films_o_tt(None, "arabic")
    assert len(Films_O_TT) == initial_count

    add_to_films_o_tt("english", None)
    assert len(Films_O_TT) == initial_count

    # Test with non-string types
    add_to_films_o_tt(123, "arabic")
    assert len(Films_O_TT) == initial_count

    add_to_films_o_tt("english", 456)
    assert len(Films_O_TT) == initial_count


@pytest.mark.fast
def test_add_to_new_players_overwrite() -> None:
    """Test that add_to_new_players can overwrite existing keys."""
    test_key = "overwrite_test_key"
    first_value = "قيمة أولى"
    second_value = "قيمة ثانية"

    # Add initial value
    add_to_new_players(test_key, first_value)
    assert players_new_keys[test_key] == first_value

    # Overwrite with new value
    add_to_new_players(test_key, second_value)
    assert players_new_keys[test_key] == second_value


@pytest.mark.fast
def test_add_to_films_o_tt_overwrite() -> None:
    """Test that add_to_films_o_tt can overwrite existing keys."""
    test_key = "overwrite_film_key"
    first_value = "قيمة فيلم أولى"
    second_value = "قيمة فيلم ثانية"

    # Add initial value
    add_to_films_o_tt(test_key, first_value)
    assert Films_O_TT[test_key] == first_value

    # Overwrite with new value
    add_to_films_o_tt(test_key, second_value)
    assert Films_O_TT[test_key] == second_value


@pytest.mark.fast
def test_players_new_keys_is_dict() -> None:
    """Test that players_new_keys is a dictionary."""
    assert isinstance(players_new_keys, dict)
    assert len(players_new_keys) > 0  # Should have some predefined entries


@pytest.mark.fast
def test_films_o_tt_is_dict() -> None:
    """Test that Films_O_TT is a dictionary."""
    assert isinstance(Films_O_TT, dict)
