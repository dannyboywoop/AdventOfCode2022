from aoc_tools import Advent_Timer


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = file.read().strip()
    return data


def all_unique_chars(chars):
    return len(chars) == len(set(chars))


def find_start_of_packet_marker(data, marker_len=4):
    for i in range(marker_len, len(data) + 1):
        chars = data[i - marker_len : i]
        if all_unique_chars(chars):
            return i


if __name__ == "__main__":
    timer = Advent_Timer()

    data = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {find_start_of_packet_marker(data)}")
    timer.checkpoint_hit()

    print(f"Star_02: {find_start_of_packet_marker(data, 14)}")
    timer.checkpoint_hit()

    timer.end_hit()
