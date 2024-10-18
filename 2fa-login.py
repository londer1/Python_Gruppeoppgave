import streamlit as st
from connection import UserDB
import hashlib

# Initialize UserDB
user_db = UserDB()

st.title("Login with 2FA")

# Step 1: Login
st.subheader("Login")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if "logged_in" not in st.session_state:
    st.session_state['logged_in'] = False

if "2fa_sent" not in st.session_state:
    st.session_state['2fa_sent'] = False

# Step 1: Validate login
if not st.session_state['logged_in'] and st.button("Login"):
    # Validate the email and password
    valid_login, user = user_db.validate_login(email, password)
    
    if valid_login:
        st.session_state['logged_in_user'] = user['email']
        st.session_state['user_password'] = password
        
        # Send the 2FA code (MD5 hash of the password) to the user's email
        md5_hash = user_db.send_2fa_email(email, password)
        
        st.session_state['expected_2fa_code'] = md5_hash
        st.session_state['2fa_sent'] = True
        
        st.success(f"A 2FA code has been sent to {email}.")
        
    else:
        st.error("Invalid email or password.")

# Step 2: 2FA Validation
if st.session_state['2fa_sent']:
    st.subheader("Enter 2FA Code")
    input_2fa = st.text_input("2FA Code", type="password")

    if st.button("Validate 2FA"):
        expected_2fa_code = st.session_state['expected_2fa_code']
        
        if input_2fa == expected_2fa_code:
            st.session_state['logged_in'] = True
            st.success("Login successful!")
        else:
            st.error("Invalid 2FA code.")

if st.session_state['logged_in']:
    st.write("Welcome to the system!")
