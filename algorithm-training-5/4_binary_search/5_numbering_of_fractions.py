# Георг Кантор доказал, что множество всех рациональных чисел счетно (т.е. все рациональные числа можно пронумеровать).
# Чтобы упорядочить дроби необходимо их положить в таблицу, как показано на рисунке.
# В строку с номером i этой матрицы по порядку записаны дроби с числителем i, а в столбец с номером j дроби с знаменателем j.

import math

while True:
    try:
        n = int(input())
        D = math.sqrt(1.000 + 8.000 * n)
        k = D / 2 - 0.500
        if int(k) - k == 0:
            res = int(k)
        else:
            res = int(k) + 1
        l = n - res * (res - 1) // 2
        if res % 2 == 0:
            print(f"{res - l + 1}/{l}")
        else:
            print(f"{l}/{res - l + 1}")
    except EOFError:
        break
