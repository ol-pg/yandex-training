# Во время контрольной работы профессор Флойд заметил, что некоторые студенты обмениваются записками.
# Сначала он хотел поставить им всем двойки, но в тот день профессор был добрым, а потому решил разделить студентов
# на две группы: списывающих и дающих списывать, и поставить двойки только первым.
#
# У профессора записаны все пары студентов, обменявшихся записками. Требуется определить, сможет ли он разделить студентов
# на две группы так, чтобы любой обмен записками осуществлялся от студента одной группы студенту другой группы.

n, m = map(int, input().split())
gr = [set() for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    gr[a].add(b)
    gr[b].add(a)

visited = [0 for i in range(n + 1)]


def dfs(now, cost):
    visited[now] = cost
    for neig in gr[now]:
        if visited[neig] == 0:
            dfs(neig, 3 - cost)
        elif visited[neig] == cost:
            return False
    return True


for i in range(1, n + 1):
    if visited[i] == 0:
        flag = dfs(i, 1)
    if not flag:
        print('NO\n')
        break
else:
    print('YES\n')
