# Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние от одной заданной вершины до другой.

import heapq


def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances[end]


n, s, f = map(int, input().split())
graph = {}
for i in range(n):
    row = list(map(int, input().split()))
    graph[i + 1] = {j + 1: row[j] for j in range(n) if row[j] != -1}

shortest_distance = dijkstra(graph, s, f)
if shortest_distance == float('inf'):
    print("-1")
else:
    print(shortest_distance)
