from itertools import pairwise
from pathlib import Path
from typing import Callable, List, TypeAlias

Report: TypeAlias = List[int]
ReportValidator: TypeAlias = Callable[[Report], bool]


def main() -> None:
    """Execute main program logic. Advent_02"""
    reports = read_reports(Path("inputs") / "advent_02_input.txt")

    count = count_safe_reports(reports, is_report_safe)
    count_with_tolerance = count_safe_reports(reports, is_report_safe_with_tolerance)

    print(f"I - Safe reports: {count} \n")
    print(f"II - Safe reports with tolerance: {count_with_tolerance} \n")


def read_reports(file_path: str) -> List[Report]:
    """Read and parse reports from file.

    Args:
        file_path: Path to input file
    Returns:
        List of numeric reports
    """
    path = Path(file_path)
    try:
        return [
            [int(num) for num in line.split()]
            for line in path.read_text().splitlines()
            if line.strip()
        ]
    except FileNotFoundError as err:
        raise FileNotFoundError(f"Input file not found: {file_path}") from err
    except ValueError as err:
        raise ValueError(f"Invalid number in file: {err}") from err


def count_safe_reports(reports: List[Report], validator: ReportValidator) -> int:
    """Count reports meeting safety criteria."""
    return sum(1 for report in reports if validator(report))


"""Part I"""


def is_level_safe(level_a: int, level_b: int, should_increase: bool) -> bool:
    distance = abs(level_a - level_b)
    current_increasing = level_a < level_b
    return 1 <= distance <= 3 and current_increasing == should_increase


def is_report_safe(report: Report) -> bool:
    """Check if report meets safety criteria.

    A report is safe if:
    - Empty or single value
    - All adjacent values differ by 1-3
    - Consistent increasing/decreasing pattern
    """
    if len(report) <= 1:
        return True
    should_increase = report[0] < report[1]
    return all(is_level_safe(a, b, should_increase) for a, b in pairwise(report))


"""Part II"""


def is_report_safe_with_tolerance(report: Report) -> bool:
    """Check if report meets safety criteria. Allowing a single exception on it."""
    if is_report_safe(report):
        return True

    return any(is_report_safe(report[:i] + report[i + 1 :]) for i in range(len(report)))


def is_report_safe_with_tolerance_v2(report: Report) -> bool:
    """Check if report meets safety criteria with one exception."""
    if len(report) <= 1:
        return True
    increasing = report[0] < report[1]
    violations = sum(not is_level_safe(a, b, increasing) for a, b in pairwise(report))
    return violations <= 1


if __name__ == "__main__":
    main()
