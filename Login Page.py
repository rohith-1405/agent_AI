import streamlit as st
from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login_page(users_collection):
    st.markdown("## 🎬 Movie Agent Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = users_collection.find_one({
            "username": username,
            "password": hash_password(password)
        })

        if user:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")
