# Создать функцию calc(a, b, operation). Описание входных параметров: 
# 1. Первое число 
# 2. Второе число 
# 3. Действие над ними: 1) + Сложить 2) - Вычесть 3) * Умножить 4) / Разделить 5) 
# В остальных случаях функция должна возвращать "Операция не поддерживается". Типизировать ее. При запуске mypy не должно быть никаких ошибок типов

import typing

def calc(a: int, b: int, operation: str) -> str:
    if operation == '+':
        return str(a + b)
    elif operation == '-':
        return str(a - b)
    elif operation == '*':
        return str(a * b)
    elif operation == '/':
        return str(a / b)
    else:
        return str('Operation not supported.')

a = int(input('First number: '))
operation = str(input('Operation: '))
b = int(input('Second number: '))
print('Result: ', calc(a, b, operation))

