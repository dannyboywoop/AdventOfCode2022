from aoc_tools import Advent_Timer


class CPU:
    def __init__(self, program):
        self.x = 1
        self.program = program
        self._execution_pointer = 0
        self._delay = False

    def run_cycle(self):
        if self.program[self._execution_pointer] == "noop":
            self._execution_pointer += 1
        elif self._delay:
            _, delta_x = self.program[self._execution_pointer].split()
            self.x += int(delta_x)
            self._delay = False
            self._execution_pointer += 1
        else:
            self._delay = True


class CRT:
    NUMBER_OF_ROWS = 6
    NUMBER_OF_COLS = 40

    def __init__(self):
        self.pixels = [[" "] * CRT.NUMBER_OF_COLS for _ in range(CRT.NUMBER_OF_ROWS)]
        self.beam_pos = 0

    def run_cycle(self, sprite_pos):
        row, col = divmod(self.beam_pos, CRT.NUMBER_OF_COLS)
        self.pixels[row][col] = "#" if abs(sprite_pos - col) <= 1 else "."
        self.beam_pos += 1

    def pretty_print(self):
        for row in range(CRT.NUMBER_OF_ROWS):
            print("".join(self.pixels[row]))


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [line.strip() for line in file]
    return data


def star_1(program):
    cpu = CPU(program)
    crt = CRT()
    total = 0
    cycles_to_record = set([20, 60, 100, 140, 180, 220])
    for cycle in range(1, 241):
        if cycle in cycles_to_record:
            total += cycle * cpu.x
        crt.run_cycle(cpu.x)
        cpu.run_cycle()
    crt.pretty_print()
    return total


if __name__ == "__main__":
    timer = Advent_Timer()

    program = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_1(program)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
