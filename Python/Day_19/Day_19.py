from re import compile as comp
from dataclasses import dataclass
from typing import TypeAlias
from enum import Enum
from collections import Counter

from aoc_tools import Advent_Timer

BLUEPRINT_REGEX = comp(
    r"Blueprint (?P<num>\d+): "
    + r"Each ore robot costs (?P<ore_robot_ore>\d+) ore\. "
    + r"Each clay robot costs (?P<clay_robot_ore>\d+) ore\. "
    + r"Each obsidian robot costs (?P<obsidian_robot_ore>\d+) ore and (?P<obsidian_robot_clay>\d+) clay\. "
    + r"Each geode robot costs (?P<geode_robot_ore>\d+) ore and (?P<geode_robot_obsidian>\d+) obsidian\."
)


class ResourceType(Enum):
    ORE = 1
    CLAY = 2
    OBSIDIAN = 3
    GEODE = 4


Resources: TypeAlias = dict[ResourceType, int]


@dataclass
class Blueprint:
    id: int
    robot_costs: dict[ResourceType, Resources]

    def __init__(self, blueprint_str):
        match = BLUEPRINT_REGEX.match(blueprint_str)
        self.id = int(match["num"])
        self.robot_costs = {
            ResourceType.CLAY: Counter({ResourceType.ORE: int(match["clay_robot_ore"])}),
            ResourceType.ORE: Counter({ResourceType.ORE: int(match["ore_robot_ore"])}),
            ResourceType.OBSIDIAN: Counter(
                {
                    ResourceType.ORE: int(match["obsidian_robot_ore"]),
                    ResourceType.CLAY: int(match["obsidian_robot_clay"]),
                }
            ),
            ResourceType.GEODE: Counter(
                {
                    ResourceType.ORE: int(match["geode_robot_ore"]),
                    ResourceType.OBSIDIAN: int(match["geode_robot_obsidian"]),
                }
            ),
        }
        self.branch_count = 0

    def available_robots(self, resources):
        return [
            robot
            for robot, costs in self.robot_costs.items()
            if all(resources[resource] >= costs[resource] for resource in costs)
        ]

    def result_of_building_robot(self, robot_to_build, current_resources, current_robots, minutes):
        resources = current_resources.copy()
        robots = current_robots.copy()
        new_robot_built = False
        while minutes > 0 and not new_robot_built:
            if robot_to_build in self.available_robots(resources):
                new_robot_built = True
                robots[robot_to_build] += 1
                resources -= self.robot_costs[robot_to_build]
            resources += current_robots
            minutes -= 1

        return resources, robots, minutes

    def potential_geodes(self, minutes=24, resources=None, robots=None):
        self.branch_count += 1
        # initialize
        if resources is None:
            resources = Counter()
        if robots is None:
            robots = Counter({ResourceType.ORE: 1})

        # break recursion
        if minutes == 0:
            return resources[ResourceType.GEODE]

        max_geodes = 0
        for robot_to_build in self.robot_costs:
            new_resources, new_robots, new_minutes = self.result_of_building_robot(
                robot_to_build, resources, robots, minutes
            )
            max_geodes = max(
                max_geodes, self.potential_geodes(new_minutes, new_resources, new_robots)
            )
        return max_geodes


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [Blueprint(line) for line in file]
    return data


def star_1(blueprints):
    for blueprint in blueprints:
        print(f"Blueprint {blueprint.id}:")
        max_geodes = blueprint.potential_geodes()
        print(max_geodes)


if __name__ == "__main__":
    timer = Advent_Timer()

    blueprints = read_data("test_input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(blueprints)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
