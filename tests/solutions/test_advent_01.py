from pathlib import Path

from src.solutions.advent_01 import (
    calculate_distance_between_list,
    calculate_similarity_score,
    read_input,
)


def test_read_input():
    """Test reading full input content."""
    sample_input = Path("inputs") / "advent_01_example.txt"
    left_list, right_list = read_input(sample_input)
    assert left_list == [3, 4, 2, 1, 3, 3]
    assert right_list == [4, 3, 5, 3, 9, 3]


def test_calculate_distance_between_lists():
    """Test distance calculation between two lists."""
    # Test basic positive numbers
    assert calculate_distance_between_list([1, 2, 3], [4, 5, 6]) == 9

    # Test with negative numbers
    assert calculate_distance_between_list([-1, -2], [1, 2]) == 6

    # Test with zeros
    assert calculate_distance_between_list([0, 0], [1, 1]) == 2

    # Test single element
    assert calculate_distance_between_list([1], [2]) == 1

    # Test empty lists
    assert calculate_distance_between_list([], []) == 0


def test_calculate_similarity_score():
    """Test similarity score between two lists."""
    # Test basic scenario with only 1 value repeated
    assert calculate_similarity_score([1], [1, 1, 1]) == 3

    # Test  scenario when none repeated
    assert calculate_similarity_score([1, 2, 3], [4, 5, 6]) == 0

    # Test scenario when repeated in multiple positions
    assert calculate_similarity_score([1, 2, 1], [4, 1, 1]) == 4

    # Test scenario when repeated in multiple positions
    assert calculate_similarity_score([1, 2], [2, 4, 1, 2, 1]) == 6

    # Test empty lists
    assert calculate_similarity_score([], []) == 0
