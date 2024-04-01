# Развлекательный телеканал транслирует шоу «Колесо Фортуны». В процессе игры участники шоу крутят большое колесо, разделенное на сектора.
# В каждом секторе этого колеса записано число. После того как колесо останавливается, специальная стрелка указывает на один из секторов.
# Число в этом секторе определяет выигрыш игрока.
#
# Юный участник шоу заметил, что колесо в процессе вращения замедляется из-за того, что стрелка задевает за выступы на колесе, находящиеся между секторами.
# Если колесо вращается с угловой скоростью v градусов в секунду, и стрелка, переходя из сектора X к следующему сектору, задевает за очередной выступ,
# то текущая угловая скорость движения колеса уменьшается на k градусов в секунду. При этом если v ≤ k, то колесо не может преодолеть препятствие и останавливается.
# Стрелка в этом случае будет указывать на сектор X.
#
# Юный участник шоу собирается вращать колесо. Зная порядок секторов на колесе, он хочет заставить колесо вращаться с такой начальной скоростью,
# чтобы после остановки колеса стрелка указала на как можно большее число. Колесо можно вращать в любом направлении и придавать ему
# начальную угловую скорость от a до b градусов в секунду.
#
# Требуется написать программу, которая по заданному расположению чисел в секторах, минимальной и максимальной начальной угловой
# скорости вращения колеса и величине замедления колеса при переходе через границу секторов вычисляет максимальный выигрыш.

n = int(input())
win = list(map(int, input().split()))

min_speed, max_speed, speed_dec = map(int, input().split())
min_shift = (min_speed - 1) // speed_dec
to_visit = min(n, (max_speed - 1) // speed_dec + 1 - min_shift)
assert to_visit > 0

max1 = 0
for di in [-1, 1]:
    pos = di * min_shift % n
    for i in range(to_visit):
        max1 = max(max1, win[pos])
        pos = (pos + di) % n

assert max1 > 0
print(max1)