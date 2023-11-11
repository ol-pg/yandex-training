# Строка называется палиндромом, если она читается одинаково как слева направо, так и справа налево.
# Например, строки abba, ata являются палиндромами.
# Вам дана строка. Ее подстрокой называется некоторая непустая последовательность подряд идущих символов.
# Напишите программу, которая определит, сколько подстрок данной строки является палиндромами.

def generate_prefixes(s, p, x):
    lens = len(s)
    s = '_' + s
    prefixes = [0] * (lens + 1)
    suffixes = [0] * (lens + 1)
    pows = [0] * (lens + 1)
    pows[0] = 1
    for i in range(1, lens + 1):
        prefixes[i] = (prefixes[i - 1] * x + ord(s[i])) % p
        suffixes[i] = (suffixes[i - 1] * x + ord(s[-i])) % p
        pows[i] = (pows[i - 1] * x) % p
    return prefixes, suffixes, pows


def is_equal(a, b, l, pows, prefixes, suffixes, lens):
    if a + l >= lens or b + l >= lens:
        return False
    hash_a = (prefixes[a + l] + suffixes[b] * pows[l]) % p
    hash_b = (suffixes[b + l] + prefixes[a] * pows[l]) % p
    return hash_a == hash_b


def find_big_polindrom(i, l, powers, prefix_hash, suffix_hash, n, s):
    result = 0
    odd = False
    even = False
    if 0 < i < n - 2:
        if s[i - 1] != s[i + 1]:
            odd = True
            result += 1
        if s[i] != s[i + 1]:
            even = True
    if odd and even:
        return result
    if odd is False:
        left = 1
        right = l
        while left <= right:
            mid = (left + right) // 2
            if is_equal(i - mid + 1, n - i - mid - 1, mid, powers, prefix_hash, suffix_hash, n):
                left = mid + 1
            else:
                right = mid - 1
        result += left - 1
    if even is False:
        left = 1
        right = l
        while left <= right:
            mid = (left + right) // 2
            if is_equal(i - mid + 1, n - i - mid - 2, mid, powers, prefix_hash, suffix_hash, n):
                left = mid + 1
            else:
                right = mid - 1
        result += left - 1
    return result


x = 257
p = 10 ** 9 + 7
s = input()
if s == '':
    print(0)
else:
    prefix_hash, suffix_hash, powers = generate_prefixes(s, p, x)
    n = len(prefix_hash)
    result = 0
    for i in range(0, n - 1):
        result += find_big_polindrom(i, i + 1, powers, prefix_hash, suffix_hash, n, s)
    print(result)




