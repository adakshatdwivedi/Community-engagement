import streamlit as st

def view_issues():
    st.title("View Issues")

    # Sample issues data
    issues = [
        {"id": 1, "title": "Pothole on Main Street", "location": "Main Street", "description": "Large pothole", "severity": "High"},
        {"id": 2, "title": "Broken Streetlight", "location": "5th Avenue", "description": "Streetlight not working", "severity": "Low"},
    ]

    for issue in issues:
        st.subheader(issue["title"])  # Title
        st.write(f"Location: {issue['location']}")
        st.write(f"Description: {issue['description']}")
        st.write(f"Severity: {issue['severity']}")

        if st.button(f"Upvote Issue {issue['id']}"):
            st.success("You upvoted the issue! (Sample upvote)")
