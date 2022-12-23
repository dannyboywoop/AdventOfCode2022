from dataclasses import dataclass


from aoc_tools import Advent_Timer


class EncryptedData:
    @dataclass
    class Element:
        value: int
        address_table_key: int

    def __init__(self, array):
        self.address_table = {i: i for i in range(len(data))}
        self.current_data = [EncryptedData.Element(val, i) for i, val in enumerate(array)]

    def calculate_new_idx(self, current_idx, offset):
        return sum(divmod(current_idx + offset, len(self.current_data))) % (
            len(self.current_data) - 1
        )

    def get_relative_element(self, address_table_key, offset):
        return self.current_data[
            (self.address_table[address_table_key] + offset) % len(self.current_data)
        ].value

    def move(self, original_idx):
        # get current and new idx of element
        current_idx = self.address_table[original_idx]
        new_idx = self.calculate_new_idx(current_idx, self.current_data[current_idx].value)

        if new_idx == current_idx:
            return

        # move element in current_data, inefficient but life's too short
        element = self.current_data.pop(current_idx)
        self.current_data = self.current_data[:new_idx] + [element] + self.current_data[new_idx:]

        # update element addresses
        self.update_address_table()

    def update_address_table(self):
        for idx, element in enumerate(self.current_data):
            self.address_table[element.address_table_key] = idx

    def __str__(self):
        return str([element.value for element in self.current_data])

    def to_array(self):
        return [element.value for element in self.current_data]


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [int(line.strip()) for line in file]
    return data


def star_1(data):
    encrypted_data = EncryptedData(data)

    # mix file
    for i in range(len(data)):
        encrypted_data.move(i)

    # find grove coordinates
    zero_element = data.index(0)
    return sum(
        encrypted_data.get_relative_element(zero_element, offset) for offset in [1000, 2000, 3000]
    )


def star_2(data, decryption_key=811589153):
    new_data = [val * decryption_key for val in data]
    encrypted_data = EncryptedData(new_data)

    # mix file 10 times
    for _ in range(10):
        for i in range(len(new_data)):
            encrypted_data.move(i)

    # find grove coordinates
    zero_element = new_data.index(0)
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

    print(f"Star_2: {star_2(data)}")
    timer.checkpoint_hit()

    timer.end_hit()
