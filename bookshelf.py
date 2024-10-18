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
    width: 100%;
    height: 400px;
    margin: 0.5%;
    margin-bottom: 15px;
    background-color: #fff;
    padding: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
    border-radius: 5px;
}

.book-card img {
    width: 100%;
    height: 200px;
}

.book-info {
    margin-top: 10px;
}

.book-title {
    font-size: 16px;
    color: #5d4037;
    word-wrap: break-word;
}

.book-price {
    font-size: 14px;
    color: #8d6e63;
}

.book-stock {
    font-size: 12px;
    color: #33291e;
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Book data
books = [
    {"title": "The Book of Bill", "price": "150 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1702662879i/203315037.jpg"},
    {"title": "Sky Full of Elephants", "price": "200 NOK", "stock": 8, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1707161023i/207293815.jpg"},
    {"title": "To Kill a Mockingbird", "price": "180 NOK", "stock": 3, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1553383690i/2657.jpg"},
    {"title": "Moby-Dick", "price": "220 NOK", "stock": 4, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327940656i/153747.jpg"},
    {"title": "War and Peace", "price": "250 NOK", "stock": 6, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1413215930i/656.jpg"},
    {"title": "Pride and Prejudice", "price": "170 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1320399351i/1885.jpg"},
    {"title": "The Catcher in the Rye", "price": "190 NOK", "stock": 2, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1398034300i/5107.jpg"},
    {"title": "Brave New World", "price": "210 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1575509280i/5129.jpg"},
    {"title": "1984", "price": "220 NOK", "stock": 8, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1348990566i/5470.jpg"},
    {"title": "The Great Gatsby", "price": "180 NOK", "stock": 10, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1490528560i/4671.jpg"},
    {"title": "Jane Eyre", "price": "195 NOK", "stock": 6, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327867269i/10210.jpg"},
    {"title": "The Hobbit", "price": "230 NOK", "stock": 9, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546071216i/5907.jpg"},
    {"title": "The Adventures of Sherlock Holmes", "price": "175 NOK", "stock": 12, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1164045516i/3590.jpg"},
    {"title": "Frankenstein", "price": "165 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1381512375i/18490.jpg"},
    {"title": "Crime and Punishment", "price": "210 NOK", "stock": 4, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1382846449i/7144.jpg"},
    {"title": "Wuthering Heights", "price": "180 NOK", "stock": 11, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388212715i/6185.jpg"},
    {"title": "The Picture of Dorian Gray", "price": "190 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546103428i/5297.jpg"},
    {"title": "Dracula", "price": "185 NOK", "stock": 3, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1387151694i/17245.jpg"},
    {"title": "Les Misérables", "price": "245 NOK", "stock": 2, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1411852091i/24280.jpg"},
    {"title": "The Brothers Karamazov", "price": "260 NOK", "stock": 1, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1427728126i/4934.jpg"},
    {"title": "The Lord of the Rings", "price": "280 NOK", "stock": 3, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1566425108i/33.jpg"},
    {"title": "Harry Potter and the Sorcerer's Stone", "price": "250 NOK", "stock": 10, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1474154022i/3.jpg"},
    {"title": "The Alchemist", "price": "175 NOK", "stock": 12, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1483412266i/865.jpg"},
    {"title": "The Da Vinci Code", "price": "220 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1720313229i/968.jpg"},
    {"title": "The Hunger Games", "price": "190 NOK", "stock": 14, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052.jpg"},
    {"title": "The Kite Runner", "price": "200 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1579036753i/77203.jpg"},
    {"title": "The Fault in Our Stars", "price": "180 NOK", "stock": 9, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1360206420i/11870085.jpg"},
    {"title": "Gone Girl", "price": "210 NOK", "stock": 11, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1554086139i/19288043.jpg"},
    {"title": "The Road", "price": "190 NOK", "stock": 6, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1600241424i/6288.jpg"},
    {"title": "Memoirs of a Geisha", "price": "220 NOK", "stock": 8, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388367666i/930.jpg"},
    {"title": "Life of Pi", "price": "200 NOK", "stock": 10, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1631251689i/4214.jpg"},
    {"title": "The Shining", "price": "240 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1353277730i/11588.jpg"},
    {"title": "The Girl on the Train", "price": "190 NOK", "stock": 6, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1574805682i/22557272.jpg"},
    {"title": "The Night Circus", "price": "230 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1387124618i/9361589.jpg"},
    {"title": "A Game of Thrones", "price": "260 NOK", "stock": 3, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1436732693i/13496.jpg"},
    {"title": "The Handmaid's Tale", "price": "195 NOK", "stock": 9, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1578028274i/38447.jpg"},
    {"title": "The Silent Patient", "price": "200 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1668782119i/40097951.jpg"},
    {"title": "Where the Crawdads Sing", "price": "230 NOK", "stock": 12, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1582135294i/36809135.jpg"},
    {"title": "A Man Called Ove", "price": "180 NOK", "stock": 8, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1405259930i/18774964.jpg"},
    {"title": "Big Little Lies", "price": "210 NOK", "stock": 4, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1559835163i/33516773.jpg"},
    {"title": "The Book Thief", "price": "220 NOK", "stock": 6, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1522157426i/19063.jpg"},
    {"title": "The Pillars of the Earth", "price": "260 NOK", "stock": 2, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1576956100i/5043.jpg"},
    {"title": "Water for Elephants", "price": "200 NOK", "stock": 9, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1722456144i/43641.jpg"},
    {"title": "Shantaram", "price": "245 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1333482282i/33600.jpg"},
    {"title": "The Help", "price": "190 NOK", "stock": 10, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1572946656i/4667024.jpg"},
    {"title": "The Goldfinch", "price": "230 NOK", "stock": 6, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1498164091i/17333223.jpg"},
    {"title": "A Thousand Splendid Suns", "price": "180 NOK", "stock": 12, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1360206445i/128029.jpg"},
    {"title": "The Lovely Bones", "price": "195 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1310485327i/12232938.jpg"},
    {"title": "The Stand", "price": "260 NOK", "stock": 3, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1213131305i/149267.jpg"},
    {"title": "The Subtle Art of Not Giving a F*ck", "price": "220 NOK", "stock": 8, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1465761302i/28257707.jpg"},
    {"title": "The House of the Spirits", "price": "200 NOK", "stock": 4, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1348323641i/9337.jpg"},
    {"title": "The Martian", "price": "210 NOK", "stock": 11, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1413706054i/18007564.jpg"},
    {"title": "American Gods", "price": "240 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1481325471i/4407.jpg"},
    {"title": "Sapiens: A Brief History of Humankind", "price": "280 NOK", "stock": 3, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1600801644i/23692271.jpg"},
    {"title": "The Immortal Life of Henrietta Lacks", "price": "190 NOK", "stock": 9, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1411103315i/6493208.jpg"},
    {"title": "Educated", "price": "230 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1506026635i/35133922.jpg"},
    {"title": "The Catcher in the Rye", "price": "200 NOK", "stock": 10, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1398034300i/5107.jpg"},
    {"title": "The Wind-Up Bird Chronicle", "price": "250 NOK", "stock": 8, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1368401800i/11275.jpg"},
    {"title": "The Light We Lost", "price": "210 NOK", "stock": 9, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1579861551i/32956365.jpg"},
    {"title": "The Name of the Wind", "price": "240 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1524415689i/186074.jpg"},
    {"title": "The Rosie Project", "price": "180 NOK", "stock": 10, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1363527183i/16181775.jpg"},
    {"title": "Norwegian Wood", "price": "200 NOK", "stock": 4, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327873761i/11297.jpg"},
    {"title": "The Blind Assassin", "price": "230 NOK", "stock": 6, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1376655379i/78433.jpg"},
    {"title": "Atonement", "price": "210 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1424131014i/6867.jpg"},
    {"title": "Beloved", "price": "220 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1568374942i/6149.jpg"},
    {"title": "Never Let Me Go", "price": "190 NOK", "stock": 9, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1502115818i/6334.jpg"},
    {"title": "Cloud Atlas", "price": "230 NOK", "stock": 4, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1405246257i/49628.jpg"},
    {"title": "All the Light We Cannot See", "price": "240 NOK", "stock": 6, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1579638723i/18143977.jpg"},
    {"title": "Little Fires Everywhere", "price": "210 NOK", "stock": 5, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1538702537i/51704136.jpg"},
    {"title": "The Secret History", "price": "250 NOK", "stock": 3, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1451554846i/29044.jpg"},
    {"title": "Circe", "price": "220 NOK", "stock": 8, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1519677140i/35959740.jpg"},
    {"title": "The Power", "price": "200 NOK", "stock": 7, "image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1460415862i/29751398.jpg"}
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
