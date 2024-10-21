import sqlite3
from datetime import datetime
import hashlib

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
                email VARCHAR(150) NOT NULL UNIQUE,
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
        borrower = True
        date_joined = datetime.now().strftime('%Y-%m-%d')
        self.conn.execute('INSERT INTO Users (email, password, date_joined, staff, borrower) VALUES (?, ?, ?, ?, ?)',
                          (email, self.hash_password(password), date_joined, staff, borrower))
        self.conn.commit()

    def validate_login(self, email, password):
        hashed_password = self.hash_password(password)
        user = self.conn.execute('SELECT * FROM Users WHERE email = ? AND password = ?', (email, hashed_password)).fetchone()
        if user:
            return True, user
        return False, None

    def delete_user(self, user_id):
        self.conn.execute('DELETE FROM Users WHERE id = ?', (user_id,))
        self.conn.commit()

    def hash_password(self, password):
        # Use SHA-256 or stronger hashing
        return hashlib.sha256(password.encode()).hexdigest()

# Example Usage
if __name__ == "__main__":
    # Initialize UserDB
    user_db = UserDB()

    # Example of adding a user
    user_db.add_user("test@example.com", "securepassword")

    # Example of login
    email = "test@example.com"
    password = "securepassword"
    is_valid, user = user_db.validate_login(email, password)
    if is_valid:
        print(f"Login successful! Welcome, {user['email']}.")
    else:
        print("Login failed. Invalid email or password.")

    # Example of deleting a user
    # user_db.delete_user(user_id)  # Replace user_id with the actual ID to delete
