# В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух
# чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D,
# а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок
# и дополнительных соглашений о приоритете операторов для своего чтения.

def postfix_query(postfix):
    stack = []
    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
            continue
        y = stack.pop()
        x = stack.pop()
        operation_dict = {'+': lambda x, y: x + y,
                          '-': lambda x, y: x - y,
                          '*': lambda x, y: x * y,
                          '/': lambda x, y: x // y}[i](x, y)
        stack.append(operation_dict)
    return stack.pop()


postfix = input().split()
print(postfix_query(postfix))