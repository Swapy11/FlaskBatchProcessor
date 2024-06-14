# tests/test_addition_controller.py
from FlaskBatchProcessor.controllers.addition_controller import perform_addition


def test_perform_addition():
    """
    Test perform_addition function with valid input.
    """
    lists_of_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_results = [6, 15, 24]
    results = perform_addition(lists_of_numbers)
    assert results == expected_results


def test_perform_addition_empty_input():
    """
    Test perform_addition function with empty input list.
    """
    lists_of_numbers = []
    results = perform_addition(lists_of_numbers)
    assert results == []


def test_perform_addition_invalid_input():
    """
    Test perform_addition function with invalid input.
    """
    lists_of_numbers = [[1, 2], [4, "a", 6], [7, 8, 9]]
    results = perform_addition(lists_of_numbers)
    assert results == [3, None, 24]
