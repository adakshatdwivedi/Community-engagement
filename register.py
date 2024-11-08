import streamlit as st

# Sample users data for checking duplicate emails
sample_users = {
    "user1@example.com": {"name": "User One", "password": "pass1"},
    "user2@example.com": {"name": "User Two", "password": "pass2"},
    "user3@example.com": {"name": "User Three", "password": "pass3"},
}

def register():
    st.title("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match!")
        elif email in sample_users:
            st.error("Email already exists!")
        else:
            sample_users[email] = {"name": name, "password": password}
            st.success("Registration successful! (Sample registration)")
