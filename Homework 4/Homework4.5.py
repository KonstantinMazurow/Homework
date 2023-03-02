# Электричка отправляется в h1:m1 и прибывает в h2:m2. Выведите время в пути электрички в формате hh:mm.

def get_time_way(x: str, y: str) -> str:
    time1 = x.split(':',maxsplit=2)
    h1, m1= int(time1[0]), int(time1[1])
    time1_min = h1 * 60 + m1
    time2 = y.split(':',maxsplit=2)
    h2, m2 = int(time2[0]), int(time2[1])
    time2_min = h2 * 60 + m2

    if h1 >= 24 or m1 >= 60 or x[2] != ':' or h2 >= 24 or m2 >= 60 or y[2] != ':':
        return print("Invalid format for time")
    #если первое время меньше чем второе.
    elif time1_min < time2_min:
        delta_time = time2_min - time1_min
    # если первое время, больше чем второе (например: электричка выехала в 23:30 и приехала в 00:30 след дня (1440 количество минут в 24 часах)    
    else:
        delta_time = 1440 - time1_min + time2_min 
    return print('Travel time: ', '{:02}'.format(delta_time // 60), ':', '{:02}'.format(delta_time % 60))

dep_time = input('Departure time in format hh:mm: ')
arriv_time = input('Arrival time in format hh:mm: ')
get_time_way(dep_time, arriv_time)

