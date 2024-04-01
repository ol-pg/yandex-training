def check_rectangles(m, n, picture):
    for i in range(m):
        for j in range(n):
            if picture[i][j] == '#':
                x1, y1 = j, i
                x2, y2 = j, i
                while x1 < n and picture[y1][x1] == '#':
                    x1 += 1
                while y2 < m and picture[y2][x2] == '#':
                    y2 += 1
                if x1 != n or y2 != m:
                    return False
    return True

m, n = map(int, input().split())
picture = [input() for _ in range(m)]

if check_rectangles(m, n, picture):
    print("YES")
    for i in range(m):
        for j in range(n):
            if picture[i][j] == '#':
                print("a", end="")
            else:
                print("b", end="")
        print()
else:
    print("NO")
