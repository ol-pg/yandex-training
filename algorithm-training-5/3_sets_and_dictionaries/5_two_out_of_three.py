# Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.


n1 = int(input())
list1 = set(map(int, input().split()))

n2 = int(input())
list2 = set(map(int, input().split()))

n3 = int(input())
list3 = set(map(int, input().split()))

result = list((list1 & list2) | (list1 & list3) | (list2 & list3))

result.sort()
for num in result:
    print(num, end=' ')

