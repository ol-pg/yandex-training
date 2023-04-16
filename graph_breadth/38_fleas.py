# На клеточном поле, размером NxM (2 ≤ N, M ≤ 250) сидит Q (0 ≤ Q ≤ 10000) блох в различных клетках.
# "Прием пищи" блохами возможен только в кормушке - одна из клеток поля, заранее известная.
# Блохи перемещаются по полю странным образом, а именно, прыжками, совпадающими с ходом обыкновенного шахматного коня.
# Длина пути каждой блохи до кормушки определяется как количество прыжков. Определить минимальное значение суммы длин
# путей блох до кормушки или, если собраться блохам у кормушки невозможно, то сообщить об этом. Сбор невозможен,
# если хотя бы одна из блох не может попасть к кормушке.

def main(N, M, S, T, Q, goals):
    steps = [[-1 for j in range(M + 1)] for i in range(N + 1)]
    steps[S][T] = 0
    queue = [(S, T)]
    head = 0

    jumps = ((1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1))
    while head < len(queue):
        x, y = queue[head]
        neighs = []
        for delta_x, delta_y in jumps:
            new_x, new_y = x + delta_x, y + delta_y
            if (
                new_x > 0
                and new_x <= N
                and new_y > 0
                and new_y <= M
                and steps[new_x][new_y] == -1
            ):
                neighs.append((new_x, new_y))
                steps[new_x][new_y] = steps[x][y] + 1
        head += 1
        queue.extend(neighs)

    ans = 0
    for x, y in goals:
        goal_steps = steps[x][y]
        if goal_steps == -1:
            print(-1)
            return
        ans += goal_steps

    print(ans)


if __name__ == "__main__":
    N, M, S, T, Q = list(map(int, input().split()))
    goals = []
    for _ in range(Q):
        goal = tuple(map(int, input().split()))
        goals.append(goal)
    main(N, M, S, T, Q, goals)