# Строка S была записана много раз подряд, после чего от получившейся строки взяли префикс и дали вам.
# Ваша задача определить минимально возможную длину исходной строки S.

s = input().strip()
X = 257
P = 10 ** 9 + 7


def is_equal(from1, from2, slen, h, x):
    return (
            (h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % P ==
            (h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % P
    )


n = len(s)
s = ' ' + s
h = [0] * (n + 1)
x = [1] * (n + 1)
for i in range(1, n + 1):
    h[i] = (h[i - 1] * X + ord(s[i])) % P
    x[i] = (x[i - 1] * X) % P
max_equal_len = 0
for cur_equal_len in range(1, n):
    if is_equal(1, n + 1 - cur_equal_len, cur_equal_len, h, x):
        max_equal_len = max(max_equal_len, cur_equal_len)
if max_equal_len == 0:
    print(n)
else:
    print(n - max_equal_len)

