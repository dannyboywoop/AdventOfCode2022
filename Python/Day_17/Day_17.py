from typing import NamedTuple, Tuple
from functools import cache

from aoc_tools import Advent_Timer


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


ROCK_SHAPES = [
    (Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)),
    (Point(1, 0), Point(0, 1), Point(1, 1), Point(2, 1), Point(1, 2)),
    (Point(0, 0), Point(1, 0), Point(2, 0), Point(2, 1), Point(2, 2)),
    (Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)),
    (Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)),
]


class Rock:
    def __init__(self, shape: Tuple[Point], origin: Point):
        self.shape = shape
        self.origin = origin

    @property
    def points(self):
        return self.offset_points(self.origin)

    @cache
    def offset_points(self, offset):
        return {point + offset for point in self.shape}


class Chamber:
    WIDTH = 7
    X_OFFSET = 2
    Y_OFFSET = 3
    WIND_EFFECT = {">": Point(1, 0), "<": Point(-1, 0)}

    def __init__(self, wind):
        self.wind = wind
        self.wind_index = 0
        self.max_height = 0
        self.occupied_spots = set()

    def wind_effect(self):
        effect = Chamber.WIND_EFFECT[self.wind[self.wind_index]]
        self.wind_index = (self.wind_index + 1) % len(self.wind)
        return effect

    def try_move(self, rock, move):
        old_origin = rock.origin
        rock.origin += move
        for point in rock.points:
            if self.outside_chamber(point) or point in self.occupied_spots:
                rock.origin = old_origin
                return False
        return True

    def drop_rock(self, shape):
        rock = Rock(shape, Point(Chamber.X_OFFSET, self.max_height + Chamber.Y_OFFSET))
        stopped = False
        while not stopped:
            # try to move under wind
            self.try_move(rock, self.wind_effect())

            # try to fall, stopping if not possible
            stopped = not self.try_move(rock, Point(0, -1))

        self.occupied_spots |= rock.points
        self.max_height = max(self.max_height, *(point.y + 1 for point in rock.points))

    def outside_chamber(self, point):
        return point.x < 0 or point.x >= Chamber.WIDTH or point.y < 0


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = list(file.read().strip())
    return data


def star_1(wind, number_of_rocks=2022):
    chamber = Chamber(wind)

    for rock_idx in range(number_of_rocks):
        chamber.drop_rock(ROCK_SHAPES[rock_idx % len(ROCK_SHAPES)])

    return chamber.max_height


if __name__ == "__main__":
    timer = Advent_Timer()

    wind = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(wind)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
