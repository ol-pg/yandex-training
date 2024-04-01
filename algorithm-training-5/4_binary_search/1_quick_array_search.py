# Дан массив из N целых чисел. Все числа от −10**9 до 10**9.
# Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения от L до R ?”.


def count_numbers_in_range():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    def binary_search(arr, target, find_first):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > target or (find_first and arr[mid] == target):
                right = mid
            else:
                left = mid + 1
        return left

    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())

        start = binary_search(arr, l, True)
        end = binary_search(arr, r, False)

        print(end - start, end=" ")


count_numbers_in_range()
