from typing import NamedTuple

from aoc_tools import Advent_Timer


SIDES_PER_CUBE = 6


class Position(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y, self.z + other.z)


def get_neighbour_counts(cubes):
    neighbours_counts = {cube: 0 for cube in cubes}
    for cube_position in cubes:
        # only need to check left, top and behind
        for direction in [Position(-1, 0, 0), Position(0, -1, 0), Position(0, 0, -1)]:
            test_position = cube_position + direction
            if test_position not in cubes:
                continue
            neighbours_counts[cube_position] += 1
            neighbours_counts[test_position] += 1
    return neighbours_counts


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = {Position(*(int(x) for x in line.strip().split(","))) for line in file}
    return data


def star_1(cubes):
    neighbour_counts = get_neighbour_counts(cubes)
    return len(cubes) * SIDES_PER_CUBE - sum(neighbour_counts.values())


if __name__ == "__main__":
    timer = Advent_Timer()

    data = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(data)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
