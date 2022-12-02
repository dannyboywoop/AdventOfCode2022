from aoc_tools import Advent_Timer


def read_data(input_file="input.txt"):
    with open(input_file, 'r') as file:
        pass
    return data


if __name__ == "__main__":
    timer = Advent_Timer()
    
    data = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
