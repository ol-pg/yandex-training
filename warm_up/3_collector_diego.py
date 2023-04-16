# Диего увлекается коллекционированием наклеек. На каждой из них написано число,
# и каждый коллекционер мечтает собрать наклейки со всеми встречающимися числами.
# Диего собрал N наклеек, некоторые из которых, возможно, совпадают.
# Как-то раз к нему пришли K коллекционеров. i-й из них собрал все наклейки с номерами не меньшими, чем pi.
# Напишите программу, которая поможет каждому из коллекционеров определить, сколько недостающих ему наклеек есть у Диего.
# Разумеется, гостей Диего не интересуют повторные экземпляры наклеек.

n = int(input())
n_list = sorted(set((map(int, input().split()))))
k = int(input())
k_list = map(int, input().split())

def mid(n_list, k_val):
    if k_val > n_list[-1]:
        return(len(n_list))
    if k_val <= n_list[0]:
        return(0)

    left = 0
    right = len(n_list)
    mid = (left + right) // 2

    while left < right:
        mid = (left + right) // 2
        if n_list[mid] == k_val:
            break
        if n_list[mid] > k_val > n_list[mid - 1]:
            break
        if n_list[mid] < k_val:
            left = mid + 1
        else:
            right = mid
    return mid

dct = {}
for p in k_list:
    if p in dct:
        print(dct[p])
    else:
        res = mid(n_list, p)
        dct[p] = res
        print(res)


