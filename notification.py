import streamlit as st

def notification_preferences():
    st.title("Notification Preferences")

    st.checkbox("Receive updates on submitted issues")
    st.checkbox("Receive updates on subscribed projects")

    if st.button("Save Preferences"):
        st.success("Notification preferences saved! (Sample save)")
