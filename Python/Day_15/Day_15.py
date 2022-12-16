from re import compile as comp
from typing import NamedTuple
from dataclasses import dataclass

from aoc_tools import Advent_Timer


SENSOR_REGEX = comp(
    r"Sensor at x=(?P<sensor_x>\-?\d+), y=(?P<sensor_y>\-?\d+): "
    + r"closest beacon is at x=(?P<beacon_x>\-?\d+), y=(?P<beacon_y>\-?\d+)"
)
FREQUENCY_MULTIPLIER = 4000000


class Position(NamedTuple):
    x: int
    y: int


@dataclass
class Sensor:
    position: Position
    nearest_beacon: Position
    distance_to_beacon: int

    def __init__(self, sensor_str):
        match = SENSOR_REGEX.match(sensor_str)
        self.position = Position(int(match["sensor_x"]), int(match["sensor_y"]))
        self.nearest_beacon = Position(int(match["beacon_x"]), int(match["beacon_y"]))
        self.distance_to_beacon = manhattan_distance(self.position, self.nearest_beacon)


def manhattan_distance(pos_1, pos_2):
    return abs(pos_2.x - pos_1.x) + abs(pos_2.y - pos_1.y)


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [Sensor(line.strip()) for line in file]
    return data


def reduce_ranges(ranges):
    """Takes a set of unsorted, potentially-overlapping ranges and returns
    the simplest set of (non-overlapping) ranges that cover the same points.
    Ranges are inclusive."""
    sorted_ranges = sorted(ranges)
    reduced_ranges = [sorted_ranges[0]]
    for i in range(1, len(sorted_ranges)):
        new_low, new_high = sorted_ranges[i]
        _, old_high = reduced_ranges[-1]
        if new_low <= old_high + 1:
            reduced_ranges[-1][1] = max(old_high, new_high)
        else:
            reduced_ranges.append(sorted_ranges[i])
    return reduced_ranges


def points_in_ranges(ranges):
    if not ranges:
        return 0

    num_of_points = 0
    # The easier method is to just convert these to sets and take the length of the union.
    # This method is much faster though (fixed time w.r.t the length of the ranges)
    for lower, upper in reduce_ranges(ranges):
        num_of_points += upper - lower + 1

    return num_of_points


def x_ranges_blocked_in_row(sensors, y_to_check):
    blocked_ranges = []
    for sensor in sensors:
        abs_delta_y = abs(sensor.position.y - y_to_check)
        if sensor.distance_to_beacon < abs_delta_y:
            continue
        delta_x = sensor.distance_to_beacon - abs_delta_y
        blocked_ranges.append([sensor.position.x - delta_x, sensor.position.x + delta_x])
    return blocked_ranges


def star_1(sensors, y_to_check=2000000):
    beacons_on_row = set(
        sensor.nearest_beacon for sensor in sensors if sensor.nearest_beacon.y == y_to_check
    )
    blocked_ranges = x_ranges_blocked_in_row(sensors, y_to_check)
    return points_in_ranges(blocked_ranges) - len(beacons_on_row)


def star_2(sensors, max_xy=4000000):
    # There has got to be a better way than this brute-force method
    for y in range(max_xy):
        blocked_ranges = reduce_ranges(x_ranges_blocked_in_row(sensors, y))

        # check any gaps
        for i in range(1, len(blocked_ranges)):
            x = blocked_ranges[i][0] - 1
            if 0 <= x <= max_xy:
                return x * FREQUENCY_MULTIPLIER + y

    return None


if __name__ == "__main__":
    timer = Advent_Timer()

    sensors = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(sensors)}")
    timer.checkpoint_hit()

    print(f"Star_2: {star_2(sensors)}")
    timer.checkpoint_hit()

    timer.end_hit()
