# Реализуйте сортировку слиянием, используя алгоритм из предыдущей задачи.
#
# На каждом шаге делите массив на две части, сортируйте их независимо и сливайте с помощью уже реализованной функции.

n = int(input())
a = list(map(int, input().split()))


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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


print(' '.join(map(str, merge_sort(a))))