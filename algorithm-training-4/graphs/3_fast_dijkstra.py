# Вам дано описание дорожной сети страны. Ваша задача – найти длину кратчайшего пути между городами А и B.

import heapq


def read_input():
    n, k = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(k):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))
    start, end = map(int, input().split())
    return graph, start, end


def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph}
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    path, current_vertex = [], end
    while previous_vertices[current_vertex] is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    if path:
        path.append(current_vertex)
        path.reverse()
    return distances[end]


graph, start, end = read_input()
shortest_distance = dijkstra(graph, start, end)
if shortest_distance == float('inf'):
    print("-1")
else:
    print(shortest_distance)
