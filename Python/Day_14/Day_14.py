from typing import NamedTuple

from aoc_tools import Advent_Timer


class Point(NamedTuple):
    x: int
    y: int


SAND_START_POS = Point(500, 0)
FLOOR_OFFSET = 2


def points_between(point_1, point_2):
    end_points = set([point_1, point_2])
    if point_1.x != point_2.x:
        internal_points = set(Point(x, point_1.y) for x in range(*sorted((point_1.x, point_2.x))))
    else:
        internal_points = set(Point(point_1.x, y) for y in range(*sorted((point_1.y, point_2.y))))
    return end_points | internal_points


class Rock:
    def __init__(self, rock_str):
        self.vertices = [
            Point(*(int(val) for val in point.strip().split(","))) for point in rock_str.split("->")
        ]

    @property
    def occupied_points(self):
        points = set()
        for i in range(1, len(self.vertices)):
            points |= points_between(self.vertices[i - 1], self.vertices[i])
        return points


class OccupancyGrid:
    def __init__(self, rocks, has_floor=False):
        self.occupied_cells = set.union(*(rock.occupied_points for rock in rocks))
        self.has_floor = has_floor
        self.lowest_point = max(cell.y for cell in self.occupied_cells) + FLOOR_OFFSET * has_floor

    def is_occupied(self, point):
        return point in self.occupied_cells or (self.has_floor and point.y == self.lowest_point)


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [Rock(line) for line in file]
    return data


def drop_sand(grid):
    sand_pos = SAND_START_POS
    while sand_pos.y < grid.lowest_point:

        # try going down
        trial_pos = Point(sand_pos.x, sand_pos.y + 1)
        if not grid.is_occupied(trial_pos):
            sand_pos = trial_pos
            continue

        # try going left
        trial_pos = Point(sand_pos.x - 1, sand_pos.y + 1)
        if not grid.is_occupied(trial_pos):
            sand_pos = trial_pos
            continue

        # try going right
        trial_pos = Point(sand_pos.x + 1, sand_pos.y + 1)
        if not grid.is_occupied(trial_pos):
            sand_pos = trial_pos
            continue

        # sand settled
        grid.occupied_cells.add(sand_pos)
        return True

    return False  # sand didn't come to rest


def star_1(rocks):
    grid = OccupancyGrid(rocks)
    count = 0
    while drop_sand(grid):
        count += 1
    return count


def star_2(rocks):
    grid = OccupancyGrid(rocks, has_floor=True)
    count = 0
    while SAND_START_POS not in grid.occupied_cells:
        drop_sand(grid)
        count += 1
    return count


if __name__ == "__main__":
    timer = Advent_Timer()

    rocks = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(rocks)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(rocks)}")
    timer.checkpoint_hit()

    timer.end_hit()
