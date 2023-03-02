# Реализуйте функцию time2min(h, m), которая переводит часы и минуты в минуты с начала суток (00:00).

def time2min(x: str) -> str:
    time = x.split(':',maxsplit=2)
    h = int(time[0])
    m = int(time[1])
    if h >= 24 or m >= 60 or x[2] != ':':
        return print("Invalid format for time")
    else: 
        sum_min = h * 60 + m
        return print('Minutes have passed since the beginning of the day: ', sum_min)

x = input('Enter time in hh:mm format: ')
time2min(x)