import streamlit as st
from connection import UserDB

# Initialize UserDB
user_db = UserDB()

st.title("Login")

# Step 1: Login
st.subheader("Login")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state['logged_in'] = False

if "2fa_sent" not in st.session_state:
    st.session_state['2fa_sent'] = False

# Step 1: Validate login
if not st.session_state['logged_in'] and st.button("Login"):
    valid_login, user = user_db.validate_login(email, password)

    if valid_login:
        st.session_state['logged_in'] = True
        st.success("Login successful!")
    else:
        st.error("Invalid email or password.")
