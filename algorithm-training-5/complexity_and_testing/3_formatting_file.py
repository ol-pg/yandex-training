# Петя - начинающий программист. Сегодня он написал код из n строк.
# К сожалению оказалось, что этот код трудно читать. Петя решил исправить это, добавив в различные места пробелы.
# А точнее, для i-й строки ему нужно добавить ровно ai пробелов.
# Для добавления пробелов Петя выделяет строку и нажимает на одну из трёх клавиш: Space, Tab, и Backspace.
# При нажатии на Space в строку добавляется один пробел. При нажатии на Tab в строку добавляются четыре пробела.
# При нажатии на Backspace в строке удаляется один пробел.
# Ему хочется узнать, какое наименьшее количество клавиш придётся нажать, чтобы добавить необходимое количество пробелов в каждую строку. Помогите ему!

def min_key_presses(n):
    total_key_presses = 0
    space_presses = n // 4
    if n % 4 == 3:
        space_presses += 1
        total_key_presses += 1
    elif n % 4 == 2:
        total_key_presses += 2
    elif n % 4 == 1:
        total_key_presses += 1
    return space_presses + total_key_presses


n = int(input())
total_count = 0
for _ in range(n):
    num = int(input())
    total_count += min_key_presses(num)

print(total_count)
