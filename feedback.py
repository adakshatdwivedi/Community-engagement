import streamlit as st

def feedback_on_resolved_issues():
    st.title("Feedback on Resolved Issues")
    issue_id = st.number_input("Enter the Issue ID", min_value=1)
    rating = st.selectbox("Rating (1-5)", [1, 2, 3, 4, 5])
    comments = st.text_area("Comments")

    if st.button("Submit Feedback"):
        st.success("Feedback submitted successfully! (Sample feedback)")
