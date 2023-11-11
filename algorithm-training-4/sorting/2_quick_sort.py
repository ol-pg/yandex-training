# Реализуйте быструю сортировку, используя алгоритм из предыдущей задачи.
#
# На каждом шаге выбирайте опорный элемент и выполняйте partition относительно него.
# Затем рекурсивно запуститесь от двух частей, на которые разбился исходный массив.

import sys
import random

sys.setrecursionlimit(9999999)


def quick_sort(mass, l=None, r=None):
    if l >= r:
        return
    q = random.randint(l, r)
    i = l
    j = r
    while i < j:
        while mass[i] < mass[q]:
            i += 1
        while j > i and mass[j] > mass[q]:
            j -= 1
        if i <= j:
            mass[i], mass[j] = mass[j], mass[i]
            i += 1
            j -= 1
            quick_sort(mass, l, j)
            quick_sort(mass, i, r)


def quick_sort_v2(mass, l, r):
    if l + 1 >= r:
        return
    e = l
    g = l
    q = mass[random.randint(l, r-1)]
    for n in range(l, r):
        if mass[n] > q:
            continue
        elif mass[n] == q:
            mass[g], mass[n] = mass[n], mass[g]
        else:
            mass[n], mass[g] = mass[g], mass[n]
            mass[g], mass[e] = mass[e], mass[g]

            e += 1
        g += 1
    quick_sort_v2(mass, l, e)
    quick_sort_v2(mass, g, r)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        N = int(f.readline())
        mass = list(map(int, f.readline().split()))
    if N > 0:
        quick_sort_v2(mass, 0, len(mass))
        print(" ".join(str(x) for x in mass))
    else:
        print()