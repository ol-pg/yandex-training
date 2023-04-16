# Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать,
# какие символы в секретных зашифрованных посланиях употребляются чаще других.
# Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов.
# Поэтому он хочет построить гистограмму количества символов в сообщении.
# Гистограмма — это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз,
# соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.

with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

mes = ''.join(input_lines).replace(' ', '').replace('\n', '')
dct_mes = {i: mes.count(i) for i in set(mes)}
max_val = max(dct_mes.values())
uniq_val = sorted(set(mes))

for i in range(max_val):
    str = ''
    for j in uniq_val:
        if dct_mes[j] >= max_val:
            str += '#'
        else:
            str += ' '
    print(str)
    max_val -= 1
print("".join(uniq_val))