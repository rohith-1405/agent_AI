def signup_page(users_collection):
    st.markdown("## 📝 Create Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password != confirm:
            st.error("Passwords do not match")
            return

        if users_collection.find_one({"username": username}):
            st.error("Username already exists")
            return

        users_collection.insert_one({
            "username": username,
            "email": email,
            "password": hash_password(password)
        })

        st.success("Account created! Please login.")
