import streamlit as st

def main():
    st.title("City Issue Reporting Platform")
    menu = ["Login", "Register", "Report Issue", "View Issues", "City Projects", "Dashboard", "Community Forums"]
    choice = st.sidebar.selectbox("Select Page", menu)

    if choice == "Login":
        import login
        login.login()
    elif choice == "Register":
        import register
        register.register()
    elif choice == "Report Issue":
        import report_issue
        report_issue.report_issue()
    elif choice == "View Issues":
        import view_issues
        view_issues.view_issues()
    elif choice == "City Projects":
        import project
        project.city_projects()
    elif choice == "Dashboard":
        import public_dashboard
        public_dashboard.public_dashboard()
    elif choice == "Community Forums":
        import forums
        forums.community_forums()

if __name__ == "__main__":
    main()
