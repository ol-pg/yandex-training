# def gen(l, r=0, s='', p=''):
#     if l == 0 and r == 0:
#         print(s)
#     if l:
#         gen(l - 1, r + 1, s + '(', p + ')')
#         gen(l - 1, r + 1, s + '[', p + ']')
#     if r:
#         gen(l, r - 1, s + p[-1], p[:-1])
#
# gen(int(input()) // 2)

# def generate_brackets(left, right=0, sequence='', previous=''):
#     if left == 0 and right == 0:
#         print(sequence)
#     if left > 0:
#         generate_brackets(left - 1, right + 1, sequence + '(', previous + ')')
#         generate_brackets(left - 1, right + 1, sequence + '[', previous + ']')
#     if right > 0:
#         generate_brackets(left, right - 1, sequence + previous[-1], previous[:-1])
#
# n = int(input())
# generate_brackets(n // 2)

def task(n):
    if n == 2:
        return ["()", "[]"]
    else:
        tmp = task(n - 2)
        res = []
        for a in tmp:
            res.append("(" + a + ")")
            res.append("[" + a + "]")
            res.append(a + "()")
            res.append(a + "[]")
        return res

n = int(input())
if n == 1 or n == 0:
    pass
else:
    t = task(n)
    # t.sort()
    for item in t:
        print(item)

# (())
# ([])
# ()()
# ()[]
# [()]
# [[]]
# []()
# [][]

# def generate_balanced_parentheses_and_brackets(n):
#     def generate_helper(left, right, s):
#         if left == 0 and right == 0:
#             result.append(s)
#         if left > 0:
#             generate_helper(left - 1, right + 1, s + '(')
#             generate_helper(left - 1, right + 1, s + '[')
#         if right > 0 and right > left:
#             generate_helper(left, right - 1, s + ')')
#             generate_helper(left, right - 1, s + ']')
#
#     result = []
#     generate_helper(n, 0, '')
#     result.sort()
#     for r in result:
#         print(r)
#
# n = int(input())
# generate_balanced_parentheses_and_brackets(n)
