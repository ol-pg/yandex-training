# Из шахматной доски по границам клеток выпилили связную (не распадающуюся на части) фигуру без дыр. Требуется определить ее периметр.

def calculate_perimeter(N, cells):
    board = [[0] * 8 for _ in range(8)]
    perimeter = 0

    for cell in cells:
        row, col = cell
        board[row - 1][col - 1] = 1

    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                if i == 0 or board[i - 1][j] == 0:
                    perimeter += 1
                if i == 7 or board[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or board[i][j - 1] == 0:
                    perimeter += 1
                if j == 7 or board[i][j + 1] == 0:
                    perimeter += 1

    return perimeter


N = int(input())
cells = [list(map(int, input().split())) for _ in range(N)]

print(calculate_perimeter(N, cells))
