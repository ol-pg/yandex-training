# Имеется калькулятор, который выполняет следующие операции:
# - умножить число X на 2;
# - умножить число X на 3;
# - прибавить к числу X единицу.
# Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.

num = int(input())
a = [0] * (num + 1)
a[1] = 0
for n in range(2, num + 1):
    minimal = a[n - 1] + 1
    if n % 2 == 0:
        minimal = min(minimal, a[n // 2] + 1)
    if n % 3 == 0:
        minimal = min(minimal, a[n // 3] + 1)
    a[n] = minimal

operations = []
i = num
while i > 1:
    if a[i] == (a[i - 1] + 1):
        operations.insert(0, 3)
        i -= 1
        continue
    if i % 2 == 0 and a[i] == a[i // 2] + 1:
        operations.insert(0, 1)
        i //= 2
        continue
    operations.insert(0, 2)
    i //= 3
print(a[num])

result=[1]
res = 1
for i in range(len(operations)):
    if operations[i] == 1:
        res=res*2
        result.append(res)
    elif operations[i] == 2:
        res = res * 3
        result.append(res)
    elif operations[i] == 3:
        res = res + 1
        result.append(res)

print(*result)