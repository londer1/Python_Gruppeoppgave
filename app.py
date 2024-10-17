import sqlite3

class PostDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    price REAL NOT NULL,
                    amount INTEGER NOT NULL
                )
            ''')

    def add_post(self, title, content, price, amount):
        with self.conn:
            self.conn.execute('INSERT INTO posts (title, content, price, amount) VALUES (?, ?, ?, ?)',
                            (title, content, price, amount))

    def update_post(self, post_id, title, content, price, amount):
        with self.conn:
            self.conn.execute('UPDATE posts SET title = ?, content = ?, price = ?, amount = ? WHERE id = ?',
                            (title, content, price, amount, post_id))

    def delete_post(self, post_id):
        with self.conn:
            self.conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))

    def fetch_all(self):
        cursor = self.conn.execute('SELECT * FROM posts')
        return [{'id': row[0], 'title': row[1], 'content': row[2], 'price': row[3], 'amount': row[4]} for row in cursor.fetchall()]

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = PostDB('database.db')
    db.add_post("Bok A", "Innhold A", 100, 5)
    db.add_post("Bok B", "Innhold B", 200, 10)
    posts = db.fetch_all()
    print("Alle poster:")
    for post in posts:
        print(post)
    if posts:
        post_id = posts[0]['id']
        db.update_post(post_id, "Bok A - Oppdatert", "Innhold A - Oppdatert", 150, 7)
    posts = db.fetch_all()
    print("\nOppdaterte poster:")
    for post in posts:
        print(post)
    if posts:
        db.delete_post(posts[0]['id'])
    posts = db.fetch_all()
    print("\nEtter sletting:")
    for post in posts:
        print(post)
    db.close()
