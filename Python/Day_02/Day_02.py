from aoc_tools import Advent_Timer

LOSS_POINTS = 0
DRAW_POINTS = 3
WIN_POINTS = 6
SHAPE_POINTS = {"ROCK": 1, "PAPER": 2, "SCISSORS": 3}
OPPONENT_MOVE = {"A": "ROCK", "B": "PAPER", "C": "SCISSORS"}
YOUR_MOVE = {"X": "ROCK", "Y": "PAPER", "Z": "SCISSORS"}
OUTCOME_POINTS = {
    ("ROCK", "ROCK"): DRAW_POINTS,
    ("ROCK", "PAPER"): WIN_POINTS,
    ("ROCK", "SCISSORS"): LOSS_POINTS,
    ("PAPER", "ROCK"): LOSS_POINTS,
    ("PAPER", "PAPER"): DRAW_POINTS,
    ("PAPER", "SCISSORS"): WIN_POINTS,
    ("SCISSORS", "ROCK"): WIN_POINTS,
    ("SCISSORS", "PAPER"): LOSS_POINTS,
    ("SCISSORS", "SCISSORS"): DRAW_POINTS,
}
SHAPE_TO_CHOOSE = {
    ("ROCK", "X"): "SCISSORS",
    ("ROCK", "Y"): "ROCK",
    ("ROCK", "Z"): "PAPER",
    ("PAPER", "X"): "ROCK",
    ("PAPER", "Y"): "PAPER",
    ("PAPER", "Z"): "SCISSORS",
    ("SCISSORS", "X"): "PAPER",
    ("SCISSORS", "Y"): "SCISSORS",
    ("SCISSORS", "Z"): "ROCK",
}


def read_data(input_file="input.txt"):
    with open(input_file, "r") as file:
        strategy = [line.strip().split() for line in file]
    return strategy


def calculate_round_score(moves):
    _, your_move = moves
    return SHAPE_POINTS[your_move] + OUTCOME_POINTS[moves]


def star_1_strategy_parser(move_codes):
    their_code, your_code = move_codes
    return (OPPONENT_MOVE[their_code], YOUR_MOVE[your_code])


def star_2_strategy_parser(move_codes):
    their_code, your_code = move_codes
    return (OPPONENT_MOVE[their_code], SHAPE_TO_CHOOSE[(OPPONENT_MOVE[their_code], your_code)])


def calculate_overall_score(strategy, strategy_parser):
    set_of_moves = [strategy_parser(move_codes) for move_codes in strategy]
    return sum(calculate_round_score(moves) for moves in set_of_moves)


if __name__ == "__main__":
    timer = Advent_Timer()

    strategy = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    Star_01 = calculate_overall_score(strategy, star_1_strategy_parser)
    print(f"Star_01: {Star_01}")
    timer.checkpoint_hit()

    Star_02 = calculate_overall_score(strategy, star_2_strategy_parser)
    print(f"Star_02: {Star_02}")
    timer.checkpoint_hit()

    timer.end_hit()
