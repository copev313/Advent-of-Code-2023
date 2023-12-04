"""
    Day 2: Cube Conundrum
"""
from utils.input import get_input_data

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def parse_input(filename: str) -> list[str]:
    """Retrieves, parses, and formats the input data."""
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = list(map(lambda x: x.replace("\n", ""), lines))
    results = []
    for index, line in enumerate(lines):
        rounds = line.split(":")[-1].strip().split(";")
        parsed_record = {
            "game": index + 1,
            "rounds": [x.strip() for x in rounds],
        }
        results.append(parsed_record)
    return results


def create_rgb_tuples(data: list[dict]) -> list[tuple[int, int, int]]:
    """Provided a list of dicts, parses each rounds attribute and returns an
    RGB tuple for each round.

    Example
    -------
        "rounds": [
            "1 blue, 2 green, 3 red",
            "7 red, 8 green",
            "1 green, 2 red, 1 blue",
            "2 green, 3 red, 1 blue",
            "8 green, 1 blue"
        ]

        "rounds": [
            (3, 2, 1),
            (7, 8, 0),
            (2, 1, 1),
            (3, 2, 1),
            (0, 8, 1),
        ]
    """
    for record in data:
        rounds_list = record["rounds"]
        rgb_tuples = []
        # Loop through each rnd string (ex: "1 blue, 2 green, 3 red")
        for rnd in rounds_list:
            red, green, blue = 0, 0, 0
            inventory_itms = rnd.split(",")
            for itm in inventory_itms:
                count, color = itm.strip().split(" ")
                match color:
                    case "red":
                        red += int(count)
                    case "green":
                        green += int(count)
                    case "blue":
                        blue += int(count)
            rgb_tuples.append((red, green, blue))
        record["rounds"] = rgb_tuples
    return data


def part1(data: list[str]) -> int:
    """Solves part 1 of the day's challenge."""
    data = create_rgb_tuples(data)
    total_sum = sum(range(1, 101))
    for record in data:
        rounds_list = record["rounds"]
        for rnd in rounds_list:
            red, green, blue = rnd
            # [CASE] If any of the colors exceed their respective max, skip:
            if red > MAX_RED_CUBES or green > MAX_GREEN_CUBES or blue > MAX_BLUE_CUBES:
                total_sum -= record["game"]
                break
    return total_sum


def part2(data: list[str]) -> int:
    """Solves part 2 of the day's challenge."""
    data = create_rgb_tuples(data)
    powers_list = []
    for record in data:
        min_red, min_green, min_blue = 0, 0, 0
        rounds_list = record["rounds"]
        for rnd in rounds_list:
            red, green, blue = rnd
            min_red = max(min_red, red)
            min_green = max(min_green, green)
            min_blue = max(min_blue, blue)
        powers_list.append(min_red * min_green * min_blue)
    return sum(powers_list)


if __name__ == "__main__":
    input_data = parse_input("day2.txt")
    solution1 = part1(input_data)
    print(f"* Part 1 Solution: {solution1}")  # 2505

    input_data = parse_input("day2.txt")
    solution2 = part2(input_data)
    print(f"* Part 2 Solution: {solution2}")  # 70265
