"""
    Day 3: Gear Ratios
"""
from utils.input import get_input_data

# =============================================================================


def parse_input(filename: str) -> list[str]:
    """Retrieves, parses, and formats the input data."""
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = map(lambda x: x.replace("\n", ""), lines)
    # print(list(lines))
    return list(lines)


def find_special_symbols(data: list[str]) -> list[str]:
    """Finds all special symbols in the data."""
    special_symbols = []
    for row_i, row_string in enumerate(data):
        for col_j, char in enumerate(row_string):
            special_symbols.append(data[row_i][col_j])
    # Generate list of unique characters:
    unique_chars = list(set(special_symbols))
    # Remove non-symbol characters:
    non_symbols = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for char in non_symbols:
        if char in unique_chars:
            unique_chars.remove(char)
    return unique_chars


# =============================================================================


def part1(data: list[list[str]]) -> int:
    """Solves part 1 of the day's challenge.

    Returns a list of valid numbers that have adjacent special symbols.
    """
    SPECIAL_SYMBOLS = find_special_symbols(data)
    MAX_ROW_INDEX = len(data) - 1
    MAX_COL_INDEX = len(data[0]) - 1
    valid_numbers = []
    for row_i in range(MAX_ROW_INDEX + 1):
        built_digit = ""
        is_valid = False
        for col_j in range(MAX_COL_INDEX + 1):
            current = data[row_i][col_j]

            # [CASE] Character is a digit:
            if current.isdigit():
                # Add current digit to built_digit:
                built_digit += current
                # Look for adjacent special symbols in all directions:
                if is_valid is False:
                    # [CHECK] Left:
                    if col_j > 0:
                        left = data[row_i][col_j - 1]
                        if left in SPECIAL_SYMBOLS:
                            is_valid = True
                    # [CHECK] Right:
                    if col_j < MAX_COL_INDEX:
                        right = data[row_i][col_j + 1]
                        if right in SPECIAL_SYMBOLS:
                            is_valid = True
                    # [CHECK] Up:
                    if row_i > 0:
                        up = data[row_i - 1][col_j]
                        if up in SPECIAL_SYMBOLS:
                            is_valid = True
                    # [CHECK] Down:
                    if row_i < MAX_ROW_INDEX:
                        down = data[row_i + 1][col_j]
                        if down in SPECIAL_SYMBOLS:
                            is_valid = True
                    # [CHECK] Up-Left:
                    if row_i > 0 and col_j > 0:
                        up_left = data[row_i - 1][col_j - 1]
                        if up_left in SPECIAL_SYMBOLS:
                            is_valid = True
                    # [CHECK] Up-Right:
                    if row_i > 0 and col_j < MAX_COL_INDEX:
                        up_right = data[row_i - 1][col_j + 1]
                        if up_right in SPECIAL_SYMBOLS:
                            is_valid = True
                    # [CHECK] Down-Left:
                    if row_i < MAX_ROW_INDEX and col_j > 0:
                        down_left = data[row_i + 1][col_j - 1]
                        if down_left in SPECIAL_SYMBOLS:
                            is_valid = True
                    # [CHECK] Down-Right:
                    if row_i < MAX_ROW_INDEX and col_j < MAX_COL_INDEX:
                        down_right = data[row_i + 1][col_j + 1]
                        if down_right in SPECIAL_SYMBOLS:
                            is_valid = True

            # [CASE] End conditions:
            if (
                current == "."
                or current in SPECIAL_SYMBOLS
                or col_j == MAX_COL_INDEX
            ):
                # [CHECK] A digit has been built:
                if built_digit != "":
                    if is_valid:
                        valid_numbers.append(int(built_digit))
                    # Empty built_digit and reset is_valid:
                    built_digit = ""
                    is_valid = False

    print(valid_numbers)
    return sum(valid_numbers)


def part2(data: list[str]) -> int:
    """Solves part 2 of the day's challenge."""
    pass


# =============================================================================

if __name__ == "__main__":
    print("\n==================== DAY 03 ====================")
    input_data = parse_input("day3.txt")
    solution1 = part1(input_data)
    assert solution1 == 546563
    print(f"* Part 1 Solution: {solution1}")

    input_data = parse_input("day3-example.txt")
    solution2 = part2(input_data)
    print(f"* Part 2 Solution: {solution2}")
