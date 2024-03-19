# Вася играет в настольную игру «Пираты Баренцева моря», которая посвящена морским битвам. Игровое поле представляет собой квадрат из
# N×N клеток, на котором расположено N кораблей (каждый корабль занимает одну клетку).
# Вася решил воспользоваться линейной тактикой, для этого ему необходимо выстроить все N кораблей в одном столбце.
# За один ход можно передвинуть один корабль в одну из четырёх соседних по стороне клеток.
# Номер столбца, в котором будут выстроены корабли, не важен. Определите минимальное количество ходов, необходимых для построения кораблей в одном столбце.
# В начале и процессе игры никакие два корабля не могут находиться в одной клетке.

# n = int(input())
# a = [tuple(map(int, input().split())) for _ in range(n)]
# a.sort(key=lambda x: x[0])
# a.sort(key=lambda x: x[1])
# d = []
# for y in range(1, n+1):
#     s = 0
#     b = [(i, j) for i, j in a if j != y]
#     c = [i for i, j in a if j == y]
#     x_set = set(range(1, n+1)) - set(c)
#     for i, x in enumerate(sorted(x_set)):
#         s += abs(x-b[i][0]) + abs(y-b[i][1])
#     d.append(s)
# print(min(d))

# def min_moves_to_align_ships(n, a):
#     a.sort(key=lambda x: x[0])
#     a.sort(key=lambda x: x[1])
#
#     d = []
#     for y in range(1, n+1):
#         s = 0
#         b = [(i, j) for i, j in a if j != y]
#         c = [i for i, j in a if j == y]
#         x_set = set(range(1, n+1)) - set(c)
#         for i, x in enumerate(sorted(x_set)):
#             s += min([abs(x-b[i][0]) + abs(y-b[i][1]) for i in range(len(b))])
#         d.append(s)
#
#     return min(d)
#
#
# n = int(input())
# a = [tuple(map(int, input().split())) for _ in range(n)]
# print(min_moves_to_align_ships(n, a))

# def min_moves_to_align_ships(n, a):
#     a.sort(key=lambda x: x[0])
#     a.sort(key=lambda x: x[1])
#
#     d = []
#     for y in range(1, n+1):
#         s = 0
#         b = [(i, j) for i, j in a if j != y]
#         c = [i for i, j in a if j == y]
#         x_set = set(range(1, n+1)) - set(c)
#         for i, x in enumerate(sorted(x_set)):
#             s += min([abs(x-b[i][0]) + abs(y-b[i][1]) for i in range(len(b))])
#         d.append(s)
#
#     return min(d)
#
# n = 20
# a = [(13, 19), (3, 13), (20, 19), (12, 8), (20, 15), (6, 10), (6, 9), (3, 19), (7, 17), (6, 3),
#      (18, 18), (5, 15), (13, 15), (9, 1), (11, 3), (9, 17), (15, 10), (18, 11), (4, 14), (16, 4)]
#
# result = min_moves_to_align_ships(n, a)
# print(result)

def min_moves_to_align_ships(n, a):
    a.sort(key=lambda x: x[0])
    a.sort(key=lambda x: x[1])

    d = []
    for y in range(1, n+1):
        s = 0
        b = [(i, j) for i, j in a if j != y]
        c = [i for i, j in a if j == y]
        x_set = set(range(1, n+1)) - set(c)
        for x in sorted(x_set):
            s += min([abs(x-i) + abs(y-j) for i, j in b])
        d.append(s)

    return min(d)

# Считываем количество кораблей N
n = 20
a = [(13, 19), (3, 13), (20, 19), (12, 8), (20, 15), (6, 10), (6, 9), (3, 19), (7, 17), (6, 3),
     (18, 18), (5, 15), (13, 15), (9, 1), (11, 3), (9, 17), (15, 10), (18, 11), (4, 14), (16, 4)]

# Вызываем функцию и выводим результат
result = min_moves_to_align_ships(n, a)
print(result)


