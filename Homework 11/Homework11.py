''' Homework 11.1.py: Используя модуль sqlite3 создать базу данных favorites
                Создать таблицу с любимыми блюдами
                Продумать поля
                Наполнить таблицу рецептами (не более 4)

    Homework 11.2.py: Создать таблицу в базе данных favorites c любимыми фильмами
                В полях таблицы обязательно должно присутствовать поле “год выпуска”
                Вывести фильмы определенного года выпуска

    Homework 11.3.py: Создать таблицу техника в базе данных favorites с желаемой техникой
                В полях таблицы обязательно должно быть поле “цена”
                Вывести продукты, цена которых меньше 1200'''


import sqlite3 as sql


class Database:

    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_dishes(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS favorite_dishes(
            id INTEGER PRIMARY KEY,
            dish_name VARCHAR(100),
            dish_nationality VARCHAR(100),
            ingredients TEXT)
        ''')
        self.con.commit()

    def insert_table_dishes(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO favorite_dishes (id, dish_name, dish_nationality, ingredients) VALUES(?,?,?,?)''', data)
        self.con.commit()

    def create_table_films(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS favorite_films(
            id INTEGER PRIMARY KEY,
            film_name VARCHAR(100),
            year_of_release INTEGER,
            rating REAL)      
        ''')

    def insert_table_films(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO favorite_films (id, film_name, year_of_release, rating) VALUES(?,?,?,?)''', data)
        self.con.commit()

    def get_films_of_year(self, year):
        sql_select_query ='''SELECT * FROM favorite_films WHERE year_of_release=?'''
        self.cur.execute(sql_select_query, (year,))
        result = self.cur.fetchall()
        return print('Фильмы', year, 'года выпуска:', result)

    def create_table_technics(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS desired_technics(
            id INTEGER PRIMARY KEY,
            technic_name VARCHAR(100),
            price REAL,
            manufacturer VARCHAR(100))
        ''')

    def insert_table_technics(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO desired_technics (id, technic_name, price, manufacturer) VALUES(?,?,?,?)''', data)
        self.con.commit()

    def get_price_lower_number(self, price):
        sql_select_query ='''SELECT * FROM desired_technics WHERE price<?'''
        self.cur.execute(sql_select_query, (price,))
        result = self.cur.fetchall()
        return print('Техника ниже цены', price, ':', result)

    def close(self):
        self.con.close()


def main():

    favorite_dishes = [
        [1, 'Чизкейк', 'Греция', 'печенье песочное, масло сливочное, сыр сливочный, яйца'], 
        [2, 'Крем-брюле', 'Англия', 'сахар коричневый, яичные желтки, ваниль в стручках, сливки'], 
        [3, 'Глинтвейн', 'Италия', 'вино красное сухое, вода, апельсин, сахар, корица, имбирь молотый'],
        [4, 'Паста болоньезе', 'Италия', 'лук, чеснок, оливковое масло, мясной фарш, перец, спагетти, сыр, орегано, петрушка, базилик']
        ]

    favorite_films = [
        [1, 'Джентльмены', 2019, 8.5], 
        [2, 'Рик и Морти', 2013, 9.0], 
        [3, 'Мир Дикого Запада', 2016, 7.9],
        [4, 'Лига справедливости Зака Снайдера', 2021, 7.8],
        [5, 'Викинги', 2013, 8.2]
        ]
    
    favorite_films = [
        [1, 'Джентльмены', 2019, 8.5], 
        [2, 'Рик и Морти', 2013, 9.0], 
        [3, 'Мир Дикого Запада', 2016, 7.9],
        [4, 'Лига справедливости Зака Снайдера', 2021, 7.8],
        [5, 'Викинги', 2013, 8.2]
        ]
    
    desired_technics = [
        [1, 'Холодильник', 1150.63, 'Samsung'], 
        [2, 'Cтиральная машина', 1601.32, 'LG'], 
        [3, 'Пылесос', 700.99, 'Xiaomi'],
        [4, 'Телевизор', 2406.47, 'Samsung'], 
        [5, 'Духовой шкаф', 1199.99, 'Electrolux']
        ]

    db1 = Database('favorites.db')
    db1.create_table_dishes()
    db1.create_table_films()
    db1.create_table_technics()
    
    db1.insert_table_dishes(favorite_dishes)
    db1.insert_table_films(favorite_films)
    db1.insert_table_technics(desired_technics)
    
    db1.get_films_of_year(2013)
    db1.get_price_lower_number(1200)


if __name__ == '__main__':
    main()