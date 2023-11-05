'''Lab task 2'''

def validate_board(board: list[str]) -> bool:
    '''Check if the board iis valid for a game.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    # Checks for repetition in a string.
    for item in board:
        line_1 = ''
        for j in item:
            if j.isdigit() and j in line_1:
                return False
            line_1 += j

    # Checks for repetition in a column.
    for i in range(len(board[0])):
        column = [board[item][i] for item in range(9)]
        line_2 = ''
        for j in column:
            if j.isdigit() and j in line_2:
                return False
            line_2 += j

    return True

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
