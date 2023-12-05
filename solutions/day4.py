"""
    Day 4: Scratchcards
"""
from utils.input import get_input_data

# =============================================================================


class Scratchcard:
    def __init__(
        self,
        card_number: int,
        winning_numbers: list[int],
        sampled_numbers: list[int],
    ):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.sampled_numbers = sampled_numbers
        self.worth_points = 0
        self.matching_numbers = []

    def __repr__(self):
        return f"Scratchcard {self.card_number}: {self.winning_numbers} | {self.sample_space}"

    @staticmethod
    def calculate_worth(num_hits: int) -> int:
        """Calculates the number of points a scratchcard is worth based on the number of hits
        (winning numbers) provided. After the first win, the value of points doubles for each
        additional win.
        """
        # [CASE] No winning numbers:
        if num_hits in [0, 1]:
            return num_hits
        # [CASE] Double the value of the scratchcard for each winning number:
        if num_hits >= 2:
            return 2 ** (num_hits - 1)
        # Just in case:
        raise ValueError("Invalid number of hits.")

    def play(self) -> list[int]:
        """Plays the scratchcard and returns a list of matching numbers."""
        # Look for each winning number:
        for winning_num in self.winning_numbers:
            if winning_num in self.sampled_numbers:
                # Winning number found -> add to list of matching numbers:
                self.matching_numbers.append(winning_num)
        # Calculate the worth of the scratchcard:
        self.worth_points = self.calculate_worth(len(self.matching_numbers))


def parse_input(filename: str) -> list[str]:
    """Retrieves, parses, and formats the input data."""
    all_cards = []
    # Define namedtuple data structure for scratchcards:
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = map(lambda x: x.replace("\n", ""), lines)
    for line in lines:
        # Gather & format card number:
        card_num = line.split(":")[0].split("Card")[1]
        card_num = int(card_num)
        assert card_num in range(1, 201)
        # Gather & format winning numbers:
        winning_nums = line.split(":")[1].split("|")[0].split(" ")
        winning_nums = filter(lambda x: x != "", winning_nums)
        winning_nums = list(map(int, winning_nums))
        assert len(winning_nums) == 10 or len(winning_nums) == 5
        # Gather & format sample space:
        sample = line.split(":")[1].split("|")[1].split(" ")
        sample = filter(lambda x: x != "", sample)
        sample = list(map(int, sample))
        assert len(sample) == 8 or len(sample) == 25
        # Create Scratchcard instance & add to list:
        all_cards.append(
            Scratchcard(
                card_number=card_num,
                winning_numbers=winning_nums,
                sampled_numbers=sample,
            )
        )
    return all_cards


# =============================================================================


def part1(data: list[Scratchcard]) -> int:
    """Solves part 1 of the day's challenge."""
    total_points = 0
    for card in data:
        card.play()
        total_points += card.worth_points
    return total_points


def part2(data: list[str]) -> int:
    """Solves part 2 of the day's challenge."""
    pass


# =============================================================================

if __name__ == "__main__":
    # example_data = parse_input("day4-example.txt")
    input_data = parse_input("day4.txt")

    solution1 = part1(input_data)
    print(f"* Part 1 Solution: {solution1}")

    solution2 = part2(input_data)
    print(f"* Part 2 Solution: {solution2}")
