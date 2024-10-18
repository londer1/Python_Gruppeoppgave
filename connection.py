# connection.py

import sqlite3

class PostDB:
    def __init__(self, db_name='db.sqlite3'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.init_db()

    def init_db(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(200) NOT NULL,
                pages INT NOT NULL,
                price INT NOT NULL,
                amount INT NOT NULL
            )
        ''')
        self.conn.commit()

    def fetch_all(self):
        return self.conn.execute('SELECT * FROM posts').fetchall()

    def add_post(self, title, pages, price, amount):
        self.conn.execute('INSERT INTO posts (title, pages, price, amount) VALUES (?, ?, ?, ?)',
                          (title, pages, price, amount))
        self.conn.commit()

    def update_post(self, id, title, pages, price, amount):
        self.conn.execute('UPDATE posts SET title = ?, pages = ?, price = ?, amount = ? WHERE id = ?',
                          (title, pages, price, amount, id))
        self.conn.commit()

    def delete_post(self, id):
        self.conn.execute('DELETE FROM posts WHERE id = ?', (id,))
        self.conn.commit()
