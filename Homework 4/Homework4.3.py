# Реализуйте функцию min2time(mm), которая минуты с начала суток переводит в часы и минуты (для показа на электронных часах).

def min2time(x: int) -> str:
    h = x // 60
    m = x % 60
    if h >= 24:
        s = h // 24
        h1 = h % 24 
        return print('Days:', s, '\n', 'Time:', '{:02}'.format(h1), ':', '{:02}'.format(m)) 
    else:
        return print('Time:', '{:02}'.format(h), ':', '{:02}'.format(m)) 

minuts = int(input('Enter the number of minutes: '))
min2time(minuts)


