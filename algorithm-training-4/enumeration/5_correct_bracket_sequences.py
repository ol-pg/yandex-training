import itertools

# Чтение входных данных
N = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(N)]

# Функция для нахождения кратчайшего цикла
def find_shortest_cycle(graph):
    min_cycle_length = float('inf')
    for node in range(N):
        for subset in itertools.combinations(range(N), N - 1):
            if len(subset) == N - 1:
                cycle = list(itertools.chain(subset, [node]))
                cycle_length = sum(graph[x][y] for x, y in zip(cycle[:-1], cycle[1:]))
                min_cycle_length = min(min_cycle_length, cycle_length)
    return min_cycle_length if min_cycle_length != float('inf') else -1

# Вывод результата
print(find_shortest_cycle(adj_matrix))
