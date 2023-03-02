# Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона, к которому относится этот месяц. 
# Например, передаем 2, на выходе получаем 'Зима'.

import typing

def month_to_season(x: int) -> str:
    if x == 1 or x == 2 or x == 12:
        return str('Winter')
    if x == 3 or x == 4 or x == 5:
        return str('Spring')
    if x == 5 or x == 6 or x == 7:
        return str('Summer')
    if x == 9 or x == 10 or x == 11:
        return str('Autumn')
    else:
        return str('Invalid month value.')


month = int(input('Enter month number: '))
print('Result: ', month_to_season(month))