import streamlit as st

def public_dashboard():
    st.title("Public Dashboard")

    # Sample issues data
    low_issues = 10
    medium_issues = 20
    high_issues = 5

    st.subheader("Issue Severity Breakdown")
    st.write(f"Low: {low_issues}, Medium: {medium_issues}, High: {high_issues}")

    # Sample projects data
    projects = [
        {"title": "Park Renovation", "votes": 15},
        {"title": "Library Upgrade", "votes": 20},
    ]

    st.subheader("Projects Overview")
    for project in projects:
        st.write(f"Project: {project['title']}, Votes: {project['votes']}")
