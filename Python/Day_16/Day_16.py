from re import compile as comp
from dataclasses import dataclass
from queue import PriorityQueue
from math import inf
from functools import cache

from aoc_tools import Advent_Timer

VALVE_REGEX = comp(
    r"Valve (?P<name>[A-Z]{2}) has flow rate=(?P<rate>\d+); "
    + r"tunnels? leads? to valves? (?P<tunnels>[A-Z, ]+)"
)


@dataclass
class Valve:
    flow_rate: int
    tunnels: set[str]


class PathPlanner:
    def __init__(self, valves):
        self.valves = valves
        self.non_zero_valves = set(name for name, valve in valves.items() if valve.flow_rate > 0)
        self.best_paths = {valve: self.find_best_paths(valve) for valve in valves}

    def find_best_paths(self, start_valve):
        """Dijkstra to find best path length from start_valve to all other valves"""
        open_set = PriorityQueue()
        best_path_length = {start_valve: 0}

        open_set.put((best_path_length[start_valve], start_valve))

        while not open_set.empty():
            current = open_set.get()[1]

            for neighbour in self.valves[current].tunnels:
                path_length_to_neighbour_via_current = best_path_length[current] + 1
                if path_length_to_neighbour_via_current < best_path_length.get(neighbour, inf):
                    best_path_length[neighbour] = path_length_to_neighbour_via_current
                    open_set.put((best_path_length[neighbour], neighbour))
        return best_path_length

    @cache
    def result_of_opening(self, current_valve, valve_to_open, time_remaining):
        """Calculate the resultant pressure release and time remaining after moving to and opening a valve."""
        new_time_remaining = max(
            time_remaining - self.best_paths[current_valve][valve_to_open] - 1, 0
        )
        return (new_time_remaining * self.valves[valve_to_open].flow_rate, new_time_remaining)

    def best_pressure_release(self, remaining_valves: set, current_valve="AA", time_remaining=30):
        if time_remaining == 0 or not remaining_valves:
            return 0

        max_pressure = 0
        for valve_checked in remaining_valves:
            pressure_released, new_time_remaining = self.result_of_opening(
                current_valve, valve_checked, time_remaining
            )
            max_pressure = max(
                max_pressure,
                pressure_released
                + self.best_pressure_release(
                    remaining_valves.copy().difference(set([valve_checked])),
                    valve_checked,
                    new_time_remaining,
                ),
            )

        return max_pressure


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        valves = {}
        for line in file:
            match = VALVE_REGEX.match(line)
            valves[match["name"]] = Valve(int(match["rate"]), set(match["tunnels"].split(", ")))
    return valves


def star_1(valves):
    planner = PathPlanner(valves)
    return planner.best_pressure_release(planner.non_zero_valves)


if __name__ == "__main__":
    timer = Advent_Timer()

    valves = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(valves)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
