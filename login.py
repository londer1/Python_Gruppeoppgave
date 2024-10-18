import streamlit as st
from connection import UserDB  # Import the UserDB class
import time

# Initialize the database connection
db = UserDB()

# Streamlit app layout
st.title('User Login System')

# View all users (for testing)
st.header('All Users')
users = db.fetch_all_users()
if users:
    for user in users:
        st.write(f"ID: {user['id']}, Email: {user['email']}, Date Joined: {user['date_joined']}, Staff: {user['staff']}, Borrower: {user['borrower']}")
else:
    st.write("No users available.")

# Create a new user
st.header('Create New User')
#
with st.form('create_user_form'):
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    submitted = st.form_submit_button('Sign Up')

    if submitted:
        existing_user = db.fetch_user_by_email(email)
        if existing_user:
            st.error('User with this email already exists!')
        else:
            db.add_user(email, password, staff=False)  # staff is False, borrower is True by default
            st.success('User created!')
            time.sleep(1)  # Simulate a short delay for effect
            st.experimental_rerun()

# Password reset form (for testing)
st.header('Reset User Password')
with st.form('reset_password_form'):
    reset_email = st.text_input('Email to reset password')
    new_password = st.text_input('New Password', type='password')
    reset_submitted = st.form_submit_button('Reset Password')
    if reset_submitted:
        existing_user = db.fetch_user_by_email(reset_email)
        if existing_user:
            db.update_user_password(reset_email, new_password)
            st.success(f'Password updated for {reset_email}!')
            time.sleep(1)  # Simulate a short delay
        else:
            st.error(f'No user found with the email {reset_email}!')

# Delete a user (for testing)
st.header('Delete User')
with st.form('delete_user_form'):
    user_id = st.number_input('User ID to Delete', min_value=1)
    delete_submitted = st.form_submit_button('Delete')

    if delete_submitted:
        db.delete_user(user_id)
        st.success(f'User with ID {user_id} deleted!')
        time.sleep(1)  # Simulate a short delay
        st.experimental_rerun()
