from aoc_tools import Advent_Timer


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = file.read().strip()
    return data


def find_start_of_packet_marker(data, marker_len=4):
    for i in range(marker_len, len(data) + 1):
        # Rather than building a set each time, you could use a Counter and
        # increment/decrement based on the moving window. That would be faster
        # in theory, and is O(1) rather than O(N) w.r.t. marker_len, but in
        # practice the overheads of the python Counter implementation eat up
        # any speed gains at this scale of marker_len.
        if len(set(data[i - marker_len : i])) == marker_len:
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
