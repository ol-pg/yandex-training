# На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами,
# параллельными линиям сетки, покрывающий все закрашенные клетки.

k = int(input())
split = input().split()

min_x = int(split[0])
max_x = min_x
min_y = int(split[1])
max_y = min_y


for i in range(k - 1):
    line = input().split()
    new_x = int(line[0])
    new_y = int(line[1])

    if new_x < min_x:
        min_x = new_x
    elif new_x > max_x:
        max_x = new_x

    if new_y < min_y:
        min_y = new_y
    elif new_y > max_y:
        max_y = new_y

print(min_x, min_y, max_x, max_y)