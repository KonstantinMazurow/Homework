# Функция принимает год (натуральное число). Напечатайте YES, если год високосный. Иначе напечатайте NO.
# Год високосный, если он делится на 4, но не делится на 100. Если год делится на 400, то он тоже считается високосным.

def get_leap_year(x: int) -> str:
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        return print('Yes')
    else: return print('No') 

year = int(input('Enter year: '))
get_leap_year(year)