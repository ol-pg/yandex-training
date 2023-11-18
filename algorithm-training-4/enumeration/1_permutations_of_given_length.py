# По данному числу N (0 < N < 10) выведите все перестановки чисел от 1 до N в лексикографическом порядке.

import itertools

N = int(input())
numbers = list(range(1, N + 1))
permutations = list(itertools.permutations(numbers))

for perm in permutations:
    print(int(''.join(map(str, perm))))