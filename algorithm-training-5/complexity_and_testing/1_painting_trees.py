# Вася и Маша участвуют в субботнике и красят стволы деревьев в белый цвет. Деревья растут вдоль улицы через равные промежутки в 1 метр.
# Одно из деревьев обозначено числом ноль, деревья по одну сторону занумерованы положительными числами 1,2 и т.д.,
# а в другую — отрицательными −1,−2 и т.д.
# Ведро с краской для Васи установили возле дерева P, а для Маши — возле дерева Q.
# Ведра с краской очень тяжелые и Вася с Машей не могут их переставить, поэтому они окунают кисть в ведро и уже с этой кистью идут красить дерево.
# Краска на кисти из ведра Васи засыхает, когда он удаляется от ведра более чем на V метров, а из ведра Маши — на M метров.
# Определите, сколько деревьев может быть покрашено.

# def count_painted_trees(V, M, P, Q):
#     painted_trees_vasya = list(range(P-V, P+V+1))
#     painted_trees_masha = list(range(Q-M, Q+M+1))
#     all = set(painted_trees_vasya+painted_trees_masha)
#
#     return len(all)
#
# P, V = map(int, input().split())
# Q, M = map(int, input().split())
#
# result = count_painted_trees(V, M, P, Q)
# print(result)


# def count_painted_trees(V, M, P, Q):
#     painted_trees_vasya = set(range(P-V, P+V+1))
#     painted_trees_masha = set(range(Q-M, Q+M+1))
#
#     return len(painted_trees_vasya.union(painted_trees_masha))
#
# P, V = map(int, input().split())
# Q, M = map(int, input().split())
#
# result = count_painted_trees(V, M, P, Q)
# print(result)


# def count_painted_trees(V, M, P, Q):
#     vasya_end = P + V
#     masha_start = Q - M
#
#     result = (V + M + 1) * 2
#     if vasya_end == masha_start:
#         result -= 1
#     elif vasya_end > masha_start:
#         result -= (vasya_end - masha_start) + 1
#     return result
#
# P, V = map(int, input().split())
# Q, M = map(int, input().split())
#
# result = count_painted_trees(V, M, P, Q)
# print(result)


def count_painted_trees(V, M, P, Q):
    if Q == P:
        return 2 * max(M, V) + 1

    right_start = max(P, Q)
    right_step = (right_start == P) and V or M
    left_start = min(P, Q)
    left_step = (left_start == P) and V or M

    if right_start - right_step <= left_start + left_step:
        left = min(left_start - left_step, right_start - right_step)
        right = max(left_start + left_step, right_start + right_step)
        return right - left + 1

    return 2 * right_step + 2 * left_step + 2

P, V = map(int, input().split())
Q, M = map(int, input().split())

result = count_painted_trees(V, M, P, Q)
print(result)



