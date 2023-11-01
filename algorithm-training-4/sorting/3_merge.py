# Базовый алгоритм для сортировки слиянием — алгоритм слияния двух упорядоченных массивов в один упорядоченный массив.
# Эта операция выполняется за линейное время с линейным потреблением памяти.
# Реализуйте слияние двух массивов в качестве первого шага для написания сортировки слиянием.

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


print(' '.join(map(str, merge(a, b))))

# def merge_arrays(a, b):
#     if not a:
#         return b
#     if not b:
#         return a
#     if a[0] < b[0]:
#         return [a[0]] + merge_arrays(a[1:], b)
#     else:
#         return [b[0]] + merge_arrays(a, b[1:])

# print(' '.join(map(str,merge_arrays(a, b))))
