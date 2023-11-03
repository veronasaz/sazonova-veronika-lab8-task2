'''Task 2'''

def validate_board(board: list[str]) -> bool:
    '''Check if the board iis valid for a game.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", \
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    # Checks for repetition in a string.
    for item in board:
        line = ''
        for j in item:
            if j in line:
                return False
            if not j in ('*', ' '):
                line += j
    return True

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
