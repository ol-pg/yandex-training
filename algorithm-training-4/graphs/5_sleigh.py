# В начале XVIII века еще не было самолетов, поездов и автомобилей, поэтому все междугородние зимние поездки совершались на санях.
# Как известно, с дорогами в России тогда было даже больше проблем, чем сейчас, а именно на N существовавших тогда городов имелась N-1 дорога,
# каждая из которых соединяла два города. Из каждого города можно было добраться в любой другой (возможно, через промежуточные города).
# В каждом городе была почтовая станция («ям»), на которой можно было пересесть в другие сани.
# При этом ямщики могли долго запрягать (для каждого города известно время,
# которое ямщики в этом городе тратят на подготовку саней к поездке) и быстро ехать (также для каждого города известна скорость,
# с которой ездят ямщики из него). Можно считать, что количество ямщиков в каждом городе не ограничено.
# Если бы олимпиада проводилась 300 лет назад, то путь участников занимал бы гораздо большее время, чем сейчас.
# Допустим, из каждого города в Москву выезжает участник олимпиады и хочет добраться до Москвы за наименьшее время
# (не обязательно по кратчайшему пути: он может заезжать в любые города, через один и тот же город можно проезжать несколько раз).
# Сначала он едет с ямщиком из своего города. Приехав в любой город, он может либо сразу ехать дальше, либо пересесть.
# В первом случае он едет с той же скоростью, с какой ехал раньше. Если сменить ямщика, он сначала ждет, пока ямщик подготовит сани,
# и только потом едет с ним (с той скоростью, с которой ездит этот ямщик). В пути можно делать сколько угодно пересадок.
#
# Определите, какое время необходимо, чтобы все участники олимпиады доехали из своего города в Москву 300 лет назад.
# Все участники выезжают из своих городов одновременно.

from typing import List, Tuple
import heapq

# class CityDescription:
#     def __init__(self, number: int, wait_time: int, speed: int):
#         self.number = number
#         self.wait_time = wait_time
#         self.speed = speed
#
# class Road:
#     def __init__(self, city_from: int, city_to: int, distance: int):
#         self.city_from = city_from
#         self.city_to = city_to
#         self.distance = distance
#
# def find_shortest_time_to_capital_from(start: int, descriptions: List[CityDescription], roads: List[List[Road]], n: int) -> Tuple[float, List[int]]:
#     prev = []
#     visited = [0] * (n + 1)
#     unhandled = []
#     times = [float("inf")] * (n + 1)
#     times[start] = 0.0
#     heapq.heappush(unhandled, (descriptions[start].wait_time, start))
#     while unhandled:
#         current = heapq.heappop(unhandled)
#         if current[1] == 1:
#             prev.append(current[1])
#             break
#         if visited[current[1]] < 2:
#             visited[current[1]] += 1
#             adjacent = roads[current[1]]
#             for road in adjacent:
#                 if visited[road.city_to] < 2:
#                     city_from, city_to, distance = road.city_from, road.city_to, road.distance
#                     prev_speed = current[0]
#                     prev_time = times[current[1]]
#                     current_num, wait_time, current_speed = descriptions[city_from].number, descriptions[city_from].wait_time, descriptions[city_from].speed
#                     no_change_travel_time = distance * 1.0 / prev_speed if prev_speed != 0 else float("inf")
#                     with_change_travel_time = distance * 1.0 / current_speed + wait_time
#                     speed = current_speed
#                     time = 0.0
#                     if no_change_travel_time <= with_change_travel_time:
#                         speed = prev_speed
#                         time = no_change_travel_time
#                     else:
#                         time = with_change_travel_time
#                     if times[city_to] > time + times[start] or (times[city_to] == float("inf") and visited[city_to] >= 1):
#                         times[city_to] = time + times[current[1]]
#                         heapq.heappush(unhandled, (speed, city_to))
#                         prev.append(city_from)
#     return (times[1], prev)
#
# def solve(descriptions: List[CityDescription], roads: List[List[Road]], n: int) -> Tuple[float, List[int]]:
#     max = find_shortest_time_to_capital_from(n, descriptions, roads, n)
#     for i in range(n - 1, 1, -1):
#         cur = find_shortest_time_to_capital_from(i, descriptions, roads, n)
#         if cur[0] >= max[0]:
#             max = cur
#     return max
#
# n = int(input())
# descriptions = [None] * (n + 1)
# for city in range(n):
#     wait_time, speed = map(int, input().split())
#     descriptions[city + 1] = CityDescription(city + 1, wait_time, speed)
# roads = [[] for _ in range(n + 1)]
# for i in range(n - 1):
#     city_from, city_to, dist = map(int, input().split())
#     roads[city_from].append(Road(city_from, city_to, dist))
#     roads[city_to].append(Road(city_to, city_from, dist))
#
# res = solve(descriptions, roads, n)
# print("{:.10f}".format(res[0]))
# print(" ".join(map(str, res[1])))

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))

def printGraph(graph):
    for src in range(len(graph.adjList)):
        print(f"{src} —>", end="")
        for (dest, weight) in graph.adjList[src]:
            print(f" ({dest}, {weight})", end="")
        print()

# Example usage
edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10), (4, 5, 1), (5, 4, 3)]
n = 6
graph = Graph(edges, n)
printGraph(graph)


# 4
# 1 1
# 10 30
# 5 40
# 1 10
# 1 2 300
# 1 3 400
# 2 4 100


# 3
# 1 1
# 0 10
# 0 55
# 1 2 100
# 2 3 10