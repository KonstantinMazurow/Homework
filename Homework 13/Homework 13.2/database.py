import sqlite3 as sql


class Database:

    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_animals(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) UNIQUE NOT NULL)
        ''')
        self.con.commit()

    def insert_table_animals(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO animals (name) VALUES (?)''', data)
        self.con.commit()

    def create_table_age(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS ages_animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_animal INTEGER UNIQUE,
            age INTEGER NOT NULL,
            FOREIGN KEY (id_animal) REFERENCES animals(id))
        ''')
        self.con.commit()

    def insert_table_age(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO ages_animals (id_animal, age) VALUES (?,?)''', data)
        self.con.commit()
    
    def create_table_gender(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS gender_animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_animal INTEGER UNIQUE,
            gender VARCHAR(255) NOT NULL,
            FOREIGN KEY (id_animal) REFERENCES animals(id))      
        ''')
        self.con.commit()
    
    def insert_table_gender(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO gender_animals (id_animal, gender) VALUES (?,?)''', data)
        self.con.commit()

    def select_older_value_left_join(self, value):
        sql_select_query = '''
            SELECT animals.id, animals.name, ages_animals.age
            FROM animals
            LEFT JOIN ages_animals
            ON animals.id = ages_animals.id_animal
            WHERE age>?
        '''
        self.cur.execute(sql_select_query, (value,))
        result = self.cur.fetchall()
        print(f'Result (LEFT JOIN): animals older {value}')
        for row in result:
            print(row)

    def select_older_value_inner_join(self, value):
        sql_select_query = '''
            SELECT animals.id, animals.name, ages_animals.age
            FROM animals
            INNER JOIN ages_animals
            ON animals.id = ages_animals.id_animal
            WHERE age>?
        '''
        self.cur.execute(sql_select_query, (value,))
        result = self.cur.fetchall()
        print()
        print(f'Result (INNER JOIN): animals older {value}')
        for row in result:
            print(row)
    
    def select_gender_animals(self, value):
        sql_select_query = '''
            SELECT animals.id, animals.name, gender_animals.gender
            FROM animals
            LEFT JOIN gender_animals
            ON animals.id = gender_animals.id_animal
            WHERE gender=?
        '''
        self.cur.execute(sql_select_query, (value,))
        result = self.cur.fetchall()
        print()
        print(f'Result (LEFT JOIN): animals gender is {value}')
        for row in result:
            print(row)

    def close(self):
        self.con.close()

