import streamlit as st
from connection import UserDB, PostDB, Search

# Custom CSS for Frontpage
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
.book-card {
    background-color: white;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
    margin-bottom: 20px;
    width: 300px;  /* Reduced box size */
}
.book-image {
    width: 80px;
    height: 120px;
    object-fit: cover;
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

# Initialize UserDB and PostDB
user_db = UserDB()
post_db = PostDB()

# Set session state for navigation
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user_role" not in st.session_state:
    st.session_state["user_role"] = None  # Staff or Borrower

if "page" not in st.session_state:
    st.session_state["page"] = "login"  # Default to the login page

# Navigation handler
def set_page(page):
    st.session_state["page"] = page

# Suppress all error messages with try-except blocks
def suppress_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            pass  # Do nothing on error, you can log if needed
    return wrapper

# Login Form
@suppress_errors
def login():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Log in"):
        valid_login, user = user_db.validate_login(email, password)
        if valid_login:
            st.session_state["logged_in"] = True
            st.session_state["user_role"] = "Staff" if user["staff"] else "Borrower"
            set_page("home")  # Navigate to the home page after login
            st.experimental_rerun()  # Refresh state to apply login
        else:
            st.error("Invalid email or password.")  # Optional error display, you can suppress it if needed

# Home page content
@suppress_errors
def home_page():
    st.title("Welcome to the Book System")
    st.write(f"You are logged in as: {st.session_state['user_role']}")
    
    # Search functionality
    st.subheader("Search Books")
    search_term = st.text_input("Search by title, author, or genre")
    
    if search_term:
        # Use the Search class to search the database
        search_obj = Search(search_term)
        books = search_obj.search()
        search_obj.close()
    else:
        books = post_db.fetch_all_posts()

    # Show books as smaller cards with images
    if books:
        for book in books:
            st.markdown(f"""
            <div class="book-card">
                <h3>{book['title']}</h3>
                <img src="{book['image_url']}" class="book-image" alt="{book['title']}"/>
                <p><strong>ID:</strong> {book['id']}</p>
                <p><strong>Pages:</strong> {book['pages']}</p>
                <p><strong>Price:</strong> ${book['price']}</p>
                <p><strong>Stock Amount:</strong> {book['amount']}</p>
                <p><strong>Author:</strong> {book['author']}</p>
                <p><strong>Genre:</strong> {book['genre']}</p>
                <p><strong>Series:</strong> {'Yes' if book['series'] else 'No'}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("No books found.")

    # Show common features for all users
    st.subheader("Common Features")
    st.write("1. View available books")
    
    # Staff-specific features
    if st.session_state["user_role"] == "Staff":
        st.subheader("Admin Features")
        if st.button("Admin User Creation"):
            set_page("admin_user_creation")
        if st.button("Book Storage"):
            set_page("book_storage_updater")
    
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user_role"] = None
        set_page("login")
        st.experimental_rerun()  # Refresh state for logout

# Admin User Creation Page (with user list and delete functionality)
@suppress_errors
def admin_user_creation_page():
    st.title("Admin - User Management")
    
    # Create new user
    st.subheader("Create New User")
    email = st.text_input("New User Email")
    password = st.text_input("New User Password", type="password")
    staff = st.checkbox("Is Staff?")
    
    if st.button("Create User"):
        if email and password:
            user_db.add_user(email, password, staff=staff)
            st.success(f"User {email} created successfully.")
            st.experimental_rerun()  # Reload the page to reflect changes
        else:
            st.error("Please enter both email and password.")

    # List all users
    st.subheader("All Users")
    users = user_db.fetch_all_users()
    for user in users:
        st.write(f"Email: {user['email']}, Role: {'Staff' if user['staff'] else 'Borrower'}")
        if st.button(f"Delete {user['email']}"):
            user_db.delete_user(user['id'])
            st.success(f"Deleted user {user['email']}")
            st.experimental_rerun()  # Reload the page after deletion

    if st.button("Back"):
        set_page("home")

# Book Storage Updater Page
@suppress_errors
def book_storage_updater_page():
    st.title("Book Storage Updater")

    # 1. Show a list of all books
    st.subheader("List of Books")
    books = post_db.fetch_all_posts()
    if books:
        for book in books:
            st.write(f"ID: {book['id']}, Title: {book['title']}, Pages: {book['pages']}, Price: {book['price']}, Stock: {book['amount']}, Author: {book['author']}")
    else:
        st.write("No books available.")

    # 2. Create a new book
    st.subheader("Add New Book")
    with st.form('create_book_form'):
        title = st.text_input('Title')
        pages = st.number_input('Pages', min_value=1)
        price = st.number_input('Price', min_value=0)
        amount = st.number_input('Stock Amount', min_value=0)
        genre = st.text_input('Genre')
        author = st.text_input('Author')
        series = st.checkbox('Is Series?')
        image_url = st.text_input('Image URL')
        submitted = st.form_submit_button('Create Book')

        if submitted and title and pages and price and amount and genre and author:
            post_db.add_post(title, pages, price, amount, genre, author, series, image_url)
            st.success('Book created successfully!')
            st.experimental_rerun()  # Reload the page after adding the book
        elif submitted:
            st.error('Please fill in all fields.')

    def update_stock(self, book_id, new_amount):
        self.conn.execute('UPDATE Posts SET amount = ? WHERE id = ?', (new_amount, book_id))
        self.conn.commit()

    # Streamlit part of the code
    st.subheader("Update Book Stock")

    # Input field to select the book ID
    book_id_to_update = st.number_input("Enter Book ID to Update", min_value=1)

    # Input field for the new stock amount
    new_stock_amount = st.number_input("Enter New Stock Amount", min_value=0)

    # Button to trigger the stock update
    if st.button("Update Stock"):
        if book_id_to_update and new_stock_amount >= 0:
            # Call the update_stock method from PostDB to update the book's stock
            post_db.update_po(book_id_to_update, new_stock_amount)
            st.success(f"Updated stock for Book ID {book_id_to_update} to {new_stock_amount}")
        else:
            st.error("Please provide a valid Book ID and Stock Amount.")

    # 3. Delete a book
    st.subheader("Delete Book")
    book_id_to_delete = st.number_input("Enter Book ID to Delete", min_value=1)
    if st.button("Delete Book"):
        post_db.delete_post(book_id_to_delete)
        st.success(f"Book with ID {book_id_to_delete} deleted successfully!")
        st.experimental_rerun()

    if st.button("Back"):
        set_page("home")

# Page handling
if not st.session_state["logged_in"]:
    login()
else:
    if st.session_state["page"] == "home":
        home_page()
    elif st.session_state["page"] == "admin_user_creation":
        admin_user_creation_page()
    elif st.session_state["page"] == "book_storage_updater":
        book_storage_updater_page()
