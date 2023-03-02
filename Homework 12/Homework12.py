import sqlite3 as sql
from pars_book_list import get_books_list


class Database:

    def __init__(self, database):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()

    def create_favorite_books(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS favorite_books(
            id INTEGER PRIMARY KEY,
            autor_book VARCHAR(100),
            book_name VARCHAR(100) UNIQUE)
        ''')
        self.con.commit()

    def insert_table_books(self, data):
        self.cur.executemany('''INSERT or IGNORE INTO favorite_books (id, autor_book, book_name) VALUES(?,?,?)''', data)
        self.con.commit()

    def get_books_info(self):
        self.cur.execute('''SELECT * FROM favorite_books''')
        result = self.cur.fetchall()
        for row in result:
            print(row)

    def get_book_info_id(self, id):
        sql_select_query ='''SELECT autor_book,book_name FROM favorite_books WHERE id=?'''
        self.cur.execute(sql_select_query, (id,))
        result = self.cur.fetchall()
        return print(f'Книга под номером {id}: {result}')

    def close(self):
        self.con.close()


def main():
    db1 = Database('favorites.db')
    db1.create_favorite_books() 
    db1.insert_table_books(get_books_list())
    db1.get_books_info()
    db1.get_book_info_id('53')


if __name__ == '__main__':
    main()
 

