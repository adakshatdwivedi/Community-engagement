import streamlit as st

# Sample users data
sample_users = {
    "user1@example.com": {"name": "User One", "password": "pass1"},
    "user2@example.com": {"name": "User Two", "password": "pass2"},
    "user3@example.com": {"name": "User Three", "password": "pass3"},
}

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = sample_users.get(username)
        if user and user["password"] == password:
            st.success("Login successful!")
        else:
            st.error("Invalid credentials!")
