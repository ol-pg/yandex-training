# Константин и Михаил играют в настольную игру «Ярость Эльфов». В игре есть n рас и m классов персонажей.
# Каждый персонаж характеризуется своими расой и классом. Для каждой расы и каждого класса существует ровно один персонаж такой расы и такого класса.
# Сила персонажа i-й расы и j-го класса равна ai j, и обоим игрокам это прекрасно известно.
#
# Сейчас Константин будет выбирать себе персонажа. Перед этим Михаил может запретить одну расу и один класс,
# чтобы Константин не мог выбирать персонажей, у которых такая раса или такой класс. Конечно же, Михаил старается,
# чтобы Константину достался как можно более слабый персонаж, а Константин, напротив, выбирает персонажа посильнее.
# Какие расу и класс следует запретить Михаилу?

def solve_h(g):
    max_ = -1
    max_i = -1
    for i in range(len(g)):
        x = max(g[i])
        if x > max_:
            max_ = x
            max_i = i
    return max_i


def solve_v(g):
    max_ = -1
    max_j = -1
    for i in range(len(g)):
        x = max(g[i])
        if x > max_:
            max_ = x
            max_j = g[i].index(x)
    return max_j


def solve_hv(g):
    rm_i = solve_h(g)
    g[rm_i] = [0] * len(g[rm_i])
    rm_j = solve_v(g)
    for i in range(len(g)):
        g[i][rm_j] = 0

    max_ = -1
    for i in range(len(g)):
        x = max(g[i])
        if x > max_:
            max_ = x

    return (max_, (rm_i, rm_j))


def solve_vh(g):
    rm_j = solve_v(g)
    for i in range(len(g)):
        g[i][rm_j] = 0
    rm_i = solve_h(g)
    g[rm_i] = [0] * len(g[rm_i])

    max_ = -1
    for i in range(len(g)):
        x = max(g[i])
        if x > max_:
            max_ = x
    return (max_, (rm_i, rm_j))


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

r1 = solve_hv(list(map(list, g)))
r2 = solve_vh(list(map(list, g)))

result = min(r1, r2)

print(result[1][0] + 1, result[1][1] + 1)
