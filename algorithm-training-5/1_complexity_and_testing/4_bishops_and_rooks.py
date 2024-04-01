# На шахматной доске стоят слоны и ладьи, необходимо посчитать, сколько клеток не бьется ни одной из фигур.
# Шахматная доска имеет размеры 8 на 8. Ладья бьет все клетки горизонтали и вертикали, проходящих через клетку, где она стоит, до первой встретившейся фигуры.
# Слон бьет все клетки обеих диагоналей, проходящих через клетку, где он стоит, до первой встретившейся фигуры.

def count_unattacked_cells():
    figures = {
        "R": [
            [],
            [0, -1], [1, 0], [0, 1], [-1, 0]
        ],
        "B": [
            [],
            [1, 1], [-1, -1], [1, -1], [-1, 1]
        ],
    }
    cnt = 64
    for row in range(8):
        line = input().strip()
        for col, char in enumerate(line):
            if char == "R":
                figures["R"][0].append([row, col])
            elif char == "B":
                figures["B"][0].append([row, col])

    coord_figures = figures["R"][0].copy()
    coord_figures.extend(figures["B"][0])
    list_coord = []

    for figure, coord_list in figures.items():
        coords = coord_list[0]
        pattern = coord_list[1:]
        for x_fig, y_fig in coords:
            cnt -= 1
            for x_mul, y_mul in pattern:
                step_plus = 1
                while True:
                    x_now = x_fig + step_plus * x_mul
                    y_now = y_fig + step_plus * y_mul

                    if [x_now, y_now] in coord_figures or x_now < 0 or x_now > 7 or y_now < 0 or y_now > 7:
                        break

                    if [x_now, y_now] not in list_coord:
                        cnt -= 1
                        list_coord.append([x_now, y_now])

                    step_plus += 1

    return cnt

result = count_unattacked_cells()
print(result)

