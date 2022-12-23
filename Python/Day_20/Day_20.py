from dataclasses import dataclass


from aoc_tools import Advent_Timer


class EncryptedData:
    @dataclass
    class Element:
        value: int
        address: int

    def __init__(self, array):
        self.data = [EncryptedData.Element(val, i) for i, val in enumerate(array)]

    def calculate_new_address(self, current_address, offset):
        return sum(divmod(current_address + offset, len(self.data))) % (len(self.data) - 1)

    def get_relative_element(self, original_idx, offset):
        wanted_address = (self.data[original_idx].address + offset) % len(self.data)
        for element in self.data:
            if element.address == wanted_address:
                return element.value
        return None

    def move(self, original_idx):
        # get current and new address of element
        current_address = self.data[original_idx].address
        new_address = self.calculate_new_address(current_address, self.data[original_idx].value)

        if new_address == current_address:
            return

        # update addresses changed by the move
        for element in self.data:
            if element.address < current_address:
                if element.address >= new_address:
                    element.address += 1
            elif element.address > current_address:
                if element.address <= new_address:
                    element.address -= 1
            else:
                element.address = new_address


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
