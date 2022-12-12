from re import compile as comp
from copy import deepcopy
from math import lcm
from collections import deque

from aoc_tools import Advent_Timer


STARTING_REGEX = comp(r"Starting items: (?P<items>[\d,\s]+)")
OPERATION_REGEX = comp(r"Operation: new = (?P<op>[old\d\+\*\s]+)")
TEST_REGEX = comp(r"Test: divisible by (?P<divisor>\d+)")
THROW_REGEX = comp(r"If (?:true|false): throw to monkey (?P<monkey>\d+)")


class MonkeyManager:
    def __init__(self):
        self.monkeys = []

    def throw_item(self, item, monkey_id):
        self.monkeys[monkey_id].items.append(item)

    def perform_rounds(self, num_of_rounds):
        for _ in range(num_of_rounds):
            for monkey in self.monkeys:
                monkey.inspect_items()

    @property
    def monkey_activity(self):
        return [monkey.inspection_count for monkey in self.monkeys]

    def __str__(self):
        string = ""
        for i, monkey in enumerate(self.monkeys):
            string += f"Monkey {i}: {monkey.items}\n"
        return string


class Monkey:
    WORRY_REDUCTION_METHOD = lambda x: x // 3

    def __init__(self, input_string, monkey_manager):
        (_, starting_line, operation_line, test_line, if_true_line, if_false_line) = [
            string.strip() for string in input_string.split("\n")
        ]
        self.items = deque(
            int(item) for item in STARTING_REGEX.match(starting_line)["items"].split(", ")
        )
        self.operation = lambda x: eval(
            OPERATION_REGEX.match(operation_line)["op"], None, {"old": x}
        )
        self.divisor = int(TEST_REGEX.match(test_line)["divisor"])
        self.throw_to = {
            True: int(THROW_REGEX.match(if_true_line)["monkey"]),
            False: int(THROW_REGEX.match(if_false_line)["monkey"]),
        }
        self.monkey_manager = monkey_manager
        self.inspection_count = 0

    def inspect_items(self):
        while self.items:
            self._inspect_item(self.items.popleft())
            self.inspection_count += 1

    def _inspect_item(self, value):
        value = self.operation(value)
        value = Monkey.WORRY_REDUCTION_METHOD(value)
        self.monkey_manager.throw_item(value, self.throw_to[self._test(value)])

    def _test(self, value):
        return value % self.divisor == 0


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        manager = MonkeyManager()
        manager.monkeys = [Monkey(monkey, manager) for monkey in file.read().split("\n\n")]
    return manager


def star_01(manager):
    manager.perform_rounds(20)
    activity = sorted(manager.monkey_activity)
    return activity[-1] * activity[-2]


def star_02(manager):
    lowest_common_multiple = lcm(*(monkey.divisor for monkey in manager.monkeys))
    Monkey.WORRY_REDUCTION_METHOD = lambda x: x % lowest_common_multiple
    manager.perform_rounds(10000)
    activity = sorted(manager.monkey_activity)
    return activity[-1] * activity[-2]


if __name__ == "__main__":
    timer = Advent_Timer()

    manager = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_01(deepcopy(manager))}")
    timer.checkpoint_hit()

    print(f"Star_02: {star_02(deepcopy(manager))}")
    timer.checkpoint_hit()

    timer.end_hit()
