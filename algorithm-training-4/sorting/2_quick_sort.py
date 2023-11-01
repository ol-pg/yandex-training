# Реализуйте быструю сортировку, используя алгоритм из предыдущей задачи.
#
# На каждом шаге выбирайте опорный элемент и выполняйте partition относительно него.
# Затем рекурсивно запуститесь от двух частей, на которые разбился исходный массив.

n = int(input())
a = list(map(int, input().split()))

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(*quicksort(a))
