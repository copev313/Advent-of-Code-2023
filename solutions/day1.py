"""
    Day 1: Trebuchet?!
"""
from utils.input import get_input_data

# =============================================================================

SPELLED_OUT_NUMBERS = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def parse_input(filename: str) -> list[str]:
    """Retrieves, parses, and formats the input data."""
    lines = get_input_data(filename)
    lines = map(lambda x: x.replace("\n", ""), lines)
    return list(lines)


def build_two_digit_nums(data: list[int]) -> int:
    """Given a list of digits, returns a two-digit number formed by the first
    and last digits.

    Example:
        Given [1, 2, 3, 4, 5], returns 15.
    """
    first, last = data[0], data[-1]
    return first * 10 + last


# =============================================================================


def part1(data: list[str]) -> int:
    """Solves part 1 of the day's challenge."""
    # Create a new list of lists, where each list contains only the digits
    # as integers:
    digits_list = []
    for line in data:
        filtered = filter(lambda x: x.isdigit(), line)
        digits_only = list(map(int, filtered))
        digits_list.append(digits_only)
    # Gather the first and last digits of each list.
    # When only one digit is present, it is both the first and last digit.
    two_digit_nums = map(build_two_digit_nums, digits_list)
    # Sum all the two-digit numbers:
    return sum(list(two_digit_nums))


def part2(data: list[str]) -> int:
    """Solves part 2 of the day's challenge."""
    lines = []
    # Find and replace all spelled-out numbers:
    for line in data:
        for spelled_out, replacement in SPELLED_OUT_NUMBERS.items():
            line = line.replace(spelled_out, replacement)
        lines.append(line)
    # Solve now using part 1 solution:
    return part1(lines)


# =============================================================================

if __name__ == "__main__":
    print("\n==================== DAY 01 ====================")
    input_data = parse_input("day1.txt")
    solution1 = part1(input_data)
    assert solution1 == 52974
    print(f"* Part 1 Solution: {solution1}")

    solution2 = part2(input_data)
    assert solution2 == 53340
    print(f"* Part 2 Solution: {solution2}")
