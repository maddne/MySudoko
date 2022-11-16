from math import ceil


def find_empty_pos(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c

    return None, None


def locate_num(row, col, board):
    """
    # To locate and print a 3x3 subgrid, the row and the column of a given position.
    """

    sub_board_of_interest = []
    row_min, row_max = get_nearest_values(row)
    col_min, col_max = get_nearest_values(col)

    for line in range(9):
        if row_min <= line < row_max:
            sub_board_of_interest.append(board[line][col_min:col_max])

    sub_board_as_list = [val for sublist in sub_board_of_interest for val in sublist]
    row_as_list = board[row]
    col_as_list = [(row[col]) for row in board]

    return row_as_list, col_as_list, sub_board_as_list


def get_nearest_values(index):
    roundup_max_float = ceil((index + 1) / 3) * 3
    roundup_max_int = int(roundup_max_float)

    if roundup_max_int <= 3:
        roundup_min_int = 0
    elif roundup_max_int <= 6:
        roundup_min_int = 3
    else:
        roundup_min_int = 6

    return roundup_min_int, roundup_max_int


def find_possible_nums(row, col, board):
    """
    Find uniqs in 3x3, row and column
    """
    target_row, target_col, sub_board = locate_num(row, col, board)

    all_uniques = set(target_row + target_col + sub_board)
    potential_values = [int(num) for num in range(10) if num not in all_uniques]

    return potential_values


def solve(board):
    # check for empty spaces, if none left, stop solving by returning True
    row, col = find_empty_pos(board)
    if row is None:
        return True

    potential_values = find_possible_nums(row, col, board)

    # try to finish the game with guessing from possible variants
    for num in potential_values:
        # wild guess and check whether it is valid
        board[row][col] = num
        # continue solving with the wild guess.
        if solve(board):
            return True

        # if wrong, backtrack and try next potential value
        board[row][col] = 0

    return False

