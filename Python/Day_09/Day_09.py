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


class Rope:
    def __init__(self, number_of_knots):
        self.knots: list[Point] = [Point() for _ in range(number_of_knots)]
        self.tail_history: set[Point] = set([Point()])

    def move_head(self, instruction):
        direction, distance = instruction
        for _ in range(distance):
            self.knots[0] = MOVE[direction](self.knots[0])
            self._update_knots()

    def _update_knots(self):
        for i in range(1, len(self.knots)):
            self._update_knot(front_index=i - 1, back_index=i)
        self.tail_history.add(self.knots[-1])

    def _update_knot(self, front_index, back_index):
        back_to_front = self.knots[front_index] - self.knots[back_index]
        if abs(back_to_front.x) > 1 or abs(back_to_front.y) > 1:
            self.knots[back_index] += back_to_front.normalize()


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [(a, int(b)) for a, b in [line.strip().split() for line in file]]
    return data


def perform_instructions(instructions, number_of_knots=2):
    rope = Rope(number_of_knots)
    for instruction in instructions:
        rope.move_head(instruction)
    return len(rope.tail_history)


if __name__ == "__main__":
    timer = Advent_Timer()

    instructions = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {perform_instructions(instructions)}")
    timer.checkpoint_hit()

    print(f"Star_02: {perform_instructions(instructions, 10)}")
    timer.checkpoint_hit()

    timer.end_hit()
