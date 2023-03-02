import sqlite3 as sql


class Database:
    
    def __init__(self, database):
        self.con = sql.connect(database, check_same_thread=False)
        self.cur = self.con.cursor()

    def create_table_joks(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS joks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user TEXT NOT NULL,
            joke TEXT UNIQUE)
        ''')

    def insert_table_joks(self, data):
        self.cur.execute('''INSERT or IGNORE INTO joks (id_user, joke) VALUES(?,?)''', data)
        self.con.commit()

    def select_random_joks(self, data):
        self.cur.execute('''SELECT joke FROM joks 
        WHERE id_user =?
        ORDER BY RANDOM() LIMIT 1;
        ''', data)
        result = self.cur.fetchall()
        return result
    
    def close(self):
        self.con.close()


