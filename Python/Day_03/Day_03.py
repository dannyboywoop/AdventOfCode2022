from aoc_tools import Advent_Timer

ASCII_VAL_UPPER_OFFSET = 38
ASCII_VAL_LOWER_OFFSET = 96
GROUP_SIZE = 3


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [line.strip() for line in file]
    return data


def get_value(char):
    ascii_val = ord(char)
    return ascii_val - (ASCII_VAL_UPPER_OFFSET if char.isupper() else ASCII_VAL_LOWER_OFFSET)


def find_poorly_sorted_item(rucksack):
    mid = len(rucksack) // 2
    items_in_first_half = set(rucksack[:mid])

    # for item in second half of rucksack
    for item in rucksack[mid:]:
        if item in items_in_first_half:
            return item

    return None


def find_common_item(rucksacks):
    return set.intersection(*(set(rucksack) for rucksack in rucksacks)).pop()


def star_01(rucksacks):
    return sum(get_value(find_poorly_sorted_item(rucksack)) for rucksack in rucksacks)


def star_02(rucksacks):
    total = 0
    for i in range(0, len(rucksacks), GROUP_SIZE):
        total += get_value(find_common_item(rucksacks[i : i + GROUP_SIZE]))
    return total


if __name__ == "__main__":
    timer = Advent_Timer()

    rucksacks = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_01(rucksacks)}")
    timer.checkpoint_hit()

    print(f"Star_02: {star_02(rucksacks)}")
    timer.checkpoint_hit()

    timer.end_hit()
