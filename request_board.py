import requests


def request_board(difficulty):

    mode = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={difficulty}")

    return mode


def choose_difficulty():
    selected_difficulty = input("Select difficulty: ")
    possible = ['easy', 'medium', 'hard', 'random']

    if selected_difficulty.lower() not in possible:
        raise ValueError("You need to select either 'easy', 'medium', 'hard' or 'random'")

    grid = request_board(selected_difficulty).json()['board']

    return grid, selected_difficulty
