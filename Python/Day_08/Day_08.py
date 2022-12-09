from aoc_tools import Advent_Timer


MAX_TREE_HEIGHT = 9
DIRECTIONS = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        data = [[int(x) for x in line.strip()] for line in file]
    return data


def star_1(tree_heights):
    # I could simplify this but I can't be bothered.
    visible_tree_indices = set()
    num_of_rows = len(tree_heights)
    num_of_cols = len(tree_heights[0])

    for row in range(num_of_rows):
        # check from left
        highest_tree = -1
        for col in range(num_of_cols):
            if tree_heights[row][col] > highest_tree:
                highest_tree = tree_heights[row][col]
                visible_tree_indices.add((row, col))
                if highest_tree == MAX_TREE_HEIGHT:
                    break

        # check from right
        highest_tree = -1
        for col in reversed(range(num_of_cols)):
            if tree_heights[row][col] > highest_tree:
                highest_tree = tree_heights[row][col]
                visible_tree_indices.add((row, col))
                if highest_tree == MAX_TREE_HEIGHT:
                    break

    for col in range(num_of_cols):
        # check from top
        highest_tree = -1
        for row in range(num_of_rows):
            if tree_heights[row][col] > highest_tree:
                highest_tree = tree_heights[row][col]
                visible_tree_indices.add((row, col))
                if highest_tree == MAX_TREE_HEIGHT:
                    break

        # check from bottom
        highest_tree = -1
        for row in reversed(range(num_of_rows)):
            if tree_heights[row][col] > highest_tree:
                highest_tree = tree_heights[row][col]
                visible_tree_indices.add((row, col))
                if highest_tree == MAX_TREE_HEIGHT:
                    break

    return len(visible_tree_indices)


def calculate_scenic_score(tree_heights, row, col):
    # I could simplify this but I can't be bothered.
    num_of_rows = len(tree_heights)
    num_of_cols = len(tree_heights[0])

    right_view = 0
    for j in range(1, num_of_cols - col):
        right_view += 1
        if tree_heights[row][col + j] >= tree_heights[row][col]:
            break

    left_view = 0
    for j in range(1, col + 1):
        left_view += 1
        if tree_heights[row][col - j] >= tree_heights[row][col]:
            break

    up_view = 0
    for i in range(1, row + 1):
        up_view += 1
        if tree_heights[row - i][col] >= tree_heights[row][col]:
            break

    down_view = 0
    for i in range(1, num_of_rows - row):
        down_view += 1
        if tree_heights[row + i][col] >= tree_heights[row][col]:
            break

    return up_view * down_view * right_view * left_view


def star_2(tree_heights):
    num_of_rows = len(tree_heights)
    num_of_cols = len(tree_heights[0])

    max_score = -1
    for row in range(1, num_of_rows - 1):
        for col in range(1, num_of_cols - 1):
            max_score = max(max_score, calculate_scenic_score(tree_heights, row, col))

    return max_score


if __name__ == "__main__":
    timer = Advent_Timer()

    tree_heights = read_data("input.txt")
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_1(tree_heights)}")
    timer.checkpoint_hit()

    print(f"Star_02: {star_2(tree_heights)}")
    timer.checkpoint_hit()

    timer.end_hit()
