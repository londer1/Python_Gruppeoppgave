import streamlit as st
import sqlite3
from connection import Search
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

# Streamlit app UI
st.title("Post Management")

db = PostDB('database.db')

# Form for adding a new post
with st.form(key='add_post_form'):
    title = st.text_input("Title")
    content = st.text_area("Content")
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    amount = st.number_input("Amount", min_value=0)
    submit_button = st.form_submit_button("Add Post")
    
    if submit_button:
        db.add_post(title, content, price, amount)
        st.success("Post added successfully!")

# Fetch and display all posts
posts = db.fetch_all()
if posts:
    st.subheader("All Posts")
    for post in posts:
        st.write(f"**{post['title']}** - {post['content']} | Price: {post['price']} | Amount: {post['amount']}")
        # Button to delete post
        if st.button(f"Delete {post['title']}", key=post['id']):
            db.delete_post(post['id'])
            st.success(f"Post '{post['title']}' deleted successfully!")

db.close()

query = st.text_input("Enter a search term")
if st.button('Search'):
    search_i = Search(query)
    results = search_i.search()
    if results:
        st.write('Results')
        for r in results:
            st.title(r)
            
    else:
        st.write('No results found')
