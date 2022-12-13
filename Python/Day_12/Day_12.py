from operator import add
from dataclasses import dataclass, field
from typing import Tuple, TypeAlias

from aoc_tools import Advent_Timer

from a_star import find_best_path


ORD_OFFSET = ord("a")

Position: TypeAlias = Tuple[int, int]


@dataclass
class Vertex:
    height: int
    neighbours: list[Position] = field(default_factory=list)


def populate_neighbours(vertices):
    for position in vertices:
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            test_position = tuple(map(add, position, direction))
            if test_position not in vertices:
                continue
            if vertices[test_position].height <= vertices[position].height + 1:
                vertices[position].neighbours.append(test_position)


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        char_map = [list(line.strip()) for line in file]
    return char_map


def prepare_vertices(char_map):
    start = None
    end = None
    vertices = {}
    for i, row in enumerate(char_map):
        for j, char in enumerate(row):
            if char == "S":
                char_map[i][j] = "a"
                start = (i, j)
            elif char == "E":
                char_map[i][j] = "z"
                end = (i, j)
            vertices[(i, j)] = Vertex(ord(char_map[i][j]) - ORD_OFFSET)

    populate_neighbours(vertices)
    return vertices, start, end


def star_1(vertices, start, end):
    best_path = find_best_path(vertices, start, end)
    return len(best_path) - 1


def star_2(vertices, end):
    shortest_path = len(vertices)
    for position, vertex in vertices.items():
        if vertex.height > 0:
            continue
        new_path = find_best_path(vertices, position, end)
        if new_path:
            shortest_path = min(shortest_path, len(new_path))
    return shortest_path - 1


if __name__ == "__main__":
    timer = Advent_Timer()

    char_map = read_data("input.txt")
    vertices, start, end = prepare_vertices(char_map)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(vertices, start, end)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(vertices, end)}")
    timer.checkpoint_hit()

    timer.end_hit()
