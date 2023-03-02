# Электричка отправляется в h1:m1 и едет h2:m2. Выведите время прибытия электрички на электронных часах в формате hh:mm.
# Формат входных данных: на одной строке h1:m1, на другой h2:m2

def get_time_way(x: str, y: str) -> str:
    time1 = x.split(':',maxsplit=2)
    h1, m1= int(time1[0]), int(time1[1])
    time1_min = h1 * 60 + m1
    time2 = y.split(':',maxsplit=2)
    h2, m2 = int(time2[0]), int(time2[1])
    time2_min = h2 * 60 + m2
    delta_time = time1_min + time2_min
    h_delta = delta_time // 60
    m_delta = delta_time % 60
    if h1 >= 24 or m1 >= 60 or x[2] != ':' or h2 >= 24 or m2 >= 60 or y[2] != ':':
        return print("Invalid format for time")
    elif delta_time >= 1440:
        s = h_delta // 24
        h1_delta = h_delta % 24 
        return print('Arrival time: after', s, 'days, in', '{:02}'.format(h1_delta), ':', '{:02}'.format(m_delta))
    else:
        return print('Arrival time: in', '{:02}'.format(h_delta), ':', '{:02}'.format(m_delta))

dep_time = input('Departure time in format hh:mm: ')
trav_time = input('Travel time in format hh:mm: ')
get_time_way(dep_time, trav_time)