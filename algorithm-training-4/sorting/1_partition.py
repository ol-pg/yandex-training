# Базовым алгоритмом для быстрой сортировки является алгоритм partition, который разбивает набор элементов
# на две части относительно заданного предиката.
# По сути элементы массива просто меняются местами так, что левее некоторой точки в нем после этой операции лежат элементы,
# удовлетворяющие заданному предикату, а справа — не удовлетворяющие ему.
# Например, при сортировке можно использовать предикат «меньше опорного», что при оптимальном выборе опорного элемента может
# разбить массив на две примерно равные части.
#
# Напишите алгоритм partition в качестве первого шага для написания быстрой сортировки.

n = int(input())
a = list(map(int, input().split()))
x = int(input())

low, high = 0, 0
for i in a:
    if x > i:
        low += 1
    else:
        high += 1
print(low)
print(high)

