"""
    Day 1: Trebuchet?!
"""
from utils.input import get_input_data


SPELLED_OUT_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_input(filename: str) -> list[str]:
    """Retrieves, parses, and formats the input data."""
    lines = get_input_data(filename)
    # Remove newline characters:
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


def find_spelled_out_numbers(line: str) -> list[tuple[int, int]]:
    """Given a string, returns a list of tuples where the first element is the
    zero-indexed position of the spelled out digit and the second element is
    the digit value itself.

    Example:
        Given "one2two3three", returns [(0, 1), (4, 2), (8, 3)].
    """
    results = []
    for spelled_out, digit in SPELLED_OUT_NUMBERS.items():
        find_start = 0
        while spelled_out in line:
            starts_at_index = line.find(spelled_out, find_start)
            results.append((starts_at_index, digit))
            # Make sure we don't find the same instance again:
            find_start = starts_at_index + 1
    return results


def part1(data: list[str]) -> int:
    """Solves part 1 of the day's challenge."""
    # Create a new list of lists, where each list contains only the digits
    # as integers:
    digits_list = []
    for line in data:
        filtered = filter(lambda x: x.isdigit(), line)
        digits_only = list(map(lambda x: int(x), filtered))
        digits_list.append(digits_only)
    # Gather the first and last digits of each list.
    # When only one digit is present, it is both the first and last digit.
    two_digit_nums = map(build_two_digit_nums, digits_list)
    # Sum all the two-digit numbers:
    return sum(list(two_digit_nums))


def part2(data: list[str]) -> int:
    """Solves part 2 of the day's challenge."""
    # Create a new list of lists, where each list contains both the spelled-out
    # number and the digits as integers:
    digits_list = []
    for line in data:
        # Build tuples where the first element is the zero-indexed position of the
        # digit (spelled out or not) and the second element is the digit value itself:
        line_digits = []
        # [CASE] Handle already digit values:
        for index, value in enumerate(line):
            if value.isdigit():
                line_digits.append((index, int(value)))
        # [CASE] Handle spelled out numbers:
        extracted_digits = find_spelled_out_numbers(line)
        line_digits.extend(extracted_digits)
        # Sort the list of tuples by the first element (the zero-indexed position):
        line_digits.sort(key=lambda x: x[0])
        # Extract the digits from the sorted list of tuples:
        digits_only = list(map(lambda x: x[1], line_digits))
        digits_list.append(digits_only)

    two_digit_nums = map(build_two_digit_nums, digits_list)
    return sum(list(two_digit_nums))


if __name__ == "__main__":
    input_data = parse_input("day1.txt")
    solution1 = part1(input_data)
    print(f"* Part 1 Solution: {solution1}")  # 52974

    input_data = parse_input("day1.txt")
    solution2 = part2(input_data)
    print(f"* Part 2 Solution: {solution2}")  # 53318 (low) | 52510 (low)
