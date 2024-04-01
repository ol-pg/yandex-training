# Вам дана последовательность измерений некоторой величины. Требуется определить, повторялась ли какое-либо число,
# причём расстояние между повторами не превосходило k.

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

seen = {}
for i, num in enumerate(numbers):
    if num in seen and i - seen[num] <= k:
        print("YES")
        break
    seen[num] = i
else:
    print("NO")
