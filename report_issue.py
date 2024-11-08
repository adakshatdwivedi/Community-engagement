import streamlit as st

def report_issue():
    st.title("Report an Issue")
    issue_title = st.text_input("Issue Title")
    location = st.text_input("Location")
    description = st.text_area("Description")
    severity = st.selectbox("Severity Level", ["Low", "Medium", "High"])

    if st.button("Submit Issue"):
        st.success("Issue reported successfully!")
