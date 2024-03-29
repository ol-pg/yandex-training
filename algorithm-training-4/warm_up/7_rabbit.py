# Кролики очень любопытны. Они любят изучать геометрию, бегая по грядкам.
# Наш кролик как раз такой. Сегодня он решил изучить новую фигуру — квадрат.
# Кролик бегает по грядке — клеточному полю N × M клеток. В некоторых из них посеяны морковки, в некоторых нет.
# Помогите кролику найти сторону квадрата наибольшей площади, заполненного морковками полностью.
#
# Формат ввода
# В первой строке даны два натуральных числа N и M.
# Далее в N строках расположено по M чисел, разделенных пробелами (число равно 0, если в клетке нет морковки или 1, если есть).
#
# Формат вывода
# Выведите одно число — сторону наибольшего квадрата, заполненного морковками.

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

dp = [[0 for j in range(m+1)] for i in range(n+1)]
k = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            if dp[i][j] > k:
                k = dp[i][j]

print(k)

