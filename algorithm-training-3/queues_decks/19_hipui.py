# В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции стандартной библиотеки)
# организовать структуру данных Heap для хранения целых чисел, над которой определены следующие операции: a) Insert(k) –
# добавить в Heap число k ; b) Extract достать из Heap наибольшее число (удалив его при этом).

n = int(input())
arr = []
for _ in range(n):
    x = input().split()
    if len(x) == 1:
        print(arr[0])
        arr[0] = arr[len(arr)-1]
        arr.pop()
        i = 0
        while i*2+2 < len(arr):
            if arr[2*i+1] > arr[i] or arr[2*i+2] > arr[i]:
                if arr[2*i+1] > arr[2*i+2]:
                    arr[i], arr[2*i+1] = arr[2*i+1], arr[i]
                    i = 2*i+1
                else:
                    arr[i], arr[2*i+2] = arr[2*i+2], arr[i]
                    i = 2 * i + 2
            else:
                break
        if 2*i+1 < len(arr) and arr[2 * i + 1] > arr[i]:
            arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
    else:
        tmp = int(x[1])
        arr.append(tmp)
        i = len(arr) - 1
        while i > 0 and arr[(i-1)//2] < arr[i]:
            arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
            i = (i - 1) // 2