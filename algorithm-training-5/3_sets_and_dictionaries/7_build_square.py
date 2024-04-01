# Задано множество, состоящее из N различных точек на плоскости. Координаты всех точек — целые числа.
# Определите, какое минимальное количество точек нужно добавить во множество, чтобы нашлось четыре точки, лежащие в вершинах квадрата.

from itertools import combinations

# Чтение ввода
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Функция для проверки, лежат ли 4 точки на вершинах квадрата
def is_square(p1, p2, p3, p4):
    sides = [p1, p2, p3, p4]
    side_lengths = [sum((a - b) ** 2 for a, b in combinations(side, 2)) for side in sides]
    side_lengths.sort()
    return side_lengths[0] == side_lengths[1] == side_lengths[2] == side_lengths[3] and side_lengths[4] == side_lengths[5]

# Поиск минимального количества точек, которые нужно добавить
min_points = float('inf')
for p1, p2, p3, p4 in combinations(points, 4):
    if is_square(p1, p2, p3, p4):
        min_points = min(min_points, 0)
    else:
        min_points = min(min_points, 4 - sum(p in {p1, p2, p3, p4} for p in points))

# Вывод результата
print(int(min_points))  # Преобразуем float в int для использования в range()
if min_points > 0:
    for _ in range(int(min_points)):
        print("0 0")  # Пример координат добавленных точек



