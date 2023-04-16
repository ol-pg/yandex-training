# Пещера представлена кубом, разбитым на N частей по каждому измерению (то есть на N3 кубических клеток). Каждая клетка
# может быть или пустой, или полностью заполненной камнем. Исходя из положения спелеолога в пещере, требуется найти,
# какое минимальное количество перемещений по клеткам ему требуется, чтобы выбраться на поверхность.
# Переходить из клетки в клетку можно, только если они обе свободны и имеют общую грань.

def main(N, graph, beg):
    if beg[0] == 0:
        print(0)
        exit(0)
    steps = [[[-1 for room in range(N)] for plane in range(N)] for block in range(N)]
    z, y, x = beg
    steps[z][y][x] = 0
    queue = [list(beg)]
    head = 0

    while True:

        now = queue[head]
        neighs = []
        for step in [-1, 1]:
            for coord in [0, 1, 2]:
                poss_neigh = [i for i in now]
                poss_neigh[coord] = poss_neigh[coord] + step
                z, y, x = poss_neigh
                if z >= N or y >= N or x >= N or z < 0 or y < 0 or x < 0:
                    continue
                if steps[z][y][x] == -1 and graph[z][y][x] == 1:
                    if z == 0:
                        print(steps[now[0]][now[1]][now[2]] + 1)
                        return
                    neighs.append(poss_neigh)

        for neigh in neighs:
            z, y, x = neigh
            steps[z][y][x] = steps[now[0]][now[1]][now[2]] + 1
            queue.append(neigh)

        head += 1


if __name__ == "__main__":
    N = int(input())
    graph = []
    beg = ()
    for block in range(N):
        graph_plane = []
        _empty = input()
        for plane in range(N):
            line = input()
            graph_line = [0 if i == "#" else 1 for i in line]
            if "S" in line:
                beg = (block, plane, line.find("S"))
            graph_plane.append(graph_line)
        graph.append(graph_plane)

    main(N, graph, beg)