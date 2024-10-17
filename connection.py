import streamlit as st
import sqlite3

# Custom CSS
page_bg_css = """
<style>
/* Generell bakgrunn og layout */
[data-testid="stAppViewContainer"] {
    background-color: #f4f1ea;  /* Lys beige bakgrunn */
    padding: 20px;
}

[data-testid="stHeader"] {
    background-color: #c8b197;  /* Lys brun header */
    color: #5d4037;  /* Mørk brun for tekst i header */
    border-bottom: 10px solid #8b6e4e;
}

/* Tekst-styling */
h1, h2, h3 {
    color: #5d4037;  /* Mørk brun for overskrifter */
    font-family: 'Georgia', serif;  /* Klassisk font */
    font-weight: bold;
}

p {
    color: #8d6e63;  /* Lysere brun for vanlig tekst */
    font-family: 'Georgia', serif;
}

/* Styling for input-felter */
input {
    background-color: #faf3e6;  /* Lys beige for input */
    color: #5d4037;  /* Mørk brun tekst */
    border: 1px solid #a1887f;  /* Lys brun border */
    padding: 10px;
    font-size: 14px;
    border-radius: 5px;
}

/* Knapp-styling */
button {
    background-color: #8b6e4e; /* Dyp brun knapp */
    color: white;
    font-size: 16px;
    border: none;
    padding: 12px 24px;
    text-align: center;
    display: inline-block;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 5px;
}

.stButton>button {
    background-color: #8b6e4e;  /* Brun for Streamlit-knapper */
    color: white;
    font-size: 16px;
    border-radius: 5px;
    padding: 10px 20px;
}

/* For tekstinnfyllingsfelter i Streamlit */
.stTextInput>div>input {
    background-color: #faf3e6;  /* Lys beige */
    color: #5d4037;  /* Mørk brun tekst */
    border: 1px solid #a1887f;
    padding: 8px;
    border-radius: 5px;
}

/* For nummerinput i Streamlit */
.stNumberInput>div>input {
    background-color: #faf3e6;
    color: #5d4037;
    border: 1px solid #a1887f;
    padding: 8px;
    border-radius: 5px;
}

/* For dropdown-meny i Streamlit */
.stSelectbox>div>input {
    background-color: #faf3e6;
    color: #5d4037;
    border: 1px solid #a1887f;
    padding: 8px;
    border-radius: 5px;
}

/* Tekstbokser */
textarea {
    background-color: #faf3e6;
    color: #5d4037;
    border: 1px solid #a1887f;
    padding: 10px;
    border-radius: 5px;
    font-family: 'Georgia', serif;
}

/* Justering av layout */
.stBlock>div {
    background-color: #e5ddd5;  /* Lys brun boks bak input-seksjon */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
"""

# Apply the custom CSS
st.markdown(page_bg_css, unsafe_allow_html=True)

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

# Initialize the database connection
db = PostDB()

# Streamlit app layout
st.title('Post Management')

# View all posts
st.header('All Posts')
posts = db.fetch_all()
if posts:
    for post in posts:
        st.write(f"ID: {post['id']}, Title: {post['title']}, Pages: {post['pages']}, Price: {post['price']}, Amount: {post['amount']}")
else:
    st.write("No posts available.")

# Create a new post
st.header('Create New Post')
with st.form('create_form'):
    title = st.text_input('Title')
    pages = st.number_input('Pages', min_value=1)
    price = st.number_input('Price', min_value=0)
    amount = st.number_input('Amount', min_value=0)
    submitted = st.form_submit_button('Create')

    if submitted:
        db.add_post(title, pages, price, amount)
        st.success('Post created!')

# Update a post
st.header('Update Post')
with st.form('update_form'):
    post_id = st.number_input('Post ID', min_value=1)
    new_title = st.text_input('New Title')
    new_pages = st.number_input('New Pages', min_value=1)
    new_price = st.number_input('New Price', min_value=0)
    new_amount = st.number_input('New Amount', min_value=0)
    update_submitted = st.form_submit_button('Update')

    if update_submitted:
        db.update_post(post_id, new_title, new_pages, new_price, new_amount)
        st.success('Post updated!')

# Delete a post
st.header('Delete Post')
with st.form('delete_form'):
    delete_id = st.number_input('Post ID to Delete', min_value=1)
    delete_submitted = st.form_submit_button('Delete')

    if delete_submitted:
        db.delete_post(delete_id)
        st.success('Post deleted!')
