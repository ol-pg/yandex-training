import sys
import heapq

INF = 10 ** 9
MOD = 10 ** 9 + 7
Q = 38
eps = 1e-9
ll_INF = 10 ** 18


def solve():
    n, m, start, finish = map(int, input().split())
    start -= 1
    finish -= 1
    g = [[] for _ in range(n)]

    for _ in range(m):
        v, u, c = map(int, input().split())
        v -= 1
        u -= 1
        g[v].append((u, c))
        g[u].append((v, c))

    d = [(ll_INF, 0) for _ in range(n)]
    par = [-1] * n
    s = []

    d[start] = (0, 0)
    par[start] = start
    heapq.heappush(s, (d[start][0], start))

    while s:
        len_, v = heapq.heappop(s)

        for u, len_u in g[v]:
            if d[u][0] > len_u + len_:
                d[u] = (len_u + len_, d[v][1] + 1)
                heapq.heappush(s, (d[u][0], u))
                par[u] = v
            elif d[u][0] == len_u + len_ and d[u][1] < d[v][1] + 1:
                d[u] = (len_u + len_, d[v][1] + 1)
                heapq.heappush(s, (d[u][0], u))
                par[u] = v

    print(d[finish][0])
    print(d[finish][1] - 1)

    finish = par[finish]
    way = []

    while par[finish] != finish:
        way.append(finish)
        finish = par[finish]

    for i in range(len(way) - 1, -1, -1):
        print(way[i] + 1, end=" ")


if __name__ == "__main__":
    t = 1

    for _ in range(t):
        solve()
