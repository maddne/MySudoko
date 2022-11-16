from request_board import choose_difficulty
from outlook import visual
from main_logic import solve


board, difficulty = choose_difficulty()


if __name__ == '__main__':
    print(f"Printing a random {difficulty} mode Sudoku.")
    visual(board)
    solve(board)
    print(f"Printing the solved Sudoku.")
    visual(board)