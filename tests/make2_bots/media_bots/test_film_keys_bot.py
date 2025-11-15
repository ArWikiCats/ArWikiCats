"""
Tests
"""
import pytest

from src.make2_bots.media_bots.film_keys_bot import get_Films_key_CAO, Films

def test_get_films_key_cao():
    # Test with a basic input
    result = get_Films_key_CAO("action films")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = get_Films_key_CAO("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_Films_key_CAO("comedy movies")
    assert isinstance(result_various, str)

def test_films():
    # Test with basic parameters using valid country codes
    result = Films("action films", "united states", "people")
    assert isinstance(result, str)

    # Test with empty parameters
    result_empty = Films("", "", "")
    assert isinstance(result_empty, str)

    # Test with different parameters using valid country codes
    result_various = Films("drama", "united kingdom", "movies", "reference")
    assert isinstance(result_various, str)
