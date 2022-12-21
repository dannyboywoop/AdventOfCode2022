from typing import NamedTuple
from math import inf
from itertools import product

from aoc_tools import Advent_Timer


SIDES_PER_CUBE = 6


class Point(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)


def get_neighbour_counts(cubes):
    neighbours_counts = {cube: 0 for cube in cubes}
    for cube_position in cubes:
        # only need to check left, top and behind
        for direction in [Point(-1, 0, 0), Point(0, -1, 0), Point(0, 0, -1)]:
            test_position = cube_position + direction
            if test_position not in cubes:
                continue
            neighbours_counts[cube_position] += 1
            neighbours_counts[test_position] += 1
    return neighbours_counts


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = {Point(*(int(x) for x in line.strip().split(","))) for line in file}
    return data


def star_1(cubes):
    neighbour_counts = get_neighbour_counts(cubes)
    return len(cubes) * SIDES_PER_CUBE - sum(neighbour_counts.values())


def bookends(some_iterable):
    """Returns 1 below min and 1 below max of an iterable"""
    min_val = inf
    max_val = -inf
    for val in some_iterable:
        min_val = min(min_val, val)
        max_val = max(max_val, val)
    return min_val - 1, max_val + 1


def initialize_sweeping_edge(cubes):
    # There is almost certainly a nicer way to do this but I CBA.
    x_lo, x_hi = bookends(cube.x for cube in cubes)
    y_lo, y_hi = bookends(cube.y for cube in cubes)
    z_lo, z_hi = bookends(cube.z for cube in cubes)

    sweeping_edge = {  # smallest cuboid of points surrounding the cubes
        Point(x, y, z)
        for x, y, z in (
            tuple(product([x_lo, x_hi], range(y_lo, y_hi + 1), range(z_lo, z_hi + 1)))
            + tuple(product(range(x_lo, x_hi + 1), [y_lo, y_hi], range(z_lo, z_hi + 1)))
            + tuple(product(range(x_lo, x_hi + 1), range(y_lo, y_hi + 1), [z_lo, z_hi]))
        )
    }

    old_sweeping_edge = (
        {  # points on the outside of the `sweeping_edge` cuboid (forces flood inwards)
            Point(x, y, z)
            for x, y, z in (
                tuple(product([x_lo - 1, x_hi + 1], range(y_lo, y_hi + 1), range(z_lo, z_hi + 1)))
                + tuple(product(range(x_lo, x_hi + 1), [y_lo - 1, y_hi + 1], range(z_lo, z_hi + 1)))
                + tuple(product(range(x_lo, x_hi + 1), range(y_lo, y_hi + 1), [z_lo - 1, z_hi + 1]))
            )
        }
    )

    return old_sweeping_edge, sweeping_edge


def sweep_inwards(old_sweeping_edge, sweeping_edge, cubes):
    positions = [
        air_pos + direction
        for air_pos, direction in product(
            sweeping_edge,
            [
                Point(-1, 0, 0),
                Point(0, -1, 0),
                Point(0, 0, -1),
                Point(1, 0, 0),
                Point(0, 1, 0),
                Point(0, 0, 1),
            ],
        )
    ]
    new_positions = [
        pos for pos in positions if pos not in sweeping_edge and pos not in old_sweeping_edge
    ]
    faces_found = len([new_pos for new_pos in new_positions if new_pos in cubes])
    new_sweeping_edge = set(new_positions) - cubes
    return sweeping_edge, new_sweeping_edge, faces_found


def star_2(cubes):
    old_sweeping_edge, sweeping_edge = initialize_sweeping_edge(cubes)
    faces = 0

    while sweeping_edge:
        old_sweeping_edge, sweeping_edge, new_faces = sweep_inwards(
            old_sweeping_edge, sweeping_edge, cubes
        )
        faces += new_faces
    return faces


if __name__ == "__main__":
    timer = Advent_Timer()

    data = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(data)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(data)}")
    timer.checkpoint_hit()

    timer.end_hit()
