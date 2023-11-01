# В группе учатся n студентов, каждый из которых имеет свой рейтинг ai.
# Им нужно выбрать старосту; для этого студенты хотят выбрать старосту таким образом чтобы суммарный уровень недовольства группы был минимальный.
# Если выбрать j-го старостой, то уровень недовольства i-го студента равен ∣ai−aj∣.

n = int(input())
a = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

for i in range(n):
    dissatisfaction = (i * a[i] - prefix_sum[i]) + ((prefix_sum[n] - prefix_sum[i + 1]) - (n - i - 1) * a[i])
    print(dissatisfaction, end=' ')
