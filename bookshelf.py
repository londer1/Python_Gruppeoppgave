import streamlit as st
from connection import PostDB  # Import your PostDB class directly

# Custom CSS for Frontpage and cards
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f4f1ea;
    padding: 20px;
}

[data-testid="stHeader"] {
    background-color: #c8b197;
    color: #5d4037;
    border-bottom: 10px solid #8b6e4e;
}

h1, h2, h3 {
    color: #5d4037;
    font-family: 'Georgia', serif;
    font-weight: bold;
}

p {
    color: #8d6e63;
    font-family: 'Georgia', serif;
}

.stButton>button {
    background-color: #33291e;
    color: white;
    font-size: 16px;
    border-radius: 5px;
    padding: 10px 20px;
}

.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    text-align: center;
}

.card img {
    max-width: 150px;
    height: auto;
    border-radius: 5px;
}

.card h3 {
    color: #5d4037;
    font-family: 'Georgia', serif;
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.card p {
    color: #8d6e63;
    font-family: 'Georgia', serif;
}

</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Frontpage content
st.title("Welcome to the Book Website!")
st.write("""
    On this page, you can explore our book collection, check availability, and purchase books.
    Discover new favorites or find the perfect book for you!
    """)
st.image("https://cdn.discordapp.com/attachments/889505398980231168/1296755505615863873/images.png?ex=6713712d&is=67121fad&hm=6a90fb28832c2ce9c87197d7833de5c8886e3eae02f9f2b3da5df812471180d6&", 
    caption="Books open new worlds", use_column_width=True)

st.subheader("What can you do here?")
st.markdown("""
    <ul style="color: #8d6e63;">
        <li><strong>View available books</strong>: Browse our current collection and discover new favorites.</li>
        <li><strong>Check availability</strong>: See how many books are in stock and the price for each title.</li>
        <li><strong>Purchase books</strong>: Select and purchase your favorite books from our collection.</li>
    </ul>
    """, unsafe_allow_html=True)

# Fetch data from PostDB directly and display it
st.subheader("Available Books")

# Initialize your PostDB instance
post_db = PostDB()

try:
    books = post_db.fetch_all_posts()  # Fetch all books from the database

    if books:
        for book in books:
            # Create a card layout for each book
            st.markdown(f"""
            <div class="card">
                <img src="{book['image_url']}" alt="Book cover">
                <h3>{book['title']}</h3>
                <p><strong>Pages:</strong> {book['pages']}</p>
                <p><strong>Price:</strong> ${book['price']}</p>
                <p><strong>Stock Amount:</strong> {book['amount']}</p>
                <p><strong>Genre:</strong> {book['genre']}</p>
                <p><strong>Author:</strong> {book['author']}</p>
                <p><strong>Series:</strong> {'Yes' if book['series'] else 'No'}</p>
            </div>
            """, unsafe_allow_html=True)  # Use HTML to structure the card layout

    else:
        st.write("No books available at the moment.")
except Exception as e:
    st.error(f"Error fetching data from PostDB: {e}")

# Links to other actions
st.markdown('<p style="color: #8d6e63; font-weight: bold;">Get started:</p>', unsafe_allow_html=True)
if st.button("View Books"):
    st.write("Viewing all books...")
if st.button("Log in"):
    st.write("Login form goes here.")
