# Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы N×M в прямоугольнике
# с левым верхним углом (x1, y1) и правым нижним (x2, y2)

def preprocess(mat, _n,_m):
    s = [[0 for j in range(_m)] for i in range(_n)]
    s[0][0] = mat[0][0]
    for i in range(1, _m):
        s[0][i] = mat[0][i]+s[0][i-1]
    for i in range(1, _n):
        s[i][0] = mat[i][0]+s[i-1][0]
    for i in range(1, _n):
        for j in range(1, _m):
            s[i][j] = mat[i][j]+s[i-1][j]+s[i][j-1]-s[i-1][j-1]
    return s


matrix = []
n, m, k = map(int, input().split())
for i in range(n):
    matrix.append(list(map(int, input().split())))
matrix = preprocess(matrix, n, m)
for i in range(k):
    a, b, c, d = map(int, input().split())
    total = matrix[c-1][d-1]
    if b - 2 >= 0:
        total -= matrix[c-1][b-2]
    if a - 2 >= 0:
        total -= matrix[a-2][d-1]
    if a-2 >= 0 and b-2 >= 0:
        total += matrix[a-2][b-2]
    print(total)