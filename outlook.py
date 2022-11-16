def visual(grid):
    """
    Prints the 9x9 matrix for better visualization
    """
    up_down_separator = "-" * 25
    print(up_down_separator)

    for i in range(1, 10):
        row = [str(_) for _ in grid[i - 1]]

        print('| ' + ' '.join(row[0:3]) + ' | ' + ' '.join(row[3:6]) + ' | ' + ' '.join(row[6:]) + ' |')

        if i % 3 == 0:
            print(up_down_separator)
