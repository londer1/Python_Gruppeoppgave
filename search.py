import sqlite3


class Search():

    def __init__(self, query, database='db.sqlite3'):
        self.query = query.lower()
        self.database = database()
        self.database = database
        self.results = []
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
    def search(self):
        if self.query:
            sql_query = 'SELECT * FROM Posts WHERE title LIKE ? OR genre LIKE ?'
            like_query = f'%{self.query}'
            self.cursor.execute(sql_query, like_query)
            self.reults = self.cursor.fetchall()
            like_query = f'%{self.query}%'
            self.cursor.execute(sql_query, (like_query, like_query))
            self.results = self.cursor.fetchall()
            return self.results
    def close():
        self.conn.close()
