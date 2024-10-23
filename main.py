import streamlit as st
from connection import PostDB  # Import the PostDB class
import sqlite3

def refresh_posts():
    st.session_state.posts = db.fetch_all_posts()

# Initialize the database connection
db = PostDB()

# Streamlit app layout
st.title('Bokhandel Lagerstyring')

# Function to sort posts
def sort_posts(sort_by):
    query = f"SELECT * FROM Posts ORDER BY {sort_by}"
    return db.conn.execute(query).fetchall()

# View all posts with sorting options
st.header('Oversikt over lager')
sort_option = st.selectbox('Sorter etter', ['Navn', 'Pris', 'Mengde'])
sort_column = {
    'Navn': 'title',
    'Pris': 'price',
    'Mengde': 'amount'
}[sort_option]
posts = sort_posts(sort_column)

if posts:
    for post in posts:
        st.write(f"ID: {post['id']}, Navn: {post['title']}, Pris: {post['price']}, Mengde: {post['amount']}, Forfatter: {post['author']}")
else:
    st.write("Ingen varer tilgjengelig.")

# Register new items (add post)
st.header('Registrer ny vare')
with st.form('create_form'):
    title = st.text_input('Navn')
    price = st.number_input('Pris', min_value=0)
    amount = st.number_input('Mengde på lager', min_value=0)
    genre = st.text_input('Sjanger')
    author = st.text_input('Forfatter')
    series = st.checkbox('Er dette en serie?')
    submitted = st.form_submit_button('Registrer')

    if submitted:
        db.add_post(title, 0, price, amount, genre, author, series)  # 0 pages since it's not used
        st.success('Vare registrert!')
        refresh_posts()

# Update inventory (update post)
st.header('Oppdater beholdning')
with st.form('update_form'):
    post_id = st.number_input('ID på varen som skal oppdateres', min_value=1)
    new_amount = st.number_input('Ny mengde på lager', min_value=0)
    update_submitted = st.form_submit_button('Oppdater')

    if update_submitted:
        post = db.conn.execute('SELECT * FROM Posts WHERE id = ?', (post_id,)).fetchone()
        if post:
            db.update_post(post_id, post['title'], post['pages'], post['price'], new_amount, post['genre'], post['author'], post['series'])
            st.success('Beholdning oppdatert!')
            refresh_posts()
        else:
            st.error('Vare ikke funnet.')

# Delete a post (delete item)
st.header('Slett vare')
with st.form('delete_form'):
    delete_id = st.number_input('ID på varen som skal slettes', min_value=1)
    delete_submitted = st.form_submit_button('Slett')

    if delete_submitted:
        db.delete_post(delete_id)
        st.success('Vare slettet!')
        refresh_posts()
