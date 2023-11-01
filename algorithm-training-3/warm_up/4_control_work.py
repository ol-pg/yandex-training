# Петя и Вася — одноклассники и лучшие друзья, поэтому они во всём помогают друг другу.
# Завтра у них контрольная по математике, и учитель подготовил целых K вариантов заданий.
#
# В классе стоит один ряд парт, за каждой из них (кроме, возможно, последней) на контрольной будут сидеть ровно два ученика.
# Ученики знают, что варианты будут раздаваться строго по порядку: правый относительно учителя ученик первой парты
# получит вариант 1, левый — вариант 2, правый ученик второй парты получит вариант 3 (если число вариантов больше двух) и т.д.
# Так как K может быть меньше чем число учеников N, то после варианта K снова выдаётся вариант 1.
# На последней парте в случае нечётного числа учеников используется только место 1.
#
# Петя самым первым вошёл в класс и сел на своё любимое место. Вася вошёл следом и хочет получить такой же вариант,
# что и Петя, при этом сидя к нему как можно ближе. То есть между ними должно оказаться как можно меньше парт,
# а при наличии двух таких мест с равным расстоянием от Пети Вася сядет позади Пети, а не перед ним. Напишите программу,
# которая подскажет Васе, какой ряд и какое место (справа или слева от учителя) ему следует выбрать.
# Если же один и тот же вариант Вася с Петей писать не смогут, то выдайте одно число  - 1.

import math

cnt_std = int(input())
cnt_var = int(input())
row = int(input())
seat = int(input())

p_seat = row * 2
if seat % 2 != 0:
    p_seat = p_seat - 1


def get_tables_between(start, end):
    if start % 2 != 0:
        start += 1
    if end % 2 == 0:
        end -= 1
    return (end - 1 - start) / 2


v_before = p_seat - cnt_var
v_after = p_seat + cnt_var

if v_before > 0 and v_after <= cnt_std:
    tables_before = get_tables_between(v_before, p_seat)
    tables_after = get_tables_between(p_seat, v_after)

    if tables_before == tables_after:
        v_place = v_after
    elif tables_before < tables_after:
        v_place = v_before
    else:
        v_place = v_after

elif v_before > 0 and v_after > cnt_std:
    v_place = v_before
elif v_before <= 0 and v_after <= cnt_std:
    v_place = v_after
else:
    v_place = 0

if v_place:
    v_row = math.ceil(v_place / 2)
    if (v_place / 2) % 1 != 0:
        v_side = 1
    else:
        v_side = 2
    print(v_row, v_side)
else:
    print('-1')

