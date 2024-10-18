import streamlit as st
from connection import UserDB

# Create an instance of UserDB
user_db = UserDB()

st.title("User Management")

# Show existing users
st.subheader("All Users")
users = user_db.fetch_all_users()

if users:
    for user in users:
        st.write(f"ID: {user['id']}, Email: {user['email']}, Date Joined: {user['date_joined']}, Staff: {user['staff']}, Borrower: {user['borrower']}")
else:
    st.write("No users available.")

# Add a new user
st.subheader("Add New User")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
staff = st.checkbox("Is Staff?", value=False)

if st.button("Add User"):
    if email and password:
        user_db.add_user(email, password, staff=staff)
        st.success("User added successfully!")
    else:
        st.error("Email and password are required to add a user.")

# Delete a user
st.subheader("Delete User")
user_id_to_delete = st.number_input("Enter User ID to delete", min_value=1)

if st.button("Delete User"):
    user_db.delete_user(user_id_to_delete)
    st.success(f"User with ID {user_id_to_delete} deleted successfully!")

