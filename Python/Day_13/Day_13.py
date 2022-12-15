from enum import IntEnum
from numpy import sign

from aoc_tools import Advent_Timer


class Comparison(IntEnum):
    LESS_THAN = -1
    EQUAL = 0
    MORE_THAN = 1


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [
            tuple(eval(item) for item in lines.split("\n")) for lines in file.read().split("\n\n")
        ]
    return data


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return Comparison(sign(left - right))

    if isinstance(left, int):
        return compare([left], right)

    if isinstance(right, int):
        return compare(left, [right])

    for i in range(min(len(left), len(right))):
        comparison = compare(left[i], right[i])
        if comparison != Comparison.EQUAL:
            return comparison

    return compare(len(left), len(right))


def star_1(pairs):
    total = 0
    for i, (left, right) in enumerate(pairs):
        if compare(left, right) == Comparison.LESS_THAN:
            total += i + 1
    return total


def find_index(packet_to_find, packets):
    index = 1
    for packet in packets:
        if compare(packet, packet_to_find) == Comparison.LESS_THAN:
            index += 1
    return index


def star_2(pairs):
    packets = [item for pair in pairs for item in pair]
    decoder_packets = ([[2]], [[6]])
    for decoder_packet in decoder_packets:
        packets.append(decoder_packet)

    decoder_key = 1
    for decoder_packet in decoder_packets:
        decoder_key *= find_index(decoder_packet, packets)
    return decoder_key


if __name__ == "__main__":
    timer = Advent_Timer()

    pairs = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_1(pairs)}")
    timer.checkpoint_hit()

    print(f"Star_02: {star_2(pairs)}")
    timer.checkpoint_hit()

    timer.end_hit()
