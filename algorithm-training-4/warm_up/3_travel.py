# Мэрия Москвы основательно подготовилась к празднованию тысячелетия города в 2147 году,
# построив под столицей бесконечную асфальтированную площадку, чтобы заменить все существующие в городе автомобильные дороги.
# В память о кольцевых и радиальных дорогах разрешили двигаться по площадке только двумя способами:
#
# В сторону точки начала координат или от неё. При этом из точки начала координат разрешено двигаться в любом направлении.
# Вдоль окружности с центром в начале координат и радиусом, который равен текущему расстоянию до начала координат.
# Двигаться вдоль такой окружности разрешается в любом направлении (по или против часовой стрелки).
# Вам, как ведущему программисту ответственной инстанции поручено разработать модуль, который будет определять кратчайший путь из точки A,
# с координатами (xA, yA) в точку B с координатами (xB, yB). Считайте, что менять направление движения можно произвольное количество раз,
# но оно должно всегда соответствовать одному из двух описанных выше вариантов.
#
# Формат ввода
# В первой строке ввода заданы четыре целых числа xA, yA, xB и yB, по модулю не превосходящие 106.
#
# Формат вывода
# Выведите одно число — минимальное расстояние, которое придётся преодолеть по пути из точки A в точку B,
# если не нарушать правил дорожного движения. Ваш ответ будет принят, если его абсолютная или относительная погрешность не превосходит 10-6.

# import math
#
# ax, ay, bx, by = map(int, input().split())
# r = (ax ** 2 + ay ** 2) ** 0.5
# alpha = abs(math.atan2((ax * by - ay * bx), (ax * bx + ay * by)))
# gip_2 = (bx ** 2 + by ** 2)
# ans1 = alpha * r  + abs(gip_2 ** 0.5 - r)
# ans2 = r + gip_2 ** 0.5
# print(min(ans1, ans2))

import math

x1, y1, x2, y2 = map(int, input().split())
r1 = (x1 ** 2 + y1 ** 2) ** 0.5
r2 = (x2 ** 2 + y2 ** 2) ** 0.5
alpha = abs(math.atan2(x1 * y2 - y1 * x2, x1 * x2 + y1 * y2))
ans1 = alpha * r1 + abs(r2 - r1)
ans2 = r1 + r2
print(min(ans1, ans2))




