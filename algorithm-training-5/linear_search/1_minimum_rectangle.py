# На клетчатой плоскости закрашено K клеток.
# Требуется найти минимальный по площади прямоугольник, со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.


K = int(input())
min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')

for _ in range(K):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print(min_x, min_y, max_x, max_y)
