from dataclasses import dataclass

from aoc_tools import Advent_Timer


class CircularDoubleLinkedList:
    @dataclass
    class Element:
        value: int
        previous_element: int
        next_element: int

    def __init__(self, array):
        self.data = {
            i: CircularDoubleLinkedList.Element(val, (i - 1) % len(array), (i + 1) % len(array))
            for i, val in enumerate(array)
        }

    def find_relative_element(self, element, offset):
        relative_element = element
        if offset < 0:
            for _ in range(1 - offset):
                relative_element = self.data[relative_element].previous_element
        else:
            for _ in range(offset):
                relative_element = self.data[relative_element].next_element
        return relative_element

    def get_relative_element(self, element, offset):
        return self.data[self.find_relative_element(element, offset)].value

    def pop(self, element):
        previous_element = self.data[element].previous_element
        next_element = self.data[element].next_element
        self.data[previous_element].next_element = next_element
        self.data[next_element].previous_element = previous_element

    def insert(self, element, position):
        temp = self.data[position].next_element
        self.data[position].next_element = element
        self.data[element].previous_element = position
        self.data[element].next_element = temp
        self.data[temp].previous_element = element

    def move(self, element, offset):
        if offset == 0:
            return
        self.pop(element)
        new_position = self.find_relative_element(element, offset)
        self.insert(element, new_position)

    def __str__(self):
        values = [self.data[0].value]
        element = self.data[0].next_element
        while element != 0:
            values.append(self.data[element].value)
            element = self.data[element].next_element
        return ", ".join(str(value) for value in values)


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [int(line.strip()) for line in file]
    return data


def star_1(data):
    encrypted_data = CircularDoubleLinkedList(data)

    # mix file
    for i, val in enumerate(data):
        encrypted_data.move(i, val)

    # find grove coordinates
    zero_element = data.index(0)
    return sum(
        encrypted_data.get_relative_element(zero_element, offset) for offset in [1000, 2000, 3000]
    )


if __name__ == "__main__":
    timer = Advent_Timer()

    data = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_1: {star_1(data)}")
    timer.checkpoint_hit()

    timer.checkpoint_hit()

    timer.end_hit()
