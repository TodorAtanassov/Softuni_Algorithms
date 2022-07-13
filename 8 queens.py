def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def can_place_queen(row, col, rows, cols, ld, rd):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in ld:
        return False
    if (row + col) in rd:
        return False
    return True


def set_queen(row, col, board, rows, cols, ld, rd):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    ld.add(row - col)
    rd.add(row + col)


def remove_queen(row, col, board, rows, cols, ld, rd):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    ld.remove(row - col)
    rd.remove(row + col)

def put_queens(row, board, rows, cols, ld, rd):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(row, col, rows, cols, ld, rd):
            set_queen(row, col, board, rows, cols, ld, rd)
            put_queens(row+1, board, rows, cols, ld, rd)
            remove_queen(row, col, board, rows, cols, ld, rd)


n = 8
board = []
[board.append(['-'] * n) for _ in range(8)]
print(board)

put_queens(0, board, set(), set(), set(), set())
