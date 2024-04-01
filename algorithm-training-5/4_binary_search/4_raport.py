# Верс нужно подготовить рапорт о последнем боевом вылете. Она уже сочинила в голове текст, осталось лишь его записать.
# Рапорт будет состоять из двух частей: первая будет содержать n слов, i-е из которых состоит из ai букв, вторая — m слов, j-е из которых состоит из bj букв.
# Язык Крии не содержит никаких знаков препинания. Верс должна записать рапорт на клетчатом рулоне бумаги, шириной w клеток.
# Так как рапорт состоит из двух частей, она разделит вертикальной чертой рулон на две части целой ширины,
# после чего в левой части напишет первую часть, а в правой — вторую. Обе части рапорта записываются аналогично, каждая на своей части рулона.
# Одна буква слова занимает ровно одну клетку. Первое слово записывается в первой строке рулона, начиная с самой левой клетки этой части рулона.
# Каждое следующее слово, если это возможно, должно быть записано в той же строке, что и предыдущее, и быть отделено от него ровно одной пустой клеткой.
# Иначе, оно пишется в следующей строке, начиная с самой левой клетки. Если ширина части рулона меньше, чем длина какого-то слова,
# которое должно быть написано в этой части, написать эту часть рапорта на части рулона такой ширины невозможно.
# Гарантируется, что можно провести вертикальную черту так, что обе части рапорта возможно написать.
# Верс хочет провести вертикальную черту так, чтобы длина рулона, которой хватит, чтобы написать рапорт, была минимальна.
# Помогите ей найти эту минимальную длину.

def first_string(m, a):
    ans = 1
    pos = 0
    for i in range(len(a)):
        if a[i] > m:
            return 1000000000
        if a[i] + pos <= m:
            pos += a[i] + 1
        else:
            pos = a[i] + 1
            ans += 1
    return ans


def second_string(m, b):
    ans = 1
    pos = 0
    for i in range(len(b)):
        if b[i] > m:
            return 1000000000
        if b[i] + pos <= m:
            pos += b[i] + 1
        else:
            pos = b[i] + 1
            ans += 1
    return ans


w, n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = 0
r = w
while l < r - 1:
    m = (l + r) // 2
    if first_string(m, a) < second_string(w - m, b):
        r = m
    else:
        l = m

result = min(max(first_string(l, a), second_string(w - l, b)), max(first_string(l + 1, a), second_string(w - l - 1, b)))
print(result)
