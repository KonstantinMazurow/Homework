import sqlite3 as sql


class Database:

    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_table_clients(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            phone VARCHAR(255) UNIQUE)
        ''')
        self.con.commit()

    def insert_table_clients(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO  clients (name, phone) VALUES(?,?)''', data)
        self.con.commit()

    def create_table_services(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS services(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                price REAL)
        ''')
        self.con.commit()

    def insert_table_services(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO services (name, price) VALUES(?,?)''', data)
        self.con.commit()

    def create_table_orders(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS orders(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_client INTEGER,
                name_service VARCHAR(255),
                FOREIGN KEY (id_client) REFERENCES clients(id),
                FOREIGN KEY (name_service) REFERENCES services(name))
        ''')

    def insert_table_orders(self, data):
        self.cur.executemany('''INSERT OR IGNORE INTO orders (id_client, name_service) VALUES(?,?)''', data)
        self.con.commit()

    def close(self):
        self.con.close()
 