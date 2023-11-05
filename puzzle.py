'''Lab task 2'''

def validate_board(board: list[str]) -> bool:
    '''
    GitHub:
    https://github.com/veronasaz/sazonova-veronika-lab8-task2

    Check if the board iis valid for a game.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
" 6  83  *", "3   7  **", "  8  2***", "  2  ****"])
    True
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
" 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
" 6  83  *", "3   7  **", "  8  2***", "  3  ****"])
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

    # Checks for repetition in a block.
    n = 0
    p = 4
    while p >= 0:
        block = ''
        for j in range(0+n, 5+n):
            block += board[j][p]
        block += board[4+n][5-n:9-n]
        line_3 = ''
        for i in block:
            if i.isdigit() and i in line_3:
                return False
            line_3 += i
        n += 1
        p -= 1

    return True

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
