# Реализуйте быструю сортировку, используя алгоритм из предыдущей задачи.
#
# На каждом шаге выбирайте опорный элемент и выполняйте partition относительно него.
# Затем рекурсивно запуститесь от двух частей, на которые разбился исходный массив.

import random


def main():
    input_file = "input.txt"
    with open(input_file, "r") as f:
        n = int(f.readline())
        if n == 0:
            print()
            return
        nums = list(map(int, f.readline().split()))
        if not is_sorted(nums):
            quick_sort(nums, 0, len(nums) - 1)
    print(nums_to_string(nums))


def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return False
    return True


def save_to_file(nums):
    with open("output.txt", "w") as f:
        f.write(nums_to_string(nums))


def quick_sort(nums, left, right):
    if left < right:
        p = partition(nums, left, right)
        quick_sort(nums, left, p)
        quick_sort(nums, p + 1, right)


def partition(nums, left, right):
    pivot = nums[left + random.randint(0, right - left)]
    length = right - left
    equal = left
    great = left
    for i in range(left, left + length + 1):
        temp = nums[i]
        if nums[i] < pivot:
            nums[i] = nums[great]
            nums[great], nums[equal] = nums[equal], nums[great]
            equal += 1
            great += 1
        elif nums[i] == pivot:
            nums[i] = nums[great]
            nums[great] = temp
            great += 1
    return equal


def nums_to_string(nums):
    return " ".join(str(num) for num in nums)


if __name__ == "__main__":
    main()
