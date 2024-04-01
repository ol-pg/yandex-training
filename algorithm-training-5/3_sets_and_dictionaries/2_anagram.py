# Задано две строки, нужно проверить, является ли одна анаграммой другой. Анаграммой называется строка, полученная из другой перестановкой букв.

from collections import Counter


def check_anagram(str1, str2):
    return Counter(str1) == Counter(str2)


str1 = input().strip()
str2 = input().strip()

if check_anagram(str1, str2):
    print("YES")
else:
    print("NO")
