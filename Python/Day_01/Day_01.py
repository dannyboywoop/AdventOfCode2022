from aoc_tools import Advent_Timer


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        elf_inventories = file.read().split("\n\n")
        elf_calories = [
            sum(int(item) for item in inventory.split()) for inventory in elf_inventories
        ]
    return elf_calories


def find_fattest_elf(elf_calories):
    most_calories = 0
    for calories in elf_calories:
        most_calories = max(most_calories, calories)
    return most_calories


def find_fattest_n_elves(elf_calories, n):
    # This is inefficient, you don't need to sort the whole list, but life is short
    sorted_calories = sorted(elf_calories)
    return sum(sorted_calories[-n:])


if __name__ == "__main__":
    timer = Advent_Timer()

    elf_calories = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_01 = find_fattest_elf(elf_calories)
    print(f"Star_01: {star_01}")
    timer.checkpoint_hit()

    star_02 = find_fattest_n_elves(elf_calories, 3)
    print(f"Star_02: {star_02}")
    timer.checkpoint_hit()

    timer.end_hit()
