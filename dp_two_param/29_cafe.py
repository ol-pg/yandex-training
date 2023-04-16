# Около Петиного университета недавно открылось новое кафе, в котором действует следующая система скидок:
# при каждой покупке более чем на 100 рублей покупатель получает купон, дающий право на один бесплатный обед
# (при покупке на сумму 100 рублей и меньше такой купон покупатель не получает).
#
# Однажды Пете на глаза попался прейскурант на ближайшие N дней. Внимательно его изучив, он решил, что будет обедать
# в этом кафе все N дней, причем каждый день он будет покупать в кафе ровно один обед. Однако стипендия у Пети небольшая,
# и поэтому он хочет по максимуму использовать предоставляемую систему скидок так, чтобы его суммарные затраты были минимальны.
# Требуется найти минимально возможную суммарную стоимость обедов и номера дней, в которые Пете следует воспользоваться купонами.

N = int(input())

cost = [0]

for _ in range(N):
    cost.append(int(input()))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[0][i] = float('inf')

dp[0][0] = 0

for i in range(1, N + 1):
    for j in range(N + 1):
        if cost[i] <= 100:
            if j < N:
                dp[i][j] = min(dp[i - 1][j] + cost[i], dp[i - 1][j + 1])
            else:
                dp[i][j] = dp[i - 1][j] + cost[i]
        else:
            if j > 0 and j < N:
                dp[i][j] = min(dp[i - 1][j + 1], dp[i - 1][j - 1] + cost[i])
            elif j == 0 and j != N:
                dp[i][j] = dp[i - 1][j + 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + cost[i]

count = min(dp[-1])
print(count)
current = list(reversed(dp[-1])).index(count)
print(abs(current - len(dp[-1]) + 1), end=' ')

used = 0
ans = []
while i > 1:
    j = dp[i].index(count)
    if j == 0:
        if dp[i - 1][j] + cost[i] == dp[i][j]:
            count -= cost[i]
        else:
            if cost[i] != 0:
                used += 1
                ans.append(i)
    elif j == N:
        count -= cost[i]
    else:
        if dp[i - 1][j] + cost[i] == dp[i][j] or dp[i - 1][j - 1] + cost[i] == dp[i][j]:
            count -= cost[i]
        else:
            if cost[i] != 0:
                used += 1
                ans.append(i)
    i -= 1
print(used)
for i in range(used - 1, -1, -1):
    print(ans[i])