# Метрополитен состоит из нескольких линий метро. Все станции метро в городе пронумерованы натуральными числами от 1 до N.
# На каждой линии расположено несколько станций. Если одна и та же станция расположена сразу на нескольких линиях,
# то она является станцией пересадки и на этой станции можно пересесть с любой линии, которая через нее проходит,
# на любую другую (опять же проходящую через нее).
#
# Напишите программу, которая по данному вам описанию метрополитена определит, с каким минимальным числом пересадок можно
# добраться со станции A на станцию B. Если данный метрополитен не соединяет все линии в одну систему,
# то может так получиться, что со станции A на станцию B добраться невозможно, в этом случае ваша программа должна это определить.

def main(N, M, stations, A, B):
    graph = [[] for line in range(M)]
    for station, lines in stations.items():
        if len(lines) > 1:
            for line in lines:
                graph[line].extend(lines)
    beg_lines = stations[A]
    fin_lines = stations[B]

    if len(set(beg_lines).intersection(fin_lines)) > 0:
        print(0)
        return

    queue = beg_lines
    head = 0
    steps = [-1 for i in range(M)]
    for beg_line in beg_lines:
        steps[beg_line] = 0

    while head < len(queue):
        neighs = graph[queue[head]]
        for neigh in neighs:
            if steps[neigh] == -1:
                if neigh in fin_lines:
                    print(steps[queue[head]] + 1)
                    return
                steps[neigh] = steps[queue[head]] + 1
                queue.append(neigh)
        head += 1
    print(-1)


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    stations = {i: [] for i in range(1, N + 1)}
    for line_num in range(M):
        line = list(map(int, input().split()))
        for station in line[1:]:
            stations[station].append(line_num)
    A, B = list(map(int, input().split()))
    main(N, M, stations, A, B)