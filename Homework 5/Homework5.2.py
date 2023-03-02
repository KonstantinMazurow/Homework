#  Напишите функцию, которая будет примет список нечетных чисел, выводит их и остановится, если встретит число 200. Типизировать ее. 
#  При запуске mypy не должно быть никаких ошибок типов

import typing

def odd_numbers(x: list) -> list:
    numbers1 = []
    for i in x:
        if i % 2 != 0:
            numbers1.append(i)
        elif i == 200:
            break
    return list(numbers1)   

numbers = []
# Создает список от 1 - 500 через 2
for x in range(1, 500, 2):
    numbers.append(x)
print(odd_numbers(numbers))