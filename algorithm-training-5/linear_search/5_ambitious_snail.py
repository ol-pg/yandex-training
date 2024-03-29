# Домашний питомец мальчика Васи — улитка Петя. Петя обитает на бесконечном в обе стороны вертикальном столбе,
# который для удобства можно представить как числовую прямую. Изначально Петя находится в точке 0.
# Вася кормит Петю ягодами. У него есть n ягод, каждая в единственном экземпляре. Вася знает, что если утром он даст Пете ягоду с номером i,
# то поев и набравшись сил, за остаток дня Петя поднимется на ai единиц вверх по столбу, но при этом за ночь, потяжелев,
# съедет на bi единиц вниз. Параметры различных ягод могут совпадать.Пете стало интересно, а как оно там, наверху, и Вася взялся ему в этом помочь.
# Ближайшие n дней он будет кормить Петю ягодами из своего запаса таким образом, чтобы максимальная высота,
# на которой побывал Петя за эти n дней была максимальной. К сожалению, Вася не умеет программировать, поэтому он попросил вас о помощи.
# Найдите, максимальную высоту, на которой Петя сможет побывать за эти n дней и в каком порядке Вася должен давать Пете ягоды, чтобы Петя смог её достичь!

def calculate_max_height(n, berries):
    berries.sort(key=lambda x: x[0] - x[1], reverse=True)
    height = 0
    order = []

    for diff, index in berries:
        if height + diff > height:
            height += diff
            order.append(index)

    return height, order


# Считываем данные
n = int(input())
berries = [tuple(map(int, input().split())) for _ in range(n)]

# Вычисляем максимальную высоту и порядок подачи ягод
max_height, order = calculate_max_height(n, berries)

# Выводим результаты
print(max_height)
print(*order)


