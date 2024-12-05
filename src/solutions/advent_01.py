from pathlib import Path
from typing import List, Tuple


def main() -> None:
    """Execute main program logic."""
    list_inputs = read_input(Path("inputs") / "advent_01_input.txt")
    distance = calculate_distance_between_list(*list_inputs)
    print(f"Part I - Distance: {distance} \n")


def read_input(file_path: str) -> Tuple[List[int], List[int]]:
    """Read number pairs from file and return sorted lists.
    Args:
        file_path: Path to input file
    Returns:
        Tuple of (left_numbers, right_numbers) as sorted integer lists
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
            left, right = zip(*pairs)
            return sorted(left), sorted(right)
        return [], []

    except FileNotFoundError as err:
        raise FileNotFoundError(f"Input file not found: {file_path}") from err


def calculate_distance_between_list(left_list: List[int], right_list: List[int]) -> int:
    """Find pair of numbers from left_list and right_list that sum to target.
    Args:
        left_list: List of integers
        right_list: List of integers
    Returns:
        int accumulated distance between each pair of numbers
    """
    return sum(abs(left - right) for left, right in zip(left_list, right_list))


if __name__ == "__main__":
    main()
