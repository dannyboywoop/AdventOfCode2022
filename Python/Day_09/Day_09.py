from dataclasses import dataclass, field
from typing import NamedTuple

from aoc_tools import Advent_Timer


class Point(NamedTuple):
    x: int = 0
    y: int = 0

    def normalize(self):
        norm_x = 0 if self.x == 0 else self.x // abs(self.x)
        norm_y = 0 if self.y == 0 else self.y // abs(self.y)
        return Point(norm_x, norm_y)

    def __add__(self, other):
        assert isinstance(other, Point)
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert isinstance(other, Point)
        return Point(self.x - other.x, self.y - other.y)


MOVE = {
    "U": lambda point: Point(point.x, point.y + 1),
    "D": lambda point: Point(point.x, point.y - 1),
    "R": lambda point: Point(point.x + 1, point.y),
    "L": lambda point: Point(point.x - 1, point.y),
}


@dataclass
class Rope:
    head: Point = Point()
    tail: Point = Point()
    previous_tail_positions: set[Point] = field(default_factory=lambda: set([Point()]))

    def move_head(self, instruction):
        direction, distance = instruction
        for _ in range(distance):
            self.head = MOVE[direction](self.head)
            self._update_tail()

    def _update_tail(self):
        tail_to_head = self.head - self.tail
        if abs(tail_to_head.x) > 1 or abs(tail_to_head.y) > 1:
            self.tail += tail_to_head.normalize()
            self.previous_tail_positions.add(self.tail)


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [(a, int(b)) for a, b in [line.strip().split() for line in file]]
    return data


def star_01(instructions):
    rope = Rope()
    for instruction in instructions:
        rope.move_head(instruction)
    return len(rope.previous_tail_positions)


if __name__ == "__main__":
    timer = Advent_Timer()

    instructions = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_01(instructions)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
