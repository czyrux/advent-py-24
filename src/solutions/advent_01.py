from pathlib import Path
from typing import List, Tuple


def main() -> None:
    """Execute main program logic."""
    list_inputs = read_input(Path("inputs") / "advent_01_input.txt")

    distance = calculate_distance_between_list(*list_inputs)
    print(f"Part I - Distance: {distance} \n")

    similarity_score = calculate_similarity_score(*list_inputs)
    print(f"Part II - Similarity score: {similarity_score} \n")


def read_input(file_path: str) -> Tuple[List[int], List[int]]:
    """Read number pairs from file and return sorted lists.
    Args:
        file_path: Path to input file
    Returns:
        Tuple of (left_numbers, right_numbers) lists preserving input order
    """
    path = Path(file_path)
    try:
        pairs = [
            # Convert to integers and make a tuple
            (int(left), int(right))
            # Split lines and filter out empty lines
            for line in path.read_text().splitlines()
            if line.strip()
            # Unpack pairs
            for left, right in [line.split()]
        ]

        # Unzip pairs if any exist
        if pairs:
            left_nums, right_nums = zip(*pairs)
            return (list(left_nums), list(right_nums))
        return [], []

    except FileNotFoundError as err:
        raise FileNotFoundError(f"Input file not found: {file_path}") from err


def calculate_distance_between_list(left_list: List[int], right_list: List[int]) -> int:
    """Calculate the total distance between two list.

    Distance is measured as the total distance between each pair of elements
    at the same position on the sorted list.

    Args:
        left_list: List of integers
        right_list: List of integers
    Returns:
        int accumulated distance between each pair of numbers
    """
    left_list, right_list = sorted(left_list), sorted(right_list)
    return sum(abs(left - right) for left, right in zip(left_list, right_list))


def calculate_similarity_score(left_list: List[int], right_list: List[int]) -> int:
    """Calculate how similar are both list.

    Score is the sum of each value times its frequency in right list.

    Args:
        left_list: List of integers
        right_list: List of integers
    Returns:
        int similarity score between both lists
    """

    # Count the frequency of each number on the right list
    right_list_frequencies = {}
    for num in right_list:
        right_list_frequencies[num] = right_list_frequencies.get(num, 0) + 1

    return sum(value * right_list_frequencies.get(value, 0) for value in left_list)


if __name__ == "__main__":
    main()
