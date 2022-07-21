def explore_area(row, col, matrix):
    if row < 0 or col < 0 or row >= len(matrix) or col >= (len(matrix[0])):
        return
    if matrix == '*':
        return
    matrix[row][col] = 'v'
    explore_area(row - 1, col, matrix)
    explore_area(row + 1, col, matrix)
    explore_area(row, col - 1, matrix)
    explore_area(row, col + 1, matrix)


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))

for row in range(rows):
    for col in range(cols):
        size = explore_area(row, col, matrix)

for row in matrix:
    print(row)
