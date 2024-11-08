import streamlit as st

def city_projects():
    st.title("City Projects Voting & Feedback")

    # Sample projects data
    projects = [
        {"id": 1, "title": "Park Renovation", "description": "Improving the park facilities"},
        {"id": 2, "title": "Library Upgrade", "description": "Adding more books and seating"},
    ]

    for project in projects:
        st.subheader(project["title"])  # Project Title
        st.write(project["description"])  # Project Description

        vote = st.radio(f"Vote on Project {project['id']}", ("Support", "Against"), key=project["id"])

        if st.button(f"Submit Vote for Project {project['id']}"):
            st.success("Vote submitted! (Sample vote)")
