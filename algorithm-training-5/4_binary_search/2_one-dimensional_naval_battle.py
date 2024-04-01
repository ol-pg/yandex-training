# Поле в игре в одномерный морской бой имеет размеры 1×n. Ваша задача — найти такое максимальное k,
# что на поле можно расставить один корабль размера 1×k, два корабля размера 1×(k−1), …, k кораблей размера 1×1,
# причем корабли, как и в обычном морском бое, не должны касаться друг друга и пересекаться.

memo = {}

def ans(n, k):
    if k == 0:
        return n
    if (n, k) in memo:
        return memo[(n, k)]
    memo[(n, k)] = ans(abs(n-1), k-1)/2 + ans(n, k-1)/2
    return memo[(n, k)]

# Input
n, k = map(int, input().split())

# Calculate and output result
result = n - ans(n, k)
print(result)


