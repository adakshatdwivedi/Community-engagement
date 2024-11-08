import streamlit as st

def community_forums():
    st.title("Community Forums")

    # Sample forum threads
    threads = [
        {"id": 1, "title": "Traffic Issues", "content": "Discussing traffic concerns"},
        {"id": 2, "title": "Park Maintenance", "content": "Thoughts on park maintenance"}
    ]

    for thread in threads:
        st.subheader(thread["title"])  # Thread Title
        st.write(thread["content"])    # Thread Content

        if st.button(f"Reply to Thread {thread['id']}"):
            comment = st.text_area("Your Comment")
            if st.button("Submit Comment"):
                st.success("Comment submitted! (Sample comment)")
