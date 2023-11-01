# Даны две рациональные дроби: a/b и c/d. Сложите их и результат представьте в виде несократимой дроби m/n.
#
# Формат ввода
# Программа получает на вход 4 натуральных числа a, b, c, d, каждое из которых не больше 100.
#
# Формат вывода
# Программа должна вывести два натуральных числа m и n такие, что m/n=a/b+c/d и дробь m/n – несократима.

def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


a, b, c, d = map(int, input().split())

k = nod((a * d + b * c), b * d)
numerator = int((a * d + b * c) / k)
denominator = int(b * d / k)

print(numerator, denominator)


