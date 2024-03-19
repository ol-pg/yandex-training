import sys

class TravellingSalesmanProblem:
    def __init__(self):
        self.adjacency_matrix = []
        self.dp = []
        self.number_of_vertices = 0

    def main(self):
        self.number_of_vertices = int(input())
        self.adjacency_matrix = [[int(x) for x in input().split()] for _ in range(self.number_of_vertices)]
        self.dp = [[sys.maxsize for _ in range(2 ** self.number_of_vertices)] for _ in range(self.number_of_vertices)]
        self.dp[0][0] = 0
        if self.number_of_vertices == 1:
            print(0)
        else:
            print(self.find_shortest_path(0, (1 << self.number_of_vertices) - 1) if self.find_shortest_path(0, (1 << self.number_of_vertices) - 1) != sys.maxsize else -1)

    def find_shortest_path(self, i, mask):
        if self.dp[i][mask] != sys.maxsize:
            return self.dp[i][mask]
        for j in range(self.number_of_vertices):
            if self.adjacency_matrix[i][j] != 0 and (mask >> j) & 1:
                self.dp[i][mask] = min(self.dp[i][mask], self.find_shortest_path(j, mask - (1 << j)) + self.adjacency_matrix[i][j])
        return self.dp[i][mask]

if __name__ == '__main__':
    tsp = TravellingSalesmanProblem()
    tsp.main()
