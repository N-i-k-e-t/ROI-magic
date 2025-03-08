import streamlit as st
from utils.auth import authenticate_user, create_access_token, get_password_hash
from utils.database import User, SessionLocal
from datetime import timedelta

def login_page():
    st.title("Login")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            user = authenticate_user(email, password)
            if user:
                access_token = create_access_token(
                    data={"sub": user.email},
                    expires_delta=timedelta(minutes=30)
                )
                st.session_state["user_token"] = access_token
                st.session_state["user_email"] = user.email
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid email or password")

def register_page():
    st.title("Register")

    with st.form("register_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Register")

        if submit:
            if password != confirm_password:
                st.error("Passwords do not match")
                return

            db = SessionLocal()
            try:
                # Check if user already exists
                existing_user = db.query(User).filter(User.email == email).first()
                if existing_user:
                    st.error("Email already registered")
                    return

                # Create new user
                new_user = User(
                    email=email,
                    name=name,
                    password_hash=get_password_hash(password)
                )
                db.add(new_user)
                db.commit()

                st.success("Registration successful! Please login.")
                st.session_state["show_login"] = True
                st.rerun()
            finally:
                db.close()

def auth_page():
    if "user_token" in st.session_state:
        if st.sidebar.button("Logout"):
            del st.session_state["user_token"]
            del st.session_state["user_email"]
            st.rerun()
        return True

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        login_page()

    with tab2:
        register_page()

    return False