def print_board(board):
    for row in board:
        print(''.join(row))
    print()


def can_place_queen(row, col, rows, cols, LD, RD):
    if row in rows:
        return False
    if col in cols:
        return False
    if row + col in RD:
        return False
    if row - col in LD:
        return False

    return True


def set_queen(row, col, board, rows, cols, LD, RD):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    LD.add(row - col)
    RD.add(row + col)


def remove_queens(row, col, board, rows, cols, LD, RD):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    LD.remove(row - col)
    RD.remove(row + col)


def put_queens(row, board, rows, cols, LD, RD):
    if row == 8:
        print(board)
        return
    for col in range(8):
        if can_place_queen(row, col):
            set_queen(row, col, board, rows, cols, LD, RD)
            put_queens(row + 1, board, rows, cols, LD, RD)
            remove_queens(row, col, board, rows, cols, LD, RD)




n = 8
board = []
[board.append(['-'] * n) for _ in range(8)]
print(board)

put_queens(0, board, set(), set(), set(), set())

