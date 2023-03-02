# Напишите функцию sum(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно. Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sum(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    add = 0
    for i in range (start, end+1):
        add += i
    return add

a = int(input("First number: "))
b = int(input("Second number: "))

print('Sum:', sum(a, b))
