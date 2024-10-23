import streamlit as st
from connection import PostDB, Search  # Import the PostDB class
import time

def refresh_posts():
    st.session_state.posts = db.fetch_all_posts()

# Initialize the database connection
db = PostDB()

# Streamlit app layout
st.title('Post Management')

# View all posts
st.header('All Posts')
posts = db.fetch_all_posts()
if posts:
    for post in posts:
        st.write(f"ID: {post['id']}, Title: {post['title']}, Pages: {post['pages']}, Price: {post['price']}, Amount: {post['amount']}, Genre: {post['genre']}, Author: {post['author']}, Series: {post['series']}")
else:
    st.write("No posts available.")

# Create a new post
st.header('Create New Post')
with st.form('create_form'):
    title = st.text_input('Title')
    pages = st.number_input('Pages', min_value=2)
    price = st.number_input('Price', min_value=1)
    amount = st.number_input('Amount', min_value=1)
    genre = st.text_input('Genre')
    author = st.text_input('Author')
    series = st.checkbox('Is Series?')
    submitted = st.form_submit_button('Create')

    if submitted:
        db.add_post(title, pages, price, amount, genre, author, series)
        st.success('Post created!')
        refresh_posts()



# Update a post
st.header('Update Post')
with st.form('update_form'):
    post_id = st.number_input('Post ID', min_value=2)
    new_title = st.text_input('New Title')
    new_pages = st.number_input('New Pages', min_value=2)
    new_price = st.number_input('New Price', min_value=1)
    new_amount = st.number_input('New Amount', min_value=1)
    new_genre = st.text_input('New Genre')
    new_author = st.text_input('New Author')
    new_series = st.checkbox('Is Series?')
    update_submitted = st.form_submit_button('Update')

    if update_submitted:
        db.update_post(post_id, new_title, new_pages, new_price, new_amount, new_genre, new_author, new_series)
        st.success('Post updated!')
        refresh_posts()

# Delete a post
st.header('Delete Post')
with st.form('delete_form'):
    delete_id = st.number_input('Post ID to Delete', min_value=2)
    delete_submitted = st.form_submit_button('Delete')

    if delete_submitted:
        db.delete_post(delete_id)
        st.success('Post deleted!')
        refresh_posts()


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
