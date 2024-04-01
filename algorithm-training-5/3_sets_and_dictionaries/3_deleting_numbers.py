# Дан массив a из n чисел. Найдите минимальное количество чисел, после удаления которых попарная разность оставшихся чисел по модулю не будет превышать 1,
# то есть после удаления ни одно число не должно отличаться от какого-либо другого более чем на 1.

_ = int(input())
numbers = list(map(int, input().split()))


def delete_numbers(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    maximum = 0
    for number in counts.keys():
        maximum = max(
            maximum,
            counts.get(number, 0) + counts.get(number - 1, 0),
            counts.get(number, 0) + counts.get(number + 1, 0)
        )

    return len(numbers) - maximum


print(delete_numbers(numbers))



