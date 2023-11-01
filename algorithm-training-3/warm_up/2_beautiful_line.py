# Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)
# Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа.

k = int(input())
s = input()

dct_val = {}
res, start, cur_letter = 0, 0, 0
for i in range(len(s)):
    letter = s[i]
    if letter not in dct_val:
        dct_val[letter] = 0
    dct_val[letter] += 1
    cur_letter = max(cur_letter, dct_val[letter])
    if i - start - cur_letter + 1 > k:
        dct_val[s[start]] -= 1
        start += 1
    res = max(res, i - start + 1)

print(res)
