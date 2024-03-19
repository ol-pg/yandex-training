# Дан массив целых положительных чисел a длины n. Разбейте его на минимально возможное количество отрезков,
# чтобы каждое число было не меньше длины отрезка которому оно принадлежит. Длиной отрезка считается количество чисел в нем.
#
# Разбиение массива на отрезки считается корректным, если каждый элемент принадлежит ровно одному отрезку.

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    res = []
    test = []
    i = 0

    while i < n:
        if len(test) == 0:
            _min = 1
        elif len(test) == 1:
            _min = test[-1]
        else:
            _min = min(_min, test[-1])

        if _min >= len(test) + 1 and a[i] >= len(test) + 1:
            test.append(a[i])
            i += 1
        else:
            res.append(len(test))
            test = []

    res.append(len(test))

    print(len(res))
    print(*res)
