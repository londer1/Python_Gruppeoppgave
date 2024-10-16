import streamlit as st
import sqlite3

class PostDB:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self.init_db()

    def init_db(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(200) NOT NULL,
                content TEXT NOT NULL,
                price INT NOT NULL,
                amount INT NOT NULL
            )
        ''')
        self.conn.commit()

    def fetch_all(self):
        return self.conn.execute('SELECT * FROM posts').fetchall()

    def add_post(self, title, content, price, amount):
        self.conn.execute('INSERT INTO posts (title, content, price, amount) VALUES (?, ?, ?, ?)',
                          (title, content, price, amount))
        self.conn.commit()

    def update_post(self, id, title, content, price, amount):
        self.conn.execute('UPDATE posts SET title = ?, content = ?, price = ?, amount = ? WHERE id = ?',
                          (title, content, price, amount, id))
        self.conn.commit()

    def delete_post(self, id):
        self.conn.execute('DELETE FROM posts WHERE id = ?', (id,))
        self.conn.commit()

# Initialize the database connection
db = PostDB()

# Streamlit app layout
st.title('Post Management')

# View all posts
st.header('All Posts')
posts = db.fetch_all()
if posts:
    for post in posts:
        st.write(f"ID: {post['id']}, Title: {post['title']}, Price: {post['price']}, Amount: {post['amount']}")
else:
    st.write("No posts available.")

# Create a new post
st.header('Create New Post')
with st.form('create_form'):
    title = st.text_input('Title')
    content = st.text_area('Content')
    price = st.number_input('Price', min_value=0)
    amount = st.number_input('Amount', min_value=0)
    submitted = st.form_submit_button('Create')

    if submitted:
        db.add_post(title, content, price, amount)
        st.success('Post created!')

# Update a post
st.header('Update Post')
with st.form('update_form'):
    post_id = st.number_input('Post ID', min_value=1)
    new_title = st.text_input('New Title')
    new_content = st.text_area('New Content')
    new_price = st.number_input('New Price', min_value=0)
    new_amount = st.number_input('New Amount', min_value=0)
    update_submitted = st.form_submit_button('Update')

    if update_submitted:
        db.update_post(post_id, new_title, new_content, new_price, new_amount)
        st.success('Post updated!')

# Delete a post
st.header('Delete Post')
with st.form('delete_form'):
    delete_id = st.number_input('Post ID to Delete', min_value=1)
    delete_submitted = st.form_submit_button('Delete')

    if delete_submitted:
        db.delete_post(delete_id)
        st.success('Post deleted!')
