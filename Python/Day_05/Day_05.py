from re import compile as comp

from aoc_tools import Advent_Timer


MOVE_REGEX = comp(r"move (\d+) from (\d+) to (\d+)")


class Stacks:
    def __init__(self, initial_stacks_str):
        self._stacks = None
        self._load_initial_stacks(initial_stacks_str)

    def _load_initial_stacks(self, initial_stacks_str):
        stack_labels = initial_stacks_str[-1].split()
        self._stacks = {label: [] for label in stack_labels}
        for row_str in reversed(initial_stacks_str[:-1]):
            for i, stack_label in enumerate(stack_labels):
                crate = row_str[1 + 4 * i]
                if crate != " ":
                    self._stacks[stack_label].append(crate)

    @staticmethod
    def _parse_row(row_str, num_of_crates):
        row = [None] * num_of_crates
        for i in range(num_of_crates):
            crate = row_str[1 + 4 * i]
            if crate != " ":
                row[i] = crate

    def make_move(self, move_str, move_multiple_at_once):
        num, source, destination = MOVE_REGEX.match(move_str).groups()
        if move_multiple_at_once:
            self._move_multiple_at_once(int(num), source, destination)
        else:
            self._move_one_at_a_time(int(num), source, destination)

    def _move_one_at_a_time(self, num, source, destination):
        for _ in range(num):
            self._stacks[destination].append(self._stacks[source].pop())

    def _move_multiple_at_once(self, num, source, destination):
        self._stacks[destination] += self._stacks[source][-num:]
        del self._stacks[source][-num:]

    @property
    def top_vals(self):
        return "".join(stack[-1] for stack in self._stacks.values())

    def __str__(self):
        return "\n".join(f"{key}: {value}" for key, value in self._stacks.items())


def read_data(input_file="input.txt"):
    initial_stacks = []
    with open(input_file, "r") as file:
        while line := file.readline().rstrip("\n"):
            initial_stacks.append(line)
        moves = file.read().splitlines()
    return initial_stacks, moves


def apply_all_moves(initial_stacks, moves, move_multiple_at_once=False):
    stacks = Stacks(initial_stacks)
    for move in moves:
        stacks.make_move(move, move_multiple_at_once)
    return stacks.top_vals


if __name__ == "__main__":
    timer = Advent_Timer()

    initial_stacks, moves = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {apply_all_moves(initial_stacks, moves)}")
    timer.checkpoint_hit()

    print(f"Star_02: {apply_all_moves(initial_stacks, moves, True)}")
    timer.checkpoint_hit()

    timer.end_hit()
