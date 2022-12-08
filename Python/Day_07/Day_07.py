from __future__ import annotations
from re import compile as comp
from dataclasses import dataclass, field
from typing import Optional

from aoc_tools import Advent_Timer


CD_COMMAND_REGEX = comp(r"\$ cd (?P<dir>[\w\/\.]+)")
LS_COMMAND_REGEX = comp(r"\$ ls")
DIR_REGEX = comp(r"dir (?P<dir>[\w\/]+)")
FILE_REGEX = comp(r"(?P<size>\d+) (?P<name>[\w\.]+)")

DIRECTORIES: dict[str, Directory] = {}


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    files: list[File] = field(default_factory=list)
    sub_dir_names: list[str] = field(default_factory=list)
    _size: Optional[int] = None

    @property
    def size(self):
        if self._size is None:
            self._size = sum(file.size for file in self.files)
            self._size += sum(DIRECTORIES[sub_dir_name].size for sub_dir_name in self.sub_dir_names)

        return self._size


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        terminal_output = [line.strip() for line in file]
    return terminal_output


def parse_terminal_output(terminal_output):
    current_dir = []
    for line in terminal_output:
        if match := LS_COMMAND_REGEX.match(line):
            continue  # do nothing

        if match := CD_COMMAND_REGEX.match(line):
            dir_name = match["dir"]
            if dir_name == "..":
                current_dir.pop()
            else:
                current_dir.append(dir_name)
                if dir_name not in DIRECTORIES:
                    DIRECTORIES[dir_name] = Directory()

        elif match := DIR_REGEX.match(line):
            DIRECTORIES[current_dir[-1]].sub_dir_names.append(match["dir"])

        elif match := FILE_REGEX.match(line):
            DIRECTORIES[current_dir[-1]].files.append(File(match["name"], int(match["size"])))


def star_1(terminal_output, max_size=100000):
    total = 0
    parse_terminal_output(terminal_output)
    for directory in DIRECTORIES.values():
        if directory.size <= max_size:
            total += directory.size
    return total


if __name__ == "__main__":
    timer = Advent_Timer()

    terminal_output = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_1(terminal_output)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
