# В игре в пьяницу карточная колода раздается поровну двум игрокам. Далее они вскрывают по одной верхней карте, и тот,
# чья карта старше, забирает себе обе вскрытые карты, которые кладутся под низ его колоды. Тот, кто остается без карт
# – проигрывает. Для простоты будем считать, что все карты различны по номиналу, а также, что самая младшая карта побеждает
# самую старшую карту ("шестерка берет туза"). Игрок, который забирает себе карты, сначала кладет под низ своей колоды
# карту первого игрока, затем карту второго игрока (то есть карта второго игрока оказывается внизу колоды).
# Напишите программу, которая моделирует игру в пьяницу и определяет, кто выигрывает. В игре участвует 10 карт,
# имеющих значения от 0 до 9, большая карта побеждает меньшую, карта со значением 0 побеждает карту 9.

from collections import deque

def is_card_greater(f_card, s_card):
    if abs(f_card - s_card) == 9:
        return f_card <= s_card
    return f_card > s_card


def get_winner(first, second):
    cnt = 0
    while cnt < 1000000:
        cnt += 1
        f = first.popleft()
        s = second.popleft()
        if is_card_greater(f, s):
            first.append(f)
            first.append(s)
        else:
            second.append(f)
            second.append(s)
        if not first:
            return f"second {cnt}"
        if not second:
            return f"first {cnt}"
    return "botva"


first = deque(list(map(int, input().split())))
second = deque(list(map(int, input().split())))
print(get_winner(first, second))