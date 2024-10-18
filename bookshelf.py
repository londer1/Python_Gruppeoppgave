import streamlit as st

# Custom CSS for the layout
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

.book-card {
    display: inline-block;
    width: 22%;
    margin: 1%;
    background-color: #fff;
    padding: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
    border-radius: 5px;
}

.book-card img {
    width: 100%;
    height: auto;
}

.book-info {
    margin-top: 10px;
}

.book-title {
    font-size: 18px;
    color: #5d4037;
}

.book-price {
    font-size: 16px;
    color: #8d6e63;
}

.book-stock {
    font-size: 14px;
    color: #33291e;
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Book data
books = [
    {"title": "The Great Gatsby", "price": "150 NOK", "stock": 5, "image": "https://example.com/gatsby.jpg"},
    {"title": "1984", "price": "200 NOK", "stock": 8, "image": "https://example.com/1984.jpg"},
    {"title": "To Kill a Mockingbird", "price": "180 NOK", "stock": 3, "image": "https://example.com/mockingbird.jpg"},
    {"title": "Moby-Dick", "price": "220 NOK", "stock": 4, "image": "https://example.com/mobydick.jpg"},
    {"title": "War and Peace", "price": "250 NOK", "stock": 6, "image": "https://example.com/warpeace.jpg"},
    {"title": "Pride and Prejudice", "price": "170 NOK", "stock": 7, "image": "https://example.com/pride.jpg"},
    {"title": "The Catcher in the Rye", "price": "190 NOK", "stock": 2, "image": "https://example.com/catcher.jpg"},
    {"title": "Brave New World", "price": "210 NOK", "stock": 5, "image": "https://example.com/brave.jpg"}
]

# Frontpage content
st.title("Explore Our Book Collection")
st.write("""
        Below are some of the books we have in our collection. You can view details about each book, including price and stock availability.
        """)
st.write("---")

# Display books in a grid
for i in range(0, len(books), 4):
    cols = st.columns(4)
    for col, book in zip(cols, books[i:i+4]):
        with col:
            st.markdown(f"""
            <div class="book-card">
                <img src="{book['image']}" alt="{book['title']}">
                <div class="book-info">
                    <p class="book-title">{book['title']}</p>
                    <p class="book-price">{book['price']}</p>
                    <p class="book-stock">In stock: {book['stock']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
