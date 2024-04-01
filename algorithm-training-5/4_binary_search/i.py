import math

def calculate_time_to_reach_ball(x, y, v):
    return math.sqrt(x**2 + y**2) / v

def find_optimal_hit_point(D, N, players):
    min_time = float('inf')
    optimal_point = (0, D)

    for x, y, v in players:
        time = calculate_time_to_reach_ball(x, D - y, v)
        if time < min_time:
            min_time = time
            optimal_point = (x, D - y)

    return min_time, optimal_point

# Input
D, N = 10, 2
players = [(1, 1, 1), (-1, 1, 1)]

# Find optimal hit point
time, point = find_optimal_hit_point(D, N, players)

# Output
print("{:.5f}".format(time))
print("{:.5f} {:.5f}".format(point[0], point[1]))
