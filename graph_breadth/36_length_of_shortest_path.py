# В неориентированном графе требуется найти длину минимального пути между двумя вершинами.

def main(N, graph, A, B):
    queue = [A]
    head = 0
    steps = [-1 for _ in range(N)]
    steps[A] = 0
    while steps[B] == -1 and head < len(queue):
        prev = queue[head]
        for node, is_neigh in enumerate(graph[prev]):
            if is_neigh == 1 and steps[node] == -1:
                queue.append(node)
                steps[node] = steps[prev] + 1
        head += 1
    print(steps[B])


if __name__ == "__main__":
    N = int(input())
    graph = []
    for _ in range(N):
        graph_line = list(map(int, input().split()))
        graph.append(graph_line)
    A, B = list(map(int, input().split()))
    main(N, graph, A - 1, B - 1)