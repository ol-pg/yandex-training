from queue import Queue

def shortest_hamiltonian_cycle(n, graph):
    # Инициализируем начальное состояние BFS
    start_state = (1, 1 << 0)
    q = Queue()
    q.put(start_state)
    # Инициализируем таблицу расстояний
    dist = {(1, 1 << 0): 0}
    # Запускаем BFS
    while not q.empty():
        u, mask = q.get()
        # Если мы посетили все вершины и вернулись в 1, то нашли кратчайший цикл
        if mask == (1 << n) - 1 and u == 1:
            return dist[(u, mask)]
        # Проходим по всем соседям вершины u
        for v in range(1, n + 1):
            if graph[u - 1][v - 1] != 0 and not (mask & (1 << (v - 1))):
                # Если сосед v еще не посещен, добавляем его в очередь
                new_mask = mask | (1 << (v - 1))
                new_state = (v, new_mask)
                if new_state not in dist:
                    dist[new_state] = dist[(u, mask)] + graph[u - 1][v - 1]
                    q.put(new_state)
    # Если не нашли кратчайший цикл, возвращаем -1
    return -1

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(shortest_hamiltonian_cycle(n, graph))