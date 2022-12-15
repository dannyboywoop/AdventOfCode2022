from operator import add
from dataclasses import dataclass
from typing import Tuple, TypeAlias
from math import inf
from queue import PriorityQueue

from aoc_tools import Advent_Timer


ORD_OFFSET = ord("a")

Position: TypeAlias = Tuple[int, int]


@dataclass
class Vertex:
    height: int
    neighbours: list[Position] = None


def populate_neighbours(vertices, reverse=False):
    for position in vertices:
        vertices[position].neighbours = []
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            test_position = tuple(map(add, position, direction))
            if test_position not in vertices:
                continue
            climb = vertices[test_position].height - vertices[position].height
            if (not reverse and climb <= 1) or (reverse and climb >= -1):
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


def star_2(vertices, end):
    populate_neighbours(vertices, reverse=True)
    return find_best_path(vertices, end, lambda pos: vertices[pos].height == 0)


def find_best_path(vertices, start_pos, goal_criteria):
    open_set = PriorityQueue()
    best_path_length_to_vertex = {start_pos: 0}

    open_set.put((best_path_length_to_vertex[start_pos], start_pos))

    while not open_set.empty():
        current = open_set.get()[1]
        if goal_criteria(current):
            return best_path_length_to_vertex[current]

        for neighbour in vertices[current].neighbours:
            path_length_to_neighbour_via_current = best_path_length_to_vertex[current] + 1
            if path_length_to_neighbour_via_current < best_path_length_to_vertex.get(
                neighbour, inf
            ):
                best_path_length_to_vertex[neighbour] = path_length_to_neighbour_via_current
                open_set.put((best_path_length_to_vertex[neighbour], neighbour))
    return None


if __name__ == "__main__":
    timer = Advent_Timer()

    char_map = read_data("input.txt")
    vertices, start, end = prepare_vertices(char_map)
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {find_best_path(vertices, start, lambda pos: pos==end)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(vertices, end)}")
    timer.checkpoint_hit()

    timer.end_hit()
