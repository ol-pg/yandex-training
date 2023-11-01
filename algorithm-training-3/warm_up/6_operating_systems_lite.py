# Васин жесткий диск состоит из M секторов. Вася последовательно устанавливал на него различные операционные системы
# следующим методом: он создавал новый раздел диска из последовательных секторов, начиная с сектора номер ai
# и до сектора bi включительно, и устанавливал на него очередную систему. При этом, если очередной раздел хотя бы
# по одному сектору пересекается с каким-то ранее созданным разделом, то ранее созданный раздел «затирается»,
# и операционная система, которая на него была установлена, больше не может быть загружена.
#
# Напишите программу, которая по информации о том, какие разделы на диске создавал Вася, определит,
# сколько в итоге работоспособных операционных систем установлено и работает в настоящий момент на Васином компьютере.

from sys import stdin

def main(M, N, points):
    sorted_points = sorted(points)
    answer = 0
    working_system = -1
    found_systems = set()
    for _, status, number in sorted_points:
        if status == 0:
            if len(found_systems) == 0 or number > max(found_systems):
                working_system = number
            found_systems.add(number)
        elif number == working_system:
            answer += 1
            working_system = -1
            found_systems.remove(number)
        else:
            found_systems.remove(number)
    print(answer)


if __name__ == "__main__":
    M = int(stdin.readline())
    N = int(stdin.readline())
    points = []
    for i in range(N):
        start, end = list(map(int, stdin.readline().split()))
        points.extend([[start, 0, i], [end, 1, i]])
    main(M, N, points)