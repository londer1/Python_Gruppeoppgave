class Search():
    def __init__(self, query, database=db.sqlite3):
        self.query = query.lower()
        self.database = database
        self.results = []
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
    def search(self):
        if self.query:
            sql_query = SELECT backup bin chess.txt client crontest.sh crontest.txt db.sqlite3 Desktop Django-Blog Documents Downloads evencv.docx id_rsa ip_to_nickname.txt layout.py log __MACOSX Music neovim node_modules olav@192.168.1.69 olvm other_ssh package.json package-lock.json Passwords.kdbx Pictures post.db Posts posts.db Public python_gui_del1.zip SocketCommander sshkey.txt Templates test.log test.sh test.txt utvikling Videos vindu.py FROM Posts WHERE title LIKE ? OR genre LIKE ?
            like_query = f%{self.query}%
            self.cursor.execute(sql_query, (like_query, like_query))
            self.results = self.cursor.fetchall()
            return self.results
    def close():
        self.conn.close()
