# Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить компоненту связности, содержащую первую вершину.

n, m = map(int, input().split())

graph = {i: [] for i in range(n)}
for i in range(m):
    inn, out = map(int, input().split())
    graph[inn - 1].append(out - 1)
    graph[out - 1].append(inn - 1)

result = set()
to_check = set()
to_check.add(0)
length = -1

while len(result) != length:
    length = len(result)
    new_to_check = set()
    for i in to_check:
        result.add(i)
        for j in graph[i]:
            new_to_check.add(j)
    to_check = new_to_check

print(len(result))
print(*list(map(lambda x: x + 1, result)))