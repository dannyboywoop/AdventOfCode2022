from dataclasses import dataclass

from aoc_tools import Advent_Timer


@dataclass
class Range:
    lower: int
    upper: int

    def __init__(self, range_str):
        self.lower, self.upper = (int(val) for val in range_str.split("-"))


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        range_pairs = [
            tuple(Range(range_str) for range_str in pair.split(","))
            for pair in [line.strip() for line in file]
        ]
    return range_pairs


def find_redundant_elves(range_pairs):
    count = 0
    for range_1, range_2 in range_pairs:
        if range_1.lower == range_2.lower:
            count += 1
        elif range_1.lower > range_2.lower:
            count += range_1.upper <= range_2.upper
        else:
            count += range_1.upper >= range_2.upper
    return count


if __name__ == "__main__":
    timer = Advent_Timer()

    range_pairs = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {find_redundant_elves(range_pairs)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
