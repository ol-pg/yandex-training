# Как же Илье надоело учиться! Сначала школа, потом университет... Вот, наконец, наступил тот долгожданный день, когда Илье утром не надо ехать на учебу.
# Но, к несчастью для Ильи, оказалось, что после окончания университета начинается самое трудное — надо устраиваться на работу.
#
# Во всемирно известной фирме «Goondex», в которую устроился Илья, принято очень много работать, в частности, для сотрудников установлена шестидневная рабочая неделя.
# Но, в качестве бонуса, «Goondex» каждый год предлагает своим сотрудникам выбрать любой день недели в качестве выходного.
# В свою очередь, оставшиеся шесть дней недели будут рабочими.
#
# Илья сообразил, что с учётом государственных праздников (которые всегда являются выходными) с помощью правильного выбора
# выходного дня недели можно варьировать количество рабочих дней в году. Теперь он хочет знать, какой день недели ему следует выбрать в качестве выходного,
# чтобы отдыхать как можно больше дней в году, или, наоборот, демонстрировать чудеса трудолюбия, работая по максимуму.

import calendar

# Ввод данных
N = int(input())
year = int(input())
holidays = []
for _ in range(N):
    day, month = input().split()
    holidays.append((int(day), month))

first_day_of_year = input()

# Определение общего количества рабочих дней в году
total_workdays = 366 - N

# Создание словаря для соответствия месяцев и чисел
months_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
               'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

# Определение дня недели первого января в году
first_day_of_year_index = calendar.weekday(year, months_dict[first_day_of_year], 1)


# Подсчет выходных дней для каждого возможного выходного дня
best_day = None
worst_day = None
max_free_days = 0
min_free_days = total_workdays

for i in range(7):
    free_days = total_workdays
    for holiday in holidays:
        holiday_date = calendar.weekday(year, months_dict[holiday[1]], holiday[0])
        if (holiday_date - first_day_of_year_index) % 7 == i:
            free_days -= 1

    if free_days > max_free_days:
        max_free_days = free_days
        best_day = calendar.day_name[i]

    if free_days < min_free_days:
        min_free_days = free_days
        worst_day = calendar.day_name[i]

# Вывод результата
print(best_day, worst_day)
