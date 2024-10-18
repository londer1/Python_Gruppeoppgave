import sqlite3
from datetime import datetime

class PostDB:
    def __init__(self, db_name='db.sqlite3'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.init_db()

    def init_db(self):
        # Create Posts table if it doesn't exist
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(200) NOT NULL,
                pages INT NOT NULL,
                price INT NOT NULL,
                amount INT NOT NULL,
                genre VARCHAR(200) NOT NULL,
                author VARCHAR(70) NOT NULL,
                series BOOL NOT NULL
            )
        ''')
        self.conn.commit()

    def fetch_all_posts(self):
        return self.conn.execute('SELECT * FROM Posts').fetchall()

    def add_post(self, title, pages, price, amount, genre, author, series):
        self.conn.execute('INSERT INTO Posts (title, pages, price, amount, genre, author, series) VALUES (?, ?, ?, ?, ?, ?, ?)',
                          (title, pages, price, amount, genre, author, series))
        self.conn.commit()

    def update_post(self, id, title, pages, price, amount, genre, author, series):
        self.conn.execute('UPDATE Posts SET title = ?, pages = ?, price = ?, amount = ?, genre = ?, author = ?, series = ? WHERE id = ?',
                          (title, pages, price, amount, genre, author, series, id))
        self.conn.commit()

    def delete_post(self, id):
        self.conn.execute('DELETE FROM Posts WHERE id = ?', (id,))
        self.conn.commit()


class UserDB:
    def __init__(self, db_name='db.sqlite3'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.init_db()

    def init_db(self):
        # Create Users table if it doesn't exist
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(150) NOT NULL,
                password VARCHAR(200) NOT NULL,
                date_joined DATE NOT NULL,
                staff BOOL NOT NULL,
                borrower BOOL NOT NULL
            )
        ''')
        self.conn.commit()

    def fetch_all_users(self):
        return self.conn.execute('SELECT * FROM Users').fetchall()

    def add_user(self, email, password, staff=False):
        """
        Adds a new user. Borrower is always True, and date_joined is set to the current date.
        Staff users must be manually set to True when calling this method.
        """
        borrower = True
        date_joined = datetime.now().strftime('%Y-%m-%d')  # Automatically add the current date
        self.conn.execute('INSERT INTO Users (email, password, date_joined, staff, borrower) VALUES (?, ?, ?, ?, ?)',
                          (email, password, date_joined, staff, borrower))
        self.conn.commit()

    def update_user(self, id, email, password, date_joined, staff, borrower):
        self.conn.execute('UPDATE Users SET email = ?, password = ?, date_joined = ?, staff = ?, borrower = ? WHERE id = ?',
                          (email, password, date_joined, staff, borrower, id))
        self.conn.commit()

    def delete_user(self, id):
        self.conn.execute('DELETE FROM Users WHERE id = ?', (id,))
        self.conn.commit()

    